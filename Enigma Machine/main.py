import pyfiglet
import loads
from time import sleep

def rotorRotacao(lista):
    lista.append(lista[0])
    del lista[0]
    return lista

def assina():
        text = pyfiglet.figlet_format("Enigma  Machine")
        print(text)
        syn = "by shiraax"
        alinhar = syn.rjust(70)
        print(alinhar)
        print('\n')
        string = ""

op = 0
i = 0
c = 5
while True:
    assina()

    #INPUTA
    mLista = []
    while len(mLista) <= 0:
            mensagem = str(input("Inpute a mensagem para criptografar ou decriptar: "))
            mLista = list(mensagem)
            if len(mLista) > 0:
                while c != 0:
                    print('Carregando' + loads.animation[i], end='\r')
                    i = (i + 1) % 4
                    sleep(0.1)
                    c = c - 1
                break

    #Decripta e Encripta
    output = []
    def double():
        for index in range(len(mLista)): 
            a = loads.alphabetDict[mLista[index].upper()]
            b = loads.rotor[a-1]
            c = loads.alphabetDict[b]
            h = loads.refletor[c-1]
            j = loads.rotor.index(h)
            k = loads.alphabet[j]
            output.append(k)
        rotorRotacao(loads.rotor)

    #chamada
    double()
    print("-" *40)
    print("A mensagem fica:",''. join(output))
    print("-" *40)
    print("[1] - Sair")
    print("[2] - Info")
    op = int(input("Escolha uma opção: "))
    while op >= 3:
         print("opção inválida...")
         op = int(input("Escolha uma opção: "))
    if op == 1:
        print("Saindo...")
        break
    elif op == 2:
         print("*" *40)
         print("A Máquina Enigma foi uma máquina de criptografia e decodificação desenvolvida na Alemanha durante os anos 1920 e amplamente utilizada durante a Segunda Guerra Mundial. A máquina Enigma usava rotores mecânicos para criptografar mensagens, tornando-as indecifráveis para qualquer pessoa sem a chave correta. A criptografia era baseada em substituição de letras, com cada letra do alfabeto sendo substituída por outra letra, de acordo com as configurações dos rotores da máquina.")
         input("Pressione ENTER para continuar.")
         break
    
    
        





        
     


     









