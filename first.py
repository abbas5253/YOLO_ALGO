import tensorflow as tf

slim = tf.contib.slim


 def darknet53(inputs):
     """
     Building CNN 
     
     """
     pass
     
def yolo(inputs,num_class,is_training=False,data_format='NCHW',reuse=False):
    
    """
    Create YOLO Model
    inputs :- a 4-D tensor [bacth_size,height,width,channels]
    num_classes :- clases to be predicted
    is_training :- data if of training or not
    reuse :- wether or not the network use its pre_trainned Variables
    
    """
    pass


def load_weights(var_list,wts_file):
    
    """
    load param and convert pre-trainned wts
    var_list :- list of network variables
    wts_file :- name of the binary file
    
    """
    
    pass

_BATCH_NORM_DECAY = 0.9
_BATCH_NORM_EPSILON = 1e-05
_LEAKY_RELU = 0.1