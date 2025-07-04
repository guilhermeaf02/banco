from cliente import menu_cliente
from categoria import menu_categoria
from produto import menu_produto
from usuario import menu_usuario, login
from venda import menu_venda

from conexao import conecta_db

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
            menu_cliente ()
        elif opcao == "2":
             menu_categoria()
        elif opcao == "3":
            menu_produto ()
        elif opcao == "4":
            menu_usuario ()
        elif opcao == "5":
            menu_venda()
        elif opcao == "6":
            print ("Sair do Sistema")
            break
        else:
            print ("Opção invalida, tenta novamente")

        
if __name__  == "__main__":
    conexao = conecta_db

    while True:
        resultando = login()
        if resultando is True:
            menu_principal()
    

    