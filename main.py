import spellchecker

sc = spellchecker.SpellChecker()
live = True  # per dire al programma quando stopparsi
while (live):
    sc.printMenu()

    txtIn = input()
    # Add input control here!


    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn, "italian")
        break   # vedi se ce un modo migliore di uscire dal while1

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn, "english")
        break

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn, "spanish")
        break

    if int(txtIn) == 4:
        break
