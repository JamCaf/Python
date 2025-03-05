menu = {"entremeada": 7,
        "Sardinha": 6,
        "Filetes": 5.5,
        "Prego": 7,
        "Hamburger": 5.5
}

x = menu["Prego"]
print(x) #a

for x in menu:
    print(x) #b

menu["omelete"] = "5" #c

print(menu) #d


for y, z in menu.items():
    print(y, z) #d

