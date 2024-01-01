import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox

# Fungsi untuk terhubung ke database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="mahasiswa",
        port=3316
    )

# Fungsi untuk menampilkan data dari database
def display_data():
    connection = connect_db() 
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mahasiswa")
    rows = cursor.fetchall()
    connection.close()
    return rows

# Fungsi untuk menambah data ke database
def insert_data(nama, nim):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mahasiswa (nama, nim) VALUES (%s, %s)", (nama, nim))
    connection.commit()
    connection.close()

# Fungsi untuk mengupdate data di database
def update_data(id, nama, nim):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("UPDATE mahasiswa SET nama=%s, nim=%s WHERE id=%s", (nama, nim, id))
    connection.commit()
    connection.close()

# Fungsi untuk menghapus data di database
def delete_data(id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM mahasiswa WHERE id=%s", (id,))
    connection.commit()
    connection.close()

# Fungsi untuk menampilkan data dalam tabel Tkinter
def show_data():
    for row in tree.get_children():
        tree.delete(row)
    
    data = display_data()
    for record in data:
        tree.insert("", "end", values=record)

# Fungsi untuk menangani tombol "Tambah"
def add_data():
    nama = entry_nama.get()
    nim = entry_nim.get()

    if nama and nim:
        insert_data(nama, nim)
        show_data()
        messagebox.showinfo("Info", "Data berhasil ditambahkan.")
    else:
        messagebox.showerror("Error", "Nama dan NIM tidak boleh kosong.")

# Fungsi untuk menangani tombol "Edit"
def edit_data():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item, 'values')
        id = item[0]
        nama = entry_nama.get()
        nim = entry_nim.get()

        if nama and nim:
            update_data(id, nama, nim)
            show_data()
            messagebox.showinfo("Info", "Data berhasil diubah.")
        else:
            messagebox.showerror("Error", "Nama dan NIM tidak boleh kosong.")
    else:
        messagebox.showerror("Error", "Pilih data yang ingin diubah.")

# Fungsi untuk menangani tombol "Hapus"
def delete_selected_data():
    selected_item = tree.selection()
    if selected_item:
        confirmation = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
        if confirmation:
            item = tree.item(selected_item, 'values')
            id = item[0]
            delete_data(id)
            show_data()
            messagebox.showinfo("Info", "Data berhasil dihapus.")
    else:
        messagebox.showerror("Error", "Pilih data yang ingin dihapus.")

# Membuat GUI Tkinter
root = Tk()
root.title("CRUD App with Tkinter and MySQL")

# Membuat label dan entry untuk Nama
label_nama = Label(root, text="Nama:")
label_nama.grid(row=0, column=0, padx=10, pady=5, sticky=W)
entry_nama = Entry(root)
entry_nama.grid(row=0, column=1, padx=10, pady=5, sticky=W)

# Membuat label dan entry untuk NIM
label_nim = Label(root, text="NIM:")
label_nim.grid(row=1, column=0, padx=10, pady=5, sticky=W)
entry_nim = Entry(root)
entry_nim.grid(row=1, column=1, padx=10, pady=5, sticky=W)

# Membuat tombol "Tambah"
btn_add = Button(root, text="Tambah", command=add_data)
btn_add.grid(row=2, column=0, columnspan=2, pady=10)

# Membuat tombol "Edit"
btn_edit = Button(root, text="Edit", command=edit_data)
btn_edit.grid(row=3, column=0, columnspan=2, pady=10)

# Membuat tombol "Hapus"
btn_delete = Button(root, text="Hapus", command=delete_selected_data)
btn_delete.grid(row=4, column=0, columnspan=2, pady=10)

# Membuat tabel untuk menampilkan data
tree_columns = ("ID", "Nama", "NIM")
tree = ttk.Treeview(root, columns=tree_columns, show="headings", selectmode="browse")
for col in tree_columns:
    tree.heading(col, text=col)
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Menampilkan data awal
show_data()

# Menjalankan GUI
root.mainloop()
