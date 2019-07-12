from tkinter import Label, Toplevel, messagebox, Tk, Entry, mainloop
from textblob import TextBlob

# Main function in program
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def callback():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        main.destroy()

def runAnalysis():  
    text = line.get()
    senti = TextBlob(text)
    print(text,senti.polarity)
    res = senti.polarity
    ploarityLabel.configure(text = "\nSentiment Polarity Score (-1 to +1) : " + '%.2f' % res + "  \n", font=("Helvetica", 15))
    if res < -0.2:
        polarityResult.configure(text = "Negative  \n",  fg = "red", font=("Helvetica", 15) )
    elif res > 0.2:
        polarityResult.configure(text = "Positive  \n", fg = "green", font=("Helvetica", 15))
    else:
        polarityResult.configure( text = "Neutral  \n", font=("Helvetica", 15))    

def runByEnter(event):
    typedText.configure(text = line.get())
    runAnalysis()

# Create main window
main = Tk()
main.title("Sentiment Analysis")
main.geometry("500x300")
main.protocol("WM_DELETE_WINDOW", callback)
main.focus()
center(main)

# addition item on window
label1 = Label(text = "Text input :", font=("Helvetica", 15))
label1.pack()


line = Entry(main, width=70)
line.focus()
line.bind("<Return>",runByEnter)
line.pack()

# labels
textLabel = Label(text = "\nEntered text is :", font=("Helvetica", 15))
textLabel.pack()
typedText = Label(text = "", fg = "blue", font=("Helvetica", 20))
typedText.pack()
ploarityLabel = Label(text = "" )
ploarityLabel.pack()
polarityResult = Label(text=" ")
polarityResult.pack()

# Run program
mainloop()