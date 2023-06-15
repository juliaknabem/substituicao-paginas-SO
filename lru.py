class Pagina:
    def __init__(self, id_pagina):
        self.id_pagina = id_pagina
        self.timestamp = 0

def substituicao_paginas_LRU(qtd_quadros, qtd_paginas, arquivo_referencia):
    quadros = []
    contador_falta_pagina = 0
    timestamp = 0

    with open(arquivo_referencia, 'r') as file:
        referencia_paginas = [int(line) for line in file]

    for referencia in referencia_paginas:
        pagina_encontrada = False
        timestamp += 1

        for quadro in quadros:
            if quadro.id_pagina == referencia:
                pagina_encontrada = True
                quadro.timestamp = timestamp
                break

        if not pagina_encontrada:
            contador_falta_pagina += 1
            if len(quadros) < qtd_quadros:
                quadros.append(Pagina(referencia))
            else:
                quadros.sort(key=lambda x: x.timestamp)
                quadros[0] = Pagina(referencia)
                quadros[0].timestamp = timestamp

    return contador_falta_pagina

# Exemplo de uso
qtd_quadros = int(input("Digite o número de quadros endereçáveis na memória: "))
qtd_paginas = int(input("Digite o total de páginas distintas endereçáveis: "))
arquivo_referencia = input("Digite o nome do arquivo contendo a lista de páginas referenciadas: ")
faltas_pagina = substituicao_paginas_LRU(qtd_quadros, qtd_paginas, arquivo_referencia)
print("Total de faltas de página:", faltas_pagina)