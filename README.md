# Conversor de Imagens para Tons de Cinza e Preto e Branco

## Descrição
Este projeto é uma implementação simples em Python que realiza a manipulação básica de imagens. Ele permite:
- **Converter imagens coloridas para tons de cinza**: Usa uma fórmula padrão para calcular os níveis de cinza com base nos valores RGB dos pixels.
- **Binarizar imagens (preto e branco)**: Transforma a imagem em tons de cinza em uma imagem binária, onde os pixels podem ter apenas dois valores (preto ou branco) com base em um limite (threshold).

## Funcionalidades
- Recebe uma imagem colorida de entrada.
- Gera duas novas imagens:
  - **Tons de cinza**: Salva como `img_cinza.jpg`.
  - **Binarizada (preto e branco)**: Salva como `img_pb.jpg`.

## Pré-requisitos
Certifique-se de ter os seguintes requisitos instalados:
- Python 3.7 ou superior.
- Biblioteca Pillow. Para instalá-la, use o comando:
  ```bash
  pip install pillow
