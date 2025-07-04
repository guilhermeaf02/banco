from conexao import conecta_db

def menu_usuario ():

    print ("----------------------------------")
    print ("       Cadastro de Usuario       ")
    print ("----------------------------------")
    print ("  1- Listar Usuario               ")
    print ("  2- Consultar Usuario por ID     ")
    print ("  3- Inserir                      ")
    print ("  4- Alterar                      ")
    print ("  5- Deletar                      ")
    print ("  6- Sair do Sistema do Usuario   ")
    print ("----------------------------------")

    while True:

        opcao = input ("Escolha uma Opção: ")

        if opcao == "1":
            listar_usuario ()
        elif opcao == "2":
            listar_usuario ()
            consultar_usuario_por_id ()
        elif opcao == "3":
            listar_usuario ()
            inserir_usuario ()
            listar_usuario ()
        elif opcao == "4":
            listar_usuario ()
            atualizar_usuario ()
            listar_usuario ()
        elif opcao == "5":
            listar_usuario ()
            deletar_usuario ()
            listar_usuario ()
        elif opcao == "6":
            print ("Sair do Sistema do Usuario")
            break
        else:
            print ("Opção invalida, tenta novamente")

def listar_usuario ():

    conexao = conecta_db ()
    cursor = conexao.cursor ()
    sql_listar = """ select id, login, admin from usuario	
                      order by id asc
                                   
    """
    cursor.execute (sql_listar)
    registros = cursor.fetchall ()

    print ("---------------_--------------------------------------------------------------------------------")
    for registro in registros:
        print (f"ID: {registro[0]} -  Login {registro[1]} - Admin {registro[2]}")
    print ("------------------------------------------------------------------------------------------------")

def login() -> bool:    
    login = input ("Digite seu login: ")
    senha = input ("Digite sua senha: ")
    conexao = conecta_db()
    cursor = conexao.cursor()
    slq_listar = """select id, login, admin from usuario
                    where login = %s and senha = %s
    """
    dados = (login,senha)
    cursor.execute (slq_listar,dados)
    registro = cursor.fetchone()

    if registro is None:
        print ("Usuario e senha inválidos")
        return False
    else:
        admin = registro [2]
        return True


def consultar_usuario_por_id ():
    id = input ("Digite o ID: ")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    cursor.execute ("select id,login,admin from usuario where id =" + id)
    registros = cursor.fetchone ()
    
    if registros is None:
        print ("Usuario não encontrada")
    else:
        print (f"ID: {registros[0]}")
        print (f"Login: {registros[1]}")
        print (f"Admin: {registros [2]}")

def inserir_usuario ():
    print ("Inserindo usuario...")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    login = input ("Login:")
    senha = input ("Senha:")
    admin = input ("Admin: ")
    sql_insert = "Insert into usuario (login,senha,admin) values (%s, %s, %s)" 
    dados = (login,senha,admin)
    cursor.execute (sql_insert,dados)
    conexao.commit ()

def atualizar_usuario ():
    print ("Atualizando Usuario")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    id = input ("Digite o ID: ")
    login = input ("Login: ")
    senha = input ("Senha: ")
    admin = input ("Admin: ")
    sql_update = "Update usuario set login = %s, senha = %s, admin = %s where id = %s"
    dados = (login,senha,admin,id)
    cursor.execute (sql_update,dados)
    conexao.commit ()

def deletar_usuario ():
    print ("Deletando Usuario...")
    conexao = conecta_db()
    cursor = conexao.cursor()
    id = input ("Digite o ID do Usuario: ")
    sql_delete = "delete from usuario where id =" + id
    cursor.execute (sql_delete)
    conexao.commit()

