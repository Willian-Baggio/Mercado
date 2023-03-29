# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:09:14 2023

@author: PC
"""

from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.conversor import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('===================================')
    print('=========== Bem-vindo(a) ==========')
    print('===================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Editar produto')
    print('4 - Remover produto')
    print('5 - Comprar produto')
    print('6 - Visualizar carrinho')
    print('7 - Fechar pedido')
    print('8 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        editar_produtos()
    elif opcao == 4:
        remover_produto()
    elif opcao == 5:
        comprar_produto()
    elif opcao == 6:
        visualizar_carrinho()
    elif opcao == 7:
        fechar_pedido()
    elif opcao == 8:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('===================')
    
    while True:
        nome = input('Informe o nome do produto: ')
        if nome.strip() and not nome.isdigit():
            break
        else:
            print('O nome do produto não pode ser estar vazio e não pode ser um valor numérico. Tente novamente.')
        
    while True:
        preco_input = input('Informe o preço do produto: ')
        try:
            preco = float(preco_input)
            if preco > 0:
                break
            else:
                print('O preço do produto deve ser um número maior que zero. Tente novamente.')
        except ValueError:
            print('O preço do produto deve ser um número. Tente novamente.')
     
    while True:
        quantidade_input = input('Informe a quantidade do produto: ')
        try:
            quantidade = int(quantidade_input)
            if quantidade > 0:
                break
            else:
                print('A quantidade do produto deve ser maior que zero. Tente novamente')
        except ValueError:
            print('A quantidade do produto deve ser um número. Tente novamente')


    produto: Produto = Produto(nome, preco, quantidade)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('----------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()
    
def editar_produtos() -> None:
    
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('----------------')
            
    print('----------------------------------------------------')
    print('=============== Opções Disponíveis ===================')
    print('1 - Editar nome do produto')
    print('2 - Editar preço do produto')
    print('3 - Editar quantidade do produto')
    print('4 - Voltar ao menu')

    opcao = int(input())

    if opcao == 1:
        print('\nInforme o código do produto que deseja alterar: ')
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)
            
        if codigo <= len(produtos):
            while True:
                novo_nome = (input("Informe o novo nome do produto: "))
                if novo_nome.strip() and not novo_nome.isdigit():
                    break
                else:
                    print('\nO nome do produto não pode ser estar vazio e não pode ser um valor numérico. Tente novamente.')
                    
            produtos[codigo - 1].editar_nome(novo_nome)
            print('Nome alterado')
            sleep(2)
            main()
        
        else:
            print('Código de produto inválido.')
            sleep(2)
            editar_produtos()
        
    elif opcao == 2:
        
        print('\nInforme o código do produto que deseja alterar: ')
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)
        

        if codigo <= len(produtos):
            while True: 
                novo_preco = input("Informe o novo preço do produto: ")
                try:
                    preco = float(novo_preco)
                    if preco > 0:
                        break
                    else:
                        print('\nO preço do produto deve ser um número maior que zero. Tente novamente.')
                except ValueError:
                    print('\nO preço do produto deve ser um número. Tente novamente.')
                    
            produtos[codigo - 1].editar_preco(preco) 
            print('Preço do produto alterado')
            sleep(2)
            main()
        
        else:
            print('Código de produto inválido.')
            sleep(2)
            editar_produtos()
        
    elif opcao == 3:
        print('\nInforme o código do produto que deseja alterar: ')
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)


        if codigo <= len(produtos):
            while True:      
                nova_quantidade = input("Informe o nova quantidade do produto: ")
                try:
                    quantidade = int(nova_quantidade)
                    if quantidade > 0:
                        break
                    else:
                        print('\nA quantidade do produto deve ser maior que zero. Tente novamente')
                except ValueError:
                    print('\nA quantidade do produto deve ser um número. Tente novamente')
            produtos[codigo - 1].editar_quantidade(quantidade) 
            print('Quantidade do produto alterado')
            sleep(2)
            main()
        
        else:
            print('Código de produto inválido.')
            sleep(2)
            editar_produtos()
        
    elif opcao == 4:
        print('Retornando ao menu')
        sleep(2)
        main()
        
    else:
        print('Opção inválida.')
        sleep(2)
        main()

def remover_produto() -> None:
    print('--------------------------------------------------------------')
    print('================== Opções Disponíveis ======================')
    print('\n1 - Remover produto da lista'
          '\n2 - Remover produto do carrinho'
          '\n3 - Voltar ao menu')
    opcao = int(input())
    
    if opcao == 1:
        if len(produtos) > 0:
            print('Listagem de produtos')
            print('--------------------')
            for produto in produtos:
                print(produto)
                print('----------------')
                
            print('--------------------------------------------------')
            print('\nInforme o código do produto que deseja remover: ')
            codigo: int = int(input())

            produto: Produto = pega_produto_por_codigo(codigo)
            
            if codigo <= len(produtos):
                del produtos[codigo - 1]
                print('Produto removido')
                sleep(2)
                main()
                
            else:
                print('Código de produto inválido.')
                sleep(2)
                remover_produto()
        else:
            print('Ainda não exite produto cadastrado')
            sleep(2)
            main()
            
    elif opcao == 2:
        if len(carrinho) > 0:
            print('Produtos no carrinho: ')
            for item in carrinho:
                for dados in item.items():
                    print(dados[0])
                    print('-----------------------')
                    sleep(1)
            
            print('--------------------------------------------------')
            print('\nInforme o código do produto que deseja remover: ')
            codigo: int = int(input())

            produto: Produto = pega_produto_por_codigo(codigo)
            
            for item in carrinho:
                if list(item.keys())[0].codigo == codigo:
                    produto_selecionado = list(item.keys())[0]
                    carrinho.remove(item)
                    print('Produto removido do carrinho')
                    sleep(2)
                    main()
                    break
                
                    # adiciona o produto de volta caso não tenha sido removido
                    carrinho.append({produto_selecionado: 1})
                else:
                   print('Código de produto inválido.')
                   sleep(2)
                   remover_produto()
    
                
        else:
            print('Ainda não existe produto cadastrado')
            sleep(2)
            main()
                   
    elif opcao == 3:
        sleep(2)
        menu()
        

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('--------------------------------------------------------------')
        print('================== Produtos Disponíveis ======================')
        for produto in produtos:
            print(produto)
            print('---------------------------------------------------------')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)
           
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quantidade: int = item.get(produto)
                    if quantidade:
                        item[produto] = quantidade + produto.quantidade
                        print(f'O produto {produto.nome} agora possui {quantidade + produto.quantidade} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para vender.')
    sleep(2)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for produto, quantidade in item.items():
                if quantidade > 1:
                    print(f'Código: {produto.codigo} \nNome: {produto.nome} \nPreço: R$ {produto.preco:,.2f} \nQuantidade: {quantidade}')
                    print('-----------------------')
                    sleep(1)
                    
                else:     
                    print(f'Código: {produto.codigo} \nNome: {produto.nome} \nPreço: R$ {produto.preco:,.2f} \nQuantidade: {produto.quantidade}')
                    print('-----------------------')
                    sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    
    if len(carrinho) > 0:
        valor_total1: float = 0
        valor_total2: float = 0
        print('Produtos do Carrinho')
        fim_compra = []
        for item in carrinho:
            valor_total1 = 0
            valor_total2 = 0
            for produto, quantidade in item.items():
                print(produto.nome)
                if quantidade > 1:
                    valor_total1 += produto.preco * quantidade
                else:
                    valor_total2 += produto.preco * produto.quantidade
            fim_compra.append(valor_total1 + valor_total2)
        soma_produtos = sum(fim_compra)
        print(f'Sua fatura é {formata_float_str_moeda(soma_produtos)}')
        print('Volte sempre!')
        sleep(5)
        carrinho.clear()
    else:
        print('Ainda não existem produtos no carrinho.')
        sleep(2)
        menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()
