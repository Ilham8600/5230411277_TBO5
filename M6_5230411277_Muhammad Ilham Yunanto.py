class Order:
    def __init__(self, id, name, details):
        self._id = id  
        self.name = name
        self.details = details

    def set_order(self, name, details):
        self.name = name
        self.details = details

    def display_order(self):
        print(f"ID Pemesanan: {self._id}")
        print(f"Nama Pemesan: {self.name}")
        print(f"Detail Pemesanan: {self.details}")


class Delivery:
    def __init__(self, id, name, information, date, address):
        self._id = id  
        self.name = name
        self.information = information
        self.date = date
        self.address = address

    def process_delivery(self):
        print(f"Memproses pengiriman untuk {self.name} pada {self.date} ke alamat {self.address}")

    def display_delivery(self):
        print(f"ID Pengiriman: {self._id}")
        print(f"Nama Pengiriman: {self.name}")
        print(f"Informasi Pengiriman: {self.information}")
        print(f"Tanggal Pengiriman: {self.date}")
        print(f"Alamat Pengiriman: {self.address}")


def main():
    orders = {}
    deliveries = {}

    while True:
        print("\n====== Menu Utama ======")
        print("1. Buat Order")
        print("2. Lihat Semua Order")
        print("3. Buat Pengiriman")
        print("4. Tampilkan Pengiriman")
        print("0. Keluar")
        pilih = input("Pilih menu di atas: ")

        if pilih == "1":
            order_id = input("Masukkan ID Pemesanan: ")
            order_name = input("Masukkan Nama Pemesan: ")
            order_details = input("Masukkan Detail Pemesanan: ")
            order = Order(id=order_id, name=order_name, details=order_details)
            orders[order_id] = order
            print("Pemesanan berhasil dibuat!")

        elif pilih == "2":
            order_id = input("Masukkan ID Pemesanan yang ingin dilihat: ")
            if order_id in orders:
                orders[order_id].display_order()
            else:
                print("ID Pemesanan tidak ditemukan.")

        elif pilih == "3":
            delivery_id = input("Masukkan ID Pengiriman: ")
            delivery_name = input("Masukkan Nama Pengiriman: ")
            delivery_info = input("Masukkan Informasi Pengiriman: ")
            delivery_date = input("Masukkan Tanggal Pengiriman: ")
            delivery_address = input("Masukkan Alamat Pengiriman: ")

            delivery = Delivery(id=delivery_id, name=delivery_name, information=delivery_info, date=delivery_date, address=delivery_address)
            deliveries[delivery_id] = delivery
            print("Pengiriman berhasil dibuat!")

        elif pilih == "4":
            delivery_id = input("Masukkan ID Pengiriman yang ingin diproses: ")
            if delivery_id in deliveries:
                deliveries[delivery_id].process_delivery()
            else:
                print("ID Pengiriman tidak ditemukan.")

        elif pilih == "0":
            print("Terima kasih, sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")



main()
