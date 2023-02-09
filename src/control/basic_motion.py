from servo import Servo
import utime
#Definimos los motores y sus posiciones asociadas




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
all_body_names= ["FEMUR_FL", "FEMUR_FR", "FEMUR_BL", "FEMUR_BR", "TIBIA_FL", "TIBIA_FR", "TIBIA_BL", "TIBIA_BR", "NECK_PITCH", "NECK_YAW", "TAIL"]
all_body = [FEMUR_FL, FEMUR_FR, FEMUR_BL, FEMUR_BR, TIBIA_FL, TIBIA_FR, TIBIA_BL, TIBIA_BR, NECK_PITCH, NECK_YAW, TAIL]
femurs = [FEMUR_FL, FEMUR_FR, FEMUR_BL, FEMUR_BR]
tibias= [TIBIA_FL, TIBIA_FR, TIBIA_BL, TIBIA_BR]





def instance_servos(L_servos: list, L_names: list):
    for i in L_servos:
        L_names[i] = Servo(L_servos[i])
        print(str(L_names[i]))

instance_servos(all_body,all_body_names)




def instance_servos(L_servos: list, L_names: list):
    for i in L_servos:
        L_names[i] = Servo(L_servos[i])
       

instance_servos(all_body,all_body_names)



while True:
    #Run every motor

    for j in range(len(all_body_names)):
        all_body_names[j].set_angle(180)
        utime.sleep(0.1)
        
    for j in range(len(all_body_names)):
        all_body_names[j].set_angle(0)
        utime.sleep(0.1)