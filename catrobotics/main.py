# run source env/bin/activate in /desktop on start

from gpiozero import Robot
import time
import board
import adafruit_hcsr04

from gpiozero import Motor

import socket

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)


host = '10.0.0.65'  # Standard loopback interface address
port = 5001        # Port to listen on (non-privileged ports are > 1023)

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind((host, port))
serv.listen(5)
serv.settimeout(0.5)

right_speed = "0.8"
left_speed = "0.8"
prev_controlled = ""
    
    
    


#robby = Robot(right=(22,23), left=(17, 27))



#robby = Robot(right=(22,23), left=(17, 27))

motor1 = Motor(22,23)
motor2 = Motor(17, 27)

sensor_distance_one = 0.0

def drive_forward():
    motor1.forward(float(left_speed))
    motor2.backward(float(right_speed))
    
def drive_backwards():
        motor1.backward(float(left_speed))
        motor2.forward(float(right_speed))
        
def drive_left():
        motor1.backward(float(left_speed))
        motor2.forward(float(0.0))
        
def drive_right():
        motor1.backward(float(0.0))
        motor2.forward(float(right_speed))
def stop_robot_wheels():
        motor1.stop()
        motor2.stop()
        
        
   

def check_space():
    sensor_distance_one = 0.0
    try:
        sensor_distance_one = sonar.distance

    except RuntimeError:
        print("Retrying!")

    return sensor_distance_one

while (True):

    
    parse_data = ""
    data = ""
    # waits 5 sec until the connection will be closed
    try:
        print("starting")
        conn, addr = serv.accept()
        
        data = conn.recv(4096)
        parse_data = data.decode('utf-8').split(",")
    except:
        print("done")
    print("here")
    
    
    
    

    print(check_space())
    if check_space() > 9.0 and check_space() < 40.0:
            print("AHHHHHHHHHHHHH")
            motor1.backward(float(left_speed))
            motor2.forward(float(0.0))
    elif len(parse_data) >= 2:
        
                
        
        # UD = Update Speed
        if str(parse_data[1]) == 'UD':
        
            
            left_speed = parse_data[2]
            right_speed = parse_data[3]
                
        # move forward
        elif str(parse_data[1]) == 'W':
                prev_controlled = "W"
                drive_forward()
        elif str(parse_data[1]) == "B":
                prev_controlled = "B"
                drive_backwards()
                
        elif str(parse_data[1]) == "L":
                prev_controlled = "L"
                drive_left()
        elif str(parse_data[1]) == "R":
                prev_controlled = "R"
        
                drive_right()
        elif str(parse_data[1]) == "CONTROL":
                prev_controlled = "CONTROL"
                
                stop_robot_wheels()
    else:
           if prev_controlled == "W":
                   drive_forward()
           elif prev_controlled == "B":
                   drive_backwards()
           elif prev_controlled == "L":
                   drive_left()
           elif prev_controlled == "R":
                   drive_right()
           else:
                   
                stop_robot_wheels()
            

