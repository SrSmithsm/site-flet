# Tela inicial:
    # Título - smzap
    # Botão: Iniciar chat
    
        # Botão iniciar:
        # Quando clicado:
        # Abrir um popup/modal/alerta
        
            # Popup:
            # Título: Bem vindo ao smzap
            # Caixa de texto : Escreva seu nome no chat
            # Botão: Entrar no chat
            
                # Botão entrar:
                # Quando apertado:
                # Fechar o popup
                # Sumir com o título
                # Sumir com o botão iniciar chat
                
                    # Vai carregar o chat
                    # Carregar o campo de enviar mensagem: "Digite sua mensagem"
                    # Botão enviar mensagem
                    
                        # Botão enviar:
                        # Quando apertado -> Enviar a mensagem
                        # Limpar a caixa de mensagem

# Flet
import flet as ft

# Criar uma função principal para rodar o aplicativo

def main(pagina: ft.Page): # Criação da função principal
    
    # Titulo
    
    titulo_pagina = ft.Text("smzap") # Criando a variavel titulo e escrevendo o texto
    
    # Função conectar os usuarios
    
    def enviar_mensagem_tunel(mensagem):
        
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    # Area de mensagem
    
    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value # Pega o valor do caixa_nome
        texto_campo_mensagem = campo_enviar_mensagem.value # Pega o valor do campo_enviar_mensagem
        mensagem = (f"{nome_usuario}: {texto_campo_mensagem}")
        pagina.pubsub.send_all(mensagem)
        
        # Limpar a caixa de enviar mensagem
        
        campo_enviar_mensagem.value = ""
        
        pagina.update()
        
    campo_enviar_mensagem = ft.TextField(label="Digite sua Mensagem", 
                                         on_submit=enviar_mensagem) # Area apara digitar mensagem
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem) # Botão de enviar mensagem
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar]) # Posicionamento dos elementos
    
    chat = ft.Column() # Criação do chat
    
    # Função do chat
    
    def entrar_chat(evento):
        # Fechar o popup
        popup.open = False
        # Sumir com o título
        pagina.remove(titulo_pagina)
        # Sumir com o botão iniciar chat
        pagina.remove(botao)
        # Carregar o chat
        pagina.add(chat)
        # Carregar o campo de enviar mensagem e Carregar o botão de enviar
        pagina.add(linha_enviar)
        # Adicionar no chat a mensagem de entrada
        nome_usuario = caixa_nome.value
        mensagem = (f"{nome_usuario}: entrou no chat")
        pagina.pubsub.send_all(mensagem)
        
        pagina.update()
    # Criar o popup
    
    titulo_popup = ft.Text("Bem Vindo ao smzap")  # Texto que aparece para o usuario
    caixa_nome = ft.TextField(label="Digite seu Nick", on_submit=entrar_chat) # Campo onde o ususario preenche com texto
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)  # Botão de entrar no chat

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,  # Definindo o popup
                           actions=[botao_popup])
    
    # Botao iniciar
    def abrir_popup(evento): # Define oque vai acontecer quando um usuario apertar o botao
        pagina.overlay.append(popup) # Adicionando o popup na pagina
        popup.open = True # Fazendo o botão aparecer
        pagina.update() # Para a pagina atualizar
    
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)  # Criando a variavel botao e escrevendo o texto
   
# Colocar Elelemntos na pagina

    pagina.add(titulo_pagina) # Adicionando a variavel titulo para a pagina
    pagina.add(botao)         # Adicionando a variavel botao para a pagina

# Executar essa função com o flet

ft.app(main, view=ft.AppView.WEB_BROWSER)

