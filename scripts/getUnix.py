#!/usr/bin/env python3

#BSD 3-Clause Licence
#Copyright (c) 2021 Yui Kadomura. All rights reserved.

import rospy
from std_msgs.msg import Float64
import time

rospy.init_node('getUnix')
pub = rospy.Publisher('get_Unix', Float64, queue_size=1)
rate = rospy.Rate(10)
t = 0.0

while not rospy.is_shutdown():
    t = time.time()
    print(type(time.time()),':',t)
    pub.publish(t)
    rate.sleep()
