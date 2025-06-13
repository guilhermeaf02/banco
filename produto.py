from conexao import conecta_db

def menu_produto ():

    print ("----------------------------------")
    print ("       Cadastro de Produto        ")
    print ("----------------------------------")
    print ("  1- Listar Produto               ")
    print ("  2- Consultar produto por ID     ")
    print ("  3- Inserir                      ")
    print ("  4- Alterar                      ")
    print ("  5- Deletar                      ")
    print ("  6- Sair do Sistema do produto   ")
    print ("----------------------------------")

    while True:

        opcao = input ("Escolha uma Opção: ")

        if opcao == "1":
            listar_produto ()
        elif opcao == "2":
            listar_produto ()
            consultar_produto_por_id ()
        elif opcao == "3":
            listar_produto ()
            inserir_produto ()
            listar_produto ()
        elif opcao == "4":
            listar_produto ()
            atualizar_produto ()
            listar_produto ()
        elif opcao == "5":
            listar_produto ()
            deletar_produto ()
            listar_produto ()
        elif opcao == "6":
            print ("Sair do Sistema do Produto")
            break
        else:
            print ("Opção invalida, tenta novamente")

def listar_produto ():

    conexao = conecta_db ()
    cursor = conexao.cursor ()
    sql_listar = """ select produto.id, produto.nome, produto.valor_venda, produto.estoque,c.id as id_categoria, c.nome as nome_categoria	
                      from produto
                      inner join categoria c on (produto.categoria_id = c.id)
                      order by produto.id asc
    
    """
    cursor.execute (sql_listar)
    registros = cursor.fetchall ()

    print ("---------------_--------------------------------------------------------------------------------")
    for registro in registros:
        print (f"ID: {registro[0]} -  Nome {registro[1]} - Valor Venda {registro[2]} - Estoque {registro[3]} - Categoria {registro [5]}")
    print ("------------------------------------------------------------------------------------------------")

def consultar_produto_por_id ():
    id = input ("Digite o ID: ")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    cursor.execute ("select id,nome,valor_venda,estoque from produto where id =" + id)
    registros = cursor.fetchone ()
    
    if registros is None:
        print ("Produto não encontrada")
    else:
        print (f"ID: {registros[0]}")
        print (f"Produto: {registros[1]}")
        print (f"Valor venda: {registros [2]}")
        print (f"Estoque: {registros [3]}")

def inserir_produto ():
    print ("Inserindo produto...")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    nome = input ("Produto:")
    valor_venda =  float (input ("Valor de Venda:"))
    estoque =  float (input ("Estoque: "))
    categoria_id = int (input("ID Cagetoria: "))
    sql_insert = "Insert into produto (nome,valor_venda,estoque,categoria_id) values ( %s, %s, %s, %s )"
    dados = (nome,valor_venda,estoque, categoria_id)
    cursor.execute (sql_insert,dados)
    conexao.commit ()

def atualizar_produto ():
    print ("Atualizando produto")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    id = input ("Digite o ID: ")
    nome = input ("Produto:")
    valor_venda = float (input ("Valor de Venda: "))
    estoque = float (input ("Estoque: "))
    sql_update = "Update produto set nome = %s, valor_venda = %s, estoque = %s where id = %s"
    dados = (nome,valor_venda,estoque,id)
    cursor.execute (sql_update,dados)
    conexao.commit ()

def deletar_produto ():
    print ("Deletando produto...")
    conexao = conecta_db ()
    cursor = conexao.cursor ()
    id = input ("Digite o ID: ")
    sql_delete = "delete from produto where id =" + id
    cursor.execute (sql_delete)
    conexao.commit ()

