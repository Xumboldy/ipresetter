#This script will connect to provided IP address to run a network reset on user's machine
import tkinter
from pypsexec.client import Client

class IPResetter:
#Defining a basic UI with a prompt, an input box, and output
    def __init__(self):
        # Framing
        self.root = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.root)
        self.bottom_frame = tkinter.Frame(self.root)
        # Labeling
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter assigned IPv4 address:')
        self.entry = tkinter.Entry(self.top_frame, width=25)
        # Packing
        self.prompt_label.pack(side='left')
        self.entry.pack(side='left')
        # Widgeting
        self.init_button = tkinter.Button(self.bottom_frame, text='Start', command=self.initiate)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.root.destroy)
        # PackingV2
        self.init_button.pack(side='left')
        self.quit_button.pack(side='left')
        # PackingV3
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
#Defining a function to run psexec command to return necessary data on assigned IPv4, subnet & DNS
    def initiate(self):
        ip_v4 = self.entry.get()
        c = Client(ip_v4)
        c.connect()
        try:
                c.create_service()
                stdout, stderr, rc=c.run_executable("cmd.exe", arguments="ipconfig /all > %temp%\ipresetter.txt")
        finally:
                c.remove_service()
                c.disconnect()

gui = IPResetter()
