import os

pasta_arquivos = "arquivos"
lista_de_arquivos = os.listdir(pasta_arquivos)
contador = 1

for arquivo in lista_de_arquivos:
    caminho_completo_origem = os.path.join(pasta_arquivos, arquivo)

    if os.path.isdir(caminho_completo_origem):
        continue

    # CHECAGEM E ATUALIZAÇÃO DO CONTADOR
    if len(arquivo) > 4 and arquivo[:3].isdigit() and arquivo[3] == "_":
        print(f"⏩ Ignorando arquivo já processado: {arquivo}")
        
        # O PULO DO GATO: Descobre o número do arquivo antigo (ex: "004" vira o número 4)
        numero_existente = int(arquivo[:3])
        
        # Se esse número for maior ou igual ao nosso contador atual,
        # o contador pula para o próximo número depois dele (ex: 4 + 1 = 5)
        if numero_existente >= contador:
            contador = numero_existente + 1
        continue

    # Se o arquivo for virgem/puro, ele pega o próximo número da sequência livre
    prefixo = str(contador).zfill(3) 
    novo_nome_arquivo = f"{prefixo}_{arquivo}"
    
    caminho_completo_destino = os.path.join(pasta_arquivos, novo_nome_arquivo)
    os.rename(caminho_completo_origem, caminho_completo_destino)
    print(f"✅ Renomeando {arquivo} -> {novo_nome_arquivo}")
    
    contador += 1