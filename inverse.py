import sys
import subprocess

""" Classe com todas as linhas de uma turing machine. """
class FiniteAutomaton(object):
    def __init__(self):
        self.machine = []
        self.input_alphabet = []
        self.lambda_ = []
        self.states = []
        self.initial_state = []
        self.final_states = []
        self.transitions = []



""" Todas as linhas da Turing Machine são pegas pelos variaveis da Classe """
fa = []
fa.append(FiniteAutomaton())
fp = open(sys.argv[1], "r")
lines_cmd = fp.readlines()
fp.close()
lines = []
for line in lines_cmd:
    lines.append(line.rstrip())
fa[0].machine = lines[0].split()
fa[0].input_alphabet = lines[1].split()
fa[0].lambda_ = lines[2]
fa[0].states = lines[3].split()
fa[0].initial_state = lines[4].split()
fa[0].final_states = lines[5].split()
for j in range(6, len(lines)):
    fa[0].transitions.append(lines[j].split())


def printfaData(fa_aux, i):
    print()
    print(f'Tipo da máquina {i+1} : {fa_aux.machine}')
    print(f'Alfabeto da máquina {i+1} : {fa_aux.input_alphabet}')
    print(f'Branco da máquina {i+1} : {fa_aux.lambda_}')
    print(f'Estados da máquina {i+1} : {fa_aux.states}')
    print(f'Estado incial da máquina {i+1} : {fa_aux.initial_state}')
    print(f'Estado final da máquina {i+1} : {fa_aux.final_states}')
    print(f'Transições da máquina {i+1} : ')
    for j in fa_aux.transitions:
        print(j)
    print()


fa.append(FiniteAutomaton())

""" Copiando o estado da máquina """
for i in range(len(fa[0].machine)):
    fa[1].machine.append(fa[0].machine[i])

""" Capituramos para Turing Machine União todos os alfabetos de entrada da 1a turing machine
        e na 2a turing machine são capturadas, apenas, as letras que não continha na 1a (2a linha) """
for j in range(len(fa[0].input_alphabet)):
    fa[1].input_alphabet.append(fa[0].input_alphabet[j])

#######################################################

""" Procuramos na Turing Machine União, a partir da letra "A" uma letra não que não estivesse
        no alfabeto da fita e que fosse diferente de "R", "L" ou "S" (4a linha) """
fa[1].lambda_.append(fa[0].lambda_)

# #######################################################

""" Criamos a quantidade de estados existens na Turing Machine União
        somando a quantidade de estados da 1a e 2a fa + 1, que é o nosso estado inicial (5a linha) """

for i in range(len(fa[0].states)):
    fa[1].states.append(fa[0].states[i])
fa[1].states.append("q" + str(len(fa[0].states)))

#######################################################

""" Definindo o estado inicial da fa União sempre como 0, que é o estado criado a mais
        que serve como controle (6a linha) """
fa[1].initial_state.append( "q" + str(len(fa[0].states)))

#######################################################

""" Definimos a os estados finas da fa União, pegando os estados finais da fa 1 e 2
        já com a referencia deles na nova fa (7a linha) """
for i in range(len(fa[0].initial_state)):
    fa[1].final_states.append(fa[0].initial_state[i])

#######################################################

""" É criado asa transições inicias da TM União que define a qual máquina o conjunto de 
        entrada pertence, de acordo com a primeira letra é possível mandar para o estado
            inicias da TM 1 ou 2 ou as duas simultaneamente sem que nada seja consumido (9a linha) """
for i in range(len(fa[0].final_states)):
    fa[1].transitions.append( 
        (str(fa[1].initial_state[0]) + " " + str(fa[1].lambda_[0]) + " " + str(fa[0].final_states[i])).split() )

######################################################

""" É copiado todas as transações da fa 1 e 2, fazendo as trocas dos estados para as suas respectivas referências
        na fa União, e também, trocando as letras que representavam o "Branco" de cada fa 
            para a letra definida como "Branco" na fa União (9a linha) """
aux = []
for i in range(len(fa[0].transitions)):
    aux = fa[0].transitions[i][0]
    (fa[0].transitions[i])[0] = str(fa[0].transitions[i][2])

    (fa[0].transitions[i])[2] = str(aux)

    fa[1].transitions.append(fa[0].transitions[i])


#######################################################

printfaData(fa[1], 1)
print("\n\n")

""" Aberto o arquivo vindo por comando, na pasta ."/fla/turing_machine_union.txt" e escreve a união das duas fa """
inverse = open(sys.argv[2], 'w')
for i in range(len(fa[1].machine)):
    inverse.write(fa[1].machine[i] + " ")
inverse.write("\n")
for i in range(len(fa[1].input_alphabet)):
    inverse.write(fa[1].input_alphabet[i] + " ")
inverse.write("\n")
for i in range(len(fa[1].lambda_)):
    inverse.write(fa[1].lambda_[i] + " ")
inverse.write("\n")
for i in range(len(fa[1].states)):
    inverse.write(str(fa[1].states[i]) + " ")
inverse.write("\n")
for i in range(len(fa[1].initial_state)):
    inverse.write(str(fa[1].initial_state[i]) + " ")
inverse.write("\n")
for i in range(len(fa[1].final_states)):
    inverse.write(str(fa[1].final_states[i]) + " ")
inverse.write("\n")
for i in range(len(fa[1].transitions)):
    for j in range(len(fa[1].transitions[i])):
        inverse.write(str(fa[1].transitions[i][j]) + " ")
    inverse.write("\n")

inverse.close()
#######################################################

""" Verifica se máquina de Turing aceita """
inputTest = ""
for i in range(len(sys.argv[3:])):
    inputTest = inputTest + sys.argv[3:][i]
return_code = subprocess.call('python3 ./fla/main.py ' + sys.argv[2] + " " + inputTest, shell=True)