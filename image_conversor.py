from PIL import Image


# Função para converter uma imagem colorida para níveis de cinza
def cor_cinza(image_path):
    # Abrir a imagem usando PIL
    img = Image.open(image_path)
    img = img.convert("RGB") 
    width, height = img.size
    pixels = img.load()

    # Criar nova imagem em tons de cinza
    imagem_cinza = Image.new("L", (width, height))  # 'L' para indicar imagem em tons de cinza
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Fórmula para converter RGB para cinza: 0.3 * R + 0.59 * G + 0.11 * B
            valor_escala_cinza = int(0.3 * r + 0.59 * g + 0.11 * b)
            imagem_cinza.putpixel((x, y), valor_escala_cinza)

    return imagem_cinza


# Função para binarizar a imagem (preto e branco)
def cinza_para_pb(img_cinza, threshold=127):
    width, height = img_cinza.size
    img_pb = Image.new("1", (width, height))  # '1' indica imagem binária (preto e branco)

    for y in range(height):
        for x in range(width):
            # Se o valor for maior que o limite (threshold), é branco (255), caso contrário é preto (0)
            pixel_value = img_pb.getpixel((x, y))
            binary_value = 255 if pixel_value > threshold else 0
            img_pb.putpixel((x, y), binary_value)

    return img_pb


# Exemplo:
if __name__ == "__main__":
    # Caminho da imagem original
    image_path = "fotoTeste.jpg"

    # Caminhos para salvar as novas imagens
    img_cinza_saida = "img_cinza.jpg"
    img_binaria_saida = "img_pb.jpg"

    # Converter para níveis de cinza
    imagem_tCinza = cor_cinza(image_path)
    imagem_tCinza.save(img_cinza_saida)
    print(f"Imagem em níveis de cinza salva em: {img_cinza_saida}")

    # Converter para binário
    imagem_binaria = cinza_para_pb(imagem_tCinza)
    imagem_binaria.save(img_binaria_saida )
    print(f"Imagem binarizada (preto e branco) salva em: {img_binaria_saida }")
