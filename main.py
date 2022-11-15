# 1. Crie um dicionário (d1) com a seguinte combinação de chave/valor:
# "nome"/"Kenzinho"
# "cidade"/"Curitiba"
# "modulo"/"M5"
#  imprima d1:
d1 = {"nome": "Kenzinho", "cidade": "Curitiba", "modulo": "M5"}  # Forma literal
d1 = dict(nome="Kenzinho", cidade="Curitiba", modulo="M5")  # Forma builtin
print(d1)


# 2. Imprima o tipo de d1;
print(type(d1))


# 3. Imprima o valor da chave "nome" de d1;
print(d1.get("nome"))


# 4. Imprima o valor da chave "cidade" de d1;
print(d1.get("cidade"))


# 5. Imprima o valor da chave "modulo" de d1;
print(d1.get("modulo"))


# 6. Tente imprimir o valor da chave "telefone" de d1,
# e caso ela não exista, imprima "a chave telefone não existe";
print(d1.get("telefone", "a chave telefone não existe"))


# 7. Imprima somente as chaves de d1 (Pode ser no formato dict_keys);
print(d1.keys())  # Formato dict_keys
print(list(d1.keys()))  # Formato com list


# 8. Imprima somente os valores de d1 (Pode ser no formato dict_values);
print(d1.values())  # Formato dict_values
print(list(d1.values()))  # Formato com list


# 9. A partir das seguintes listas, crie um dicionario d2 em que lista_1 sejam suas chaves
# e lista_2 sejam seus valores, na mesma ordem. Imprima d2;
lista_1 = ["telefone", "casado", "idade"]
lista_2 = ["999-999-999", True, 32]

d2 = dict(zip(lista_1, lista_2))
print(d2)


# 10. Atualize o dicionário d1 com o conteúdo do dicionário d2. Imprima d1;
d1 = d2  # Forma literal
d1.update(d2)  # Formato builtin
print(d1)


# 11. Delete a chave "casado" de d1;
del d1["casado"]
print(d1)


# 12. Remova e imprima o valor da chave "idade" de d1. Imprima d1;
print(d1.pop("idade"))
print(d1)


# 13. Remova todos items do dicionário d1. Imprima d1;
d1.clear()
print(d1)
