agenda = {
    "2025-07-05": "ocupado",
    "2025-07-12": "livre",
    "2025-07-19": "livre",
    "2025-07-26": "ocupado",
    "2025-08-02": "livre",
    "2025-08-09": "ocupado",
}

def datas_disponiveis(agenda):
    lista_resultado = []
    for chave, valor in agenda.items():
        if valor == "livre":
            lista_resultado.append(chave)
        
    return sorted(lista_resultado)

filtro = datas_disponiveis(agenda)
for item in filtro:
    print(item)

    
    