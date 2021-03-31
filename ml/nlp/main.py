# deps.
import numpy as np
import tensorflow as tf

# ext. modules
from preprocessing import encoding
from read import read_ds
from model import history

# READ DATA
sentences, labels, urls = read_ds()

# ENCODE DATA
sequences, padded = encoding(sentences)

# TRAIN TEST SPLIT
vocab_size = 26709
training_size = 20000
testing_size = 6709

training_sentences = sentences[0:training_size]
testing_sentences = sentences[training_size:]
training_labels = sentences[0:testing_size]
testing_labels = sentences[testing_size:]

# get the new fitted model to just the training_sentences
training_sequences, training_padded = encoding(training_sentences)
testing_sequences, testing_padded = encoding(testing_sentences)
# numpy casting
training_sentences = np.array(training_sentences)
training_padded = np.array(training_padded)
testing_sequences = np.array(testing_sequences)
testing_padded = np.array(testing_padded)

history = history(training_padded, training_labels, testing_padded, testing_labels)

print(history)

