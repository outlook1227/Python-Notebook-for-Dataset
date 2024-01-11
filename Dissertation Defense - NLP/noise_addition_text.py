import numpy as np
import re
import nltk
nltk.download('punkt')
from nltk import word_tokenize
import unidecode
from type import type_rhyme, word_couples
import string
import skfuzzy as fuzzy

class SynthesizeWords(object):
    def __init__(self): 
        # Implement for Vietnamese (29 letters) in alphabet
        self.vietnamese_alphabet = ["a", "ă", "â", "b", "c", "d", "đ", "e", "ê", "g", "h", "i", "k", "l", 
                                    "m", "n", "o", "ô", "ơ", "p", "q", "r", "s", "t", "u", "ư", "v", "x", "y"]
        
        self.len_vn_alphabet = len(self.vietnamese_alphabet)

        self.vie_alphabet_upper = [vn_alphabet.upper() for vn_alphabet in self.vietnamese_alphabet]

        self.words_segmentation = word_tokenize

        # Implement the Vietnamese Telex type keyboard (A letter of Vietnamese)
        self.vietnamese_type_keyboard = {"ă":"aw","â":"aa","á":"as","à":"af","ả":"ar","ã":"ax","ạ":"aj","ắ":"aws","ổ":"oor","ỗ":"oox","ộ":"ooj","ơ":"ow",
                  "ằ":"awf","ẳ":"awr","ẵ":"awx","ặ":"awj","ó":"os","ò":"of","ỏ":"or","õ":"ox","ọ":"oj","ô":"oo","ố":"oos","ồ":"oof",
                  "ớ":"ows","ờ":"owf","ở":"owr","ỡ":"owx","ợ":"owj","é":"es","è":"ef","ẻ":"er","ẽ":"ex","ẹ":"ej","ê":"ee","ế":"ees","ề":"eef",
                  "ể":"eer","ễ":"eex","ệ":"eej","ú":"us","ù":"uf","ủ":"ur","ũ":"ux","ụ":"uj","ư":"uw","ứ":"uws","ừ":"uwf","ử":"uwr","ữ":"uwx",
                  "ự":"uwj","í":"is","ì":"if","ỉ":"ir","ị":"ij","ĩ":"ix","ý":"ys","ỳ":"yf","ỷ":"yr","ỵ":"yj","đ":"dd",
                  "Ă":"Aw","Â":"Aa","Á":"As","À":"Af","Ả":"Ar","Ã":"Ax","Ạ":"Aj","Ắ":"Aws","Ổ":"Oor","Ỗ":"Oox","Ộ":"Ooj","Ơ":"Ow",
                  "Ằ":"AWF","Ẳ":"Awr","Ẵ":"Awx","Ặ":"Awj","Ó":"Os","Ò":"Of","Ỏ":"Or","Õ":"Ox","Ọ":"Oj","Ô":"Oo","Ố":"Oos","Ồ":"Oof",
                  "Ớ":"Ows","Ờ":"Owf","Ở":"Owr","Ỡ":"Owx","Ợ":"Owj","É":"Es","È":"Ef","Ẻ":"Er","Ẽ":"Ex","Ẹ":"Ej","Ê":"Ee","Ế":"Ees","Ề":"Eef",
                  "Ể":"Eer","Ễ":"Eex","Ệ":"Eej","Ú":"Us","Ù":"Uf","Ủ":"Ur","Ũ":"Ux","Ụ":"Uj","Ư":"Uw","Ứ":"Uws","Ừ":"Uwf","Ử":"Uwr","Ữ":"Uwx",
                  "Ự":"Uwj","Í":"Is","Ì":"If","Ỉ":"Ir","Ị":"Ij","Ĩ":"Ix","Ý":"Ys","Ỳ":"Yf","Ỷ":"Yr","Ỵ":"Yj","Đ":"Dd"}

        self.letters_diacritics = ['ă', 'â', 'á', 'à', 'ả', 'ã', 'ạ', 'ắ', 'ổ', 'ỗ', 'ộ', 'ơ', 'ằ', 'ẳ', 
                                    'ẵ', 'ặ', 'ó', 'ò', 'ỏ', 'õ', 'ọ', 'ô', 'ố', 'ồ', 'ớ', 'ờ',
                                    'ở', 'ỡ', 'ợ', 'é', 'è', 'ẻ', 'ẽ', 'ẹ', 'ê', 'ế', 'ề', 'ể', 'ễ', 'ệ', 
                                    'ú', 'ù', 'ủ', 'ũ', 'ụ', 'ư', 'ứ', 'ừ', 'ử', 'ữ', 'ự', 'í', 
                                    'ì', 'ỉ', 'ị', 'ĩ', 'ý', 'ỳ', 'ỷ', 'ỵ', 'đ',
                                    'Ă', 'Â', 'Á', 'À', 'Ả', 'Ã', 'Ạ', 'Ắ', 'Ổ', 'Ỗ', 'Ộ', 'Ơ', 'Ằ', 'Ẳ', 'Ẵ', 'Ặ', 'Ó', 'Ò', 'Ỏ', 'Õ', 
                                    'Ọ', 'Ô', 'Ố', 'Ồ', 'Ớ', 'Ờ', 'Ở', 'Ỡ', 'Ợ', 'É', 'È', 'Ẻ', 'Ẽ', 'Ẹ', 
                                    'Ê', 'Ế', 'Ề', 'Ể', 'Ễ', 'Ệ', 'Ú', 'Ù', 'Ủ', 'Ũ', 'Ụ', 'Ư', 'Ứ', 'Ừ', 'Ử', 
                                    'Ữ', 'Ự', 'Í', 'Ì', 'Ỉ', 'Ị', 'Ĩ', 'Ý', 'Ỳ', 'Ỷ', 'Ỵ', 'Đ']
        
        self.type_rhyme = type_rhyme()
        self.word_couples = word_couples()

        self.letter_couples =  [["s", "x"], ["x", "s"], ["ch", "tr"], ["tr", "ch"],["gi", "d"], ["d", "gi"], ["r", "d"], ["d", "r"],
                               ["r", "gi"],["gi", "r"], ["i", "y"], ["y", "i"], ["ng", "ngh"], ["ngh", "ng"], ["g", "ng"], ["l", "n"], 
                               ["n", "l"]]
        
        self.teencode_dictionary = {"mình" : ["mk", "mjk", "mik"], "thôi" : ["thui", "thoy", "hoy"], "vui" : ["zui"], "hôn" : ["hun"],
                                    "không" : ["k", "ko", "khum", "hổng", "hong", "kh", "hok"], "vậy" : ["z", "zậy"], 
                                    "anh" : ["a"], "em" : ["e"], "yêu" : ["iu"], "tôi" : ["t", "tui"], "tao" : ["t"], "mày" : ["m"],
                                    "chồng" : ["ck"], "vợ" : ["vk"], "nhiều" : ["nhìu"], "bạn" : ["b"], "giờ" : ["h"],
                                    "rồi" : ["rùi", "r"], "biết" : ["bít", "bjk"], "vời" : ["zời"], "ôi" : ["ui"], "quá" : ["wá"], 
                                    "sao" : ["seo"], "buồn" : ["bùn"], "muốn" : ["mún"], "uống" : ["ún"], "à" : ["ah", "ak", "ò"],
                                    "ừ" : ["uhm", "uh", "ỏ", "ừa"], "lắm" : ["lém", "nhắm"], "luôn" : ["lun"], "với" : ["vs"], "tức" : ["tứk"],
                                    "nhé" : ["nha", "nhó", "nhá", "ó"], "mà" : ["mò"], "chơi" : ["chs"], "chết" : ["chít", "chiết"]}

        self.get_all_letters_couples = self.get_all_letter_couples()
        self.all_word_couples = self.get_all_word_couples(self.word_couples)
        self.string_all_word_couples = ' '.join(self.all_word_couples)

    def replace_teencode(self, words):
        # Random selection for the list of teencode words in top line
        suggestions = self.teencode_dictionary.get(words, None)
        if suggestions is None:
            chosen_words = 0
        else:
            chosen_words = np.random.randint(0, len(suggestions))
        return suggestions[chosen_words]

    def get_all_word_couples(self, word_couple):
        all_word_couples = []
        for couples in word_couple:
            all_word_couples.extend(couples)
        return all_word_couples

    def get_all_letter_couples(self, ):
        all_letter_couples = []
        for couples in self.letter_couples:
            all_letter_couples.extend(couples)
        return all_letter_couples
    
    def replace_char_couples(self, letter):
        # Return a homophone or char word in the text 
        for couple in self.letter_couples:
            for i in range(2):
                if couple[i] == letter:
                    if i == 0:
                        return couple[1]
                    else:
                        return couple[0]
                    
    def replace_word_candidate(self, word):
        # Return a homophone word of the input word.
        capital_flag = word[0].isupper()
        word = word.lower()
        if capital_flag and word in self.teencode_dictionary:
            return self.replace_teencode(word).capitalize()
        elif word in self.teencode_dictionary:
            return self.replace_teencode(word)

        for couple in self.word_couples:
            for i in range(2):
                if couple[i] == word:
                    if i == 0:
                        if capital_flag:
                            return couple[1].capitalize()
                        else:
                            return couple[1]
                    else:
                        if capital_flag:
                            return couple[0].capitalize()
                        else:
                            return couple[0]

    def replace_keyboard_text(self, letter):
        # Return letter is has type in keyboard
        # index = np.random.randint(0, 1)
        return self.vietnamese_type_keyboard[letter]
    
    def replace_with_type_keyboard(self, letter, one_hot_label):
        """
        Replace from a type correct letter to incorrect letter telex type

        Note: 
            - letter: A list of word has segmented (each word is one_hot_label)
            - one_hot_label: One hot array indicate position of word that has already modify, so this
            function only choose the word that do not has one hot label == 1 

        Return: A list of word segmentation has one words that replaced 
                for type Vietnamese Telex keyboard 
        """
        index = np.random.randint(0, len(one_hot_label))
        prevent_loop = 0
        while one_hot_label[index] == 1 or letter[index].isnumeric() or letter[index] in string.punctuation:
            index = np.random.randint(0, len(one_hot_label))
            prevent_loop = prevent_loop + 1
            if prevent_loop > 10:
                return False, letter, one_hot_label
                
        index_noise = index
        one_hot_label[index_noise] = 1

        word_noise = letter[index_noise]
        for i in range(len(word_noise)):
          char = word_noise[i]

          if char in self.vietnamese_type_keyboard:
            replaced = self.replace_keyboard_text(char)
            word_noise = word_noise[: i] + replaced + word_noise[i + 1:]
            letter[index_noise] = word_noise
            return True, letter, one_hot_label
        
        return True, letter, one_hot_label

    def replace_type_rhyme_keyboard(self, letters, one_hot_label):
        """
        Replace from a type correct letter to incorrect type letter rhyme

        Note:
            - letter: A list of word has segmented (each word is one_hot_label)
            - one_hot_label: One hot array indicate position of word that has already modify, so this
            function only choose the word that do not has one hot label == 1

        Return: A list of word segmentation has one words that replaced for type rhyme of Vietnamese
        pronunciation including for diacritics and letters
        """
        index = np.random.randint(0, len(one_hot_label))
        prevent_loop = 0
        while one_hot_label[index] == 1 or letters[index].isnumeric() or letters[index] in string.punctuation:
            index = np.random.randint(0, len(one_hot_label))
            prevent_loop = prevent_loop + 1
            if prevent_loop > 10:
                return False, letters, one_hot_label

        index_noise = index
        one_hot_label[index_noise] = 1
        char_noise = letters[index_noise]

        rhyme = self.type_rhyme
        for char in rhyme.keys():
            if char in char_noise:
                replaced = np.random.choice(a=rhyme[char])
                char_noise = char_noise.replace(char, replaced)
                letters[index_noise] = char_noise
                break

        return True, letters, one_hot_label

    def replace_with_homophones_words(self, letters, one_hot_label):
        """
        Replace with homophones words in the given letters. You can replace with homophones word (for writing) and 
        pronunciation is exactly the same or replace with teencode
        - In Northern Vietnamese, they always pronounce r-gi-d is z (zero), ch-tr (chicken) and s-x ()
        - You can replace with teencode, in the top of function, if the word has in the list of teencode

        Note:
            - letters: A list of word has segmented (each word is one hot label)
            - one_hot_label: A word is one hot label, and save to array and change the 
                             homophone letters in the top line

        Return: 
            True if the letter is changed successful and else False, text
        """
        candidates = []
        for i in range (len(letters)):
            if letters[i].lower() in self.all_word_couples or letters[i].lower() in self.teencode_dictionary.keys():
                candidates.append((i, letters[i]))

        if len(candidates) == 0:
            return False, letters, one_hot_label
        
        index = np.random.randint(0, len(candidates))
        prevent_loop = 0
        while one_hot_label[candidates[index][0]] == 1:
            index = np.random.choice(np.arange(0, len(candidates)))
            prevent_loop = prevent_loop + 1
            if prevent_loop > 5:
                return False, letters, one_hot_label
        
        letters[candidates[index][0]] = self.replace_word_candidate(candidates[index][1])
        one_hot_label[candidates[index][0]] == 1
        return True, letters, one_hot_label
    
    def inserting_unnecessary_letters(self, letter, one_hot_label):
        """
        Inserting for letter is unnecessary in text or sentence

        Note:
            - letters: A list of word has segmented (each word is a one_hot_label)
            - one_hot_label: One hot array indicate position of word that has already modify, so this
            function only choose the word that do not has one hot label == 1 

        Return:
            A word has been selected for random and add one letter in word
            Example: a word "cho" (give) -> chco
        """
        index = np.random.randint(0, len(one_hot_label))
        prevent_loop = 0
        chosen_letter = letter[index][np.random.randint(0, len(letter[index]))]

        while one_hot_label[index] == 1 or letter[index].isnumeric() or letter[index] in string.punctuation:
            prevent_loop = prevent_loop + 1
            if prevent_loop > 10:
                return False, letter, one_hot_label
        
        addition = chosen_letter + self.vietnamese_alphabet[np.random.randint(0, self.len_vn_alphabet)]
        letter[index] = re.sub(chosen_letter, addition, letter[index])
        one_hot_label[index] = 1
        return True, letter, one_hot_label
    
    def remove_letters(self, letter, one_hot_label):
        """
        Random selection for the letters want to remove of the sentence

        Note:
            - letters: A list of word has segmented (each word is a one_hot_label)
            - one_hot_label: one hot array indicate position of word that has already modify, so this
            function only choose the word that do not has one hot label == 1.

        Return: A letter of word will be chosen and removed from the word
        """
        index = np.random.randint(0, len(one_hot_label))
        prevent_loop = 0
        chosen_letter = letter[index][np.random.randint(0, len(letter[index]))]

        while one_hot_label[index] == 1 or letter[index].isnumeric() or letter[index] in string.punctuation:
            prevent_loop = prevent_loop + 1
            if prevent_loop > 10:
                return False, letter, one_hot_label
        
        one_hot_label[index] = 1
        letter[index] = re.sub(chosen_letter, " ", letter[index])
        return True, letter, one_hot_label

    def replace_diacritics(self, letters, one_hot_label):
        """
        Replace words or letters has diacritics (remove unidecode)

        Note:
            - letters: A list of word has segmented (each word is a one_hot_label)
            - one_hot_label: one hot array indicate position of word that has already modify, so this
            function only choose the word that do not has one hot label == 1.

        Return: A word has been removed random for diacritics
        """
        index = np.random.randint(0, len(one_hot_label))
        prevent_loop = 0
        while one_hot_label[index] == 1 or letters[index] == unidecode.unidecode(letters[index]) or letters[index] in string.punctuation:
            prevent_loop = prevent_loop + 1
            if prevent_loop > 10:
                return False, letters, one_hot_label
    
        one_hot_label[index] = 1
        letters[index] = unidecode.unidecode(letters[index])
        return True, letters, one_hot_label

    def replace_letter(self, letter, one_hot_label):
        """
        Random selection for a letter of word and replace with a letter different

        Note:
            - letters: A list of word has segmented (each word is a one_hot_label)
            - one_hot_label: one hot array indicate position of word that has already modify, so this
            function only choose the word that do not has one hot label == 1.

        Result: A letter in word has been replaced with the random letter selection
        """
        index = np.random.randint(0, len(one_hot_label))
        prevent_loop = 0
        chosen_letter = letter[index][np.random.randint(0, len(letter[index]))]

        while one_hot_label[index] == 1 or letter[index].isnumeric() or letter[index] in string.punctuation:
            prevent_loop = prevent_loop + 1
            if prevent_loop > 10:
                return False, letter, one_hot_label
        
        one_hot_label[index] = 1
        replace = self.vietnamese_alphabet[np.random.randint(0, self.len_vn_alphabet)]
        letter[index] = re.sub(chosen_letter, replace, letter[index])
        return True, letter, one_hot_label

    def swap_letters(self, letters, one_hot_label):
        # Random and swap letter of the sentences
        index = np.random.randint(0, len(one_hot_label))
        prevent_loop = 0
        char_list = list(letters)

        while one_hot_label[index] == 1 or letters[index].isnumeric() or letters[index] in string.punctuation:
            random_choice = np.random.choice(len(letters), 2, replace = False)
            prevent_loop = prevent_loop + 1
            if prevent_loop > 10:
                return False, letters, one_hot_label
            
        one_hot_label[index] == 1
        random_choice = np.random.choice(len(letters), len(one_hot_label) + 1)

        if random_choice[index] != random_choice[index + 1]:
            char_list[random_choice[index]] = self.swap_letter_in_word(char_list[random_choice[index]])
            # char_list[random_choice[index+1]] = self.swap_letter_in_word(char_list[random_choice[index+1]])
            return True, char_list, one_hot_label

        return True, letters, one_hot_label

    def swap_letter_in_word(self, word):
        # Count the letter of the word, each word is one hot label
        index_1 = np.random.randint(0, len(word))
        index_2 = np.random.randint(0, len(word))

        # Swap letter in word only if word has len > 1
        while index_2 == index_1 and len(word) > 1:
            index_2 = np.random.randint(0, len(word))

        word_list = list(word)
        word_list[index_1], word_list[index_2] = word_list[index_2], word_list[index_1]
        swapped_word = ''.join(word_list)
        return swapped_word

    def noise_addition_text(self, sentence, percent_error = 0.45, num_type_error = 7):
        ## Result the noise addition functionality has implemented in top line
        ## Example the sentence in Vietnamese: Nguyễn Thuỳ Trang - Cục trưởng cục tình báo TocoToco
        ## (English: Nguyễn Thuỳ Trang - Director of the TocoToco General Department of Intelligence)

        word_segmented = self.words_segmentation(sentence)
        one_hot_label = [0] * len(word_segmented)

        ## Give percent_error = 0.18 or percent_error = 0.45 
        ## If the generated sentence contains more noise, the model can learn and correct errors more effectively. 
        num_wrong = int(np.ceil(percent_error * len(word_segmented)))
        # num_wrong = np.random.randint(1, num_wrong + 1)
        if np.random.rand() < 0.02:
            num_wrong = 0

        ## Define Fuzzy set
        rate_error = fuzzy.trapmf(np.arange(0, 1.1, 0.1), [0, 0, 0.2, 0.5]) # Update rate_error size
        error_impact = fuzzy.trimf(np.arange(0, 1.1, 0.1), [0, 0.5, 1])

        ## Compute the impact level using Fuzzy logic
        total_error = 0
        rate = np.random.uniform(0, 1)  # Random rate error from 0 to 1
        error_rate = fuzzy.interp_membership(np.arange(0, 1.1, 0.1), rate_error, rate)
        impact = fuzzy.interp_membership(np.arange(0, 1.1, 0.1), error_impact, error_rate)
        assert len(np.arange(0, 1.1, 0.1)) == len(error_impact)

        for _ in range(0, num_wrong):
            error = np.random.randint(0, num_type_error + 1)
            # Apply error generation functions with the calculated impact level
            match error:
                case 0:
                    _, word_segmented, one_hot_label = self.replace_with_homophones_words(word_segmented, one_hot_label)
                    extra = 0.25
                case 1:
                    _, word_segmented, one_hot_label = self.inserting_unnecessary_letters(word_segmented, one_hot_label)
                    extra = 0.5
                case 2:
                    _, word_segmented, one_hot_label = self.replace_type_rhyme_keyboard(word_segmented, one_hot_label)
                    extra = 0.75
                case 3:
                    _, word_segmented, one_hot_label = self.replace_with_type_keyboard(word_segmented, one_hot_label)
                    extra = 0.75
                case 4:
                    _, word_segmented, one_hot_label = self.remove_letters(word_segmented, one_hot_label)
                    extra = 0.5
                case 5:
                    _, word_segmented, one_hot_label = self.replace_diacritics(word_segmented, one_hot_label)
                    extra = 0.25
                case 6:
                    _, word_segmented, one_hot_label = self.replace_letter(word_segmented, one_hot_label)
                    extra = 0.5
                case 7:
                    _, word_segmented, one_hot_label = self.swap_letters(word_segmented, one_hot_label)
                    extra = 0.5
                case _:
                    continue

            ## Apply the impact level to the error generation function's rate
            impact += fuzzy.defuzz(np.arange(0, 1.1, 0.1), error_impact, "centroid") * extra
            
            ## Adjust the error generation function's rate based on the impact level
            impact = np.clip(impact, 0, 1)
            total_error = max(total_error, impact)

        print("Total error: ", total_error)

        ## Remove excessive spaces before joining the words
        sentence = " ".join(word_segmented)
        sentence = re.sub(' +', ' ', sentence)
        return sentence

synthesis = SynthesizeWords()
# sentence = "Nguyễn Thuỳ Trang ứng tuyển vào cục trưởng cục tình báo TocoToco" 
sentence = "Trên thông thiên văn dưới tường địa lý"
for i in range(1, 11):
    print("Epoch for create noise:", i)
    noise_sentence = synthesis.noise_addition_text(sentence, percent_error = 0.45, num_type_error = 7)
    print(noise_sentence)
    print("-" * 15)
