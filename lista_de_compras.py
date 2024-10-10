# 1- Adicionar o produto.
# 2- Retirar o produto.
# 3- Pesquisar produto.
# 4- Sair do programa.


id_product = 1 

def add_product():
    
    global id_product
    global name
    
    name = input("Digite o nome do produto: ")
    
    print("Selecione a unidade de medida:")
    print(" 1: Kg\n 2: Gramas\n 3: Litro\n 4: Mililitro\n 5: Unidade\n 6: Metro\n 7: Centímetro")
    
    size = input("Digite o número correspondente à unidade de medida: ")

    value_size = None
    size_type = ""

    if size == '1':
        value_size = float(input("Digite quantos kilogramas o produto tem: "))
        size_type = "Kg"
    elif size == '2':
        value_size = float(input("Digite quantas gramas o produto tem: "))
        size_type = "Gramas"
    elif size == '3':
        value_size = float(input("Digite quantos litros o produto tem: "))
        size_type = "Litros"
    elif size == '4':
        value_size = float(input("Digite quantos mililitros o produto tem: "))
        size_type = "Mililitros"
    elif size == '5':
        value_size = int(input("Digite a unidade do produto: "))
        size_type = "Unidades"
    elif size == '6':
        value_size = float(input("Digite quantos metros o produto tem: "))
        size_type = "Metros"
    elif size == '7':
        value_size = float(input("Digite quantos centímetros o produto tem: "))
        size_type = "Centímetros"
    else:
        print("ERRO, por favor, selecione um número válido correspondente à unidade de medida!")
        return None  

    quantity = int(input("Digite a quantidade de itens que será adicionada: "))
    product_description = input("Digite uma descrição do produto: ")

    products = {
        "ID": id_product,
        "Nome do produto": name,
        "Medida": f"{value_size} {size_type}",
        "Quantidade": quantity,
        "Descrição": product_description, 
    }

    id_product += 1
    
    return products

def remove_product(product_list):
    
    if not product_list:
        print("\nNão há produtos para remover!")
        return

    id_remove = int(input("\nDigite o ID do produto que deseja remover: "))

    find_product = False
    for product in product_list:
        if product["ID"] == id_remove:
            product_list.remove(product)
            find_product = True
            print(f"\nProduto com ID {id_remove} removido com sucesso!")
            break

    if not find_product:
        print(f"\nProduto com ID {id_remove} não encontrado!")



def list_products(product_list):
    if not product_list:
        print("\nNenhum produto foi adicionado ainda!")
        return

    print("\nLista de produtos do mercado:")
    for product in product_list:
        print(f"\nID: {product['ID']}")
        print(f"Nome: {product['Nome do produto']}")
        print(f"Medida: {product['Medida']}")
        print(f"Quantidade: {product['Quantidade']}")
        print(f"Descrição: {product['Descrição']}")
   

def search_for_name(product_list):
    if not product_list:
        print(" Nenhum produto foi encontrado!")
        return

    productName = input("\nDigite o nome do produto que deseja visualizar")
    if productName == name:
        print(f"Aqui está o produto {name}")
    else:
        print("Produto nao encontrado.")
        

def options_menu_of_products():
    product_list = []
    
    while True:
        print("\nBem vindo ao mercado do Joaozin!\n\nPor favor selecione uma das opções abaixo: ")
        print("1: Adicionar produto")
        print("2: Remover Produto")
        print("3: Visualizar produtos adicionados")
        print("4: Pesquisar produto")
        print("Digite 'esc' ou 'ESC' para sair do programa! ")
        option = input()
        
        if option == 'esc' or option == 'ESC':
            print("Obrigado e volte sempre!")
            break
        
        if option not in ['1', '2', '3', '4']:
            print("ERRO, por favor, tente novamente abaixo! \n\n")
            continue
        
        if option == '1':
            productsAdd = add_product()
            product_list.append(productsAdd)
            print("\nProduto adicionado com sucesso!")
            print(productsAdd)
        
        if option == '2':
            remove_product(product_list)
        
        if option == '3':
            list_products(product_list)
        
        if option == '4':
            search_for_name(product_list)
            
            
                     
options_menu_of_products()