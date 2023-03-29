# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:08:30 2023

@author: PC
"""

from utils.conversor import formata_float_str_moeda

class Produto:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float, quantidade: int) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        self.__quantidade: int = quantidade
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco
    
    @property
    def quantidade(self: object) -> int:
        return self.__quantidade

    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nPeço: {formata_float_str_moeda(self.preco)} \nQuantidade: {self.quantidade}'
    
    def editar_nome(self: object, novo_nome: str) -> None:
        self.__nome = novo_nome

    def editar_preco(self: object, novo_preco: float) -> None:
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            print("O preço deve ser maior do que zero.")

    def editar_quantidade(self: object, nova_quantidade: int) -> None:
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            print("A quantidade não pode ser negativa.")