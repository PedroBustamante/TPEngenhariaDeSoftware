class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.value = 0

def main():
    numAccounts = 1000
    while(1):
        userInput = input("Entre com seu ID de conta, ou 'new' para criar uma nova conta, ou '0' para sair\n")
        if userInput == '0':
            return
        elif userInput == 'new':
            name = input("Criar novo usuário.\nSeu nome?\n")
            account = User(numAccounts, name)
            print('Conta criada!\n')
            print('ID: ', account.id)
            print('Nome: ', account.name)
            print('Saldo: ', account.value)
        else:
            return
            
main()