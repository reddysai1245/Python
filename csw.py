from tkinter import * 
import csv

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.output()
    def exit(self):
        
        root.destroy()
        

    def output(self):
        Label(text='Name:').pack(side=LEFT,padx=5,pady=5)
        self.e = Entry(root, width=40)
        self.e.pack(side=LEFT,padx=5,pady=5)

        self.b = Button(root, text='Submit', command=self.writeToFile,bg="green",fg="white")
        self.b.pack(side=RIGHT,padx=5,pady=5)
        self.b = Button(root, text='Exit', command=self.exit,bg="red",fg="white")
        self.b.pack(side=RIGHT,padx=6,pady=9)

    def writeToFile(self):
        with open('WorkOrderLog.csv', 'a') as f:
            w=csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow([self.e.get()])
            self.e.delete(0,END)

if __name__ == "__main__":
    r
    root.title('Auto Logger')
    root.geometry('500x500')
    app=App(master=root)
    
    app.mainloop()
    root.mainloop()
