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
        self.nth_term = 0
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
        self.reaching_status = {}
        for coordinate in self.given_coordinates:
            self.reaching_status[f"{coordinate}"] = 0
    
    def run(self, startTime):
        #print(self.setpoint, self.reaching_status[f"{self.setpoint}"])
        if (-0.20 <= self.error[0] <= 0.2 and -0.20 <= self.error[1] <= 0.2 and-0.20 <= self.error[2] <= 0.2) and self.reaching_status.get(f"{self.setpoint}") != 1:
            self.reaching_status[f"{self.setpoint}"] = 1
            self.nth_term += 1
            if self.nth_term < len(self.given_coordinates) - 1:
                self.setpoint = self.given_coordinates[self.nth_term]
            else:
                self.setpoint = self.given_coordinates[-1]


if __name__ == '__main__':

    swift_drone = waypoint_coordinate_updater()
    start_time = time.time()
    r = rospy.Rate(29.99) #specify rate in Hz based upon your desired PID sampling time, i.e. if desired sample time is 33ms specify rate as 30Hz
    while not rospy.is_shutdown():
        swift_drone.pid()
        swift_drone.run(start_time)
        r.sleep()
