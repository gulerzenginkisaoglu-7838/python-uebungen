import tkinter as tk
from tkinter import messagebox

def bewertung_webseite(ladezeit, html_valid, mobile_freundlich, seo_optimierung):
    if ladezeit < 2:
        if html_valid and mobile_freundlich:
            if seo_optimierung > 80:
                return "Hervorragend"
            elif seo_optimierung > 50:
                return "Gut, SEO könnte besser sein"
            else:
                return "Schwaches SEO"
        else:
            return "Gute Ladezeit, aber nicht valide oder nicht mobilfreundlich"
    else:
        if html_valid:
            if mobile_freundlich:
                return "Langsam, aber valide und mobilfreundlich"
            else:
                return "Langsam und nicht mobilfreundlich"
        else:
            return "Langsam und nicht valide"

def bewertung_start():
    try:
        ladezeit = float(entry_ladezeit.get())
        html_valid = var_html.get()
        mobile_freundlich = var_mobile.get()
        seo_optimierung = int(entry_seo.get())
        
        result = bewertung_webseite(ladezeit, html_valid, mobile_freundlich, seo_optimierung)
        messagebox.showinfo("Bewertung", result)
    except ValueError:
        messagebox.showerror("Fehler", "Lütfen tüm alanlara geçerli sayılar girin!")

# Arayüz oluştur
root = tk.Tk()
root.title("Website Bewertung")

tk.Label(root, text="Ladezeit (saniye):").grid(row=0, column=0, sticky="e")
entry_ladezeit = tk.Entry(root)
entry_ladezeit.grid(row=0, column=1)

tk.Label(root, text="HTML gültig:").grid(row=1, column=0, sticky="e")
var_html = tk.BooleanVar()
tk.Checkbutton(root, variable=var_html).grid(row=1, column=1, sticky="w")

tk.Label(root, text="Mobilfreundlich:").grid(row=2, column=0, sticky="e")
var_mobile = tk.BooleanVar()
tk.Checkbutton(root, variable=var_mobile).grid(row=2, column=1, sticky="w")

tk.Label(root, text="SEO Optimierung (0-100):").grid(row=3, column=0, sticky="e")
entry_seo = tk.Entry(root)
entry_seo.grid(row=3, column=1)

tk.Button(root, text="Bewerten", command=bewertung_start).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
