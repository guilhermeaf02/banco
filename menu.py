from cliente import menu_cliente
def menu_principal():
    print ("----------------------------------")
    print ("       Menu - Programas           ")
    print ("----------------------------------")
    print ("         1- Cliente               ")
    print ("         2- Categoria             ")
    print ("         3- Produtos              ")
    print ("         4- Usuario               ")
    print ("         5- Vendas                ")
    print ("         6- Sair do Sistema       ")
    print ("----------------------------------")


    while True:
        opcao = input ("Escolha uma Opção:")

        if opcao == "1":
            print ("Cadastro de cliente")
            menu_cliente ()
        elif opcao == "2":
            print ("Cadastro Categoria")
        elif opcao == "3":
            print ("Cadastro de Produto")
        elif opcao == "4":
            print ("Cadastro de Usuario")
        elif opcao == "5":
            print ("Cadastro de Venda")
        elif opcao == "6":
            print ("Sair do Sistema")
            break
        else:
            print ("Opção invalida, tenta novamente")

        
if __name__  == "__main__":
    menu_principal()