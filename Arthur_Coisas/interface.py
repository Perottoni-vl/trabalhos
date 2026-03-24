import customtkinter as ctk
from insert import cadastrar_aluno

# Configuração visual
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Escola - Cadastro")
        self.geometry("450x650") # Aumentei um pouco para caber tudo

        # Título
        self.label = ctk.CTkLabel(self, text="CADASTRO DE ALUNO", font=("Roboto", 24))
        self.label.pack(pady=20)

        # Campos de entrada
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome completo", width=300)
        self.entry_nome.pack(pady=10)

        self.entry_data = ctk.CTkEntry(self, placeholder_text="Data de Nascimento (DD/MM/AAAA)", width=300)
        self.entry_data.pack(pady=10)

        self.entry_cpf = ctk.CTkEntry(self, placeholder_text="CPF (Somente números)", width=300)
        self.entry_cpf.pack(pady=10)

        # Botão Salvar
        self.btn_salvar = ctk.CTkButton(self, text="SALVAR NO BANCO", command=self.salvar_dados)
        self.btn_salvar.pack(pady=20)

        # Botão Atualizar Lista
        self.btn_listar = ctk.CTkButton(self, text="ATUALIZAR LISTA", command=self.atualizar_lista, fg_color="green")
        self.btn_listar.pack(pady=10)

        # Caixa de rolagem (Scrollable Frame)
        self.lista_frame = ctk.CTkScrollableFrame(self, width=380, height=200, label_text="Lista de Alunos")
        self.lista_frame.pack(pady=20, padx=20)

    # --- AGORA AS FUNÇÕES ESTÃO FORA DO __INIT__ ---

    def atualizar_lista(self):
        # Limpar a lista antiga
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        # Chamar a função do seu arquivo select.py
        from select import listar_alunos
        dados = listar_alunos()

        # Criar as etiquetas para cada aluno
        for aluno in dados:
            texto_aluno = f"👤 {aluno[1]} | CPF: {aluno[3]}"
            label_item = ctk.CTkLabel(self.lista_frame, text=texto_aluno, anchor="w")
            label_item.pack(fill="x", padx=10, pady=5)

    def salvar_dados(self):
        nome = self.entry_nome.get()
        data = self.entry_data.get()
        cpf = self.entry_cpf.get()

        sucesso = cadastrar_aluno(nome, data, cpf)

        if sucesso:
            self.label.configure(text="ALUNO SALVO NO BANCO!", text_color="green")
            self.entry_nome.delete(0, 'end')
            self.entry_data.delete(0, 'end')
            self.entry_cpf.delete(0, 'end')
            # Opcional: atualiza a lista automaticamente após salvar
            self.atualizar_lista()
        else:
            self.label.configure(text="ERRO AO SALVAR!", text_color="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()