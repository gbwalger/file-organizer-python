import pandas as pd
import os

def carregar_planilha(planilha):
    df = pd.read_excel(planilha)
    return df

def criar_pastas(df):
    pasta_arquivos = "arquivos"
    for _, linha in df.iterrows():
        caminho_pasta = os.path.join(pasta_arquivos, linha["categoria"])
        os.makedirs(caminho_pasta, exist_ok=True)
        
