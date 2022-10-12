# função para a conversão de bin para dec
def convToDec(bin):
    n = float()
    x = len(bin)
    for i in range(1,x-1):
        if bin[i+1] == "1":
            n = n + 2 ** (-i)
    return n 

# Entrada de dados 
print("Nome do projeto: Conversor de números reais para binário")
print("Integrantes do grupo:\n", "Gabriel Freire\n", "Giovanna Nacarato\n", "Nathan Vieira\n", "Rafaela Moura\n")
n = float(input("Dado de entrada: "))
dec = n
arm = "0."
binMenor = "0." 
cont = 0
bits = 5

# Validação da entrada de dados
if (n > 0) and (n < 1) :
    while bits <= 16:
        n = dec
        arm = "0."
        binMenor = "0." 
    # Converte para os binários pelas multiplicações sucessivas
        while (cont < bits):
            n *= 2
            if (n > 1):
                arm += "1"
                n -= 1 
            else:
                arm += "0"
            cont += 1
    
        # Formata os decimais binarios para obter o mais negativo
        binMenor = arm[::-1]
        x = binMenor.find('0')
        binMaior = str()


        # Separa os binarios
        for i in range(0, x):
            binMaior += '0'


        binMaior += '1'
        binMaior += binMenor[x+1:]
        binMaior = binMaior[::-1]
        binMenor = binMenor[::-1]


        # Converte os binários para decimais pela função
        decMenor = convToDec(arm)
        decMaior = convToDec(binMaior)

        # Calcula a porcentagem de Erro maior e menor
        erro = ((dec - decMenor) / dec) * 100
        erro2 = ((dec - decMaior) / dec) * 100

        if erro < 0:
            erro = erro * -1
        if erro2 < 0:  
            erro2 = erro2 * -1
        print("%d Bits" % bits)
        print('Aproximação a menor: {} -> {} com erro = {:.3f} %'.format(arm,decMenor,erro))
        print('Aproximação a maior: {} -> {} com erro = {:.3f} % \n'.format(binMaior,decMaior,erro2))

        bits += 1
        cont = 0
    
else:
    print("ERRO, dados incorretos")