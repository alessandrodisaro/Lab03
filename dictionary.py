class Dictionary:
    def __init__(self, lingua):
        self.lingua = lingua
        self._dict = []

    def loadDictionary(self, path):
        with open(path, "r") as file:   #aggiungi l enncoding utf 8 per lo spagnolo
            for line in file:
                self._dict.append(line)

    def printAll(self):
        for line in self._dict:
            print(line)

    @property
    def dict(self):
        return self._dict
