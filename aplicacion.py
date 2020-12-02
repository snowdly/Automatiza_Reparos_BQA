from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename

class App:
    def __init__(self, root):
        direccion = 'selecciona fichero asignaciones'
        #setting title
        root.title("Gestor reparos")
        #setting window size
        width=550
        height=650
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_808=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_808["font"] = ft
        GLabel_808["fg"] = "#333333"
        GLabel_808["justify"] = "center"
        GLabel_808["text"] = "GENERALES:"
        GLabel_808.place(x=40,y=10,width=110,height=25)

        GLabel_990=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_990["font"] = ft
        GLabel_990["fg"] = "#333333"
        GLabel_990["justify"] = "center"
        GLabel_990["text"] = "Excel AA:"
        GLabel_990.place(x=110,y=60,width=70,height=25)

        #cuadro direccion excell Asignaciones
        GLineEdit_142=tk.Entry(root)
        GLineEdit_142["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_142["font"] = ft
        GLineEdit_142["fg"] = "#333333"
        GLineEdit_142["justify"] = "center"
        GLineEdit_142["text"] = "Selecciona el fichero"
        GLineEdit_142.place(x=210,y=60,width=153,height=30)
        #boton seleecionar fichero
        GButton_454=tk.Button(root)
        GButton_454["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_454["font"] = ft
        GButton_454["fg"] = "#000000"
        GButton_454["justify"] = "center"
        GButton_454["text"] = "Button"
        GButton_454.place(x=390,y=60,width=70,height=25)
        GButton_454["command"] = self.GButton_454_command



        GLabel_414=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_414["font"] = ft
        GLabel_414["fg"] = "#333333"
        GLabel_414["justify"] = "center"
        GLabel_414["text"] = "Auditor:"
        GLabel_414.place(x=110,y=110,width=70,height=25)

        GLabel_751=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_751["font"] = ft
        GLabel_751["fg"] = "#333333"
        GLabel_751["justify"] = "center"
        GLabel_751["text"] = "Fecha:"
        GLabel_751.place(x=100,y=150,width=70,height=25)




        GListBox_703=tk.Listbox(root)
        GListBox_703["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_703["font"] = ft
        GListBox_703["fg"] = "#333333"
        GListBox_703["justify"] = "center"
        GListBox_703.place(x=210,y=110,width=80,height=25)
        GListBox_703["selectmode"] = "single"

        GLineEdit_773=tk.Entry(root)
        GLineEdit_773["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_773["font"] = ft
        GLineEdit_773["fg"] = "#333333"
        GLineEdit_773["justify"] = "center"
        GLineEdit_773["text"] = "calendario"
        GLineEdit_773.place(x=210,y=150,width=70,height=25)

        GLabel_463=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_463["font"] = ft
        GLabel_463["fg"] = "#333333"
        GLabel_463["justify"] = "center"
        GLabel_463["text"] = "ID AA:"
        GLabel_463.place(x=100,y=200,width=70,height=25)

        GListBox_406=tk.Listbox(root)
        GListBox_406["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_406["font"] = ft
        GListBox_406["fg"] = "#333333"
        GListBox_406["justify"] = "center"
        GListBox_406.place(x=210,y=200,width=80,height=26)

        #boton generar .docs
        GButton_974=tk.Button(root)
        GButton_974["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_974["font"] = ft
        GButton_974["fg"] = "#000000"
        GButton_974["justify"] = "center"
        GButton_974["text"] = "Generar .docs"
        GButton_974.place(x=310,y=290,width=90,height=30)
        GButton_974["command"] = self.GButton_974_command

        #boton añadir reparos
        GButton_853=tk.Button(root)
        GButton_853["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_853["font"] = ft
        GButton_853["fg"] = "#000000"
        GButton_853["justify"] = "center"
        GButton_853["text"] = "Add reparo"
        GButton_853.place(x=170,y=290,width=84,height=30)
        GButton_853["command"] = self.GButton_853_command


        #listado de reparos
        #calculo numero de reparos
        n = 0
        GLabel_357=tk.Label(root)
        GLabel_357["bg"] = "#edeaea"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_357["font"] = ft
        GLabel_357["fg"] = "#333333"
        GLabel_357["justify"] = "center"
        GLabel_357["text"] = str(n) + " Reparos asociados"
        GLabel_357.place(x=130,y=330,width=313,height=36)

        GLabel_654=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_654["font"] = ft
        GLabel_654["fg"] = "#333333"
        GLabel_654["justify"] = "center"
        GLabel_654["text"] = "REPAROS:"
        GLabel_654.place(x=50,y=250,width=110,height=25)


        GButton_49=tk.Button(root)
        GButton_49["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_49["font"] = ft
        GButton_49["fg"] = "#000000"
        GButton_49["justify"] = "center"
        GButton_49["text"] = "Exit"
        GButton_49.place(x=460,y=10,width=70,height=25)
        GButton_49["command"] = root.destroy

    #funcion buscar fichero
    def GButton_454_command(self):
        #tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        return filename


    def GButton_974_command(self):
        print("command")

    #funcion ventana añadir reparos
    def GButton_853_command(self):

        toplevel = Toplevel()
        # setting title
        toplevel.title("undefined")
        # setting window size
        width = 640
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        toplevel.geometry(alignstr)
        toplevel.resizable(width=False, height=False)

        GLabel_972 = tk.Label(toplevel)
        ft = tkFont.Font(family='Times', size=14)
        GLabel_972["font"] = ft
        GLabel_972["fg"] = "#333333"
        GLabel_972["justify"] = "center"
        GLabel_972["text"] = "AÑADIR REPARO:"
        GLabel_972.place(x=10, y=10, width=160, height=25)

        GLabel_968 = tk.Label(toplevel)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_968["font"] = ft
        GLabel_968["fg"] = "#333333"
        GLabel_968["justify"] = "center"
        GLabel_968["text"] = "Tipo Auditoria:"
        GLabel_968.place(x=100, y=50, width=87, height=30)

        GLineEdit_690 = tk.Entry(toplevel)
        GLineEdit_690["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_690["font"] = ft
        GLineEdit_690["fg"] = "#333333"
        GLineEdit_690["justify"] = "center"
        GLineEdit_690["text"] = "RTI"
        GLineEdit_690.place(x=260, y=50, width=244, height=30)

        GLabel_985 = tk.Label(toplevel)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_985["font"] = ft
        GLabel_985["fg"] = "#333333"
        GLabel_985["justify"] = "center"
        GLabel_985["text"] = "Desc Checklist:"
        GLabel_985.place(x=100, y=100, width=84, height=30)

        GLineEdit_901 = tk.Entry(toplevel)
        GLineEdit_901["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_901["font"] = ft
        GLineEdit_901["fg"] = "#333333"
        GLineEdit_901["justify"] = "center"
        GLineEdit_901["text"] = "a.1.1 - Inventariado Acceso Móvil GIROS"
        GLineEdit_901.place(x=260, y=100, width=246, height=30)

        GLabel_816 = tk.Label(toplevel)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_816["font"] = ft
        GLabel_816["fg"] = "#333333"
        GLabel_816["justify"] = "center"
        GLabel_816["text"] = "Desc Check (code reparo):"
        GLabel_816.place(x=90, y=150, width=166, height=30)

        GLineEdit_966 = tk.Entry(toplevel)
        GLineEdit_966["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_966["font"] = ft
        GLineEdit_966["fg"] = "#333333"
        GLineEdit_966["justify"] = "center"
        GLineEdit_966["text"] = "AIG1-Codificación y Creación de Emplazamientos según Normativa. "
        GLineEdit_966.place(x=260, y=150, width=254, height=30)

        GLabel_678 = tk.Label(toplevel)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_678["font"] = ft
        GLabel_678["fg"] = "#333333"
        GLabel_678["justify"] = "center"
        GLabel_678["text"] = "¿Bloquearse?"
        GLabel_678.place(x=50, y=200, width=166, height=30)

        GRadio_23 = tk.Radiobutton(toplevel)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_23["font"] = ft
        GRadio_23["fg"] = "#333333"
        GRadio_23["justify"] = "center"
        GRadio_23["text"] = "SI"
        GRadio_23.place(x=230, y=200, width=85, height=25)
        GRadio_23["command"] = self.GRadio_23_command

        GLabel_265 = tk.Label(toplevel)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_265["font"] = ft
        GLabel_265["fg"] = "#333333"
        GLabel_265["justify"] = "center"
        GLabel_265["text"] = "Tipo de bloqueo:"
        GLabel_265.place(x=80, y=250, width=126, height=30)

        GLineEdit_965 = tk.Entry(toplevel)
        GLineEdit_965["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_965["font"] = ft
        GLineEdit_965["fg"] = "#333333"
        GLineEdit_965["justify"] = "center"
        GLineEdit_965["text"] = "CAUSA ORANGE"
        GLineEdit_965.place(x=260, y=250, width=230, height=30)

        GLabel_46 = tk.Label(toplevel)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_46["font"] = ft
        GLabel_46["fg"] = "#333333"
        GLabel_46["justify"] = "center"
        GLabel_46["text"] = "Descripción del  reparo:"
        GLabel_46.place(x=90, y=300, width=136, height=30)

        GLineEdit_694 = tk.Entry(toplevel)
        GLineEdit_694["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_694["font"] = ft
        GLineEdit_694["fg"] = "#333333"
        GLineEdit_694["justify"] = "center"
        GLineEdit_694["text"] = "Texto descriptivo"
        GLineEdit_694.place(x=260, y=300, width=230, height=30)

        GLabel_174 = tk.Label(toplevel)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_174["font"] = ft
        GLabel_174["fg"] = "#333333"
        GLabel_174["justify"] = "center"
        GLabel_174["text"] = "Adjunto reparo :"
        GLabel_174.place(x=80, y=400, width=123, height=30)

        GLineEdit_573 = tk.Entry(toplevel)
        GLineEdit_573["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_573["font"] = ft
        GLineEdit_573["fg"] = "#333333"
        GLineEdit_573["justify"] = "center"
        GLineEdit_573["text"] = "nombre fichero"
        GLineEdit_573.place(x=260, y=400, width=201, height=30)

        GButton_413 = tk.Button(toplevel)
        GButton_413["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_413["font"] = ft
        GButton_413["fg"] = "#000000"
        GButton_413["justify"] = "center"
        GButton_413["text"] = "Guardar"
        GButton_413.place(x=530, y=400, width=56, height=30)
        GButton_413["command"] = self.GButton_413_command

        GButton_630 = tk.Button(toplevel)
        GButton_630["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_630["font"] = ft
        GButton_630["fg"] = "#000000"
        GButton_630["justify"] = "center"
        GButton_630["text"] = "Buscar"
        GButton_630.place(x=470, y=400, width=52, height=30)
        GButton_630["command"] = self.GButton_630_command

        GLabel_452 = tk.Label(toplevel)
        GLabel_452["bg"] = "#d2d1d1"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_452["font"] = ft
        GLabel_452["fg"] = "#333333"
        GLabel_452["justify"] = "center"
        GLabel_452["text"] = "0 ficheros adjuntos"
        GLabel_452.place(x=150, y=350, width=317, height=30)

        GLabel_412 = tk.Label(toplevel)
        GLabel_412["bg"] = "#d2d1d1"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_412["font"] = ft
        GLabel_412["fg"] = "#333333"
        GLabel_412["justify"] = "center"
        GLabel_412["text"] = "lista ficheros  cargados"
        GLabel_412.place(x=150, y=470, width=320, height=34)

        GButton_947=tk.Button(toplevel)
        GButton_947["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_947["font"] = ft
        GButton_947["fg"] = "#000000"
        GButton_947["justify"] = "center"
        GButton_947["text"] = "Volver atras"
        GButton_947.place(x=540,y=10,width=70,height=25)
        GButton_947["command"] = toplevel.destroy


    def GRadio_23_command(self):
        print("command")

    def GButton_413_command(self):
        print("command")

    def GButton_630_command(self):
        print("command")


    def GButton_49_command(self):
        print("command")




#llamar a la aplicacion
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
