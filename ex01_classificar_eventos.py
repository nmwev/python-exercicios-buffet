eventos = [
    {"nome": "Casamento Silva", "convidados": 320},
    {"nome": "Aniversário 15 anos", "convidados": 80},
    {"nome": "Confraternização empresa", "convidados": 45},
    {"nome": "Formatura medicina", "convidados": 210},
    {"nome": "Chá de bebê", "convidados": 30},
]

def classificar_eventos(lista_eventos):
    lista_resultado = []

    for evento in lista_eventos:
        if evento["convidados"] < 50:
            lista_resultado.append({"nome": evento["nome"], "porte": "pequeno"})
        elif 50 <= evento["convidados"] < 150:
            lista_resultado.append({"nome": evento["nome"], "porte": "medio"})
        else:
            lista_resultado.append({"nome": evento["nome"], "porte": "grande"})

    return lista_resultado

resultado = classificar_eventos(eventos)
for item in resultado:
    print(item)