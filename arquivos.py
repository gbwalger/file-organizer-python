import pandas as pd
import os
import shutil
import logging

logging.basicConfig(
    filename="relatorio_planilha.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def renomear_arquivos(origem, destino):
    try:
        nome_origem = os.path.basename(origem)
        nome_destino = os.path.basename(destino)
        if os.path.exists(origem):
            os.rename(origem, destino)
            return True
        else:
            return False
    except Exception as e:
        logging.error(f"❌ [ERROR] Arquivo: {nome_origem}\nErro: {e}")
def mover_arquivos(origem, destino):
    try:
        nome_origem = os.path.basename(origem)
        nome_destino = os.path.basename(destino)
        if os.path.exists(origem):
            shutil.move(origem, destino)
            return True
        else:
            return False
    except Exception as e:
        logging.error(f"❌ [ERROR] Arquivo: {nome_origem}\nErro: {e}")

