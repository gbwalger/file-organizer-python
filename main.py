import os
import logging
from planilha import carregar_planilha, criar_pastas
from arquivos import renomear_arquivos, mover_arquivos

logging.basicConfig(
    filename="relatorio_planilha.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

df = carregar_planilha("planilha_cliente.xlsx")

criar_pastas(df)

pasta_arquivos = "arquivos"

arquivos_processados = 0
arquivos_renomeados = 0
arquivos_movidos = 0
erros_encontrados = 0

for _, linha in df.iterrows():
    nome_atual = os.path.join(pasta_arquivos, linha["arquivo_atual"])
    novo_nome = os.path.join(pasta_arquivos, linha["novo_nome"])
    nome_pasta = os.path.join(pasta_arquivos, linha["categoria"])

    arquivos_processados += 1

    if renomear_arquivos(nome_atual, novo_nome):
        logging.info(f"Renomeando {linha['arquivo_atual']} -> {linha['novo_nome']} ✅")
        arquivos_renomeados +=1
        if mover_arquivos(novo_nome, nome_pasta):
            logging.info(f"🚚 Movendo {linha['novo_nome']} para {linha['categoria']}...")
            arquivos_movidos += 1
        else:
            logging.error(f"❌ Arquivo {linha['novo_nome']} não encontrado.")
    else:
        logging.error(f"❌ Arquivo {linha['arquivo_atual']} não encontrado.")
        erros_encontrados += 1
         
print("📝 RELÁTORIO - Resumo Geral:")
print(f"📂 Arquivos processados: {arquivos_processados}")
print(f"✍ Arquivos renomeados: {arquivos_renomeados}")
print(f"🚚 Arquivos movidos: {arquivos_movidos}")
print(f"❌ Erros encontrados: {erros_encontrados}")
    


    


    