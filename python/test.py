while True:
    symbols = input("Shu lardan birini tanleng(+, -, *, /, %): ")
    
    if symbols in ["+", "-", "*", "/", "%"]:
        print(f"Tanlangan symbol: {symbols}")
        break 
    else: 
        print("Iltimos, quyidagi belgilarni tanlang(+, -, *, /, %)")
