import math

foc = 4895.0  # 镜头焦距
real_hight_person = 66.9  # 行人高度
real_hight_car = 57.08  # 轿车高度
real_hight_bottle = 9.06  # 瓶子高度
camera_height = 1.5  # 相机高度

image_width = 3840
image_height = 2160


# 自定义函数，单目测距
def person_distance(h):
    dis_inch = (real_hight_person * foc) / (h - 2)
    dis_cm = dis_inch * 2.54
    dis_cm = int(dis_cm)
    dis_m = dis_cm / 100
    return dis_m


def car_distance(h):
    dis_inch = (real_hight_car * foc) / (h - 2)
    dis_cm = dis_inch * 2.54
    dis_cm = int(dis_cm)
    dis_m = dis_cm / 100
    return dis_m


def bottle_distance(h):
    dis_inch = (real_hight_bottle * foc) / (h - 2)
    dis_cm = dis_inch * 2.54
    dis_cm = int(dis_cm)
    dis_m = dis_cm / 100
    return dis_m


def world_xy(dis_m, mid_x):  # 该坐标系是以光轴为y轴，从屏幕中心出发平行于相机底边向右的射线为x轴
    world_x = (mid_x - image_width / 2) * dis_m / foc
    world_y = (dis_m ** 2 - world_x ** 2) ** 0.5
    return world_x, world_y


def revolve_xy(angle, x, y):  # 旋转坐标系
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return new_x, new_y


def transform_xy(angle, x, y, d, h):  # 非标志物目标 坐标转换
    new_x, new_y = revolve_xy(angle, x, y)
    new_x = d - new_x
    new_y = new_y - h
    return new_x, new_y
