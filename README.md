# ClimateCore

Projeto de hackathon sobre mudanças climáticas usando somente:

- Python
- Flask
- HTML
- CSS

Sem JavaScript.

## Funcionalidades

- Página inicial
- Calculadora de CO2
- Gráfico gerado com Matplotlib
- Clima atual por cidade
- Histórico aproximado de temperatura
- Emissões globais dos últimos 20 anos
- Página sobre gelo polar
- Impactos
- Cenários futuros
- Notícias via RSS
- Soluções

## Instalação no Windows

Abra o terminal dentro da pasta do projeto.

### 1. Criar ambiente virtual

```text
python -m venv venv
```

### 2. Ativar

```text
venv\Scripts\activate
```

### 3. Instalar dependências

```text
pip install -r requirements.txt
```

### 4. Executar

```text
python app.py
```

### 5. Abrir

No navegador:

http://127.0.0.1:5000

## APIs e fontes

Clima:
Open-Meteo.

Emissões:
Our World in Data / Global Carbon Project.

Referências:
NASA, NOAA, NSIDC, ESA e IPCC.

Notícias:
feeds RSS configurados em `services/news_api.py`.

## Observação

Os fatores da calculadora são educativos e devem ser revisados e citados antes da apresentação final do hackathon.

Os dados externos podem mudar, ficar indisponíveis ou utilizar metodologias diferentes.
