from servo import Servo
import utime
import math
# Definimos los motores y sus posiciones asociadas


FEMUR_FL = 0
FEMUR_FR = 1
FEMUR_BL = 2
FEMUR_BR = 3
TIBIA_FL = 4
TIBIA_FR = 5
TIBIA_BL = 6
TIBIA_BR = 7
NECK_PITCH = 8
NECK_YAW = 9
TAIL = 10
all_body_names = ["FEMUR_FL", "FEMUR_FR", "FEMUR_BL", "FEMUR_BR", "TIBIA_FL",
                  "TIBIA_FR", "TIBIA_BL", "TIBIA_BR", "NECK_PITCH", "NECK_YAW", "TAIL"]
all_body = [FEMUR_FL, FEMUR_FR, FEMUR_BL, FEMUR_BR, TIBIA_FL,
            TIBIA_FR, TIBIA_BL, TIBIA_BR, NECK_PITCH, NECK_YAW, TAIL]
femurs = [FEMUR_FL, FEMUR_FR, FEMUR_BL, FEMUR_BR]
tibias = [TIBIA_FL, TIBIA_FR, TIBIA_BL, TIBIA_BR]


def instance_servos(L_servos: list, L_names: list):
    for i in L_servos:
        L_names[i] = Servo(L_servos[i])


instance_servos(all_body, all_body_names)


# Todos los motores a 90 deg
def setup_position():
    for j in range(len(all_body_names)):
        all_body_names[j].set_angle(90)
        utime.sleep(0.01)


def stand_michi():
    for j in range(4):
        all_body_names[j].set_angle(120)
        utime.sleep(0.01)
    for j in range(4):
        all_body_names[j+4].set_angle(60)
        utime.sleep(0.01)


def inverse_kinematics(x, z):
    a = 47 #length of each link 
    q2 = math.pi - \
        math.acos(1 - (math.pow(x, 2) + math.pow(z, 2))/(2*math.pow(a, 2)))
    if x == 0:
        q1 = math.pi/2 + q2/2
    elif x > 0:
        q1 = math.atan(-z/x) + q2/2
    else:
        q1 = math.pi + q2/2 - math.atan(z/x)

    q2 = math.degrees(q2)
    q1 = math.degrees(q1)
    q1 = round(q1, 1)
    q2 = round(q2, 1)
    return q1, q2
