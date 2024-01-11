import os, re, string, itertools
import numpy as np
import pickle
import matplotlib.pyplot as plt
import pickle as cPickle
from tqdm import tqdm
from nltk.util import ngrams
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from keras.optimizers import Adam
from keras.models import load_model
from keras.callbacks import Callback, ModelCheckpoint
from noise_addition_text import SynthesizeWords
from keras import layers, models
from sklearn.model_selection import train_test_split
