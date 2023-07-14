import tensorflow as tf

class FIFOPlugin:
  def input(self, inputfile):
      pass

  def run(self):
   q = tf.FIFOQueue(3, 'float')
   init = q.enqueue_many(([0.,0.,0.],))

   x=q.dequeue()
   y=x+1
   q_inc=q.enqueue([y])


   with tf.Session() as sess:
    init.run()

    for _ in range(0,10):
        q_inc.run()
    r,r1,r2=sess.run(x), sess.run(x), sess.run(x)
    print(r, " ", r1, " ", r2)

  def output(self, outputfile):
      pass
