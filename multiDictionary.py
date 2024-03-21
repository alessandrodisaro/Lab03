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
            richWord = rw.RichWord(parole_input[x])
            if dizionario._dict.__contains__(parole_input[x] + "\n"):
                richWord.corretta = True
            else:
                richWord.corretta = False
            listaRichWord.append(richWord)

        return listaRichWord

    def searchWordLinear(self, words, language):
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

        # col metodo contains MA IN RICERCA LINEAR

        for parola_da_cercare in parole_input:
            richWord = rw.RichWord(parola_da_cercare)
            for current in dizionario.dict:
                if current == parola_da_cercare + "\n":
                    richWord.corretta = True
                    break
                richWord.corretta = False
            listaRichWord.append(richWord)
        return listaRichWord

    def searchWordDichotomic(self, words, language):
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
        lunghTot = len(dizionario.dict)
        mezzo_attuale = lunghTot // 2
        mezzo_precedente = mezzo_attuale  # per stopparlo quando serve  # MAGARI LEVALO
        tmp = 0  # quello che usi per fare il riposizionamento della meta in cui cercare
        # RICERCA DICOTOMICA
        for parola_da_cercare in parole_input:
            richWord = rw.RichWord(parola_da_cercare)

            trovata=False
            low = 0
            high = len(dizionario._dict) - 1
            while low <= high and not trovata:
                mezzo = (low + high) // 2
                provo = dizionario._dict[mezzo]
                if provo == parola_da_cercare+"\n":
                    richWord.corretta = True
                    trovata=True
                elif provo<(parola_da_cercare):
                    low = mezzo + 1
                elif provo>(parola_da_cercare):                     #else:  # provo < dizionario[mezzo]
                    high = mezzo - 1
            if richWord.corretta==None:
                richWord.corretta=False
            listaRichWord.append(richWord)
        return listaRichWord

