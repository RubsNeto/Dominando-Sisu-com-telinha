from os import read
from tkinter import *
from tkinter import messagebox


def Tela_resultados(Linguagens, Ciencia_natureza, Humanas, Matematica, Redacao, window):
    
    try:
        Nota_Linguagens       = float(Linguagens.get())
        Nota_Ciencia_natureza = float(Ciencia_natureza.get())
        Nota_Humanas          = float(Humanas.get())
        Nota_Matematica       = float(Matematica.get())
        Nota_Redacao          = float(Redacao.get())

    except:
        messagebox.showinfo('Alerta','Valores vazios ou inválidos!\nNão se esqueça de colocar ponto e não virgula.')

    peso_linguagens = [ 2, 2, 2, 2, 2, 2.5, 2.5, 3 ]
    peso_humanas = [ 1, 1, 1, 1.5, 1, 3, 2, 2.5 ]
    peso_natureza = [ 2.5, 1.5, 1, 3, 3, 1, 1, 1 ]
    peso_matematica = [ 3, 4, 4, 1.5, 2, 1, 2, 1 ]
    peso_redacao = [ 1.5, 1.5, 2, 2, 2, 2.5, 2.5, 2.5 ]


    nota_final = list()

    roda = 0
    while roda != len(peso_linguagens):
        validando_casas_decimanis = (Nota_Linguagens * float(peso_linguagens[roda]) +  Nota_Humanas * float(peso_humanas[roda])  +  Nota_Ciencia_natureza * float(peso_natureza[roda])  +  Nota_Matematica * float(peso_matematica[roda])  +  Nota_Redacao * float(peso_redacao[roda]))/10 
        nota_final.append(round(validando_casas_decimanis,1))
        roda+=1



    window.destroy()
    window = Tk()
    window.iconbitmap('icone/icone.ico')
    window.title('Dominando o SiSU')

    img = PhotoImage(file="Imagens_tela_resultados/Fundo_tela_resultado.png")

    window.geometry("729x618")
    window.configure(bg = "#ffffff")        
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 618,
        width = 730,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    imagem = canvas.create_image(364.45,310,
        image = img)

    #Segunda chamada
    Segunda_chamada_img = PhotoImage(file = f"Imagens_tela_resultados/img_textBox0.png")
    Segunda_chamada_bg = canvas.create_image(
        561.0, 384.5,
        image = Segunda_chamada_img)

    Segunda_chamada = Listbox(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        font = ('Roboto-Medium',13))

        

    Segunda_chamada.place(
        x = 435.0, y = 261,
        width = 252.0,
        height = 245)

    #Primeira chamada
    Primeira_chamada_img = PhotoImage(file = f"Imagens_tela_resultados/img_textBox1.png")
    Primeira_chamada_bg = canvas.create_image(
        173.0, 384.5,
        image = Primeira_chamada_img)

    Primeira_chamada = Listbox(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        font = ('Roboto-Medium',13))

    Primeira_chamada.place(
        x = 47.0, y = 261,
        width = 252.0,
        height = 245)

    for numero_grupo in range(1,9):

        with open(f"nota/G{numero_grupo}/G{numero_grupo}_media_chamada_regular.txt", mode="r", encoding="utf-8") as media_regular: # Primeira chamada
            for linha in media_regular:
                tira_traco = linha.split('-')
                media_nota_antiga = float(tira_traco[4].split('\n')[0])

                if nota_final[numero_grupo - 1] >= media_nota_antiga:
                    Primeira_chamada.insert(END," ")
                    Primeira_chamada.insert(END, f"Curso:      {tira_traco[0]}")
                    Primeira_chamada.insert(END, f"Turno:      {tira_traco[1]}")
                    Primeira_chamada.insert(END, f"Grau:       {tira_traco[2]}")
                    Primeira_chamada.insert(END, f"Cidade:     {tira_traco[3]}")
                    Primeira_chamada.insert(END, f"Nota média: {tira_traco[4]}")
                    Primeira_chamada.insert(END," ")



        with open(f"nota/G{numero_grupo}/G{numero_grupo}_media_segunda_chamada.txt", mode="r", encoding="utf-8") as media_regular: # Segunda Chamada
            for ver in media_regular:
                tira_traco = ver.split('-')
                media_nota_antiga = float(tira_traco[4].split('\n')[0])

                if nota_final[numero_grupo - 1] >= media_nota_antiga:
                    Segunda_chamada.insert(END," ")
                    Segunda_chamada.insert(END, f"Curso:      {tira_traco[0]}")
                    Segunda_chamada.insert(END, f"Turno:      {tira_traco[1]}")
                    Segunda_chamada.insert(END, f"Grau:       {tira_traco[2]}")
                    Segunda_chamada.insert(END, f"Cidade:     {tira_traco[3]}")
                    Segunda_chamada.insert(END, f"Nota média: {tira_traco[4]}")
                    Segunda_chamada.insert(END," ")



    canvas.create_text(
        173.0, 238.5,
        text = "Primeira chamada",
        fill = "#ffffff",
        font = ("Roboto-Medium", int(18.0)))

    canvas.create_text(
        561.0, 238.5,
        text = "Segunda chamada",
        fill = "#ffffff",
        font = ("Roboto-Medium", int(18.0)))

    #G1
    G1_img = PhotoImage(file = f"Imagens_tela_resultados/img_textBox6.png")
    G1_bg = canvas.create_image(
        57.5, 197.5,
        image = G1_img)

    G1 = Label(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        justify = 'center',
        text = nota_final[0],
        font = ("Roboto-Medium", int(12.0)))

    G1.place(
        x = 34.0, y = 182,
        width = 47.0,
        height = 29)

    #G2
    G2_img = PhotoImage(file = f"Imagens_tela_resultados/img_textBox7.png")
    G2_bg = canvas.create_image(
        145.5, 197.5,
        image = G2_img)

    G2 = Label(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        justify = 'center',
        text = nota_final[1],
        font = ("Roboto-Medium", int(12.0)))

    G2.place(
        x = 122.0, y = 182,
        width = 47.0,
        height = 29)

    #G3
    G3_img = PhotoImage(file = f"Imagens_tela_resultados/img_textBox8.png")
    G3_bg = canvas.create_image(
        234.0, 197.5,
        image = G3_img)

    G3 = Label(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        justify = 'center',
        text = nota_final[2],
        font = ("Roboto-Medium", int(12.0)))

    G3.place(
        x = 210.0, y = 182,
        width = 48.0,
        height = 29)

    #G4
    G4_img = PhotoImage(file = f"Imagens_tela_resultados/img_textBox9.png")
    G4_bg = canvas.create_image(
        323.0, 197.5,
        image = G4_img)

    G4 = Label(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        justify = 'center',
        text = nota_final[3],
        font = ("Roboto-Medium", int(12.0)))

    G4.place(
        x = 299.0, y = 182,
        width = 48.0,
        height = 29)

    #G5
    G5_img = PhotoImage(file = f"Imagens_tela_resultados/img_textBox2.png")
    G5_bg = canvas.create_image(
        410.5, 197.5,
        image = G5_img)

    G5 = Label(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        justify = 'center',
        text = nota_final[4],
        font = ("Roboto-Medium", int(12.0)))

    G5.place(
        x = 387.0, y = 182,
        width = 47.0,
        height = 29)

    # G6
    G6_img = PhotoImage(file = f"Imagens_tela_resultados/img_textBox3.png")
    G6_bg = canvas.create_image(
        498.5, 197.5,
        image = G6_img)

    G6 = Label(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        justify= 'center',
        text = nota_final[5],
        font = ("Roboto-Medium", int(12.0)))

    G6.place(
        x = 475.0, y = 182,
        width = 47.0,
        height = 29)

    #G7
    G7_img = PhotoImage(file = f"Imagens_tela_resultados/img_textBox4.png")
    G7_bg = canvas.create_image(
        587.0, 197.5,
        image = G7_img)

    G7 = Label(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        justify = 'center',
        text = nota_final[6],
        font = ("Roboto-Medium", int(12.0)))

    G7.place(
        x = 563.0, y = 182,
        width = 48.0,
        height = 29)

    #G8
    G8_img = PhotoImage(file = f"Imagens_tela_resultados/img_textBox5.png")
    G8_bg = canvas.create_image(
        676.0, 197.5,
        image = G8_img)

    G8 = Label(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        justify = 'center',
        text = nota_final[7],
        font = ("Roboto-Medium", int(12.0)))

    G8.place(
        x = 652.0, y = 182,
        width = 48.0,
        height = 29)

    canvas.create_text(
        57.5, 168.5,
        text = "G1",
        fill = "#ffffff",
        font = ("Roboto-Medium", int(15.0)))

    canvas.create_text(
        145.5, 168.5,
        text = "G2",
        fill = "#ffffff",
        font = ("Roboto-Medium", int(15.0)))

    canvas.create_text(
        233.5, 168.5,
        text = "G3",
        fill = "#ffffff",
        font = ("Roboto-Medium", int(15.0)))

    canvas.create_text(
        322.5, 168.5,
        text = "G4",
        fill = "#ffffff",
        font = ("Roboto-Medium", int(15.0)))

    canvas.create_text(
        410.5, 168.5,
        text = "G5",
        fill = "#ffffff",
        font = ("Roboto-Medium", int(15.0)))

    canvas.create_text(
        498.5, 168.5,
        text = "G6",
        fill = "#ffffff",
        font = ("Roboto-Medium", int(15.0)))

    canvas.create_text(
        586.5, 168.5,
        text = "G7",
        fill = "#ffffff",
        font = ("Roboto-Medium", int(15.0)))

    canvas.create_text(
        675.5, 168.5,
        text = "G8",
        fill = "#ffffff",
        font = ("Roboto-Medium", int(15.0)))

    window.resizable(False, False)
    window.mainloop()


def Tela_inicio():
        
    window = Tk()
    window.iconbitmap('icone/icone.ico')
    window.title('Dominando o SiSU')

    window.geometry("584x583")

    img = PhotoImage(file="Imagens_inicio/vdc.png")


    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 583,
        width = 584,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge",)
    canvas.place(x = 0, y = 0)

    imagem = canvas.create_image(292,292,
        image = img)

    canvas.create_text(
        275.5, 95.5,
        text = "Bem vindo ao dominando o SiSU\nDigite sua nota.",
        fill = "#ffffff",
        font = ("Rubik-Medium", int(20.0)))

    canvas.create_text(
        157.0, 175.5,
        text = "Linguagens",
        fill = "#ffffff",
        font = ("Rubik-Medium", int(19.0)))

    canvas.create_text(
        157.0, 273.0,
        text = "Humanas",
        fill = "#ffffff",
        font = ("Rubik-Medium", int(19.0)))

    Ciencia_natureza_img = PhotoImage(file = f"Imagens_inicio/img_textBox0.png")
    Ciencia_natureza_bg = canvas.create_image(
        423.0, 213.0,
        image = Ciencia_natureza_img)

    Ciencia_natureza = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        font = ("Rubik-Medium", int(13.0)),
        justify='center')

    Ciencia_natureza.place(
        x = 327.0, y = 191,
        width = 192.0,
        height = 42)

    Linguagens_img = PhotoImage(file = f"Imagens_inicio/img_textBox1.png")
    Linguagens_bg = canvas.create_image(
        156.0, 213.0,
        image = Linguagens_img)

    Linguagens = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        font = ("Rubik-Medium", int(13.0)),
        justify='center')

    Linguagens.place(
        x = 59.0, y = 191,
        width = 194.0,
        height = 42)

    canvas.create_text(
        421.0, 175.5,
        text = "Ciências da Natureza",
        fill = "#ffffff",
        font = ("Rubik-Medium", int(19.0)))

    Matematica_img = PhotoImage(file = f"Imagens_inicio/img_textBox2.png")
    Matematica_bg = canvas.create_image(
        423.0, 310.5,
        image = Matematica_img)

    Matematica = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        font = ("Rubik-Medium", int(13.0)),
        justify='center')

    Matematica.place(
        x = 326.5, y = 289,
        width = 193.0,
        height = 41)

    Humanas_img = PhotoImage(file = f"Imagens_inicio/img_textBox3.png")
    Humanas_bg = canvas.create_image(
        156.0, 310.5,
        image = Humanas_img)

    Humanas = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        font = ("Rubik-Medium", int(13.0)),
        justify='center')

    Humanas.place(
        x = 58.5, y = 289,
        width = 195.0,
        height = 41)

    Redacao_img = PhotoImage(file = f"Imagens_inicio/img_textBox4.png")
    Redacao_bg = canvas.create_image(
        156.0, 407.5,
        image = Redacao_img)

    Redacao = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        font = ("Rubik-Medium", int(13.0)),
        justify='center')

    Redacao.place(
        x = 58.5, y = 386,
        width = 195.0,
        height = 41)

    canvas.create_text(
        423.5, 273.0,
        text = "Matemática",
        fill = "#ffffff",
        font = ("Rubik-Medium", int(19.0)))

    canvas.create_text(
        157.0, 372.0,
        text = "Redação",
        fill = "#ffffff",
        font = ("Rubik-Medium", int(19.0)))

    img0 = PhotoImage(file = f"Imagens_inicio/img0.png")

    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: Tela_resultados(Linguagens, Ciencia_natureza, Humanas, Matematica, Redacao, window),
        relief = "flat")

    b0.place(
        x = 360, y = 380,
        width = 124,
        height = 49)


    window.resizable(False, False)

    window.mainloop()


Tela_inicio()
