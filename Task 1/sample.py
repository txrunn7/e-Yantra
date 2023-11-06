#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import numpy as np

class Nodo(object):
    def __init__(self):
        rospy.init_node('whycon_display_image_view')
        self.image = None
        self.br = CvBridge()
        self.loop_rate = rospy.Rate(30)

        rospy.Subscriber("/swift/camera_rgb/image_raw", Image, self.callback)

    def callback(self, msg):
        rospy.loginfo('Image received...')
        self.image = self.br.imgmsg_to_cv2(msg)

    def infocheck(self):
        print(self.image)
    def start(self):
        rospy.loginfo("Timing images")
        rospy.spin()
        rospy.loginfo('processing image')
        #br = CvBridge()
        
        imgray=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        imgray=cv2.GaussianBlur(imgray,(1,1),0)
        _,thresh=cv2.threshold(imgray,211,255,cv2.THRESH_BINARY)

        thresh = cv2.erode(thresh, None, iterations=2)
        thresh = cv2.dilate(thresh, None, iterations=4)

        labels=measure.label(thresh, connectivity=2,  background=0)
        mask = np.zeros(thresh.shape, dtype="uint8")

        for label in np.unique(labels):
            if label == 0:
                continue

            labelMask = np.zeros(thresh.shape, dtype="uint8")
            labelMask[labels == label] = 255
            numPixels = cv2.countNonZero(labelMask)
            if numPixels > 10:
                mask = cv2.add(mask, labelMask)

        cnts,_=cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts=contours.sort_contours(cnts)[0]

        cntrd=[]
        areas=[]
        a=len(cnts)
        for c in cnts:
            area=cv2.contourArea(c)
            M = cv2.moments(c)
            if M["m00"] != 0:
                cx = float(M["m10"] / M["m00"])
                cy = float(M["m01"] / M["m00"])

            areas.append(area)
            cntrd.append((cx,cy))

            if not cntrd:
                rospy.loginfo("No contours found")
        with open("temp.txt", "a+") as file:
            file.write([areas, cntrd])
        self.loop_rate.sleep()
'''          
if __name__ == '__main__':
    rospy.init_node("imagetimer111", anonymous=True)
    my_node = Nodo()
    my_node.infocheck()
'''
if __name__ == '__main__':

    swift_drone = Nodo()
    r = rospy.Rate(30) #specify rate in Hz based upon your desired PID sampling time, i.e. if desired sample time is 33ms specify rate as 30Hz
    while not rospy.is_shutdown():
        swift_drone.start()
        r.sleep()
