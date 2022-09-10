import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class Criptografia(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.resizable(False, False)
        self.title("Criptografia")
        self.montar_ui()


    def montar_ui(self) -> None:
        config = {
            "padx" : 10,
            "pady" : 5,
        }

        self.painel_opcoes = self._montar_frame_opcoes(config)
        self.painel_opcoes.grid(row=0, **config)
        self.painel_chave = self._montar_frame_chave(config)
        self.painel_chave.grid(row=1, **config)
        self.painel_entrada = self._montar_frame_entrada(config)
        self.painel_entrada.grid(row=2, **config)
        self.painel_saida = self._montar_frame_saida(config)
        self.painel_saida.grid(row=3, **config)

        self.criptografia.current(0)
        self.metodo.set(0)

    def _montar_frame_opcoes(self, config: dict) -> ttk.Frame:
        frame = ttk.LabelFrame(self, text="Criptografia")
        cript_selecionada = tk.StringVar()
        self.criptografia = ttk.Combobox(
            frame, textvariable=cript_selecionada, width=80)
        self.criptografia["values"] = [
            "Criptografia 1", "Criptografia 2", "Criptografia 3"]
        self.criptografia["state"] = "readonly"
        self.criptografia.pack(fill=tk.BOTH, expand=True, **config)

        return frame

    def _montar_frame_chave(self, config: dict) -> ttk.Frame:
        frame = ttk.LabelFrame(self, text="Chave Criptografia")
        self.chave = tk.StringVar()
        entrada_chave = ttk.Entry(
            frame, textvariable=self.chave, width=67).pack(
                side=tk.LEFT, **config)
        btn_gerar = ttk.Button(frame, text='Gerar').pack(
            side=tk.RIGHT, **config)

        return frame

    def _montar_frame_entrada(self, config: dict) -> ttk.Frame:
        frame = ttk.LabelFrame(self, text="Entrada")
        frame.columnconfigure(2, weight=3)
        self.metodo = tk.StringVar()
        rb_cripgrafar = ttk.Radiobutton(
            frame, text='Criptografar', value=0, variable=self.metodo).grid(
                row=0, column=0, sticky=tk.W, **config)
        rb_decripgrafar = ttk.Radiobutton(
            frame, text='Decriptografar', value=1, variable=self.metodo).grid(
                row=0, column=1, sticky=tk.W, **config)
        self.entrada = ScrolledText(frame, width=60, height=5).grid(
            row=1, column=0, columnspan=3, sticky=tk.EW, **config)
        btn_importar = ttk.Button(frame, text='Importar').grid(
            row=2, column=0, sticky=tk.W, **config)
        btn_criptografar = ttk.Button(frame, text='Criptografar').grid(
            row=2, column=2, sticky=tk.E, **config)

        return frame

    def _montar_frame_saida(self, config: dict) -> ttk.Frame:
        frame = ttk.LabelFrame(self, text="Saida")
        self.saida = ScrolledText(frame, width=60, height=5)
        self.saida.pack(fill=tk.BOTH, expand=True, padx= 10, pady=10)
        btn_exportar = ttk.Button(frame, text='Exportar').pack(
            side=tk.LEFT, **config)

        return frame


def main():
    c = Criptografia()
    c.mainloop()

if __name__ == "__main__":
    main()