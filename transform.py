import pandas as pd

def calc_horas(coluna_tempo_voo):
    return coluna_tempo_voo / 60

def classifica_turno(coluna_data_hora):
    hora = coluna_data_hora.hour
    if hora >= 6 and hora < 12:
        return "MANHÃ"
    elif hora >= 12 and hora < 18:
        return "TARDE"
    elif hora >= 18 and hora < 24:
        return "NOITE"
    else:
        return "MADRUGADA"

def transform_data(df):
    df['tempo_voo_horas'] = calc_horas(df['tempo_voo'])
    df['turno'] = df['data_hora'].apply(classifica_turno)
    print(df.head())
    return df