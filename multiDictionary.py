import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        pass

    def printDic(self, language):
        if language == "english":
            dizionario = d.Dictionary("english")
            dizionario.loadDictionary("resources/English.txt")
        elif language == "italian":
            dizionario = d.Dictionary("italian")
            dizionario.loadDictionary("resources/Italian.txt")
        elif language == "spanish":
            dizionario = d.Dictionary("spanish")
            dizionario.loadDictionary("resources/Spanish.txt")
        dizionario.printAll()

    def searchWord(self, words, language):

        # cerchi una specifica parola in un dizionario restituendo una lista di richword con i true o false per ogni parola
        if language == "english":
            dizionario = d.Dictionary("english")
            dizionario.loadDictionary("resources/English.txt")
        elif language == "italian":
            dizionario = d.Dictionary("italian")
            dizionario.loadDictionary("resources/Italian.txt")
        elif language == "spanish":
            dizionario = d.Dictionary("spanish")
            dizionario.loadDictionary("resources/Spanish.txt")

        parole_input = words.split()
        listaRichWord = []
        # col metodo contains

        lunghezza = len(parole_input)

        for x in range(lunghezza):
            richWord=rw.RichWord(parole_input[x])
            if dizionario._dict.__contains__(parole_input[x]+"\n"):
                richWord.corretta=True
            else:
                richWord.corretta=False
            listaRichWord.append(richWord)


        return listaRichWord













