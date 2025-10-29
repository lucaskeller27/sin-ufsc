# Separar as palavras da frase
frase = [x for x in input().split('-')]
cobol = 'cobol'
bug = False

print(frase)

for i in range(len(frase)):
    if frase[i][1] or frase[i][-1] != cobol[i]:
        continue
    else:
        bug = True
        break

if not bug:
    print('GRACE HOPPER')
else:
    print("BUG")