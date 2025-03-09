# 🏦 Banco Digital - Sistema de Gerenciamento Bancário

## 📚 Descrição
Este é um projeto de um **banco digital** desenvolvido em **Python**. O sistema permite criar usuários, abrir contas, realizar depósitos, saques e exibir extratos bancários. Ele também impede que um usuário tenha mais de uma conta. 

## ✨ Funcionalidades
- 👨‍👩‍👦 Criar novos usuários
- 🏦 Criar contas bancárias (impedindo duplicatas por CPF)
- 💰 Realizar depósitos
- 💳 Efetuar saques com limite por transação e diário
- 📊 Exibir extrato bancário
- 🔢 Listar contas cadastradas

## 📝 Como Usar
1. Execute o script `main.py` para iniciar o sistema.
2. Utilize o menu interativo para acessar as opções disponíveis.
3. Siga as instruções na tela para cadastrar usuários e contas, realizar transações e visualizar extratos.

## 🔄 Estrutura do Código
- `menu()`: 👀 Exibe o menu interativo para o usuário.
- `depositar(saldo, valor, extrato)`: 💵 Realiza um depósito na conta.
- `sacar(saldo, valor, extrato, limite, numero_saques, limit_saques)`: 💸 Efetua um saque com restrições.
- `exibir_extrato(saldo, extrato)`: 📝 Mostra o extrato bancário.
- `criar_usuario(usuarios)`: 👤 Cadastra um novo usuário no sistema.
- `criar_conta(agencia, numero_conta, usuarios, contas)`: 🏦 Cria uma nova conta bancária se o CPF não estiver cadastrado.
- `listar_contas(contas)`: 🔢 Lista todas as contas criadas.
- `filtrar_usuario_por_cpf(cpf, usuarios)`: 🔍 Busca um usuário pelo CPF.
- `filtrar_conta_por_cpf(contas, cpf)`: 🔍 Verifica se um usuário já possui conta.
- `main()`: 🎨 Gerencia a execução principal do programa.

## 💪 Requisitos
- Python 3.x

## 🛠️ Como Executar
1. Instale o Python (se ainda não tiver instalado).
2. Baixe ou clone o repositório.
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. Siga as instruções no terminal para interagir com o sistema.

## 💡 Melhorias Futuras
- 🌐 Implementar armazenamento de dados em banco de dados.
- 💻 Criar uma interface gráfica (GUI).
- 🔐 Adicionar autenticação de usuários.
- ⚖️ Melhorar a segurança das transações.

## 👨‍👩‍👧 Autor
Desenvolvido por [Seu Nome] 🌟

