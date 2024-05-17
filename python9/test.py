with open("ilk_fayl.txt", "w") as f:
    f.write("i love you")

with open("ilk_fayl.txt", "r") as f:
    first_line = f.readline().upper()

with open("ikinci_fayl.txt", "w") as f:
    f.write(first_line)