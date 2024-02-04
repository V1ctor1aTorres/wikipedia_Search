from tkinter import *
#Criar uma interface gráfica (importa todos os elementos)
import wikipedia as w
#Buscar e imprimir algo da da Wikipedia

#Define o idioma da pesquisa, para que as consultas sejam feitas na Wikipedia em português
w.set_lang("pt")
#Será executada quando o botão de pesquisa for pressionado.
def on_press():
    #Obtém o texto inserido no Entry
    consulta=get_q.get()
    #Insere o resumo da Wikipedia correspondente à consulta na posição atual do widget de texto
    text.insert(INSERT,w.summary(consulta))


#Cria a janela principal da interface gráfica
base = Tk()
# Define o título da janela
base.title('App de Pesquisa')
#Cria uma etiqueta (Label) com o texto 'Pergunta'
question = Label(base, text='Pergunta')
#Coloca a etiqueta na janela
question.pack()
#Cria um widget de entrada (Entry) para permitir que o usuário insira a pergunta
get_q= Entry(base, bd=5)
#Coloca o widget de entrada na janela
get_q.pack()
#Cria um botão com o texto 'Pesquisar' e associa a função on_press a ser executada quando o botão for pressionado
submit= Button(base, text='Pesquisar',command=on_press)
#Coloca o botão na janela
submit.pack()
#Cria um widget de texto (Text) para exibir o resumo da Wikipedia
text=Text(base)
#Coloca o widget de texto na janela
text.pack()

#Inicia o loop principal da interface gráfica, aguardando a interação do usuário
base.mainloop()
