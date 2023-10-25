#!/usr/bin/env python3

from position_hold import swift 
from swift_msgs.msg import *
from geometry_msgs.msg import PoseArray
from std_msgs.msg import Int16
from std_msgs.msg import Int64
from std_msgs.msg import Float64
from pid_tune.msg import PidTune
import rospy
import time



class waypoint_coordinate_updater(swift):
    def __init__(self):
        super().__init__()
        self.given_coordinates = [
            [0, 0, 23],
            [2, 0, 23],
            [2, 2, 23],
            [2, 2, 25],
            [-5, 2, 25],
            [-5, -3, 25],
            [-5, -3, 21],
            [7, -3, 21],
            [7, 0, 21],
            [0, 0, 19]

        ]
        self.setpoint = [0,0,23]
        self.Kp = [93*0.1,91*0.07,115*0.07]
        self.Ki = [6*0.0001,6*0.0001,8*0.0001]
        self.Kd = [12*0.7, 4*0.3, 590*0.3]
    def run(self):
        print(self.drone_position)
        if -0.20 <= self.error[0] <= 0.20 and -0.20 <= self.error[1] <= 0.20 and -0.20 <= self.error[2] <= 0.20:
            if self.setpoint != [0,0,19]:
                self.given_coordinates.remove(self.setpoint)
                self.setpoint = self.given_coordinates[0]
                print("-"*70)
            else:
                self.setpoint = [0,0,19]


if __name__ == '__main__':

    swift_drone = waypoint_coordinate_updater()
    #start_time = time.time()
    r = rospy.Rate(29.99) #specify rate in Hz based upon your desired PID sampling time, i.e. if desired sample time is 33ms specify rate as 30Hz
    while not rospy.is_shutdown():
        swift_drone.pid()
        swift_drone.run()
        r.sleep()
