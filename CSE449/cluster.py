# -*- coding: utf-8 -*-
"""cluster

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cRwy9084j69FM_gj9gFw7HH7IAnFLY8r
"""

import tensorflow as tf

# Define the cluster configuration with master and worker machines
cluster = {
    "worker": [
        "192.168.1.2:12345",  # Master laptop IP
        "192.168.1.3:12345"   # Worker laptop IP
    ]
}

# Create a cluster resolver to configure the strategy
cluster_resolver = tf.distribute.cluster_resolver.TFConfigClusterResolver(cluster)

# Create the MultiWorkerMirroredStrategy
strategy = tf.distribute.MultiWorkerMirroredStrategy(cluster_resolver)

# Print number of devices (GPUs/CPUs) in the strategy to confirm the setup
print('Number of devices: ', strategy.num_replicas_in_sync)

