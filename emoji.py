import tkinter as tk
import random

class EmojiYuzOyunu:
    def __init__(self, root):
        self.root = root
        self.root.title("Emoji Yüz Oluşturucu")
        self.root.geometry("400x400")
        self.root.config(bg="#ffe4e1")  # Arka plan rengi: Pembe tonları

        # Başlık
        self.baslik = tk.Label(
            root,
            text="😊 Emoji Yüz Oluşturucu 😊",
            font=("Helvetica", 16, "bold"),
            bg="#ffe4e1",
            fg="#333"
        )
        self.baslik.pack(pady=20)

        # Emoji gösterim alanı
        self.emoji_label = tk.Label(
            root,
            text="(?.?.?)",
            font=("Courier", 30, "bold"),
            bg="#fff",
            fg="#333",
            width=15,
            height=2,
            relief="ridge",
            bd=2
        )
        self.emoji_label.pack(pady=20)

        # Oluştur butonu
        self.olusbuton = tk.Button(
            root,
            text="Rastgele Yüz Oluştur 🎲",
            font=("Helvetica", 12, "bold"),
            bg="#4caf50",
            fg="white",
            command=self.rastgele_yuz_olustur
        )
        self.olusbuton.pack(pady=20)

        # Çıkış butonu
        self.cikisbuton = tk.Button(
            root,
            text="Çıkış 🚪",
            font=("Helvetica", 12, "bold"),
            bg="#f44336",
            fg="white",
            command=root.quit
        )
        self.cikisbuton.pack(pady=10)

    def rastgele_yuz_olustur(self):
        # Rastgele yüz elemanlarını seç
        gozler = random.choice(['^', 'o', 'O', '-', '*', 'x'])
        agiz = random.choice(['_', 'v', 'w', 'o', '.', 'U'])
        yuz = f"({gozler}.{agiz}.{gozler})"
        
        # Emoji yüzünü güncelle
        self.emoji_label.config(text=yuz)

# Ana pencere
root = tk.Tk()
oyun = EmojiYuzOyunu(root)
root.mainloop()
