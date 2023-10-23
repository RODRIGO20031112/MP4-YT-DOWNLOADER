from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
from threading import Thread

def baixar_video(url, caminho_destino='.'):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(caminho_destino)
        messagebox.showinfo("Sucesso", f"Vídeo baixado com sucesso para {caminho_destino}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

def baixar_com_interface_grafica():
    url = entry_url.get()
    caminho_destino = entry_caminho.get()
    
    if not url:
        messagebox.showwarning("Aviso", "Por favor, insira a URL do vídeo.")
        return
    
    download_thread = Thread(target=baixar_video, args=(url, caminho_destino))
    download_thread.start()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Baixar Vídeo do YouTube")

# Labels e Entry para a URL do vídeo
label_url = tk.Label(root, text="URL do Vídeo:")
label_url.pack()
entry_url = tk.Entry(root, width=50)
entry_url.pack()

# Labels e Entry para o caminho de destino
label_caminho = tk.Label(root, text="Caminho de Destino:")
label_caminho.pack()
entry_caminho = tk.Entry(root, width=50)
entry_caminho.pack()

# Botão para iniciar o download
botao_download = tk.Button(root, text="Baixar Vídeo", command=baixar_com_interface_grafica)
botao_download.pack()

root.mainloop()
