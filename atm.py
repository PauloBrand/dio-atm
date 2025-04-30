
from datetime import datetime

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
withdrawal_limit_amount = 500
statement = ""

transaction_count = 0
transaction_count_limit = 10
transaction_first_date = ""
today = datetime.now()

def can_transact ():
    global transaction_first_date, transaction_count, today
    
    # Primeiro Saque do Dia
    if not transaction_first_date or today > transaction_first_date:
        transaction_count = 0
        transaction_first_date = datetime.now()
        return True
    
    ## Limite de transações
    if transaction_count >= 10:
        print("Número máximo de transações atinguidas.")
        return False
    
    return True
    

def mask (operation, amount, columns = COLUMNS):
    operation = f"{operation} "
    amount = f"R$ {amount:,.2f}"
    dots = '.' * (columns - len(operation) - len(amount) - 3)
    return f"\n{operation}{dots} : {amount}"
    
print(welcome_message)

while True:
    
    option = input(menu)
    
    if option == "d":
        
        if not can_transact():
            continue
        
        amount = float(input("Informe o valor à depositar: "))
        
        if amount <= 0:
            print("Valor inválido! Operação Cancelada.")
            continue
        
        balance += amount
        statement += mask(today.strftime("%d/%m/%y") + ' - Deposito', amount)
        transaction_count += 1
        continue
        
    if option == "s":
        
        if not can_transact():
            continue
        
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
            
        balance -= amount
        statement += mask(today.strftime("%d/%m/%y") + ' - Saque', amount)
        transaction_count += 1
        continue
        
    if option == "e":
        print((" Extrato ").center(COLUMNS,"*"))
        print("Sem movimentações" if not statement else statement)
        print(mask('Saldo', balance))
        continue
    
    if option == "q":
        break
        
    print("Ops! Não temos essa opção. Favor selecionar uma das opções abaixo.")
    