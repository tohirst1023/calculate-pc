def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "0 ga bo'lish mumkin emas!"  
    return x // y

while True:

    while True:
        try:
            son1 = int(input("1-chi sonni kiriting: "))
            break  
        except ValueError:
            print("Iltimos, faqat son kiriting.")

    while True:
        try:
            son2 = int(input("2-chi sonni kiriting: "))
            break  
        except ValueError:
            print("Iltimos, faqat son kiriting.")

    while True:
        tanlashi = input("Shu lardan birini tanleng(+, -, *, /): ")
        
        if tanlashi in ["+", "-", "*", "/"]:
            print(f"Tanlangan symbol: {tanlashi}")
            break 
        else: 
            print("Iltimos, quyidagi belgilarni tanlang(+, -, *, /)")

    if tanlashi == "+":
        resultat = son1+son2 
    elif tanlashi == "-":
        resultat = son1-son2
    elif tanlashi == "*":
        resultat = son1*son2
    elif tanlashi == "/":
        try:
            resultat = son1//son2
        except ZeroDivisionError:
            resultat = "0 ga bo'lish mumkin emas idiot!" 
    else:
        print(" Tanlashdan notog'ri terdingiz")
    print("Sizi Jovobingiz: ",resultat)



# son1 = int(input("soni kiriting: "))

# if 0<= son1 <10:
#     print("bu 1 xonaliy son")

# elif 11<= son1 <99:
#     print("bu 2 xonaliy son")

# elif 100<= son1 <1000 :
#     print("bu 3 xonaliy son")

# elif 1000<= son1 <9999:
#     print("bu 4 xonaliy son")

# elif 10000<= son1 <99999:
#     print("bu 5 xonaliy son")

# else: 
#     print("qaytatan kiriting") 



# 
# son = int(input("Son kiriting: "))

# if son > 1:
#     for i in range(2, son):
#         if (son % i) == 0:
#             print(f"{son} tub emas.")
#             break
#     else:
#         print(f"{son} tub son.")
# else:
#     print(f"{son} tub emas.")
