from w3_tugas1 import Chef
from w3_tugas2 import Pelayan
from w3_tugas3 import Menu
import os

while True:
    os.system('cls')
    print("Menu")
    print("1. Isi data Chef")
    print("2. Isi data Pelayan")
    print("3. Isi data Menu")
    print("4. Lihat Data Chef")
    print("5. Lihat Data Pelayan")
    print("6. Lihat Data Menu")
    print("0. Keluar")
    pilih = int(input("Pilih menu: "))
    if pilih == 1:
        namaChef = input("Nasukan Nama Chef : ")
        idChef = input("Masukan Id Chef : ")
        emailChef = input("Masukan Email Chef : ")
        chef1 = Chef(namaChef, idChef, emailChef)
    
    elif pilih == 2:
        namaPelayan = input("Masukan Nama Pelayan : ")
        idPelayan = input("Masukan Id Pelayan : ")
        emailPelayan = input("Masukan Email Pelayan : ")
        pelayan1 = Pelayan(namaPelayan, idPelayan, emailPelayan)

    elif pilih == 3:
        namaMakanan = input("Masukan Nama Makanan : ")
        hargaMakanan = int(input("Masukan Harga Makanan : "))
        namaMinumam = input("Masukan Nama Minuman : ")
        hargaMinumam = int(input("Masukan Harga Minumam : "))
        daftarMenu = Menu(namaMakanan, hargaMakanan, namaMinumam, hargaMinumam)
    
    elif pilih == 4:
        chef1.data_chef()
    
    elif pilih == 5:
        pelayan1.data_pelayan()
    
    elif pilih == 6:
        daftarMenu.list_menu()

    else:
        print("Terimakasih")
        break
    os.system("pause")
