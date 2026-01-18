kata = "kursi"
tebakan = []
kesempatan = 6 

print ("=== Hangman 2.0 ===")

while kesempatan > 0:
    tampil = ""
    for h in kata:
        tampil += h if h in tebakan else "_"

    print("\nKata:", tampil)
    print("Sisa kesempatan:", kesempatan)

    if "_" not in tampil:
        print("Kamu Menang!")
        break

    huruf = input("Tebak Huruf: ").lower()

    if huruf in tebakan:
        print("Huruf sudah ditebak")
        continue

    tebakan.append(huruf)
    kesempatan -= 1
    if kesempatan == 0:
        print("\n Kamu Kalah :(")
        print("Kata yang bener:", kata)