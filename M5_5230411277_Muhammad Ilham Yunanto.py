class Music:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul  
        self.penyanyi = penyanyi
        self.genre = genre

    def tampil(self):
        print(f"Judul: {self.judul}, Penyanyi: {self.penyanyi}, Genre: {self.genre}")

class English(Music):
    def __init__(self, judul, penyanyi, genre):
        super().__init__(judul, penyanyi, genre)

class Indonesia(Music):
    def __init__(self, judul, penyanyi, genre):
        super().__init__(judul, penyanyi, genre)

class Japanese(Music):
    def __init__(self, judul, penyanyi, genre):
        super().__init__(judul, penyanyi, genre)

def add_Esong(Esongs):
    try:
        judul = input("Masukan Judul Lagu: ")
        if any(Esong.judul == judul for Esong in Esongs):
            print("Judul lagu sudah ada, lagu gagal ditambahkan.")
            return
        
        penyanyi = input("Masukan Nama Penyanyi: ")
        genre = input("Masukan Genre Musik: ")
        new_esong = English(judul, penyanyi, genre)
        Esongs.append(new_esong)
        print("Lagu berhasil ditambahkan.")
    except ValueError:
        print("Input tidak Valid")

def Display_ESong(Esongs):
    if not Esongs:
        print("Tidak Ada Lagu.")
    else:
        for esong in Esongs:
            esong.tampil()

def main():
    Esongs = []
    Isongs = []
    Jsongs = []

    while True:
        print("=====Playlist Music=====")
        print("1. English Song")
        print("2. Indonesian Song")
        print("3. Japanese Song")
        print("4. Display All")
        print("5. Search Music")
        print("0. Exit Program")
        pilih = input("Pilih Menu di Atas: ")

        if pilih == "1":
            while True:
                print("=====English Song=====")
                print("1. Display Song")
                print("2. Add Song")
                print("0. Kembali ke Menu Utama")
                pilih = input("Pilih Menu di Atas: ")
                if pilih == "1":
                    Display_ESong(Esongs)
                elif pilih == "2":
                    add_Esong(Esongs)
                elif pilih == "0":
                    break

        elif pilih == "2":
            while True:
                print("=====Indonesian Song=====")
                print("1. Display Song")
                print("2. Add Song")
                print("0. Kembali ke Menu Utama")
                pilih = input("Pilih Menu di Atas: ")
                if pilih == "1":
                    Display_ESong(Isongs)  
                elif pilih == "2":
                    pass
                elif pilih == "0":
                    break

        elif pilih == "3":
            while True:
                print("=====Japanese Song=====")
                print("1. Display Song")
                print("2. Add Song")
                print("0. Kembali ke Menu Utama")
                pilih = input("Pilih Menu di Atas: ")
                if pilih == "1":
                    Display_ESong(Jsongs)  
                elif pilih == "2":
                    pass
                elif pilih == "0":
                    break

        elif pilih == "0":
            print("Anda Keluar Program")
            break
        else:
            print("Pilihan Tidak Valid")

main()
