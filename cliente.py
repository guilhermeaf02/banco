from conexao import conecta_db


def menu_cliente():
    
    print ("----------------------------------")
    print ("       Cadastro de Cliente        ")
    print ("----------------------------------")
    print ("  1- Listar Clientes              ")
    print ("  2- Consultar um cliente por ID  ")
    print ("  3- Inserir                      ")
    print ("  4- Alterar                      ")
    print ("  5- Deletar                      ")
    print ("  6- Sair do Sistema do Cliente   ")
    print ("----------------------------------")

    while True:

        opcao = input ("Escolha uma Opção: ")

        if opcao == "1":
            listar_clientes ()
        elif opcao == "2":
            listar_clientes ()
            consultar_cliente_por_id ()
        elif opcao == "3":
            listar_clientes ()
            inserir_cliente ()
            listar_clientes ()
        elif opcao == "4":
            listar_clientes ()
            atualizar_cliente ()
            listar_clientes ()
        elif opcao == "5":
            listar_clientes ()
            deletar_cliente ()
            listar_clientes ()
        elif opcao == "6":
            print ("Sair do Sistema do Cliente")
            break
        else:
            print ("Opção invalida, tenta novamente")

def listar_clientes ():

    conexao = conecta_db ()
    cursor = conexao.cursor ()
    cursor.execute ("select id, nome from cliente")
    registros = cursor.fetchall ()

    print ("--------------------------")
    for registro in registros:
        print (f"ID: {registro[0]} -  Nome {registro[1]}")
    print ("---------------------------")

def consultar_cliente_por_id ():
    id = input ("Digite o ID: ")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    cursor.execute ("select id, nome from cliente where id =" + id)
    registros = cursor.fetchone ()

    if registros is None:
        print ("Cliente não encontrado")
    else:
        print (f" ID: {registros[0]}")
        print (f" Nome: {registros[1]}")

def inserir_cliente ():
    print ("Inserindo o cliente..: ")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    nome = input ("Nome: ")
    sql_insert = "Insert into cliente (nome) values ('" + nome + "')"
    cursor.execute (sql_insert)
    conexao.commit ()
    
def atualizar_cliente ():
    print ("Atualizando cadastro...")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    id = input ("Digite o ID: ")
    nome = input ("Nome: ")
    sql_update = "Update cliente set nome = '" + nome + "' ""where id =" + id
    cursor.execute (sql_update)
    conexao.commit ()

def deletar_cliente ():
    print ("Deletando cliente..")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    id = input ("Digite o ID: ")
    sql_delete = "delete from cliente where id =" + id
    cursor.execute (sql_delete)
    conexao.commit ()









        
        




