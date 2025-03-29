# Apresentação
Trabalho final da disciplina de Python for Data Engineer, da turma "2024 - MBA DE_06".
Professora Carolina Zambelli Kamada.

# Integrantes do Grupo

Ellen Cristina Sousa Viana | RA: 2404184
Gabriela Yuri Uyeda Ando | RA: 2404207
Guilherme Akira Enokihara | RA: 2403928

# Pipeline de Processamento de Voos

Este projeto realiza a limpeza e transformação de dados de uma base de voos contida no link abaixo:
https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv

## Estrutura

- `data_clean.py`: Limpa os dados brutos e salva a base tratada na pasta data\processed.
- `transform.py`: Aplica transformações com as funções criadas de conversão de tempo em horas e classificação por turno do horário de partida do voo.
- `main.py`: Executa o pipeline completo.
- `requirements.txt`: Dependências do projeto.

## Como executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Rode o pipeline:
   ```bash
   python main.py
   ```

## Logs

Os logs são salvos na pasta `./logs/`.# voos-pipeline-python
# voos-pipeline-python
# voos-pipeline-python
