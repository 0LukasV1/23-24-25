import random
import string

alphabet = string.ascii_lowercase

otazka = input('zadaj 1 ak kodujes a 2 ak dekodujes:')

res_file = open('vystupny_text.txt','w',encoding='utf-8')

premenna = ''
if otazka == '1':
    with open('vstupny_text.txt','r',encoding= 'utf-8') as fp:
        for line in fp:
            key = random.randrange(0,25)
            res_file.write(alphabet[key-1])
            for i in line:
                if i in alphabet:
                    indexos = alphabet.find(i)
                    novy_index = indexos + key
                    if novy_index >= len(alphabet):
                        novy_index = novy_index - len(alphabet)
                        res_file.write(alphabet[novy_index])
                        premenna += alphabet[novy_index]
                    else:
                        res_file.write(alphabet[novy_index])
                        premenna += alphabet[novy_index]
                elif i == ' ':
                    res_file.write(' ')
                    premenna += ' '
                else:
                    res_file.write(i)
                    premenna += i
else:
    with open('zasifrovany_text_2.txt','r',encoding= 'utf-8') as fp:
        for line in fp:
            key2 = alphabet.find(line[0]) + 1
            for j in line[1::]:
                if j in alphabet:
                    indexos2 = alphabet.find(j)
                    novy_index2 = indexos2 - key2
                    if novy_index2 < 0:
                        novy_index2 = len(alphabet) + novy_index2
                        res_file.write(alphabet[novy_index2])
                        premenna += alphabet[novy_index2]
                    else:
                        res_file.write(alphabet[novy_index2])
                        premenna += alphabet[novy_index2]
                elif j == ' ':
                    res_file.write(' ')
                    premenna += ' '
                else:
                    res_file.write(j)
                    premenna += j
