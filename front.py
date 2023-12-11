import tkinter as tk
from tkinter import messagebox
import pywhatkit
import keyboard
import time
from datetime import datetime

class MsgInterFace:
    def __init__(self, master):
        self.master = master
        master.title("ChatBot")

        self.master.geometry("350x290")

        self.contact_frame = tk.Frame(master)
        self.message_frame = tk.Frame(master)
        self.time_frame = tk.Frame(master)

        self.label_contact = tk.Label(self.contact_frame, text="Número do Contato:", font=("Arial", 12))
        self.entry_contact = tk.Entry(self.contact_frame)

        self.label_message = tk.Label(self.message_frame, text="Mensagem:", font=("Arial", 12))
        self.entry_message = tk.Entry(self.message_frame)

        self.label_time = tk.Label(self.time_frame, text="Horário (hh:mm):", font=("Arial", 12))
        self.entry_time = tk.Entry(self.time_frame)

        self.send_button = tk.Button(master, text="Enviar Mensagem", command=self.send_message)

        self.contact_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.message_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.time_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.send_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.label_contact.pack(side="left", padx=10, pady=10)
        self.entry_contact.pack(side="right", expand=True, fill="both", padx=10, pady=10)
        self.label_message.pack(side="left", padx=10, pady=10)
        self.entry_message.pack(side="right", expand=True, fill="both", padx=10, pady=10)
        self.label_time.pack(side="left", padx=10, pady=10)
        self.entry_time.pack(side="right", expand=True, fill="both", padx=10, pady=10)
     
    def send_message(self):
        contato = self.entry_contact.get()
        mensagem = self.entry_message.get()

        try:
            hora, minuto = self.entry_time.get().split(":")
            hora = int(hora)
            minuto = int(minuto)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira o horário no formato hh:mm.")
            return

        if not contato or not mensagem:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        mensagem = mensagem + "\nEsta mensagem é automatizada, ChatBot"

        try:
            pywhatkit.sendwhatmsg(contato, mensagem, hora, minuto)
            time.sleep(20)
            keyboard.press_and_release('ctrl + w')
            messagebox.showinfo("Sucesso", "Mensagem enviada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao enviar a mensagem: {str(e)}")
