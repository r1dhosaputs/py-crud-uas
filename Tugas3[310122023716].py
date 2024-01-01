import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox, scrolledtext
from time import sleep


# ToolTip Class
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        "Display text in a tooltip window"
        if self.tip_window or not tip_text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")  # get size of widget
        x = x + self.widget.winfo_rootx() + 25  # calculate to display tooltip
        y = y + cy + self.widget.winfo_rooty() + 25  # below and to the right
        self.tip_window = tw = tk.Toplevel(self.widget)  # create new tooltip window
        tw.wm_overrideredirect(True)  # remove all Window Manager (wm) decorations
        #         tw.wm_overrideredirect(False)                 # uncomment to see the effect
        tw.wm_geometry("+%d+%d" % (x, y))  # create window size

        label = tk.Label(
            tw,
            text=tip_text,
            justify=tk.LEFT,
            background="#ffffe0",
            relief=tk.SOLID,
            borderwidth=1,
            font=("tahoma", "8", "normal"),
        )
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()


# OOP Class
class OOP:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Python GUI")
        self.costum_font = ("Arial", 16)

        # Create a notebook
        self.notebook = ttk.Notebook(self.win)
        self.notebook.pack(expand=True, fill="both")

        # Create tabs
        tab1 = ttk.Frame(self.notebook)
        tab2 = ttk.Frame(self.notebook)

        self.notebook.add(tab1, text="Tab 1")
        self.notebook.add(tab2, text="Tab 2")

        def create_ToolTip(widget, text):
            toolTip = ToolTip(widget)  # Call TollTip Class

            def enter(event):
                try:
                    toolTip.show_tip(text)
                except:
                    pass

            def leave(event):
                toolTip.hide_tip()

            widget.bind("<Enter>", enter)
            widget.bind("<Leave>", leave)

        # Content for Tab 1
        mighty_tab1 = ttk.Labelframe(tab1, text="Mighty_tab1 Python Tab 1")
        mighty_tab1.grid(column=0, row=0, padx=5, pady=8, sticky="W")

        # Entername
        self.enterName = ttk.Label(mighty_tab1, text="Enter a name:")
        self.enterName.grid(column=0, row=0, sticky="w")
        self.name = tk.StringVar()
        self.nameEntered = ttk.Entry(mighty_tab1, width=20, textvariable=self.name)
        self.nameEntered.grid(column=0, row=1, sticky="w")

        # Choose Number
        self.chNumber = ttk.Label(mighty_tab1, text="Choose a number:")
        self.chNumber.grid(column=1, row=0)
        self.number = tk.StringVar()
        self.numberChosen = ttk.Combobox(
            mighty_tab1, width=12, textvariable=self.number
        )
        self.numberChosen["values"] = (1, 5, 10, 15, 20, 25, 30)
        self.numberChosen.grid(column=1, row=1)
        self.numberChosen.current(0)

        # Click Me
        self.action = ttk.Button(mighty_tab1, text="Click Me!", command=self.click_Me)
        self.action.grid(column=2, row=1)

        # Spinbox
        def _spin():
            value = self.spin.get()
            self.scr.insert(tk.INSERT, value + "\n")

        self.spin = tk.Spinbox(
            mighty_tab1, from_=0, to=10, width=5, bd=8, command=_spin
        )
        self.spin.grid(column=0, row=2)

        # self.spin2 = tk.Spinbox(mighty_tab1, from_=0, to=10, width=5, bd=20, command=_spin)
        # self.spin2.grid(column=1, row=2)

        # Scroll Text
        scrolW = 40
        scrolH = 5
        self.scr = scrolledtext.ScrolledText(
            mighty_tab1, width=scrolW, height=scrolH, wrap=tk.WORD
        )
        self.scr.grid(column=0, row=6, columnspan=3, sticky="WE")

        self.nameEntered.focus()

        # tab 1 tooltip
        create_ToolTip(self.spin, "This is A Spin Control")
        # create_ToolTip(self.spin2,'This is A Spin Control 2')
        create_ToolTip(self.nameEntered, "Please Enter Name")
        create_ToolTip(self.action, "This A Button")
        create_ToolTip(self.numberChosen, "This Select Option")
        create_ToolTip(self.scr, "This Scrolled Text")

        # Content for Tab 2
        mighty_tab2 = ttk.Labelframe(tab2, text="Python Tab 2")
        mighty_tab2.grid(column=0, row=0, padx=5, pady=8, sticky="W")

        # Function to quit the application
        def _quit():
            self.win.quit()
            self.win.destroy()
            exit()

        def _exit():
            result = msg.askyesno("Quit Option", "Warning! Are You Sure Want Quit?")
            if result:
                _quit()

        # Create menu bar
        m_bar = Menu(self.win)
        self.win.config(menu=m_bar)

        # File Menu
        file_menu = Menu(m_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit")
        m_bar.add_cascade(label="File", menu=file_menu)

        def _msgBox():
            msg.showinfo("Information", "This is an information message.")

        # Help Menu
        help_menu = Menu(m_bar, tearoff=0)
        help_menu.add_command(label="About", command=_msgBox)
        m_bar.add_cascade(label="Help", menu=help_menu)

        # ProgressBar
        self.progbar = ttk.Progressbar(
            mighty_tab2, orient="horizontal", length=286, mode="determinate"
        )
        self.progbar.grid(column=0, row=4, pady=2)

        def run_progbar():
            self.progbar["maximum"] = 100
            for i in range(101):
                sleep(0.05)
                self.progbar["value"] = i
                self.progbar.update()
            self.progbar["value"] = 0

        def start_progbar():
            self.progbar.start()

        def stop_progbar():
            self.progbar.stop()

        def progbar_stop_after(wait_ms=1000):
            self.win.after(wait_ms, stop_progbar)

        self.runbtn = ttk.Button(mighty_tab2, text="Run Prog Bar", command=run_progbar)
        self.runbtn.grid(column=0, row=0, sticky="W")
        self.startbtn = ttk.Button(
            mighty_tab2, text="Start Prog Bar", command=start_progbar
        )
        self.startbtn.grid(column=0, row=1, sticky="W")
        self.stopbtn = ttk.Button(
            mighty_tab2, text="Stop Prog Bar", command=stop_progbar
        )
        self.stopbtn.grid(column=0, row=2, sticky="W")
        self.stopafter = ttk.Button(
            mighty_tab2, text="StopAfter Prog Bar", command=progbar_stop_after
        )
        self.stopafter.grid(column=0, row=3, sticky="W")

        # self.win.mainloop()
        # Tab 2 ToolTip
        create_ToolTip(self.progbar, "This Progbar")
        create_ToolTip(self.runbtn, "This RunButton")
        create_ToolTip(self.startbtn, "This StartButton")
        create_ToolTip(self.stopbtn, "This StopButton")
        create_ToolTip(self.stopafter, "This StopAfterButton")

    def click_Me(self):
        self.action.configure(
            text="Hello " + self.nameEntered.get() + " " + self.numberChosen.get()
        )


# Create an instance of the class
oop = OOP()
oop.win.mainloop()
