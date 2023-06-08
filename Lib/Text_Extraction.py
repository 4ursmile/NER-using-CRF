import numpy as np
from pyvi.ViTokenizer import ViTokenizer
import re
class Text_Extraction:
    def __init__(self):
        pass
    def ExtractNameEntity(self, text):
        pattern = re.compile(r'<ENAMEX TYPE="(.*)">(.*)<')
        match = re.search(pattern, text)
        if match:
            return match.group(1), match.group(2)
        else:
            return None, None
    def Remove_punctuation(self, text):
        text = re.sub(r'[^\w\s]','',text)
        return text
    def TextConstructer(self, text):
        First = text.split('<ENAMEX TYPE="')[0]
        ft = ViTokenizer.tokenize(First)
        ft = self.Remove_punctuation(ft)
        name_lib_first = []
        for word in ft.split():
            word = word.lower()
            name_lib_first.append((word, 'O'))
        NE, word = self.ExtractNameEntity(text)
        if NE is None:
            return name_lib_first
        word = self.Remove_punctuation(word)
        lword = ViTokenizer.tokenize(word).split()
        name_lib = []
        for i, word in enumerate(lword):
            word = word.lower()
            name_lib.append((word, NE))
        return name_lib_first + name_lib
    def text_extract(self,text):
        list_text = text.split('/ENAMEX>')
        list_t = []
        for text in list_text:
            list_t += self.TextConstructer(text)
        return np.array(list_t)