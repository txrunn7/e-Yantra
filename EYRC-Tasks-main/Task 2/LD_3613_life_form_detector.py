#!/usr/bin/env python3

from position_hold import swift 
from swift_msgs.msg import *
from geometry_msgs.msg import PoseArray
from std_msgs.msg import Int16
from luminosity_drone.msg import Biolocation
from std_msgs.msg import Int64
from std_msgs.msg import Float64
from pid_tune.msg import PidTune
from cv_bridge import CvBridge
import cv2
import rospy
import time
import math
from sensor_msgs.msg import Image
from imutils import contours
from skimage import measure
import numpy as np


i = 0
class waypoint_coordinate_updater(swift):
    def __init__(self):
        super().__init__()
        self.given_coordinates = [
            [0, 0, 23],
            [-7, -7.5, 23],
            [-7, -2, 23],
            [-7, 3, 23],
            [-7, 4, 23],
            [-7, 7.5, 23],
            [-4.5, 7.5, 23],
            [-4.5, 4, 23],
            [-4.5, 3, 23],
            [-4.5, -2, 23],
            [-4.5, -7.5, 23],
            [0, -7.5, 23],
            [0, -2.5, 23],
            [0, 3.5, 23],
            [0, 4.5, 23],
            [0, 7.5, 23],
            [4, 7.5, 23],
            [4, 4, 23],
            [4, 3, 23],
            [4, -2, 23],
            [4, -7.5, 23],
            [7.5, -7.5, 23],
            [7.5, -2, 23],
            [7.5, 3, 23],
            [7.5, 4, 23],
            [7.5, 7.5, 23]

        ]
        self.bio = Biolocation()
        self.setpoint = [0,0,23]
        self.detected_setpoint = [0, 0, 0]
        self.br = CvBridge()
        self.image = None
        self.pause = False
        self.reach_base = False
        self.alien = "alien_b"

        self.Kp = [110*0.1,110*0.07,130*0.07]
        self.Ki = [7*0.0001,0,8*0.0001]
        self.Kd = [8*0.7, 2*0.3, 595*0.3] 

        #Publishers
        self.alien_pub = rospy.Publisher('/astrobiolocation', Biolocation, queue_size=10)

         # Subscribers
        rospy.Subscriber("/swift/camera_rgb/image_raw",Image,self.callback)

    def callback(self, msg):
        '''CallBack function for swift camera subscriber'''
        self.image=msg
        self.imager = self.br.imgmsg_to_cv2(msg)
    
    def corrections_toSetpoint(self, ledc):
        '''Function to find the centroid and corrections to approach setpoint'''
        tx = []
        ty = []
        final_x = 0
        final_y = 0
        centroid = ()
        # if len(ledc) == 2:
        #     alien = "alien_a"
        # elif len(ledc) == 3:
        #     alien = "alien_b"
        # elif len(ledc) == 4:
        #     alien = "alien_c"

        for i in ledc:
            tx.append(i[0])
            ty.append(i[1])
        centroid = (sum(tx)/len(ledc), sum(ty)/len(ledc))
        #print(centroid)
        if not self.reach_base:
            print(centroid)
            if self.drone_position[0]<0 and self.drone_position[1]>0:
                if centroid[0]>50:
                    final_x+=0.5

                if centroid[1]<460:
                    final_y-=0.5

            elif self.drone_position[0]<0 and self.drone_position[1]<0:
                if centroid[0]>50:
                    final_x+=0.5

                if centroid[1]>50:
                    final_y+=0.5

            elif self.drone_position[0]>0 and self.drone_position[1]<0:
                if centroid[0]<460:
                    final_x-=0.5

                if centroid[1]>50:
                    final_y+=0.5

            elif self.drone_position[0]>0 and self.drone_position[1]>0:
                if centroid[0]<460:
                    final_x-=0.5

                if centroid[1]<460:
                    final_y-=0.5

            
            
            #self.reach_base = True

        return (final_x, final_y)



    def image_processing_function(self):
        '''Function dedicated to Image processing'''
        if self.image is not None:
            image = self.imager
            imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            imgray = cv2.GaussianBlur(imgray, (1,1), 0)
            _, thresh = cv2.threshold(imgray, 211, 255, cv2.THRESH_BINARY)
            thresh = cv2.erode(thresh, None, iterations=2)
            thresh = cv2.dilate(thresh, None, iterations=4)
            labels = measure.label(thresh, connectivity=2, background=0)
            mask = np.zeros(thresh.shape, dtype="uint8")
            for label in np.unique(labels):
                if label == 0:
                    continue
                labelMask = np.zeros(thresh.shape, dtype="uint8")
                labelMask[labels == label] = 255
                numPixels = cv2.countNonZero(labelMask)

                if numPixels > 10:
                    mask = cv2.add(mask, labelMask)
            cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(cnts) != 0:
                cnts = contours.sort_contours(cnts)[0]
                cntrd = []
                areas = []
                a = len(cnts)
                for c in cnts:
                    area = cv2.contourArea(c)
                    M = cv2.moments(c)
                    if M["m00"] != 0:
                        cx = float(M["m10"] / M["m00"])
                        cy = float(M["m01"] / M["m00"])
                    areas.append(area)
                    cntrd.append((cx, cy))
                if len(cntrd) != 0:
                     if len(cntrd) != 0:
                        self.pause = True
                        correction1, correction2 = self.corrections_toSetpoint(cntrd)
                        self.detected_setpoint = [self.drone_position[0] + correction1, self.drone_position[1] + correction2, 21]
                    #self.pause = True
                    # if len(cntrd) == 2:
                    #     self.alien = "alien_a"
                    # elif len(cntrd) == 3:
                    #     self.alien = "alien_b"
                    # elif len(cntrd) == 4:
                    #     self.alien = "alien_c"
                    # self.detected_setpoint = [int(self.drone_position[0]+0.5), int(self.drone_position[1]+0.5), 21]

    def run(self):
        self.image_processing_function()
        if self.pause: #and #not self.reach_base:
            self.setpoint = self.detected_setpoint
            global i
            if i == 0:
                self.bio.organism_type = self.alien
                self.bio.whycon_x = self.drone_position[0]
                self.bio.whycon_y = self.drone_position[1]
                self.bio.whycon_z = self.drone_position[2]
                self.alien_pub.publish(self.bio)
                i = 1

        else:
            if -0.99 <= self.error[0] <= 0.99 and -0.99 <= self.error[1] <= 0.99 and -0.99 <= self.error[2] <= 0.99:
                if not self.reach_base:
                    if self.setpoint != [7, 7, 23] and (self.setpoint in self.given_coordinates):
                        self.given_coordinates.remove(self.setpoint)
                        self.setpoint = self.given_coordinates[0]
                    else:
                        self.setpoint = [7, 7, 23]
                else:
                    pass


if __name__ == '__main__':

    swift_drone = waypoint_coordinate_updater()
    #start_time = time.time()
    r = rospy.Rate(29.99) #specify rate in Hz based upon your desired PID sampling time, i.e. if desired sample time is 33ms specify rate as 30Hz
    while not rospy.is_shutdown():
        swift_drone.pid()
        swift_drone.run()
        r.sleep()