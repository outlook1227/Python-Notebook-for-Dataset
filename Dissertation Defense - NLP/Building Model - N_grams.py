import os, re, string, itertools
import numpy as np
import pickle
import matplotlib.pyplot as plt
import pickle as cPickle
import warnings
warnings.filterwarnings('ignore')
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
from 

class FileData(object):
    def __init__(self, path):
        self.path = path
        with open(path, encoding='utf-16') as f:
          self.data = f.read()
          #print(self.data)

ABSOLUTE_PATH = "/content/drive/MyDrive/Dissertation_Defense/Dataset/Train_Full"

c_tri =  "/Chinh tri Xa hoi"

d_song = "/Doi song"

khoa_hoc = "/Khoa hoc"

kinh_doanh = "/Kinh doanh"

p_luat = "/Phap luat"

suc_khoe = "/Suc khoe"

the_gioi = "/The gioi"

the_thao = "/The thao"

van_hoa = "/Van hoa"

vi_tinh = "/Vi tinh"

corpus = [c_tri, d_song, khoa_hoc, kinh_doanh, p_luat, suc_khoe, the_gioi, the_thao, van_hoa, vi_tinh]

for folder in range(len(corpus)):
    corpus[folder] = ABSOLUTE_PATH + corpus[folder]

file_list = []
#count = 0

for folder_path in corpus:
    count = 0
    for name in os.listdir(folder_path):
        count +=1
        if count == 300:
          break
        path = os.path.join(folder_path, name)
        if not os.path.isfile(path):
            continue
        file = FileData(path)
        file_list.append( file.data )

print("Total files:", len(file_list))

pk_path = '/content/drive/MyDrive/Dissertation_Defense/Dataset/train.p'

with open(pk_path, "wb") as f:
    cPickle.dump(file_list, f)

with open(pk_path, "rb") as f:
    data = cPickle.load(f)

alphabet = '^[ _abcdefghijklmnopqrstuvwxyz0123456789áàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđ!\"\',\-\.:;?_\(\)]+$'

def latin_extract(data):

    # extract Latin- characters only

    latin_extract_data=[]
    # duyet qua tung van ban
    for i in data:
      if i == 1:
        break
      # thay the xuong dong la dau cham ket thuc
      i=i.replace("\n",".")
      # tach van ban theo dau cham ket thuc
      sentences=i.split(".")
      for j in sentences:
          #print("j hien tai = ", j)
          # print( "split=", j.split() )
          # print(len(j.split()))
          if len(j.split()) > 2 and re.match(alphabet, j.lower()):

              latin_extract_data.append(j)
              # print("j moi = ",j)

    return latin_extract_data

training_data = latin_extract(data)
print(len(training_data))
training_data[10]

def extract_phrases(text):
    return re.findall(r'\w[\w ]+', text)

phrases = itertools.chain.from_iterable(extract_phrases(text) for text in training_data)
phrases = [p.strip() for p in phrases if len(p.split()) > 1]

def _extract_phrases(data):
    phrases = itertools.chain.from_iterable(extract_phrases(text) for text in data)
    phrases = [p.strip() for p in phrases if len(p.split()) > 1]

    return phrases

phrases = _extract_phrases(training_data)

print(len(phrases))
print(phrases[10])

def gen_ngrams(words, n=2):
    return ngrams(words.split(), n)

def generate_bi_grams(phrases):
    list_ngrams = []
    for p in tqdm(phrases):

      # neu khong nham trong bang chu cai thi bo qua
      if not re.match(alphabet, p.lower()):
        continue

      # tach p thanh cac bi gram
      for ngr in gen_ngrams(p, NGRAM):
        if len(" ".join(ngr)) < MAXLEN:
          list_ngrams.append(" ".join(ngr))

    return list_ngrams
