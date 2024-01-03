import tkinter as tk
from verisetim import MetinSınıfı

pencere = tk.Tk()
pencere.title("Metin Sınıflandırma Projesi")

pencere.geometry("470x300")
pencere.configure(bg="#ADD8E6")

project_label = tk.Label(pencere, text="Metin Sınıflandırma Uygulamasına Hoşgeldiniz", font=("Times New Roman", 18), bg="#ADD8E6")
project_label.pack(pady=10)

# veri seti yüklemek ve eğitmek
classifier = MetinSınıfı()

# sınıflandır butonu
def classify_text():
    user_input = entry.get()
    category = classifier.predict_category(user_input)
    sonuc_label.config(text=f"Kategori: {category}")

kullanici_label = tk.Label(pencere, text="Lütfen kelime girin:", font=("Times New Roman", 12), bg="#ADD8E6")
kullanici_label.pack()

entry = tk.Entry(pencere, font=("Times New Roman", 12))
entry.pack()

siniflandir_button = tk.Button(pencere, text="Sınıflandır", command=classify_text, font=("Times New Roman", 12))
siniflandir_button.pack(pady=10)

sonuc_label = tk.Label(pencere, text="Kategori: ", font=("Times New Roman", 12), bg="#ADD8E6")
sonuc_label.pack()

cikis_button = tk.Button(pencere, text="Çıkış", command=pencere.destroy, font=("Times New Roman", 12))
cikis_button.pack(side=tk.BOTTOM)

pencere.mainloop()


