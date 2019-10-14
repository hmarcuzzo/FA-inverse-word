import sys
import subprocess

""" Classe com todas as linhas de um automato finito. """
class FiniteAutomaton(object):
    def __init__(self):
        self.machine = []
        self.input_alphabet = []
        self.lambda_ = []
        self.states = []
        self.initial_state = []
        self.final_states = []
        self.transitions = []



""" Todas as linhas do automato finito são pegas pelos variaveis da Classe """
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

""" Capituramos para o Automato Finito inverso todos os alfabetos de entrada do automato finito principal"""
for j in range(len(fa[0].input_alphabet)):
    fa[1].input_alphabet.append(fa[0].input_alphabet[j])

#######################################################

""" Copia o lambda de um automato para outro """
fa[1].lambda_.append(fa[0].lambda_)

# #######################################################

""" Copiamos os estados existens no Automato finito """

for i in range(len(fa[0].states)):
    fa[1].states.append(fa[0].states[i])
fa[1].states.append("q" + str(len(fa[0].states)))

#######################################################

""" Define como estado inicial do automato inverso, o estado criado para ser o inicializador """
fa[1].initial_state.append( "q" + str(len(fa[0].states)))

#######################################################

""" Define como estado final da automato inverso, o estado inical do automato principal """
for i in range(len(fa[0].initial_state)):
    fa[1].final_states.append(fa[0].initial_state[i])

#######################################################

""" São copiadas as transições para depois fazerem as devidas trocas """
for i in range(len(fa[0].final_states)):
    fa[1].transitions.append( 
        (str(fa[1].initial_state[0]) + " " + str(fa[1].lambda_[0]) + " " + str(fa[0].final_states[i])).split() )

######################################################

""" É feita a inversão das transições """
aux = []
for i in range(len(fa[0].transitions)):
    aux = fa[0].transitions[i][0]
    (fa[0].transitions[i])[0] = str(fa[0].transitions[i][2])

    (fa[0].transitions[i])[2] = str(aux)

    fa[1].transitions.append(fa[0].transitions[i])


#######################################################

printfaData(fa[1], 1)
print("\n\n")

""" Aberto o arquivo vindo por comando, na pasta ."/fla/dfa.txt" e escreve a união das duas fa """
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

""" Verifica se o automato aceita """
inputTest = ""
for i in range(len(sys.argv[3:])):
    inputTest = inputTest + sys.argv[3:][i]
return_code = subprocess.call('python3 ./fla/main.py ' + sys.argv[2] + " " + inputTest, shell=True)