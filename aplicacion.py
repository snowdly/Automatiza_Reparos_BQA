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

    def GButton_454_command(self):
        #tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        return filename


    def GButton_974_command(self):
        print("command")


    def GButton_853_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
