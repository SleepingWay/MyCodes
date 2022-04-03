def decrypto(k,encrypto):   #解密函数
    s = [i for i in range(0, 256)]  # 初始化S

    kvalue = list()
    for i in k:
        kvalue.append(ord(i))

    klen = len(k)  # 初始化T
    t = list()
    for i in range(0, 256):
        t.append(kvalue[i % klen])

    j = 0  # 初始排列S
    for i in range(0, 256):
        j = (j + s[i] + int(t[i])) % 256
        s[i], s[j] = s[j], s[i]

    K = list()
    i, j = 0, 0  # 产生密钥流
    for r in range(len(encrypto)):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        t = (s[i] + s[j]) % 256
        K.append(s[t])
    message = list()
    for i in range(len(encrypto)):
        message.append(chr(ord(encrypto[i]) ^ K[i]))
    print('Decryption results are as follows:{}'.format(message))
message = input('please input the message:')
s = [i for i in range(0,256)] #初始化S
k = 'apexlegend'  #密钥
kvalue = list()
for i in k:
    kvalue.append(ord(i))
klen = len(k)       #初始化T
t=list()
for i in range(0,256):
    t.append(kvalue[i%klen])
j = 0         #初始排列S
for i in range(0,256):
    j = (j + s[i] + int(t[i])) % 256
    s[i],s[j]=s[j],s[i]
K = list()
i,j = 0,0     #产生密钥流
for r in range(len(message)):
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    s[i],s[j] = s[j],s[i]
    t = (s[i] + s[j]) % 256
    K.append(s[t])
encrypto = list()           #加密
for i in range(len(message)):
    encrypto.append(chr(ord(message[i]) ^ K[i] ))
print('The encryption result is:{}'.format(encrypto))
decrypto(k,encrypto)