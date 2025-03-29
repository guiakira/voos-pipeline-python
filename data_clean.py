import pandas as pd
import datetime
import logging
import re

# configurar logging
logging.basicConfig(filename='logs/flights_pipe.log', level=logging.INFO)
logger = logging.getLogger()

# url da base e caminho para salvar
url = "https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv"
output_path = "./data/processed/base_tratada.csv"

def padroniza_str(obs):
    return re.sub('[^A-Za-z0-9]+', '', obs.upper())

def clean_data(url, path_save):
    df = pd.read_csv(url, index_col=0)
    logger.info(f'Início da execução ; {datetime.datetime.now()}')

    # Seleção de colunas
    usecols = ["year", "month", "day", "hour", "minute", "dep_delay", "arr_delay", "carrier", "flight", "air_time", "distance", "origin", "dest"]

    if not set(usecols).issubset(set(df.columns)):
        logger.error(f"Mudança de schema; {datetime.datetime.now()} ")
        raise Exception("Mudança de schema")

    df_raw = df.loc[
        (~df["carrier"].isna()) &
        (~df["flight"].isna()) &
        (~df["year"].isna()) &
        (~df["hour"].isna()) &
        (~df["minute"].isna()) &
        (df["air_time"] > 0)
    ].loc[:, usecols]

    df_raw.drop_duplicates(inplace=True)
    df_raw = df_raw.astype("object")

    df_raw["date_time"] = pd.to_datetime(df_raw[["year", "month", "day", "hour", "minute"]], dayfirst=True)

    usecols2 = ["date_time", "arr_delay", "carrier", "flight", "air_time", "distance", "origin", "dest"]
    new_columns = ["data_hora", "atraso_chegada", "companhia", "id_voo", "tempo_voo", "distancia", "origem", "destino"]
    columns_map = {usecols2[i]: new_columns[i] for i in range(len(usecols2))}

    df_work = df_raw.loc[:, usecols2].copy()
    df_work.rename(columns=columns_map, inplace=True)

    df_work["distancia"] = df_work["distancia"].astype(float)
    df_work["companhia"] = df_work["companhia"].astype(str)
    df_work["id_voo"] = df_work["id_voo"].astype(str)
    df_work["atraso_chegada"] = df_work["atraso_chegada"].astype(str)
    df_work["origem"] = df_work["origem"].astype(str)
    df_work["destino"] = df_work["destino"].astype(str)

    for col in ["companhia", "id_voo", "origem", "destino"]:
        df_work[col] = df_work[col].apply(lambda x: padroniza_str(x))

    # salvar base tratada
    df_work.to_csv(path_save, index=False)

    # validação de perda de dados
    perc_perda = 1 - len(df_raw) / len(df)
    if perc_perda > 0.05:
        logger.warning(f"Muitas observações perdidas na seleção; {datetime.datetime.now()} ")

    logger.info(f'Base tratada exportada com {len(df_work)} registros ; {datetime.datetime.now()}')
    return df_work
