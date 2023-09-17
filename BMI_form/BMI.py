#!/usr/bin/python3
import tkinter as tk


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(background="pink", height=500, pady=50, width=200)
        toplevel1.geometry("500x500")
        toplevel1.maxsize(500, 500)
        toplevel1.minsize(500, 500)
        toplevel1.resizable(False, False)
        label1 = tk.Label(toplevel1)
        label1.configure(
            background="pink",
            cursor="arrow",
            font="{Calibri} 24 {bold}",
            foreground="hot pink",
            text='Your BMI')
        label1.pack(fill="both", padx=20, pady=10, side="top")
        entry2 = tk.Entry(toplevel1)
        entry2.configure(background="white", highlightbackground="hot pink")
        entry2.place(anchor="nw", height=30, width=260, x=150, y=100)
        label2 = tk.Label(toplevel1)
        label2.configure(
            background="pink",
            font="{Calibri} 16 {bold}",
            foreground="hot pink",
            text='Height')
        label2.place(anchor="nw", height=30, relx=0.0, rely=0.0, x=50, y=100)
        label3 = tk.Label(toplevel1)
        label3.configure(
            background="pink",
            font="{Calibri} 16 {bold}",
            foreground="hot pink",
            text='Weight')
        label3.place(anchor="nw", height=30, relx=0.0, rely=0.0, x=50, y=170)
        entry3 = tk.Entry(toplevel1)
        entry3.configure(background="white", highlightbackground="hot pink")
        entry3.place(
            anchor="nw",
            height=30,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=260,
            x=150,
            y=170)
        label4 = tk.Label(toplevel1)
        label4.configure(
            background="pink",
            font="{Calibri} 16 {bold}",
            foreground="hot pink",
            text='BMI')
        label4.place(anchor="nw", height=30, relx=0.0, rely=0.0, x=50, y=240)
        entry4 = tk.Entry(toplevel1)
        entry4.configure(background="white", highlightbackground="hot pink")
        entry4.place(anchor="nw", height=30, width=260, x=150, y=240)
        button1 = tk.Button(toplevel1)
        button1.configure(
            font="{Calibri} 14 {bold}",
            foreground="hot pink",
            highlightbackground="white",
            text='Get result')
        button1.place(anchor="nw", height=30, x=200, y=310)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = NewprojectApp()
    app.run()
