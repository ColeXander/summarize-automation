import nltk
import tkinter
import openai
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

def download_nltk_resources():
    nltk.download('punkt')

def summarize_text(text, num_sentences=3):
    # Initialize parser and tokenizer
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Initialize TextRank summarizer
    summarizer = TextRankSummarizer()

    # Summarize the text
    summary = summarizer(parser.document, num_sentences)

    # Build the summary text
    summary_text = ""
    for sentence in summary:
        summary_text += str(sentence) + " "

    return summary_text.strip()

# Check if the 'punkt' resource is downloaded, and download it if needed
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    download_nltk_resources()

def freeVersion():
    # Create the window
    window = tkinter.Tk()
    window.title('Summarizer Basic')
    tkinter.Label(window, text='Input File Name').grid(row=0)
    tkinter.Label(window, text='Output File Name').grid(row=1)
    inputFileName = tkinter.Entry(window)
    outputFileName = tkinter.Entry(window)
    inputFileName.grid(row=0, column=1)
    outputFileName.grid(row=1, column=1)
    
    def summarize_file():
        input_file = open(inputFileName.get(), "r")
        input_list = input_file.readlines()
        input_file.close()
        
        input_text = ' '.join(input_list)
        
        summary = summarize_text(input_text, num_sentences=3)
        
        output_file = open(outputFileName.get(), "w")
        output_file.write(summary)
        output_file.close()
        
    summarize = tkinter.Button(window, text='Summarize!', width=25, command=summarize_file).grid(row=2)
    window.mainloop()

def paidVersion():
    window = tkinter.Tk()
    window.title('Summarizer Pro')
    tkinter.Label(window, text='ChatGPT API Key').grid(row=0)
    tkinter.Label(window, text='Input File Name').grid(row=1)
    tkinter.Label(window, text='Output File Name').grid(row=2)
    chatgptApiKey = tkinter.Entry(window)
    inputFileName = tkinter.Entry(window)
    outputFileName = tkinter.Entry(window)
    chatgptApiKey.grid(row=0, column=1)
    inputFileName.grid(row=1, column=1)
    outputFileName.grid(row=2, column=1)

    def summarize_file():
        openai.api_key = chatgptApiKey.get()

        input_file = open(inputFileName.get(), "r")
        input_list = input_file.readlines()
        input_file.close()

        input_text = ' '.join(input_list)
        
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=input_text,
            max_tokens=100,
            temperature=0.3,
            top_p=1.0,
            n=1,
            stop=None,
            temperature_decay=0.0
        )

        output_file = open(outputFileName.get(), "w")
        output_file.write(response.choices[0].text.strip())
        output_file.close()
        
    summarize = tkinter.Button(window, text='Summarize!', width=25, command=summarize_file).grid(row=2)
    window.mainloop()

def aboutVersion():
    window = tkinter.Tk()
    window.title('Summarizer Automation About - Cole Bohrer')

    tkinter.Label(window, text='Summarizer Automation').grid(row=0)
    tkinter.Label(window, text='This program was created by Cole Bohrer').grid(row=1)
    tkinter.Label(window, text='This was made to summarize text from one file to another!').grid(row=2)
    tkinter.Label(window, text="There really isn't anything else here.")

def selectVersion():
    window = tkinter.Tk()
    window.title('Summarizer Automation - Cole Bohrer')

    def free():
        window.destroy()
        freeVersion()
    def paid():
        window.destory()
        paidVersion()
    def about():
        window.destory()
        aboutVersion()
    
    freeButton = tkinter.Button(window, text='Summarizer Basic', width=30, command=free).grid(row=0)
    paidButton = tkinter.Button(window, text='Summarizer Pro (Requires ChatGPT API)', width=30, command=paid).grid(row=1)
    aboutButton = tkinter.Button(window, text='About Summarizer', width=30, command=about).grid(row=2)
    window.mainloop()

selectVersion()