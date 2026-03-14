import random

from domanda import Domanda
from giocatore import Giocatore

f = open("domande.txt", "r").read().splitlines()
d=[] #creo una lista di oggetti domanda legendo il file
for ii in range(0, len(f), 7):
    #step = 7 → vai avanti di 7 in 7: sette solo le righe di 1 domanda
    d.append(Domanda(testo=f[ii], diff=f[ii+1], corretta=f[ii+2], opzioni=f[ii+2:ii+6]))

flag=True
current_diff = 0
max_diff = max(d, key=lambda x: x.difficoltà).difficoltà
# max() trova il massimo di una lista, ma con key gli dici come confrontare gli elementi
punti=0


while(flag):
    current_d=[] #creo una sottolista di domande con la difficoltà desiderata
    current_d = [x for x in d if int(x.difficoltà)==current_diff]
    # La versione "lunga" equivalente:
    # current_d = []
    # for x in d:
    #     if int(x.difficoltà) == current_diff:
    #         current_d.append(x)

    ii = random.randint(0,len(current_d)-1) # → numero casuale tra 0 e l'ultimo indice della lista
    current_opzioni = current_d[ii].opzioni_random() #fa lo shuffle delle opzioni della domanda
    print("Livello "+ current_d[ii].difficoltà + ") "+ current_d[ii].testo)
    for jj in range(len(current_opzioni)):
        print(str(jj+1) + '. ' + current_opzioni[jj])
    n_risposta = input("Inserisci risposta: ")
    risposta = current_opzioni[int(n_risposta)-1] #extract the corr verbose answer (e.g. 'Roma')

    if risposta != current_d[ii].corretta:
        flag=False
        print("Risposta sbagliata! La risposta era: " + str(current_opzioni.index(current_d[ii].corretta) +1))
        print("Punteggio: ", punti)
        nick = input("Inserisci nickname: ")
    else:
        print("Risposta corretta!")
        current_diff = current_diff+1
        punti=punti+1
        if current_diff > int(max_diff):
            print("Hai vinto! Punteggio: ", punti)
            flag=False
            nick = input("Inserisci nickname: ")

f = open("punti.txt", "r").read().splitlines()
g=[]
for ii in range(len(f)):
    g.append(Giocatore(giocatore=f[ii].split(' ')[0], punti=f[ii].split(' ')[1]))
g.append(Giocatore(giocatore=nick, punti=punti))

g.sort(key=lambda x: int(x.punti), reverse=True)

with open('punti.txt', 'w') as f:
    for jj in g:
        nick = jj.giocatore
        punti = jj.punti
        f.write(nick+ ' ' + str(punti) + '\n')