#Zadanie wypisz wszystkie liczby od 1 do 1000 za pomocą liczb rzymskich

"""
Przypomnienie notacji:
I = 1.
V = 5.
X = 10.
L = 50.
C = 100.
D = 500.
M = 1 000
"""
#słownik
dict = {1:'I',5:'V',10:'X',50:"L",100:"C",500:'D',1000:'M'}

def konwert(n):
    answer = []
    lista_cyfr=list(str(n))
    #Lista kolejnych cyfr np. 413 -> [4,1,3]
    for i in range(0,len(lista_cyfr)):
        if int(lista_cyfr[i])== 0:
            pass
        elif int(lista_cyfr[i]) < 4:
            answer.append(int(lista_cyfr[i])*dict[10**(len(lista_cyfr)-i-1)])
        elif int(lista_cyfr[i]) == 4:
            answer.append(dict[10**(len(lista_cyfr)-i-1)]+dict[5*10**(len(lista_cyfr)-i-1)])
        elif int(lista_cyfr[i]) < 9:
            #answer.append(int(lista_cyfr[i])*dict[10**(len(lista_cyfr)-i-1)])
            answer.append(dict[5*10**(len(lista_cyfr)-i-1)]+((int(lista_cyfr[i])-5)*dict[(10**(len(lista_cyfr)-i-1))]))
        elif int(lista_cyfr[i]) == 9:
            answer.append(dict[10**(len(lista_cyfr)-i-1)]+dict[10*10**(len(lista_cyfr)-i-1)])
    print(n,'-',''.join(answer))
#Iteracja na zadanym zakresie
for n in range(1,1001):
    konwert(n)