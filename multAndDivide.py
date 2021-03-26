from tkinter import*
import translator
import dictionary

def count(sign):
    if sign == '+':
        return 'sum'
    elif sign == '-':
        return 'min'
    elif sign =='*':
        return 'mult'
    elif sign == '/':
        return 'div'
    else:
        return "Выберите операцию!"

class Application(Frame):
    def __init__(self, master):
        self.dictionary = None
        self.translator = None
        self.choose = StringVar()
        self.choose.set(None)
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.lbl1 = Label(self,
                          text = "Первое число",
                          font = "Times 30",
                          fg='linen',
                          bg='lightsteelblue',
                          width=23)
        self.lbl1.grid(row = 0,
                       column = 0,
                       columnspan = 2,
                       sticky = N)
        self.lbl2 = Label(self,
                          text = "Второе число",
                          font = "Times 30",
                          fg='deep sky blue',
                          bg='honeydew',
                          width=22)
        self.lbl2.grid(row = 0,
                       column = 3,
                       columnspan = 2,
                       sticky = N)
        self.ent1 = Entry(self,
                          fg='teal',
                          justify='center',
                          width=36,
                          font="Times 21")
        self.ent1.grid(row = 1,
                       column = 0,
                       columnspan = 2,
                       sticky = N)
        self.ent2 = Entry(self,
                          fg='teal',
                          justify='center',
                          width=35,
                          font="Times 21")
        self.ent2.grid(row = 1,
                       column = 3,
                       columnspan = 2,
                       sticky = N)
        self.lbl3 = Label(self,
                          text = "Система счисления",
                          font = "Times 30",
                          fg = 'slateblue',
                          bg = 'springgreen',
                          width=45)
        self.lbl3.grid(row = 3,
                       column = 1,
                       columnspan = 3,
                       sticky = N)
        self.ent3 = Entry(self,
                          fg='teal',
                          justify='center',
                          width=71,
                          font="Times 21")
        self.ent3.grid(row = 4,
                       column = 1,
                       columnspan = 3,
                       sticky = N)
        Radiobutton(self,
                    text="Сложение",
                    variable = self.choose,
                    value="+",
                    width=63,
                    fg='royalblue',
                    font="Times 21",
                    bg='red').grid(row=5,column=0,columnspan=4,sticky=N)
        Radiobutton(self,
                    text="Вычитание",
                    variable = self.choose,
                    value="-",
                    width=63,
                    fg='royalblue',
                    font="Times 21",
                    bg='red').grid(row=6,column=0,columnspan=4,sticky=N)
        Radiobutton(self,
                    text="Умножение",
                    variable = self.choose,
                    value="*",
                    width=63,
                    fg='royalblue',
                    font="Times 21",
                    bg='red').grid(row=7,column=0,columnspan=4,sticky=N)
        Radiobutton(self,
                    text="Деление",
                    value="/",
                    variable = self.choose,
                    width=63,
                    fg='royalblue',
                    font="Times 21",
                    bg='red').grid(row=8,column=0,columnspan=4,sticky=N)
        self.bttn = Button(self,
                           text = "Посчитать",
                           font = "Times 30",
                           fg='turquoise',
                           bg='royalblue',
                           command = self.calculate,
                           width = 22)
        self.bttn.grid(row = 9,
                       column = 0,
                       columnspan = 2,
                       sticky = S+N)
        self.txt=Text(self,
                      width=23,
                      height=1,
                      wrap=WORD,
                      font = "Times 30",
                      fg='turquoise')
        self.txt.grid(row=9,
                      column=2,
                      columnspan=3,
                      sticky=W)
    def calculate(self):
        if self.ent1.get() and self.ent2.get() and self.ent3.get():
            first = str(self.ent1.get())
            second = str(self.ent2.get())
            count_system = int(self.ent3.get())
            #creating the dictionary for translating
            self.dictionary = dictionary.Dictionary("base.csv","r",",")
            #creating the translator
            self.translator = translator.Translator(self.dictionary.get_dictionary(count_system), first)
            if self.translator.get_collection() == None:
                self.txt.delete(0.0, END)
                self.txt.insert(0.0, "Перепроверьте введенные данные!")
            else:
                self.translator = translator.Translator(self.dictionary.get_dictionary(count_system), second)
                if self.translator.get_collection() == None:
                    self.txt.delete(0.0, END)
                    self.txt.insert(0.0, "Перепроверьте введенные данные!")
                else:
                    self.txt.delete(0.0, END)
                    self.txt.insert(0.0, count(self.choose.get()))
        else:
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, "Не все поля заполнены!")
            
root = Tk()
root.title("CALCULATOR")
root.configure(bg='skyblue')
root.geometry("1000x500")
root.resizable(False, False)
root.grab_set()
app = Application(root)
root.mainloop()
