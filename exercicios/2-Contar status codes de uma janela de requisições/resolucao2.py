status_codes = [200, 200, 404, 500, 200, 404, 200, 500, 500, 500]

def contar_status(status_codes):
    # Cria um dicionário para armazenar a contagem de cada status code
    contagem = {}
    # percorre a lista de status codes e conta a ocorrência de cada um
    for status in status_codes:
        # verifica se o status code já está no dicionário, se não estiver, adiciona com valor inicial 0
        if status not in contagem:
            contagem[status]=0
            # a cada vez que o status code é encontrado, incrementa a contagem em 1
        contagem[status] += 1
    print(contagem)
    
    return contagem
        


