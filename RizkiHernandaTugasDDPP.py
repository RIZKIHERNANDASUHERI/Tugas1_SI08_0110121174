def periksa():
    email = input("Masukkan email: ")
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        print("Email Tidak Valid, Ulangi")
        return periksa()
def check_katasandi():
    password = input("Masukkan katasandi: ")
    chaeSept = ["!", "@", "#", "$"]
    if len(password) >= 8:
        if any(word.isnumeric() for word in password):
            if any(word.islower() for word in password):
                if any(word.isupper() for word in password):
                    if any(word in chaeSept for word in password):
                        return True
                    else:
                        print("Katasandi Salah")
                        return check_katasandi()
                else:
                    print("Katasandi Salah")
                    return check_katasandi()
            else:
                print("Katasandi Salah")
                return check_katasandi()
        else:
            print("Katasandi Salah")
            return check_katasandi()
    else:
        print("Katasandi Salah")
        return check_katasandi()

def Membership():
    level = input("Masukkan Level Membership Anda(Perunggu/Emas/Platinum): ")
    while level != "Perunggu" and level != "Emas" and level != "Platinum":
        level = input ("Masukan Salah, Ulangi: ")
    else:
        if level == "Perunggu":
            if u < 5:
                diskon = i * (5/100)
                print("Selamat! Anda mendapatkan Promo diskon sebesar 5%")
            else:
                diskon = i * (10/100)
                print("Selamat! Anda mendapatkan Promo diskon sebesar 10%")
        elif level == "Emas":
            if u < 5:
                diskon = i * (10/100)
                print("Selamat! Anda mendapatkan Promo diskon sebesar 10%")
            else:
                diskon = i * (15/100)
                print("Selamat! Anda mendapatkan Promo diskon sebesar 15%")
        elif level == "Platinum":
            if u < 5:
                diskon = i * (15/100)
                print("Selamat! Anda mendapatkan Promo diskon sebesar 15%")
            else:
                diskon = i * (20/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 20%")
        setelah_diskon = i - diskon
        print(" Seluruh Total Harga Produk yang harus dibayar: ", float(setelah_diskon))
        quit()
u = 0
i = 0

while True:
    j = input("Masukkan nama produk yang akan dibeli atau X untuk selesai: ")
    if j == "X" and u == 0:
        print("Terima Kasih,Sampai Jumpa lagi")
        quit()
    if j == "X" and u > 0:
        print("Jumlah produk yang dibeli:", u)
        print("Jumlah harga produk: ", i)
        break
    else:
        y = int(input("Masukkan harga produk: "))
        print("Berhasil menambahkan", j, "dengan harga", y)
        u += 1
        i += y
h = input("Apakah Anda seorang anggota? (Y/T): ")
if h == "Y":
    if periksa():
        if check_katasandi():
            Membership()
                
        else:
            check_katasandi()
else:
    print("Seluruh Total harga produk yang harus dibayar:", i)
    print("Terima kasih telah berbelanja di TokoElektronikNF.")
print("Terima kasih. Semoga Berbelanja Ditempat kami membuat anda puas.")
