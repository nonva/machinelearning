#!/usr/bin/python
#################################################################
#
#    file: train_captcha.py
#   usage: ./train_captcha.py
#   brief:
#  author: *******
#   email: *******
# created: 2017-08-01 15:52:05
#
#################################################################
import tensorflow as tf
import numpy as np
import string
import generate_captcha
import captcha_model

if __name__ == '__main__':
    captcha = generate_captcha.generateCaptcha()
    width,height,char_num,characters,classes = captcha.get_parameter()

    x = tf.placeholder(tf.float32, [None, height,width,1])
    y_ = tf.placeholder(tf.float32, [None, char_num*classes])
    keep_prob = tf.placeholder(tf.float32)

    model = captcha_model.captchaModel(width,height,char_num,classes)
    y_conv = model.create_model(x,keep_prob)
    #cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_,logits=y_conv))
    cross_entropy = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=y_,logits=y_conv))
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

    predict = tf.reshape(y_conv, [-1,char_num, classes])
    real = tf.reshape(y_,[-1,char_num, classes])
    correct_prediction = tf.equal(tf.argmax(predict,2), tf.argmax(real,2))
    correct_prediction = tf.cast(correct_prediction, tf.float32)
    accuracy = tf.reduce_mean(correct_prediction)

    saver = tf.train.Saver()
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.95)
    with tf.Session(config=tf.ConfigProto(log_device_placement=False,gpu_options=gpu_options)) as sess:
        sess.run(tf.global_variables_initializer())
        step = 1
        while True:
            batch_x,batch_y = next(captcha.gen_captcha(64))
            _,loss = sess.run([train_step,cross_entropy],feed_dict={x: batch_x, y_: batch_y, keep_prob: 0.75})
            print ('step:%d,loss:%f' % (step,loss))
            if step % 100 == 0:
                batch_x_test,batch_y_test = next(captcha.gen_captcha(100))
                acc = sess.run(accuracy, feed_dict={x: batch_x_test, y_: batch_y_test, keep_prob: 1.})
                print ('###############################################step:%d,accuracy:%f' % (step,acc))
                if acc > 0.99:
                    saver.save(sess,"./capcha_model.ckpt")
                    break
            step += 1

