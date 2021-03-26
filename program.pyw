from tkinter import*
import translator
import dictionary
from PIL import Image, ImageTk

class Application(Frame):
    def __init__(self, master):
        self.dictionary = None
        self.translator = None
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.lbl1 = Label(self,
                          text = "Исходная система счисления",
                          font = "Times 30",
                          fg='linen',
                          bg='lightsteelblue')
        self.lbl1.grid(row = 0,
                       column = 0,
                       columnspan = 2,
                       sticky = N)
        self.lbl2 = Label(self,
                          text = "Новая система счисления",
                          font = "Times 30",
                          fg='deep sky blue',
                          bg='honeydew',
                          width=22)
        self.lbl2.grid(row = 2,
                       column = 0,
                       columnspan = 2,
                       sticky = N)
        self.ent1 = Entry(self,
                          fg='teal',
                          justify='center',
                          width=35,
                          font="Times 21")
        self.ent1.grid(row = 1,
                       column = 0,
                       columnspan = 2,
                       sticky = S+N)
        self.ent2 = Entry(self,
                          fg='teal',
                          justify='center',
                          width=35,
                          font="Times 21")
        self.ent2.grid(row = 3,
                       column = 0,
                       columnspan = 2,
                       sticky = S+N)
        self.lbl3 = Label(self,
                          text = "Число для перевода",
                          font = "Times 30",
                          fg = 'slateblue',
                          bg = 'springgreen',
                          width=22)
        self.lbl3.grid(row = 4,
                       column = 0,
                       columnspan = 2,
                       sticky = S+N)
        self.ent3 = Entry(self,
                          fg='teal',
                          justify='center',
                          width=35,
                          font="Times 21")
        self.ent3.grid(row = 5,
                       column = 0,
                       columnspan = 2,
                       sticky = S+N)
        self.bttn = Button(self,
                           text = "Посчитать",
                           font = "Times 30",
                           fg='turquoise',
                           bg='royalblue',
                           command = self.calculate,
                           width = 22)
        self.bttn.grid(row = 6,
                       column = 0,
                       columnspan = 2,
                       sticky = S+N)
        self.txt = Text(self,
                        width = 35,
                        height = 3,
                        wrap = CHAR,
                        font="Times 21")
        self.txt.grid(row = 7,
                      column = 0,
                      columnspan = 2,
                      sticky = N+S)
    def calculate(self):
        if self.ent1.get() and self.ent2.get() and self.ent3.get():
            input_str = str(self.ent3.get())
            from_ = int(self.ent1.get())
            to_ = int(self.ent2.get())
            input_str = input_str.upper()
            #creating the dictionary for translating
            self.dictionary = dictionary.Dictionary("base.csv","r",",")
            #creating the translator
            self.translator = translator.Translator(self.dictionary.get_dictionary(from_), input_str)
            if self.translator.get_collection() == None:
                self.txt.delete(0.0, END)
                self.txt.insert(0.0, "Перепроверьте введенные данные!")
            else:
                self.txt.delete(0.0, END)
                self.txt.insert(0.0, str(self.translator.translate_from_to(from_, to_, self.translator.get_collection())))
        else:
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, "Не все поля заполнены!")
            
root = Tk()
root.title("BETWEEN SYSTEMS")
root.configure(bg='skyblue')
root.geometry("500x500")
root.resizable(False, False)
root.grab_set()
app = Application(root)
root.mainloop()
