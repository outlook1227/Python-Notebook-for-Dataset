import numpy as np
import string, re
from collections import Counter 
from nltk.util import ngrams
from keras.models import load_model
import warnings
warnings.filterwarnings("ignore")
import time

N_GRAM = 2
MAX_LENGTH = 30
link_model = "spell_tiendo2k1_128_256_0.001_n_grams_0.99-1.hdf5"
model = load_model(link_model)
model.make_predict_function()

class Spell_Corrections(object):
    def __init__(self):
        self.maxlen = MAX_LENGTH
        
        self.model = model

        self.alphabet = ['\x00', ' ', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
                        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        'á', 'à', 'ả', 'ã', 'ạ', 'â', 'ấ', 'ầ', 'ẩ', 'ẫ', 'ậ', 'ă', 'ắ', 'ằ', 
                        'ẳ', 'ẵ', 'ặ', 'ó', 'ò', 'ỏ', 'õ', 'ọ', 'ô', 'ố', 'ồ', 'ổ', 'ỗ', 'ộ', 'ơ', 'ớ', 'ờ', 
                        'ở', 'ỡ', 'ợ', 'é', 'è', 'ẻ', 'ẽ', 'ẹ', 'ê', 'ế', 'ề', 'ể', 'ễ', 'ệ', 'ú', 'ù', 'ủ', 
                        'ũ', 'ụ', 'ư', 'ứ', 'ừ', 'ử', 'ữ', 'ự', 'í', 'ì', 'ỉ', 'ĩ', 'ị', 'ý', 'ỳ', 'ỷ', 'ỹ', 'ỵ', 'đ', 
                        'Á', 'À', 'Ả', 'Ã', 'Ạ', 'Â', 'Ấ', 'Ầ', 'Ẩ', 'Ẫ', 'Ậ', 'Ă', 'Ắ', 'Ằ', 'Ẳ', 'Ẵ', 'Ặ', 'Ó', 'Ò', 'Ỏ', 'Õ', 'Ọ', 'Ô', 'Ố',
                        'Ồ', 'Ổ', 'Ỗ', 'Ộ', 'Ơ', 'Ớ', 'Ờ', 'Ở', 'Ỡ', 'Ợ', 'É', 'È', 'Ẻ', 'Ẽ', 'Ẹ', 'Ê', 'Ế', 'Ề', 'Ể', 
                        'Ễ', 'Ệ', 'Ú', 'Ù', 'Ủ', 'Ũ', 'Ụ', 'Ư', 'Ứ', 'Ừ', 'Ử', 'Ữ', 'Ự', 'Í', 'Ì', 'Ỉ', 'Ĩ', 'Ị', 'Ý', 'Ỳ', 'Ỷ', 'Ỹ', 'Ỵ', 'Đ']
        
        self.letters = list("abcdefghijklmnopqrstuvwxyzáàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗ\
                            ộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđABCDEFGHIJKLMNO\
                            PQRSTUVWXYZÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÉÈẺẼẸÊẾỀỂỄ\
                            ỆÚÙỦŨỤƯỨỪỬỮỰÍÌỈĨỊÝỲỶỸỴĐ")
        
        self.accepted_char = list((string.digits + ''.join(self.letters)))
              
    def extract_phrases(self, text):
        pattern = r'\w[\w ]*|\s\W+|\W+'
        return re.findall(pattern, text)

    def encoder_data(self, text):
        # Add "\x00" padding at the end of 2-grams in order to equal their length
        text = "\x00" + text
        x = np.zeros((self.maxlen, len(self.alphabet)))
        for i, c in enumerate(text[:self.maxlen]):
            x[i, self.alphabet.index(c)] = 1
        if i < self.maxlen - 1:
            for j in range(i + 1, self.maxlen):
                x[j, 0] = 1
        return x
        
    def decoder_data(self, x):
        x = x.argmax(axis = -1)
        return ''.join(self.alphabet[i] for i in x)
    
    def word_segmentation(self, words, n = N_GRAM):
        # Word segmentation with n_grams (Give n_gram = 2)
        return ngrams(words.split(), n)
    
    def guess(self, n_gram):
        # Model prediction for the word has corrected is true
        text = " ".join(n_gram)
        prediction = self.model.predict(np.array([self.encoder_data(text)]), verbose=0)
        return self.decoder_data(prediction[0]).strip('\x00')

    def correction(self, sentence):
        "Result the correction sentence from the model prediction"
        # Checking for the sentence has information in the character
        start_time = time.time()
        for i in sentence:
            if i not in self.accepted_char:
                sentence = sentence.replace(i, " ")

        # The text has segmented with n_grams
        n_grams = list(self.word_segmentation(sentence, n = N_GRAM))
        guess_n_grams = list(self.guess(n_gram) for n_gram in n_grams)

        # Show the n_grams word has segmented
        print("N-Grams:", n_grams)
        print(" " * 20)
        print("Guess N-Grams:", guess_n_grams)
        print("-" * 20)

        # Count the word of sentence and result the sentence has corrected
        candidates = [Counter() for _ in range(len(guess_n_grams) + N_GRAM - 1)]
        for n_index, n_gram in (enumerate(guess_n_grams)):
            for w_index, word in (enumerate(re.split(" +", n_gram))):
                candidates[n_index + w_index].update([word])
       
        output = " ".join(c.most_common(1)[0][0] for c in candidates)
        end_time = time.time()

        # Compute the time for processing data and correction
        execution_time = end_time - start_time
        print(f"Time for processing and correction: {execution_time:.4f} seconds")
        print("-" * 20)
        return output
    
    def call(self, sentence):
        # Call the sentence in Vietnamese has been corrected
        guess = self.correction(sentence)
        return guess
