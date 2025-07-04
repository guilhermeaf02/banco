from conexao import conecta_db
from datetime import datetime

def menu_venda():
    print ("|---------------------------------")
    print ("|          MENU - VENDAS          ")
    print ("|---------------------------------")
    print ("|       1 - CONSULTAR VENDAS      ")
    print ("|       2 - INSERIR VENDAS        ")
    print ("|       3 - SAIR                  ")
    print ("----------------------------------")
    
    conexao = conecta_db()

    while True:
        opcao = input ("Escolha uma opção:")
        if opcao == "1":
            consultar_venda()
        elif opcao == "2":
             inserir_venda(conexao)
        elif opcao == "3":
             ("Sair")
             break
        else:
            print ("Opção Inválida, tente novamente")
            continue

def consultar_venda ():
    print ("Não Implemantado")

def insert_item_venda (conexao,item_venda):
    cursor = conexao.cursor ()
    sql_insert_item = """
        insert into itens_venda (id_venda,id_produto,quantidade,valor_unitario,valor_total)
        values (%s, %s, %s, %s, %s)
"""
    cursor.execute (sql_insert_item, item_venda)
    conexao.commit ()

    
def inserir_venda(conexao):
    id_cliente = input ("Digite o ID do cliente:")
    data_venda = datetime.now()
    numero = input ("Digite o número da venda:")
    valor_venda = 0

    cursor = conexao.cursor ()
    sql_insert_venda = """
    insert into venda (id_cliente, data_venda, numero_venda, valor_venda)
    values (%s, %s, %s, %s) returning id;
"""    
    dados_vendas = (id_cliente, data_venda, numero, valor_venda)
    cursor.execute (sql_insert_venda,dados_vendas)
    conexao.commit ()
    venda_id = cursor.fetchone ()[0]


    itens_venda = []
    while(True):
        id_produto = int (input("Digite o ID do produto:"))
        quantidade = float (input("Digite a quantidade: "))
        preco_unitario = float (input("Digite o valor únitario: "))
        valor_total = quantidade * preco_unitario
        
        itens_venda.append ({"id_produto": id_produto,
                            "quantidade": quantidade,
                            "preco_unitario": preco_unitario,
                            "valor_total": valor_total})
        
        print (itens_venda)
        continua = input ("Desejar adicionar outro item? (S/N):")
        if continua == "N":
            break

    id_venda = venda_id
    for item in itens_venda: 
        item_data = (id_venda, item['id_produto'], item['quantidade'], item['preco_unitario'], item['valor_total'])
        insert_item_venda (conexao, item_data)
        
