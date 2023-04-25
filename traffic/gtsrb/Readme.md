Run with python3 traffic.py gtsrb

Dropout and hidden layers are irrelevant in this tutorial more hidden layers like 128 make accuracy close to no hidden layers 0.5 dropout makes 0.05 accuracy and 0.1 make 0.82 while 0.01 make 0.95

Pool size also makes no such difference for example 3 multiply 3 pool and 5 multiply 5 pool have a 2 percent deficit.

The number of filters is also not such a big deal 32 filters and 10 filters make a 2 percent deficit also 5 filters make a 4 percent deficit.

Change activation function for output layer from softmax to relu, softplus and tanh make the model unstable and reach accuracy near 0 or 1 percent.

Change activation function for convolution from relu to softmax or sigmoid increase accuracy, It looks like softmax is the best activation function.

Activation function on convolution layer make more effects in this model in compare with the output layer.

Adadelta optimizer not proper for this model Adagrad drop the accuracy 30 percent, and ftrl drop by 60 percent It looks like Adam optimizer is the fittest for this project.

Probabilistic losses, regression losses, and Hinge losses made good results but probabilistic is faster, mean-absolute-percentage-error and hinge function drop accuracy by 15 percent. We use categorical-crossentropy that make results slightly better.

For cv resize interpolation INTER_AREA is the fastest and have the most accuracy.
