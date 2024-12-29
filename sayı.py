import tkinter as tk
from tkinter import messagebox
import random

class SayiTahminOyunu:
    def __init__(self, root):
        self.root = root
        self.root.title("Sayı Tahmin Oyunu")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f8ff")  # Arka plan rengi

        self.gizli_sayi = random.randint(1, 100)
        self.tahmin_hakki = 7

        # Başlık
        self.baslik = tk.Label(
            root,
            text="🎯 Sayı Tahmin Oyunu 🎯",
            font=("Helvetica", 16, "bold"),
            bg="#f0f8ff",
            fg="#333"
        )
        self.baslik.pack(pady=20)

        # Bilgilendirme
        self.bilgi_label = tk.Label(
            root,
            text="1 ile 100 arasında bir sayı tuttum.\nTahmin etmeye çalış!",
            font=("Helvetica", 12),
            bg="#f0f8ff",
            fg="#555"
        )
        self.bilgi_label.pack(pady=10)

        # Kullanıcı giriş kutusu
        self.tahmin_entry = tk.Entry(
            root,
            font=("Helvetica", 14),
            justify="center"
        )
        self.tahmin_entry.pack(pady=10)

        # Onay butonu
        self.onay_butonu = tk.Button(
            root,
            text="Tahmin Et",
            font=("Helvetica", 12, "bold"),
            bg="#4caf50",
            fg="white",
            command=self.tahmin_et
        )
        self.onay_butonu.pack(pady=10)

        # Bilgilendirme alanı
        self.sonuc_label = tk.Label(
            root,
            text="Kalan Hakkınız: 7",
            font=("Helvetica", 12),
            bg="#f0f8ff",
            fg="#555"
        )
        self.sonuc_label.pack(pady=10)

    def tahmin_et(self):
        try:
            tahmin = int(self.tahmin_entry.get())
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")
            return

        if tahmin < 1 or tahmin > 100:
            messagebox.showwarning("Uyarı", "Tahmininiz 1 ile 100 arasında olmalı!")
            return

        self.tahmin_hakki -= 1
        if tahmin == self.gizli_sayi:
            messagebox.showinfo("Tebrikler!", f"Doğru tahmin! Sayı: {self.gizli_sayi}")
            self.reset_oyun()
        elif tahmin < self.gizli_sayi:
            self.sonuc_label.config(text=f"Daha büyük bir sayı dene! 🔼\nKalan Hakkınız: {self.tahmin_hakki}")
        else:
            self.sonuc_label.config(text=f"Daha küçük bir sayı dene! 🔽\nKalan Hakkınız: {self.tahmin_hakki}")

        if self.tahmin_hakki == 0:
            messagebox.showerror("Kaybettiniz", f"Üzgünüm, doğru sayı {self.gizli_sayi} idi.")
            self.reset_oyun()

    def reset_oyun(self):
        self.gizli_sayi = random.randint(1, 100)
        self.tahmin_hakki = 7
        self.sonuc_label.config(text="Kalan Hakkınız: 7")
        self.tahmin_entry.delete(0, tk.END)


# Ana pencere
root = tk.Tk()
oyun = SayiTahminOyunu(root)
root.mainloop()
