""" Pipeline for softmax optimization experiments

Author: Francois Fagan
"""

from load_data import load_data
from run import run
import pickle
import time
import sys

t0 = time.time()

# Parameters (in the future can pass these in from the command line)
learning_rate = 0.0001
epochs = 1
num_epochs_record = 1
num_sampled = 5
num_repeat = 1
sgd_name = 'LogTricks'  # 'Implicit' # 'Softmax'  #
dataset_name = 'mnist'  # 'Eurlex'  # 'Delicious' # 'Bibtex'  # 'LSHTC' # 'AmazonCat' #

if len(sys.argv) > 1:
    sgd_name = sys.argv[1]
    dataset_name = sys.argv[2]

# for sgd_name in ['Umax', 'Implicit', 'Softmax']:
#     for dataset_name in ['LSHTC']: #['Eurlex', 'Delicious', 'Bibtex']:
print(sgd_name, dataset_name)

# if sgd_name in {'softmax'}:
#
# else:
train, test = load_data(dataset_name)
results = run(train, test, learning_rate, num_epochs_record, num_repeat, epochs, sgd_name, num_sampled)
pickle.dump(results, open('./Results/' + sgd_name + '_' + dataset_name + '.p', 'wb'))

t1 = time.time()
print('Time', t1 - t0)
