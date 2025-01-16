README - Conversor de Imagens para Tons de Cinza e Preto e Branco
Descrição
Este projeto é uma implementação simples em Python para manipulação de imagens, que realiza as seguintes funções:

Converter imagens coloridas para tons de cinza: Aplica uma fórmula padrão para calcular os níveis de cinza com base nos valores RGB dos pixels.

Binarizar imagens (preto e branco): Transforma a imagem em tons de cinza em uma imagem binária, onde os pixels podem ter apenas dois valores (preto ou branco) com base em um limite (threshold).

Funcionalidades
Recebe uma imagem colorida de entrada.
Gera duas imagens:
Em tons de cinza: Salva como img_cinza.jpg.
Binarizada: Salva como img_pb.jpg.
Pré-requisitos
Python 3.7 ou superior.
Biblioteca Pillow instalada (pip install pillow).
Como usar
Coloque a imagem que deseja processar no mesmo diretório do script e renomeie-a para fotoTeste.jpg.
Execute o script.
Verifique os arquivos gerados:
img_cinza.jpg: Imagem em tons de cinza.
img_pb.jpg: Imagem binarizada.
Exemplo de Entrada
Imagem colorida: fotoTeste.jpg.

Exemplos de Saída
Imagem em tons de cinza: img_cinza.jpg.
Imagem binarizada: img_pb.jpg.
