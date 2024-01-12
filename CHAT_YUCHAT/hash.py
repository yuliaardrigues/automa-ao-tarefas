import flet as ft

def main(page):

    texto = ft.Text("YUchat")

    name_user = ft.TextField(label="Escreva seu nome: ")

    chat =ft.Column()

    def enviar_mensagem_tunel(informacoes):
      chat.controls.append(ft.Text(informacoes))  
      page.update()
    
        
    page.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        #colocar o nome do usuario na mensagem
        texto_campo_mensagem = f'{name_user.value}: {campo_mensagem.value}'
        page.pubsub.send_all(texto_campo_mensagem)
        #limpar campo de mensagem
        campo_mensagem.value = ""
        page.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem: ", on_submit=enviar_mensagem)    
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
  
    def entrar_chat(evento):
       #fechar popup
       popup.open = False
       #remover botao iniciar
       page.remove(botao_iniciar)
        #adicionar chat
       page.add(chat)
        #adicionar campo de mensagem
       linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
          )
       page.add(linha_mensagem)
       #botao de enviar mensagem
       texto = f'{name_user.value} entrou no chat'
       page.pubsub.send_all(texto)  
       #atualizar pagina
       page.update()
    
    popup = ft.AlertDialog(
       open=False, 
       modal=True, 
       title=ft.Text(" bem-vindo ao YUchat"),
       content=name_user,
       actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
       )

    def iniciar_chat(evento):
       #abrir popup
       page.dialog = popup   
       #atualizar pagina
       popup.open = True
       page.update()

    #botao iniciar
    botao_iniciar = ft.ElevatedButton("Iniciar", on_click=iniciar_chat)
    #adicionar elementos na pagina
    page.add(texto)
    page.add(botao_iniciar) 
    
 #executar aplicacao   
#ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)

