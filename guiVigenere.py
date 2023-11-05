import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from pandastable import Table, TableModel


def vigenere(text, key, mode):
    key = key.lower()
    result = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            if char.isupper():
                offset = ord('A')
            else:
                offset = ord('a')
            if mode == 'encrypt':
                result_char = chr(((ord(char) - offset + shift) % 26) + offset)
            else:
                result_char = chr(((ord(char) - offset - shift) % 26) + offset)
            key_index += 1
            result += result_char
        else:
            result += char
    return result


def select_file():
    file_path = filedialog.askopenfilename()
    input_text.delete(1.0, tk.END)
    input_text.insert(tk.END, open(file_path).read())


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, 'w') as file:
        file.write(output_text.get(1.0, tk.END))
    messagebox.showinfo("Info", "Teks berhasil disimpan ke dalam file.")


def encrypt():
    input_text_value = input_text.get(1.0, tk.END)
    key = key_entry.get()
    output_text_value = vigenere(input_text_value, key, 'encrypt')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, output_text_value)


def decrypt():
    input_text_value = input_text.get(1.0, tk.END)
    key = key_entry.get()
    output_text_value = vigenere(input_text_value, key, 'decrypt')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, output_text_value)


def show_vigenere_table():
    vigenere_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vigenere_table_data = []
    for row in range(26):
        vigenere_table_data.append(
            [vigenere_key[row]] + list(vigenere(vigenere_key, vigenere_key[row], 'encrypt')))

    df = pd.DataFrame(vigenere_table_data, columns=[
                      'Key'] + list(vigenere_key))
    table = Table(tab2, dataframe=df, showstatusbar=True)
    table.show()
    plt.show()


app = tk.Tk()
app.title("Vigenere Cipher GUI")

tab_control = ttk.Notebook(app)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Enkripsi/Dekripsi')
tab_control.add(tab2, text='Tabel Vigenere')
tab_control.pack(expand=1, fill='both')

frame = ttk.Frame(tab1)
frame.grid(row=0, column=0, padx=10, pady=10)

input_label = ttk.Label(frame, text="Teks Input:")
input_label.grid(row=0, column=0, sticky="w")

input_text = tk.Text(frame, width=40, height=10)
input_text.grid(row=1, column=0)

file_button = ttk.Button(frame, text="Pilih File", command=select_file)
file_button.grid(row=2, column=0)

key_label = ttk.Label(frame, text="Kunci Vigenere:")
key_label.grid(row=3, column=0, sticky="w")

key_entry = ttk.Entry(frame)
key_entry.grid(row=4, column=0)

encrypt_button = ttk.Button(frame, text="Enkripsi", command=encrypt)
encrypt_button.grid(row=5, column=0)

decrypt_button = ttk.Button(frame, text="Dekripsi", command=decrypt)
decrypt_button.grid(row=6, column=0)

output_label = ttk.Label(frame, text="Teks Hasil:")
output_label.grid(row=7, column=0, sticky="w")

output_text = tk.Text(frame, width=40, height=10)
output_text.grid(row=8, column=0)

save_button = ttk.Button(frame, text="Simpan Hasil", command=save_file)
save_button.grid(row=9, column=0)

vigenere_table_button = ttk.Button(
    tab2, text="Tampilkan Tabel Vigenere", command=show_vigenere_table)
vigenere_table_button.grid(row=0, column=0)

app.mainloop()
