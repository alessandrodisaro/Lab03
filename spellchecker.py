import time

import multiDictionary as md


class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        lista_corrette=[]
        diz=md.MultiDictionary()
        txtInLowered=txtIn.lower()

        ##### correggo i caratteri
        txtInCorrect=self.replaceChars(txtInLowered)

        print("Ricerca con 'Contains': ")
        time_stamp_start = time.time()                 # qua prendo il timestamp di qaundo inizio
        lista_corrette = diz.searchWord(txtInCorrect, language)
        cnt=False # contatore per vedere se ne ha sritta almeno una
        for parola in lista_corrette:
            if parola.corretta==False:
                print(parola)
                cnt=True
        time_stamp_finish= time.time() # qua predno il timestamp di fine
        if cnt==False:
            print("Nessun errore")
        print(f"Tempo impiegato: {time_stamp_finish-time_stamp_start} ")   # faccio la differenza per ottenere il tempo di processo

        # qua inserisci poi le chiamate per gli altri tipi di ricerca


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


    def replaceChars(self,text):
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            text = text.replace(c, "")
        return text
