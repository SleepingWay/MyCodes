import random

from pyDes import des, PAD_PKCS5, ECB
import random as ran
import string

UserMessage = {}
AllString = string.ascii_letters
Users = string.ascii_uppercase
global n2
global K


def KDC(user1, user2, N1):      # send Eka[ks||N1||Ekb(ks||IDa)]
    global K
    Ks = ''.join(ran.choices(AllString, k=8))  # 为会话分配的密钥Ks
    K = Ks
    IDa = user1  # 用户1的身份码
    K1, K2 = 0, 0
    if user1 not in UserMessage.keys():
        K1 = ''.join(random.choices(AllString, k=8))
        UserMessage[user1] = K1
    else:
        K1 = UserMessage[user1]
    if user2 not in UserMessage.keys():
        K2 = ''.join(random.choices(AllString, k=8))
        UserMessage[user2] = K2
    else:
        K2 = UserMessage[user2]
    des_user1 = des(K1, ECB, '12345678', padmode=PAD_PKCS5)
    des_user2 = des(K2, ECB, '12345678', padmode=PAD_PKCS5)
    Ks_des_user2 = des_user2.encrypt(Ks)
    IDa_des = des_user2.encrypt(IDa)
    n1_des = des_user1.encrypt(str(N1))  # 用Ka加密的N1
    Ks_des_user1 = des_user1.encrypt(Ks)  # 用Ka加密的Ks
    send_to_user1_Ks = des_user1.encrypt(Ks_des_user2)  # 用Ka加密发送给用户2的Ks
    send_to_user1_IDa = des_user1.encrypt(IDa_des)  # 用Ka加密发送给用户2的IDa
    return [Ks_des_user1, n1_des, send_to_user1_Ks, send_to_user1_IDa]


def UserRequest_1(user1, lst):  # A receive Eka[ks||N1||Ekb(ks||IDa)] send Ekb(ks||IDa)
    K1 = UserMessage[user1]
    des_user1 = des(K1, ECB, '12345678', padmode=PAD_PKCS5)
    send_to_user2_Ks = des_user1.decrypt(lst[2])
    send_to_user2_IDa = des_user1.decrypt(lst[3])
    return [send_to_user2_Ks, send_to_user2_IDa]


def UserRequest_2(user1, user2, lst):   # B receive Ekb(ks||IDa) send Eks(N2)
    global n2
    K2 = UserMessage[user2]
    des_user2 = des(K2, ECB, '12345678', padmode=PAD_PKCS5)
    Ks = des_user2.decrypt(lst[0])
    IDa = des_user2.decrypt(lst[1])
    if IDa == user1:
        print('确认是从 {} 发来的消息'.format(user1))
    N2 = ran.randint(1, 1000)
    n2 = N2
    des_ks = des(Ks, ECB, '12345678', padmode=PAD_PKCS5)
    return des_ks.encrypt(str(N2))


def UserRequest_3(message):     # A receive Eks(N2) send Eks[f(N2)]  f(x) = x ** 2 % 1551
    global K
    des_ks = des(K, ECB, '12345678', padmode=PAD_PKCS5)
    N2 = des_ks.decrypt(message)
    return des_ks.encrypt(str(int(N2) ** 2 % 1551))


def UserRequest_4(message):     # B receive Eks[f(N2)] and confirm
    global K
    global n2
    des_ks = des(K, ECB, '12345678', padmode=PAD_PKCS5)
    fN2 = des_ks.decrypt(message)
    if int(fN2) == n2 ** 2 % 1551:
        print('完成认证')


def Distribution(user1, user2, N1):
    message = KDC(u1, u2, n1)
    message = UserRequest_1(u1, message)
    mes = UserRequest_2(u1, u2, message)
    mes = UserRequest_3(mes)
    UserRequest_4(mes)

for i in range(10):     # 随机选取10对用户进行算法检验
    u1 = ran.choice(Users)
    u2 = ran.choice(Users)
    n1 = ran.randint(1, 1000)
    Distribution(u1, u2, n1)
    print(u1, ':', UserMessage[u1], '\t\t\t', u2, ':', UserMessage[u2], '\t\t\t', 'Key', ':', K, '\n')
