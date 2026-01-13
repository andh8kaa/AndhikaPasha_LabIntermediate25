rahasia = 'kursi'
a = input("masukin huruf: ").lower()

if len(a) == 1:
    if a in rahasia:
        print("huruf ADA")
    else:
        print("huruf TIDAK ada")
else:
    print("salah, hanya 1 huruf")

