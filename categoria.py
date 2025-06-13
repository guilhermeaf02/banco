from conexao import conecta_db


def menu_categoria():

    print ("----------------------------------")
    print ("       Cadastro de Categoria      ")
    print ("----------------------------------")
    print ("  1- Listar Categoria             ")
    print ("  2- Consultar categoria por ID   ")
    print ("  3- Inserir                      ")
    print ("  4- Alterar                      ")
    print ("  5- Deletar                      ")
    print ("  6- Sair do Sistema do Categoria ")
    print ("----------------------------------")

    while True:

        opcao = input ("Escolha uma Opção: ")

        if opcao == "1":
            listar_categoria ()
        elif opcao == "2":
            listar_categoria ()
            consultar_categoria_por_id ()
        elif opcao == "3":
            listar_categoria ()
            inserir_categoria ()
            listar_categoria ()
        elif opcao == "4":
            listar_categoria ()
            atualizar_categoria ()
            listar_categoria ()
        elif opcao == "5":
            listar_categoria ()
            deletar_categoria ()
            listar_categoria ()
        elif opcao == "6":
            print ("Sair do Sistema do Categoria")
            break
        else:
            print ("Opção invalida, tenta novamente")

def listar_categoria ():

    conexao = conecta_db ()
    cursor = conexao.cursor ()
    cursor.execute ("select id, nome from categoria")
    registros = cursor.fetchall ()

    print ("--------------------------")
    for registro in registros:
        print (f"ID: {registro[0]} -  Nome {registro[1]}")
    print ("---------------------------")

def consultar_categoria_por_id ():
    id = input ("Digite o ID: ")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    cursor.execute ("select id, nome from categoria where id =" + id)
    registros = cursor.fetchone ()

    if registros is None:
        print ("Categoria não encontrada")
    else:
        print (f" ID: {registros[0]}")
        print (f" Categora: {registros[1]}")

def inserir_categoria ():
    print ("Inserindo categoria...")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    nome = input ("Categoria:")
    sql_insert = "Insert into categoria (nome) values ('" + nome + "')"
    cursor.execute (sql_insert)
    conexao.commit ()

def atualizar_categoria ():
    print ("Atualizando categoria")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    id = input ("Digite o ID: ")
    nome = input ("Nome:")
    sql_update = "Update categoria set nome = '" + nome + "' ""where id =" + id
    cursor.execute (sql_update)
    conexao.commit ()

def deletar_categoria ():
    print ("Deletando categoria")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    id = input ("Digite o ID: ")
    sql_delete = "delete from categoria where id =" + id
    cursor.execute (sql_delete)
    conexao.commit ()