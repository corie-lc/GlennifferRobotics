# Glenniffer Robotics
  Glenniffer is a robotics project using the raspberry pi 4b, built to patrol and interact with my cat
  
 # Features
   (Current)
   - 18500 Battery powers the raspberry pi and 14650 powers the motors (a dedicated motor controller)
   - Remotely control Glenniffer via a Java application using sockets (local network only).
   - Update speeds, use arrow keys and stop the robot from Glenniffer Controller (GUI)
   - Autonomous mode currently allows the robot to drive around without hitting anything via an ultra-sonic proximity sensor

  (Upcoming)
   - Use the Raspberry Pi camera & OpenCV to find a cats face (demo created, just need to attach camera)
   - Pick up receipts, crumple (for sound) and throw the receipt (my cat wont play with any toys, but will chase receipts)
   - OpenCV will find the receipt, pick it up and throw it. If Glenniffer can't find it, she will pull a recept from storage
