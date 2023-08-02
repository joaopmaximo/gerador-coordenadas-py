import requests
from tkinter import *

def obter_coordenadas():
    coordenadas = []
    saida_coordenadas.delete(1.0, END)
    enderecos = saida_enderecos.get(1.0, END).splitlines()

    for endereco in enderecos:
        url = f"https://geocode.maps.co/search?q={endereco}"
        response = requests.get(url)
        data = response.json()

        if data:
            latitude = data[0]["lat"]
            longitude = data[0]["lon"]
        else:
            latitude = "erro"
            longitude = "erro"

        coordenadas.append((latitude, longitude, endereco))

    with open("coordenadas.txt", "w") as arquivo:
        for latitude, longitude, endereco in coordenadas:
            if (latitude == "erro" or longitude == "erro"):
                saida_coordenadas.insert(END, f"não foi possível obter as coordenadas para o endereço: {endereco}\n")
            else:
                saida_coordenadas.insert(END, f"{latitude} {longitude}\n")
                arquivo.write(f"{latitude} {longitude}\n")
            
janela = Tk()
janela.title("Coordenadas")
janela.geometry("1150x650")

frame = Frame(janela, pady=20)
frame.pack()

titulo = Label(frame, text="Gerador de Coordenadas")
titulo.grid(column=0, row=0)

frame_saidas = Frame(frame)
frame_saidas.grid(column=0, row=1, pady=20)

label_enderecos = Label(frame_saidas, text="Insira os endereços aqui:")
label_enderecos.grid(column=0, row=0, sticky="w")
saida_enderecos = Text(frame_saidas, width = 65, height=30)
saida_enderecos.grid(column=0, row=1)

label_coordenadas = Label(frame_saidas, text="Coordenadas:")
label_coordenadas.grid(column=1, row=0, sticky="w", padx=20)
saida_coordenadas = Text(frame_saidas, width = 65, height=30)
saida_coordenadas.grid(column=1, row=1, padx=20)

botao = Button(frame, text="gerar coordenadas", command=obter_coordenadas)
botao.grid(column=0, row=2, sticky="w")

janela.mainloop()