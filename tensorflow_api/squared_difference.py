#!/usr/bin/python
#################################################################
#
#    file: squared_difference.py
#   usage: ./squared_difference.py
#   brief:
#  author: *******
#   email: *******
# created: 2017-07-21 16:06:55
#
#################################################################
import tensorflow as tf
import numpy as np

initial_x = [[1.,1.],[2.,2.]]
x = tf.Variable(initial_x,dtype=tf.float32)
initial_y = [[3.,3.],[4.,4.]]
y = tf.Variable(initial_y,dtype=tf.float32)
diff = tf.squared_difference(x,y)
init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    print sess.run(diff)

