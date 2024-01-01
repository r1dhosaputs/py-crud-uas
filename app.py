import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox
from time import sleep
from tkinter import *
from mysql_class import (
    MySQL,
)


class MySQLGUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("CRUD PYTHON")
        self.costum_font = ("Arial", 16)
        self.win.resizable(0, 0)
        self.mySQL = MySQL()
        self.create_widgets()
        self.msg = messagebox

    def show_data(self):
        # Implement your show data logic here
        show = self.mySQL.showData("mahasiswa")
        # Clear existing text in ScrolledText ( menghapus yang sudah ada misal kaya refresh )
        # self.tree.delete("1.0", tk.END)
        self.tree.delete(*self.tree.get_children())

        for no, row in enumerate(show, start=1):
            # Mengabaikan kolom ID (indeks 0)
            row_str = "\t".join(map(str, row[1:]))
            # Menambahkan nomor urut sebagai prefix jadi nomor tambah hasil row
            row_with_number = f"{no}. {row_str}"
            # self.scr_txt.insert(tk.END, row_with_number + "\n")
            self.tree.insert(
                "", "end", values=row_with_number, tags=(row[0])
            )  # tags buat id biar tersembunyi dari read show

    def insert_data(self):
        name = self.entry_name.get()
        nim = self.entry_nim.get()
        gender = self.gender_var.get()

        if name and nim and gender:
            data = {
                "name": name,
                "nim": nim,
                "gender": gender,
            }
            self.mySQL.insertData(data)
            self.msg.showinfo("Sukses", "Data Berhasil Dimasukkan")
            self.show_data()
        else:
            self.msg.showinfo("Gagal", "Data Gagal Dimasukkan")

    def edit_selected(self):
        # Implement your edit selected logic here
        # self.msg.showinfo("Edit Selected", "Edit selected operation")
        selected = self.tree.selection()
        if selected:
            item_info = self.tree.item(selected)

            item_values = item_info["values"]
            item_tags = item_info["tags"]

            id = item_tags[0]
            name = self.entry_name.get()
            nim = self.entry_nim.get()
            gender = self.gender_var.get()

            # jika tidak di isi salah satu isi dengan yang lama
            if not name:
                name = item_values[1]

            if not nim:
                nim = item_values[2]

            if not gender:
                gender = item_values[3]

            data = {
                "id": id,
                "name": name,
                "nim": nim,
                "gender": gender,
            }

            if data:
                # print(name, nim, gender)
                # print(data)
                query = self.mySQL.editData(data)
                if query == True:
                    self.msg.showinfo("Info", "Data Berhasil Diubah.")
                    self.show_data()

            else:
                self.msg.showerror("Error", "Data Tidak Valid/Ditemukan")

    def delete_selected(self):
        # Implement your delete selected logic here
        # messagebox.showinfo("Delete Selected", "Delete selected operation")
        selected = self.tree.selection()
        if selected:
            confirmation = self.msg.askyesno("Konfirmasi", "Yakin Ingin Menghapus?")
            if confirmation:
                item = self.tree.item(selected, "tags")
                id = item[0]
                self.mySQL.deleteData(id)
                self.show_data()
                self.msg.showinfo("Info", "Data berhasil dihapus.")
            else:
                self.msg.showinfo("Info", "Baiklah")
        else:
            self.msg.showerror("Error", "Data Tidak Valid/Ditemukan")

    def create_widgets(self):
        # Tab Control
        tab_control = ttk.Notebook(self.win)

        # MySQL Tab
        tab_mysql = ttk.Frame(tab_control)
        tab_control.add(tab_mysql, text="MySQL")
        tab_control.pack(expand=1, fill="both")
        # db Tab
        tab_db = ttk.Frame(tab_control)
        tab_control.add(tab_db, text="db")
        tab_control.pack(expand=2, fill="both")

        # My Frame
        my_frame1 = ttk.LabelFrame(tab_mysql, text="Python Database ")
        my_frame1.grid(column=0, row=0, padx=8, pady=4)

        self.label_name = ttk.Label(my_frame1, text="Nama:")
        self.label_name.grid(column=0, row=1, padx=5, pady=5, sticky="WE", columnspan=5)
        self.name = tk.StringVar()
        self.entry_name = ttk.Entry(my_frame1, textvariable=self.name)
        self.entry_name.grid(column=1, row=1, padx=5, pady=5, sticky="WE", columnspan=5)

        self.label_nim = ttk.Label(my_frame1, text="NIM:")
        self.label_nim.grid(column=0, row=2, padx=5, pady=5, sticky="WE", columnspan=5)
        self.nim = tk.StringVar()
        self.entry_nim = ttk.Entry(my_frame1, textvariable=self.nim)
        self.entry_nim.grid(column=1, row=2, padx=5, pady=5, sticky="WE", columnspan=5)

        # Radio buttons for gender
        self.label_gender = ttk.Label(my_frame1, text="Gender:")
        self.label_gender.grid(column=0, row=3, padx=5, pady=5, sticky="W")

        self.gender_var = tk.StringVar()
        self.radio_male = ttk.Radiobutton(
            my_frame1, text="Laki-Laki", variable=self.gender_var, value="Laki-Laki"
        )
        self.radio_male.grid(column=1, row=3, padx=5, pady=5, sticky="W")

        self.radio_female = ttk.Radiobutton(
            my_frame1, text="Perempuan", variable=self.gender_var, value="Perempuan"
        )
        self.radio_female.grid(column=2, row=3, padx=5, pady=5, sticky="W")

        # Buttons
        self.action_show_data = ttk.Button(
            my_frame1, text="Show Data", command=self.show_data
        )
        self.action_show_data.grid(column=0, row=0, sticky="W")

        self.action_edit_selected = ttk.Button(
            my_frame1, text="Edit Selected", command=self.edit_selected
        )
        self.action_edit_selected.grid(column=1, row=0, sticky="W")

        self.action_delete_selected = ttk.Button(
            my_frame1, text="Delete Selected", command=self.delete_selected
        )
        self.action_delete_selected.grid(column=2, row=0, sticky="W")

        self.action_insert_data = ttk.Button(
            my_frame1, text="Insert Data", command=self.insert_data
        )
        self.action_insert_data.grid(column=0, row=4)

        # ScrolledText
        # self.scr_txt = scrolledtext.ScrolledText(
        #     my_frame1, width=40, height=10, wrap=tk.WORD
        # )
        # self.scr_txt.grid(column=0, row=5, columnspan=125, pady=4)
        # self.scr_txt.config(state=tk.NORMAL)

        # tabel pakai tree gabisa pakai scr text
        self.tree_col = ("No", "Nama", "NIM", "Kelamin")
        self.tree = ttk.Treeview(
            my_frame1, columns=self.tree_col, show="headings", selectmode="browse"
        )
        for col in self.tree_col:
            self.tree.heading(col, text=col)
        self.tree.grid(row=5, column=0, columnspan=125, padx=10, pady=10)

        
        # Create menu bar
        m_bar = Menu(self.win)
        self.win.config(menu=m_bar)

        # File Menu
        file_menu = Menu(m_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit")
        m_bar.add_cascade(label="File", menu=file_menu)

app = MySQLGUI()
app.win.mainloop()
