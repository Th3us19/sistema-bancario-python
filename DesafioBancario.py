nome = input("Digite seu nome: ")
print(f"Seja bem vindo(a) {nome} ao banco Python!")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar conta
[q] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITESAQUES = 3

usuarios = []

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o avalor do depsoito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é invalido.")
        
    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITESAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n" #2f coloca duas casas decimais
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é invalido.")
    
    elif opcao == "c":
        print("\n===Cadastro do usuário===")
        nome = input("Nome completo: ")
        cpf = int(input("CPF (somente números): "))
        data_nascimento = input("Data nascimento (dd-mm-aaaa): ")
        
        usuario_existente = [u for u in usuarios if u["cpf"] == cpf]
            
        if usuario_existente:
            print("\nJá existe usuário com esse CPF!")
        else:
            usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento})
            print("\nUsuário cadastrado com sucesso!")
            print(usuarios)
    
    elif opcao == "e":
        print("\n================EXTRATO================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")
        
    elif opcao == "q":
        break