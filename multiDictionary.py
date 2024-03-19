import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
       pass

    def printDic(self, language):
        pass

    def searchWord(self, words, language):

        #cerchi una specifica parola in un dizionario restituendo una lista di richword con i true o false per ogni parola
        if language == "english":
            dizionario=d.Dictionary("english")
            dizionario.loadDictionary("resources/English.txt")
        elif language == "italian":
            dizionario=d.Dictionary("italian")
            dizionario.loadDictionary("resources/Italian.txt")
        elif language == "spanish":
            dizionario=d.Dictionary("spanish")
            dizionario.loadDictionary("resources/Spanish.txt")


        #qua prima devi caricare il dizionario della lingua giusta E POI CONTINUI CON IL RESTO

        parole_input=words.split()
        listaRichWord=[]
        #col metodo contains
        for parola in parole_input:             # scorro tutte le parole della frase
            for entry in dizionario.dict():     # scorro tutto il dizionario
                if parola in entry:             # se la parola della frase e' contenuta in quella del dizionario
                    if parola == entry:         # se la parola e' uguale (E QUINDI GIUSTA)
                        richWord=rw.RichWord(parola)
                        richWord.corretta=True
                    else:
                        richWord=rw.RichWord(parola)
                        richWord.corretta=False
                listaRichWord.append(richWord)  # metto nella lista in base a come e'


        return listaRichWord

