import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from PIL import Image

# Rede Neural 
class ScanRedeNeural(nn.Module):

    # Inicialização
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(1, 1)

    # Computação dos dados
    def forward(self, img):
        return self.layers(img)



        
# Preparando os Dados 

def pre_processimg(cam):
    global redimen

    caminho = Image.open(cam)
    redimen = caminho.resize((224, 224))

def analisar():
    
    redimen

