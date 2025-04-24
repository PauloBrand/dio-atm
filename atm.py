
welcome_message = """
***************************************
   Bem Vindo PTM, Seu Atm em Python!
***************************************
"""

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

COLUMNS = 40
balance = 0
withdrawal_count = 0
withdrawal_limit = 3
withdrawal_limit_amount = 500
statement = ""

def mask (operation, amount, columns = COLUMNS):
    operation = f"{operation} "
    amount = f"R$ {amount:,.2f}"
    dots = '.' * (columns - len(operation) - len(amount) - 3)
    return f"\n{operation}{dots} : {amount}"
    
print(welcome_message)

while True:
    
    option = input(menu)
    
    if option == "d":
        amount = float(input("Informe o valor à depositar: "))
        
        if amount <= 0:
            print("Valor inválido! Operação Cancelada.")
            continue
        
        balance += amount
        statement += mask('Deposito', amount)
        continue
        
    if option == "s":
        
        amount = float(input("Informe o valor à sacar: "))
        
        if amount <= 0:
            print("Valor inválido! Operação Cancelada.")
            continue
        
        if amount > balance:
            print("Saldo insuficiente. Operação Cancelada")
            continue
            
        if amount > withdrawal_limit_amount:
            print(f"Limite por saque é de R$ {withdrawal_limit_amount:.2f}. Operação Cancelada")
            continue
            
        if withdrawal_count >= withdrawal_limit:
            print(f" Número máximo de saques excedido. Operação Cancelada")
            continue
            
        balance -= amount
        statement += mask('Saque', amount)
        withdrawal_count += 1
        continue
        
    if option == "e":
        print((" Extrato ").center(COLUMNS,"*"))
        print("Sem movimentações" if not statement else statement)
        print(mask('Saldo', balance))
        continue
    
    if option == "q":
        break
        
    print("Ops! Não temos essa opção. Favor selecionar uma das opções abaixo.")
    