def verif_cuv(file_name, wort, neuwort):
    news = ""
    cnt = 0
    f = open(file_name, 'r')
    for line in f:
        words = line.split(" ")
        for word in words:
            word = word.strip()
            if word == wort:
                news += neuwort
                cnt += 1
            else:
                news += word
            news += ' '
        news +='\n'
    f.close()
    f = open(file_name, 'w')
    f.write(news)
    print(f"Ersetzt {ew} durch {neuwort} an {str(cnt)} Stelle")

neuwort = input("Mit Welches Wort willst du ersetzen ? ")
ew = input("Wort zu ersetzen: ")
verif_cuv("Satz.txt", ew, neuwort)