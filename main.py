def menu():
    menu = """
    ======Banco=======
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuario
    [q] Sair
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if(valor > 0):
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso")
    else:
        print("Operação inválida, tente novamente")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limit_saques): 
    excedeu_saldo = saldo - valor < 0
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limit_saques

    if excedeu_saldo or excedeu_limite or excedeu_saques:
        print("Operação inválida, tente novamente")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("===INICIO EXTRATO===")
    if extrato:
        print(extrato)
    else:
        print("Sem operações")
    print(f"Saldo: R$ {saldo:.2f}")
    print("===FIM EXTRATO===")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF: ")

    usuario = filtrar_usuario_por_cpf(cpf, usuarios)

    if usuario:
        print("Usuario já cadastrado")
        return
    
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento: (dd-mm-aaaa) ")
    endereco = input("Digite o endereço completo: ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,"cpf": cpf, "endereco": endereco})
    
    print("Usuário cadastrado com sucesso")

def criar_conta(agencia,numero_conta, usuarios,contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario_por_cpf(cpf, usuarios)
    conta = filtrar_conta_por_cpf(contas,cpf)
    #verifica se o usuário existe
    if not usuario:
        print("Usuário não encontrado")
        return None
    #verifica se o usuário já possui conta
    if conta:
        print("Usuário já possui conta")
        return None
    #cria a conta
    print("Conta Criada com sucesso!")
    return {"agencia": agencia, "numero": numero_conta, "usuario": usuario}
   
def listar_contas(contas):
    print("===Contas===")
    for conta in contas:
        print(f"Agência: {conta['agencia']} Conta: {conta['numero']} Titular: {conta['usuario']['nome']}")
        print("===")

def filtrar_conta_por_numero(numero_conta, contas):
    contas_filtradas = list(filter(lambda conta: conta["numero"] == numero_conta, contas))
    if contas_filtradas:
        return contas_filtradas[0]
    return None

def filtrar_conta_por_cpf(contas,cpf):
    filtrar_conta_por_cpf = list(filter(lambda conta: conta["usuario"]["cpf"] == cpf, contas))
    if filtrar_conta_por_cpf:
        return filtrar_conta_por_cpf[0]
    return None

def filtrar_usuario_por_cpf(cpf,usuarios):
    usuarios_filtrados = list(filter(lambda usuario: usuario["cpf"] == cpf, usuarios))
    if usuarios_filtrados:
        return usuarios_filtrados[0]
    return None

def main():
    print("Bem-vindo ao banco")

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
   
    contas = []
    usuarios = []
    saldo = 0
    extrato = ""
    limite = 1000
    numero_saques = 0

    while True:
        opcao = menu()

        #depositar
        if opcao == 'd':
            
            valor = float(input("Digite o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        #sacar
        elif opcao == 's':
            valor = float(input("Digite o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limit_saques = LIMITE_SAQUES,
                ) 
        #extrato
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        #nova conta
        elif opcao == 'nc':
            #conta iniciando em 1 e incrementando.
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios,contas) 

            if conta:
                contas.append(conta)
        #listar contas
        elif opcao == 'lc':
            listar_contas(contas)
        #novo usuario
        elif opcao == 'nu':
            criar_usuario(usuarios)
            
        elif opcao == 'q':
            break
        else:
            print("Opção inválida")
    print("Até mais!")

main()
