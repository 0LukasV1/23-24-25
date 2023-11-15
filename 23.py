import string

alphabet = string.ascii_lowercase
posun = ''
key = input('zadaj kluc')
otazka = input('zadaj 1 ak sifrujes a 2 ak desifrujes')

dlzka = len(key)
counter = 0
res = ''

entry = ''
if otazka == '1':
    with open('vstupny_text.txt','r',encoding= 'utf-8') as fp:
        for line in fp:
            entry += line
            entry = entry.replace('\n','$')
        print(entry)
        for i in entry:
            if i in alphabet:
                indexos = alphabet.find(i)+1
                poradie_text = entry.find(i,counter)
                novy_index = indexos + alphabet.find(key[poradie_text % dlzka])
                if novy_index >= len(alphabet):
                    res += alphabet[novy_index-len(alphabet)]
                    posun += key[poradie_text % dlzka]
                else:
                    res += alphabet[novy_index]
                    posun += key[poradie_text % dlzka]
            elif i == ' ':
                posun += ' '
                res += ' '
            else:
                posun += i
                res += i
            counter +=1
else:
    with open('zasifrovany_text_1.txt','r',encoding= 'utf-8') as fp:
        for line in fp:
            for i in line:
                if i in alphabet:
                    indexos = alphabet.find(i)
                    poradie_text = line.find(i,counter)
                    stary_index = alphabet.find(key[poradie_text % dlzka])+1
                    res += alphabet[indexos-stary_index]
                elif i == ' ':
                    res += ' '
                else:
                    res += i
                counter +=1
            counter = 0

print(res)