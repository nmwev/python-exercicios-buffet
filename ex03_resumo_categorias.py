servicos = [
    {"servico": "buffet completo", "categoria": "alimentacao", "valor": 8500},
    {"servico": "DJ", "categoria": "entretenimento", "valor": 2200},
    {"servico": "decoracao flores", "categoria": "decoracao", "valor": 3100},
    {"servico": "buffet drinks", "categoria": "alimentacao", "valor": 1800},
    {"servico": "fotografia", "categoria": "entretenimento", "valor": 2900},
    {"servico": "iluminacao", "categoria": "decoracao", "valor": 1500},
]
def resumo_por_categoria(servicos):
    totais_categorias = {}

    for item in servicos:
        nome_cat = item["categoria"]
        valor_gasto = item["valor"]

        if nome_cat in totais_categorias:
            totais_categorias[nome_cat] += valor_gasto
        else:
            totais_categorias[nome_cat] = valor_gasto

    return totais_categorias

print(resumo_por_categoria(servicos))