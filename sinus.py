import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sinus va kosinus grafigini chizish funksiyasi
def plot_sin_cos():
    # Grafikni chizishdan oldin tozalash
    ax.clear()
    
    # 0 dan 4π gax cha bo'lgan x qiymatlarini generatsiya qilish
    x = np.linspace(0, 4 * np.pi, 1000)
    
    # x ning sinus va kosinusini hisoblash
    sin_y = np.sin(x)
    cos_y = np.cos(x)
        
    # Sinus va kosinus funksiyalarini chizish
    ax.plot(x, sin_y, label='sin(x)', color='blue')
    ax.plot(x, cos_y, label='cos(x)', color='red')
    
    # Grafik uchun nomlar va sarlavha qo'yish
    ax.set_title('Sinus va Kosinus Funksiyalari')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    
    # Canvasni qaytadan chizish
    canvas.draw()

# Asosiy oynani yaratish
root = tk.Tk()
root.title('Sinus va Kosinus Grafi')

# Grafik uchun frame yaratish
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Matplotlibda grafik va o'q yaratish
fig, ax = plt.subplots(figsize=(5, 4))

# Grafikni joylashtirish uchun Tkinter canvas yaratish
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Sinus va kosinusni chizish uchun tugma qo'shish
plot_button = ttk.Button(root, text='Sinus & Kosinusni Chizish', command=plot_sin_cos)
plot_button.pack()

# Tkinter tadbirlar tsiklini boshlash
root.mainloop()





# import math

# a = math.pi/6

# sin = math.sin(a)
# cos = math.cos(a)
# tan = math.tan(a)

# print(sin,cos,tan)



