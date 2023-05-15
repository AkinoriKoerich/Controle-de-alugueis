import cv2
import tkinter as tk
from tkinter import filedialog
from deepface import DeepFace

# Cria a janela de seleção de arquivos
root = tk.Tk()
root.withdraw()

# Abre a janela de seleção de arquivos e espera o usuário selecionar uma imagem
file_path = filedialog.askopenfilename()

# Lê a imagem selecionada
imagem = cv2.imread(file_path)

# Executa a análise de emoções e idade na imagem
resultado = DeepFace.analyze(imagem, actions=("emotion", "age", "gender", "race"))

# Exibe o resultado da análise
print(resultado)