import numpy as np
import cv2
import matplotlib.pyplot as plt

# ========================================
# Imagem
# ========================================
imagem = input("Imagem: ")
matriz = cv2.imread(imagem, cv2.IMREAD_GRAYSCALE)

# Preto = bloqueio
# Branco = abertura
A = matriz.astype(np.float64) / 255.0

# ========================================
# Parametros Fisicos
# ========================================

# Recebe os parametros fisicos do usuario
lambda_ = float(input("Comprimento de onda (m): "))
L = float(input("Tamanho físico da imagem (m): "))
d = float(input("Distância de propagação (m): "))

#Faz diretamente por codigo
# lambda_ = 633e-9
# L = 0.002
# d = 0.005

# ========================================
# Tamanho da imagem
# ========================================
ny, nx = A.shape

dx = L / nx
dy = L / ny

# ========================================
# Frequencias espaciais
# ========================================
fx = np.fft.fftfreq(nx, d=dx)
fy = np.fft.fftfreq(ny, d=dy)

FX, FY = np.meshgrid(fx, fy)

# ========================================
# Numero de Onda
# ========================================
k = 2 * np.pi / lambda_

# ========================================
# Propagador de Fresnel
# ========================================
propagator = np.exp(
    1j * k * d
) * np.exp(
    -1j * np.pi * lambda_ * d * (FX**2 + FY**2)
)

# ========================================
# Campo no dominio das frequencias
# ========================================
U = np.fft.fft2(A)

U_propagado = U * propagator

# ========================================
# IFFT 
# ========================================
campo = np.fft.ifft2(U_propagado)

# ========================================
# Intensidade 
# ========================================
I = np.abs(campo)**2
I = I / I.max()
I_log = np.log1p(1000 * I)  # Escala logaritmica para ver melhor

# ========================================
#  Vizualizacao
# ========================================
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(A, cmap='gray')
plt.title('Abertura')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(I_log, cmap='plasma')
plt.title(f'Difração de Fresnel - d = {d} m')
plt.axis('off')

plt.tight_layout()
plt.show()