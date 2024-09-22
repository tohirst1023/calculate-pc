# import tkinter as tk
# from tkinter import messagebox
# import math

# # Funksiya kvadrat ildizni hisoblaydi
# def calculate_sqrt():
#     try:
#         # Foydalanuvchi kiritgan qiymatni olamiz
#         number = float(entry.get())
#         # Agar raqam manfiy bo'lsa, xatolik ko'rsatamiz
#         if number < 0:
#             messagebox.showerror("Xatolik", "Manfiy raqamning kvadrat ildizini hisoblab bo'lmaydi!")
#         else:
#             # Kvadrat ildizni hisoblaymiz
#             result = math.sqrt(number)
#             # Natijani chiqaramiz
#             messagebox.showinfo("Natija", f"{number} sonining kvadrat ildizi: {result}")
#     except ValueError:
#         # Agar raqam emas narsa kiritilsa, xatolik ko'rsatamiz
#         messagebox.showerror("Xatolik", "Iltimos, to'g'ri raqam kiriting!")

# # Tkinter oynasini yaratamiz
# root = tk.Tk()
# root.title("Kvadrat Ildiz Hisoblagich")

# # Kirish joyi uchun yorliq
# label = tk.Label(root, text="Raqam kiriting:")
# label.pack(pady=10)

# # Kirish joyini yaratamiz
# entry = tk.Entry(root)
# entry.pack(pady=5)

# # Hisoblash tugmasini yaratamiz
# button = tk.Button(root, text="Hisobla", command=calculate_sqrt)
# button.pack(pady=10)

# # Oynani namoyish qilamiz
# root.mainloop()




import math

number = int(input("Son kiriting:"))
square_root = math.sqrt(number)
print(f"The square root of {number} is {square_root}.")
