#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from tf.transformations import euler_from_quaternion
import numpy as np
import time

class TurtleControl:

    def __init__(self):
        rospy.init_node("tb3control_node", anonymous=True)
        self.vel_publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        rospy.Subscriber("/odom", Odometry, self.update_pose)
        rospy.Subscriber("/scan", LaserScan, self.update_scan)
        self.pose = Pose()
        self.rate = rospy.Rate(10)
        self.max_vel = 0.22
        self.max_ang = 2.84
    
    def update_pose(self, msg):
        orientation_q = msg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
        self.pose.x = msg.pose.pose.position.x
        self.pose.y = msg.pose.pose.position.y
        self.pose.theta =  yaw
        
    def update_scan(self, msg):
        self.scan = msg
    
    def ref_distance(self, ref_pose):
        return np.sqrt(  (ref_pose.x - self.pose.x)**2 + (ref_pose.y - self.pose.y)**2)

    def linear_vel_control(self, ref_pose, kp = 1.5):
        distance = self.ref_distance(ref_pose)
        control = kp* distance
        if abs(control) > self.max_vel:
            control = self.max_vel*np.sign(control)
        return control

    def angular_vel_control(self, ref_pose, kp=6):
        angle_r = np.arctan2(ref_pose.y - self.pose.y,  ref_pose.x - self.pose.x )        
        control = kp*(angle_r - self.pose.theta)
        if abs(control) > self.max_ang:
            control = self.max_ang*np.sign(control)
        return control

    def move2ref(self, x_ref, y_ref):
        ref_pose = Pose()
        ref_pose.x = x_ref
        ref_pose.y = y_ref
        ref_tol = 0.01
        vel_msg = Twist()
        colisao = False
        bot = TurtleControl()
        
        while self.ref_distance(ref_pose) >= ref_tol:
            for i in self.scan.ranges:
            	if(i<0.5):
            	    colisao = True
            	    
            if(colisao==False):
                vel_msg.linear.x = self.linear_vel_control(ref_pose)
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = self.angular_vel_control(ref_pose)
                self.vel_publisher.publish(vel_msg)
                self.rate.sleep()
            else:
                break
        vel_msg.linear.x = 0
        vel_msg.angular.z= 0
        self.vel_publisher.publish(vel_msg)
                
        if(colisao==True):
            rospy.loginfo("Colisão iminente detectada!\n")
            ref_pose.x = self.pose.x - 0.5
            ref_pose.y = self.pose.y - 0.5
            while self.ref_distance(ref_pose) >= ref_tol:
                vel_msg.linear.x = self.linear_vel_control(ref_pose)
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = self.angular_vel_control(ref_pose)
                self.vel_publisher.publish(vel_msg)
                self.rate.sleep()
           

        
        while not rospy.is_shutdown():
            rospy.loginfo("Coordenada X:")
            x = int(input())
            rospy.loginfo("Coordenada Y:")
            y = int(input())
            bot.move2ref(x, y)

if __name__ == '__main__':
    bot = TurtleControl()
    rospy.loginfo("\n\nINICIANDO SIMULADOR...\n")
    rospy.sleep(5)
    rospy.loginfo("Coordenada X:")
    x = int(input())
    rospy.loginfo("Coordenada Y:")
    y = int(input())
    bot.move2ref(x, y)



