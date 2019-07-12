from tkinter import Label, Toplevel, messagebox, Tk, Entry, mainloop
import tweepy
from textblob import TextBlob

consumer_key= 'sPzRTNRkRevUEy6ZxcK9XfGst'
consumer_secret= 'hxjEj0cDcGRO1S64i1wIhqNnfPMt8jNI3MEIDwuiRRBc1oLGxv'
access_token='837725409219231744-7OJwVlCq8JEXqai8dwIyP0qx1WZOVnT'
access_token_secret='0KR1K0Mmc8hUcPymbN1R2O5yOTGg8cSgYB7jGX5euWqdG'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

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

def runAnalysis(count):  
    num = count # no of tweets
    senti = 0.0
    text = ""
    text = line.get() # input tag
    tweets = tweepy.Cursor(api.search, q=text, lang = "en").items(num) # get tweets
    for tweet in tweets:
        analysis = TextBlob(tweet.text) # analyse tweets
        res = analysis.sentiment.polarity
        senti += res
        text += tweet.text[0:30] +"..." + "  || Polarity: " + '%.2f' % res + "\n"
    # calculate average polarity and show the result
    res = senti / num
    tweetLabel.configure(text = text, font=("Helvetica", 15))
    headLabel.configure(text = "Tweets with individual polarity")
    polarityLabel.configure(text = "\nOverall Sentiment Polarity Score (-1 to +1) : " + '%.2f' % res + "  \n", font=("Helvetica", 15))
    if res < -0.2:
        polarityResult.configure(text = "Negative  \n",  fg = "red", font=("Helvetica", 15) )
    elif res > 0.2:
        polarityResult.configure(text = "Positive  \n", fg = "green", font=("Helvetica", 15))
    else:
        polarityResult.configure( text = "Neutral  \n", font=("Helvetica", 15))    

def runByEnter(event):
    # clear labels
    tweetLabel.configure(text = "")
    headLabel.configure(text = "")
    polarityLabel.configure(text = "")
    polarityResult.configure(text = "")
    textLabel.configure(text = "")

    # get number of tweets
    count = num.get()
    try:
        # only positive integers are allowed
        number = int(count)
        if number <= 0:
            number = 5
            messagebox.showwarning("Invalid Input", "Only positive numbers are allowed. Default value used")
    except:
        number = 5
    # try to analyse the input text
    try:
        textLabel.configure(text = "\nEntered keyword is :")
        typedText.configure(text = line.get())
        runAnalysis(number)
    except:
        messagebox.showwarning("Warning", "Either you have entered an invalid keyword or you are not connected to the internet")

# Create main window
main = Tk()
main.title("\nTwitter Sentiment Analysis\n\n")
main.geometry("600x900")
main.protocol("WM_DELETE_WINDOW", callback)
main.focus()
center(main)

# addition item on window
titleLabel = Label(text = "\nTwitter Sentiment Analysis\n", fg = "green", font = ("Helvetica", 30))
titleLabel.pack()
label1 = Label(text = "Enter keyword/tag to search about (hit ENTER for analysis):", font=("Helvetica", 15))
label1.pack()

# input field
line = Entry(main, width=70)
line.focus()
line.bind("<Return>",runByEnter)
line.pack()
label2 = Label(text = "Number of tweets to search( Default:5) :", font=("Helvetica", 15))
label2.pack()
num = Entry(main, width= 10)
num.pack()

# Labels
textLabel = Label(text = "", font=("Helvetica", 15))
textLabel.pack()
typedText = Label(text = "", fg = "blue", font=("Helvetica", 20))
typedText.pack()
polarityLabel = Label(text = "" )
polarityLabel.pack()
polarityResult = Label(text=" ")
polarityResult.pack()
headLabel = Label(text = "", fg = "blue", font=("Helvetica", 20))
headLabel.pack()
tweetLabel = Label(text = "" )
tweetLabel.pack()
# Run program
mainloop()