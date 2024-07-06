#Lorrana Costa
#Estágio em Programação/Desenvolvimento
#Python


produtos = []


def cadastrar_produto(nome, descricao, valor, disponivel):
   
    novo_produto = {
        "Nome": nome,
        "Descrição": descricao,
        "Valor": valor,
        "Disponível": disponivel
    }
    
    produtos.append(novo_produto)
    
    listar_produtos()


def listar_produtos():
    
    produtos_ordenados = sorted(produtos, key=lambda x: x["Valor"])
    
    print("Lista de Produtos (ordenada por valor):")
    for produto in produtos_ordenados:
        print(f"Nome: {produto['Nome']}, Valor: {produto['Valor']}")
    print("\n")


cadastrar_produto("Produto A", "Descrição A", 50.0, "Sim")
cadastrar_produto("Produto B", "Descrição B", 30.0, "Sim")
cadastrar_produto("Produto C", "Descrição C", 70.0, "Não")


listar_produtos()
