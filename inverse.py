import sys
import subprocess

""" Classe com todas as linhas de uma turing machine. """
class TuringMachine(object):
    def __init__(self):
        self.machine = "TM"
        self.input_alphabet = []
        self.tape_alphabet = []
        self.whitespace = []
        self.states = []
        self.initial_state = []
        self.final_states = []
        self.number_of_tapes = []
        self.transitions = []


tm = []

""" Todas as linhas da Turing Machine são pegas pelos variaveis da Classe """
for i in range(2):
    tm.append(TuringMachine())
    fp = open(sys.argv[i+1], "r")
    lines_cmd = fp.readlines()
    fp.close()
    lines = []
    for line in lines_cmd:
        lines.append(line.rstrip())
    lines = lines[1:]
    tm[i].input_alphabet = lines[0].split()
    tm[i].tape_alphabet = lines[1].split()
    tm[i].whitespace = lines[2]
    tm[i].states = lines[3].split()
    tm[i].states = [int(p) for p in tm[i].states]
    tm[i].states.sort()
    tm[i].initial_state = lines[4]
    tm[i].initial_state = [int(p) for p in tm[i].initial_state]
    tm[i].final_states = lines[5].split()
    tm[i].final_states = [int(p) for p in tm[i].final_states]
    tm[i].number_of_tapes = lines[6]
    tm[i].number_of_tapes = [int(p) for p in tm[i].number_of_tapes]
    for j in range(7, len(lines)):
        tm[i].transitions.append(lines[j].split())


def printTmData(tm_aux, i):
    print()
    print(f'Alfabeto da máquina {i+1} : {tm_aux.input_alphabet}')
    print(f'Alfabeto da fita da máquina {i+1} : {tm_aux.tape_alphabet}')
    print(f'Branco da máquina {i+1} : {tm_aux.whitespace}')
    print(f'Estados da máquina {i+1} : {tm_aux.states}')
    print(f'Estado incial da máquina {i+1} : {tm_aux.initial_state}')
    print(f'Estado final da máquina {i+1} : {tm_aux.final_states}')
    print(f'N de fitas da máquina {i+1} : {tm_aux.number_of_tapes}')
    print(f'Transições da máquina {i+1}')
    for j in tm_aux.transitions:
        print(j)
    print()


tm.append(TuringMachine())

""" Capituramos para Turing Machine União todos os alfabetos de entrada da 1a turing machine
        e na 2a turing machine são capturadas, apenas, as letras que não continha na 1a (2a linha) """
for j in range(len(tm[0].input_alphabet)):
    tm[2].input_alphabet.append(tm[0].input_alphabet[j])


for i in range(len(tm[1].input_alphabet)):
    if tm[1].input_alphabet[i] not in tm[0].input_alphabet:
        tm[2].input_alphabet.append(tm[1].input_alphabet[i])
#######################################################

""" Capituramos para a Turing Machine União todos os alfabeto da fita da 1a turing machine
        e na 2a pegamos, apenas, as letras que não continha na 1a (3a linha) """
for j in range(len(tm[0].tape_alphabet)):
    tm[2].tape_alphabet.append(tm[0].tape_alphabet[j])


for i in range(len(tm[1].tape_alphabet)):
    if tm[1].tape_alphabet[i] not in tm[0].tape_alphabet:
        tm[2].tape_alphabet.append(tm[1].tape_alphabet[i])

#######################################################

""" Procuramos na Turing Machine União, a partir da letra "A" uma letra não que não estivesse
        no alfabeto da fita e que fosse diferente de "R", "L" ou "S" (4a linha) """
letter = 65
for i in range(26):
    if chr(letter) != 'R' or chr(letter) != 'L' or chr(letter) != 'S':
        if chr(letter) not in tm[2].tape_alphabet:
            tm[2].whitespace.append(chr(letter))
            break
    letter += 1

#######################################################

""" Criamos a quantidade de estados existens na Turing Machine União
        somando a quantidade de estados da 1a e 2a TM + 1, que é o nosso estado inicial (5a linha) """
tam_final = len(tm[0].states) + len(tm[1].states) + 1

for i in range(tam_final):
    tm[2].states.append(i)
#######################################################

""" Definindo o estado inicial da TM União sempre como 0, que é o estado criado a mais
        que serve como controle (6a linha) """
tm[2].initial_state.append(0)
#######################################################

ref_states = [[], []]


""" É criado uma matriz 2x(tamanho de estados de cada TM) para que fosse possível saber
        qual a referência de um estado da TM 1 e 2 na TM união"""
for i in range(len(tm[0].states)):
    ref_states[0].append(i+1)

for i in range(len(tm[1].states)):
    ref_states[1].append(len(tm[0].states) + 1 + i)
#######################################################

""" Definimos a os estados finas da TM União, pegando os estados finais da TM 1 e 2
        já com a referencia deles na nova TM (7a linha) """
for i in range(2):
    for j in range(len(tm[i].final_states)):
        tm[2].final_states.append(
            ref_states[i][tm[i].final_states[j]])
#######################################################

""" Define a quantidade de fitas que haverá na TM União, sabendo que 
        a quantidade de fintas na TM 1 e 2 são iguais (8a linha) """
tm[2].number_of_tapes.append(tm[0].number_of_tapes[0])

#######################################################

""" É criado asa transições inicias da TM União que define a qual máquina o conjunto de 
        entrada pertence, de acordo com a primeira letra é possível mandar para o estado
            inicias da TM 1 ou 2 ou as duas simultaneamente sem que nada seja consumido (9a linha) """
for j in range(2):
    for i in range(len(tm[j].input_alphabet)):
        tm[2].transitions.append(
            ("0 " + str(ref_states[j][tm[j].initial_state[0]]) + " " + tm[j].input_alphabet[i] + " " +
                tm[2].input_alphabet[j] + " S").split())
#######################################################

""" É copiado todas as transações da TM 1 e 2, fazendo as trocas dos estados para as suas respectivas referências
        na TM União, e também, trocando as letras que representavam o "Branco" de cada TM 
            para a letra definida como "Branco" na TM União (9a linha) """
for j in range(2):
    for i in range(len(tm[j].transitions)):

        (tm[j].transitions[i])[0] = str(ref_states[j][int(
            (tm[j].transitions[i])[0], 10)])

        (tm[j].transitions[i])[1] = str(ref_states[j][int(
            (tm[j].transitions[i])[1], 10)])

        for k in range(2, len(tm[j].transitions[i])):
            if (tm[j].transitions[i])[k] == tm[j].whitespace[0]:
                (tm[j].transitions[i])[k] = tm[2].whitespace[0]

        tm[2].transitions.append(tm[j].transitions[i])


#######################################################

# printTmData(tm[2], 2)

""" Aberto o arquivo vindo por comando, na pasta ."/fla/turing_machine_union.txt" e escreve a união das duas TM """
union = open(sys.argv[3], 'w')
union.write("T M\n")
for i in range(len(tm[2].input_alphabet)):
    union.write(tm[2].input_alphabet[i] + " ")
union.write("\n")
for i in range(len(tm[2].tape_alphabet)):
    union.write(tm[2].tape_alphabet[i] + " ")
union.write("\n")
for i in range(len(tm[2].whitespace)):
    union.write(tm[2].whitespace[i] + " ")
union.write("\n")
for i in range(len(tm[2].states)):
    union.write(str(tm[2].states[i]) + " ")
union.write("\n")
for i in range(len(tm[2].initial_state)):
    union.write(str(tm[2].initial_state[i]) + " ")
union.write("\n")
for i in range(len(tm[2].final_states)):
    union.write(str(tm[2].final_states[i]) + " ")
union.write("\n")
for i in range(len(tm[2].number_of_tapes)):
    union.write(str(tm[2].number_of_tapes[i]) + " ")
union.write("\n")
for i in range(len(tm[2].transitions)):
    for j in range(len(tm[2].transitions[i])):
        union.write(str(tm[2].transitions[i][j]) + " ")
    union.write("\n")

union.close()
#######################################################

""" Verifica se máquina de Turing aceita """
inputTest = ""
for i in range(len(sys.argv[4:])):
    inputTest = inputTest + sys.argv[4:][i]
return_code = subprocess.call('python3 ./fla/main.py union.txt '+ inputTest, shell=True)