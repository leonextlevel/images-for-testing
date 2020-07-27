import os
import cv2
from werkzeug.datastructures import FileStorage
import tempfile


def img_transform(path_img, rotacao=0, zoom=1.0, force_gray=False, desfoque=False):
    imagem = cv2.imread(path_img)
    altura, largura = imagem.shape[:2]
    ponto = (largura / 2, altura / 2)

    # Rotaciona a imagem
    img_rotacao = cv2.getRotationMatrix2D(ponto, rotacao, zoom)
    result = cv2.warpAffine(imagem, img_rotacao, (largura, altura))

    # Converte imagem para escala de cinza
    if force_gray:
        result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    # Aplica um desfoque na imagem
    if desfoque:
        result = cv2.GaussianBlur(result, (35, 35), 0)

    folder = tempfile.mkdtemp()
    cv2.imwrite(os.path.join(folder, 'image.png'), result)
   
    f = open(os.path.join(folder, 'image.png'), 'rb')
    file = FileStorage(f, 'image.png', name='file', content_type='image/png')
    return file
