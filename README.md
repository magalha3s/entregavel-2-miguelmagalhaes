# Entregável 2 — Harpia UFRJ
> Miguel Rangel de Magalhães


## Sobre o projeto

Este projeto implementa uma aplicação em Python para visualizar anotações de objetos em imagens por meio de bounding boxes (caixas delimitadoras).

Os dados são obtidos do arquivo dados/anotacoes.csv, que contém os identificadores das classes e as coordenadas de cada retângulo. Com essas informações, o programa associa as anotações às respectivas imagens, desenha as caixas utilizando OpenCV e apresenta os arquivos individualmente em uma janela interativa.

As imagens processadas são armazenadas em resultados/, preservando seus nomes originais. A ferramenta permite inspecionar visualmente as anotações fornecidas e verificar o posicionamento dos retângulos antes de utilizar os dados em aplicações de visão computacional.

## Dependências

Para executar o projeto, são necessários:

- **Python**
- **opencv-python**

A leitura do CSV e o gerenciamento dos caminhos utilizam os módulos csv e pathlib, disponíveis na biblioteca padrão do Python.

## Como executar

Clone o repositório e acesse seu diretório:
```
git clone https://github.com/magalha3s/entregavel2-miguelmagalhaes.git
cd entregavel2-miguelmagalhaes
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/main.py
```
A execução deve ocorrer a partir da raiz do projeto, em um ambiente com suporte à interface gráfica do OpenCV.

## Navegação

| Tecla  |  Função          |   |   |   |
|--------|------------------|---|---|---|
| Espaço | Avançar Imagem   |   |   |   |
| q      | Sair do Programa |   |   |   |
|        |                  |   |   |   |

As demais teclas não alteram o estado do programa.
## Identificação das classes

As anotações são diferenciadas visualmente por suas cores:

- Classe 1: azul.
- Classe 0: verde.

A legenda apresentada na janela relaciona cada cor ao respectivo identificador. Os IDs são mantidos conforme os dados de entrada, sem atribuir significado semântico às classes.

## Organização do código
```
├── dados/
│   └── anotacoes.csv
├── imagens/
│   └── arquivos JPG originais
├── resultados/
│   └── imagens anotadas
├── evidencias/
│   ├── terminal.png
│   └── visualizador.png
├── src/
│   ├── main.py
│   ├── modelos.py
│   ├── globals.py
│   └── arquivos.py
├── requirements.txt
└── README.md
```
## Arquivos gerados

As imagens anotadas são gravadas no diretório resultados/, utilizando os nomes dos arquivos de entrada. O desenho das caixas é realizado sobre a imagem carregada em memória, sem sobrescrever diretamente os arquivos originais.