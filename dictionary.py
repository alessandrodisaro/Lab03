import spellchecker as sp

class Dictionary:
    def __init__(self, lingua):
        self.lingua = lingua
        self._dict = []
        self.spc=sp.SpellChecker()

    def loadDictionary(self, path):
        with open(path, "r", encoding='utf-8') as file:   #aggiungi l enncoding utf 8 per lo spagnolo
            for line in file:
                self._dict.append(self.spc.replaceChars(line))  # #SE PASSI SOLO LINE VA BENE PER L ITALIANO E INGLESE VA MOLTO PIU VELOCE

    def printAll(self):
        for line in self._dict:
            print(line)

    @property
    def dict(self):
        return self._dict
