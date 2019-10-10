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
fa[0].states = [int(p) for p in range(len(fa[0].states))]
fa[0].initial_state = lines[4].split()
fa[0].initial_state = [int(p) for p in range(len(fa[0].initial_state))]
fa[0].final_states = lines[5].split()    
fa[0].final_states = [int(p) for p in range(len(fa[0].final_states))]
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
    print(f'Transições da máquina {i+1}')
    for j in fa_aux.transitions:
        print(j)
    print()


fa.append(FiniteAutomaton())

""" Copiando o estado da máquina """
fa[1].machine.append(fa[0].machine[0])

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
fa[1].states.append(len(fa[0].states))
#######################################################

""" Definindo o estado inicial da fa União sempre como 0, que é o estado criado a mais
        que serve como controle (6a linha) """
fa[1].initial_state.append(len(fa[0].states))

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
        (str(fa[1].states[len(fa[0].states)]) + " " + str(fa[1].lambda_[0]) + " " + str(fa[0].final_states[i])))

#######################################################

# """ É copiado todas as transações da fa 1 e 2, fazendo as trocas dos estados para as suas respectivas referências
#         na fa União, e também, trocando as letras que representavam o "Branco" de cada fa 
#             para a letra definida como "Branco" na fa União (9a linha) """
# for j in range(2):
#     for i in range(len(fa[j].transitions)):

#         (fa[j].transitions[i])[0] = str(ref_states[j][int(
#             (fa[j].transitions[i])[0], 10)])

#         (fa[j].transitions[i])[1] = str(ref_states[j][int(
#             (fa[j].transitions[i])[1], 10)])

#         for k in range(2, len(fa[j].transitions[i])):
#             if (fa[j].transitions[i])[k] == fa[j].whitespace[0]:
#                 (fa[j].transitions[i])[k] = fa[2].whitespace[0]

#         fa[2].transitions.append(fa[j].transitions[i])


#######################################################

for i in range(2):
    printfaData(fa[i], i)

# """ Aberto o arquivo vindo por comando, na pasta ."/fla/turing_machine_union.txt" e escreve a união das duas fa """
# union = open(sys.argv[3], 'w')
# union.write("T M\n")
# for i in range(len(fa[2].input_alphabet)):
#     union.write(fa[2].input_alphabet[i] + " ")
# union.write("\n")
# for i in range(len(fa[2].tape_alphabet)):
#     union.write(fa[2].tape_alphabet[i] + " ")
# union.write("\n")
# for i in range(len(fa[2].whitespace)):
#     union.write(fa[2].whitespace[i] + " ")
# union.write("\n")
# for i in range(len(fa[2].states)):
#     union.write(str(fa[2].states[i]) + " ")
# union.write("\n")
# for i in range(len(fa[2].initial_state)):
#     union.write(str(fa[2].initial_state[i]) + " ")
# union.write("\n")
# for i in range(len(fa[2].final_states)):
#     union.write(str(fa[2].final_states[i]) + " ")
# union.write("\n")
# for i in range(len(fa[2].number_of_tapes)):
#     union.write(str(fa[2].number_of_tapes[i]) + " ")
# union.write("\n")
# for i in range(len(fa[2].transitions)):
#     for j in range(len(fa[2].transitions[i])):
#         union.write(str(fa[2].transitions[i][j]) + " ")
#     union.write("\n")

# union.close()
#######################################################

# """ Verifica se máquina de Turing aceita """
# inputTest = ""
# for i in range(len(sys.argv[4:])):
#     inputTest = inputTest + sys.argv[4:][i]
# return_code = subprocess.call('python3 ./fla/main.py union.txt '+ inputTest, shell=True)