# Entrada de dados 

n = float(input("Entre com um número decimal: "))
y = 0
arm = []
x = -10
cont = 0

# Validação da entrada de dados
if (n > 0) and (n < 1) :
    #print("Nome do projeto: Conversor de números reais para binário")
    #print("Integrantes do grupo:\n", "Gabriel Freire\n", "Giovanna Nacarato\n", "Nathan Vieira\n", "Rafaela Moura\n")
    while(cont < 5):
        n *= 2
        arm.append(int(n))
        if (n > 1):
           n -= 1 
        cont += 1
    print(arm)

else:
    print("ERRO, dados incorretos")