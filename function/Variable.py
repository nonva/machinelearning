#!/usr/bin/python
#################################################################
#
#    file: Variable.py
#   usage: ./Variable.py
#   brief:
#  author: *******
#   email: *******
# created: 2017-07-21 10:28:34
#
#################################################################
import tensorflow as tf
initial = tf.truncated_normal(shape=[10,10],mean=0,stddev=1)
W=tf.Variable(initial)
list = [[1.,1.],[2.,2.]]
X = tf.Variable(list,dtype=tf.float32)
init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    print sess.run(W)
    print ("##################################")
    print sess.run(W[:2,:2])
    op = W[:2,:2].assign(22.*tf.ones((2,2)))
    print ("##################################")
    print sess.run(op)
    print ("##################################")
    print (W.eval(sess)) #computes and returns the value of this variable
    print ("##################################")
    print (W.eval())  #Usage with the default session
    print ("##################################")
    print sess.run(X)

