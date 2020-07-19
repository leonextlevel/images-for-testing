import os
import cv2
import numpy as np
from werkzeug.datastructures import FileStorage
import tempfile

def img_rotated(path_img):
    imagem = cv2.imread(path_img)
    altura, largura = imagem.shape[:2]
    ponto = (largura / 2, altura / 2)
    rotacao = cv2.getRotationMatrix2D(ponto, 90, 1)
    rotacionado = cv2.warpAffine(imagem, rotacao, (largura, altura))
    folder = tempfile.mkdtemp()
    cv2.imwrite(os.path.join(folder, 'image.png'), rotacionado)
    f = open(os.path.join(folder, 'image.png'), 'rb')
    file = FileStorage(f, 'image.png', name='file', content_type='image/png')
    return file
