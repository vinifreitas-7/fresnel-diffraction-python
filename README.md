# Difração de Fresnel

Simulação da difração de Fresnel a partir de uma imagem de uma abertura.

## Requisitos

* Python 3
* NumPy
* OpenCV
* Matplotlib

Instale as bibliotecas com:

```bash
pip install numpy opencv-python matplotlib
```

## Como usar

Execute o programa:

```bash
python main.py
```

Informe:

1. Nome da imagem
2. Comprimento de onda em metros
3. Tamanho físico da imagem em metros
4. Distância de propagação em metros

Exemplo:

```text
Imagem: fenda.png
Comprimento de onda (m): 633e-9
Tamanho físico da imagem (m): 0.002
Distância de propagação (m): 0.005
```

O programa mostra a abertura e o padrão de difração de Fresnel.

## Observação

Na imagem de entrada:

* **Preto** = bloqueio
* **Branco** = abertura
