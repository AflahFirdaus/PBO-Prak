class Aflah:
    def __init__(self, nama, no_identitas, alamat, pekerjaan, jumlah_tabungan, penghasilan):
        self.nama = nama
        self.__no_identitas = no_identitas
        self._alamat = alamat
        self.pekerjaan = pekerjaan
        self.__jumlah_tabungan = jumlah_tabungan
        self._penghasilan = penghasilan

    def input_data(self):
        print("Nama: ",self.nama)
        print("No Identitas: ",self.__no_identitas)
        print("Alamat: ",self._alamat)
        print("Pekerjaan",self.pekerjaan)
        print("Jumlah Tabungan",self.__jumlah_tabungan)
        print("Penghasilan: ",self._penghasilan)

    def public_data(self):
        print("Nama: ",self.nama)
        print("Pekerjaan: ",self.pekerjaan)

    def _prtected_data(self):
        print("Nama: ",self.nama)
        print("Pekerjaan: ",self.pekerjaan)
        print("Alamat",self._alamat)
        print("Penghasilan",self._penghasilan)

    def __privat_data(self):
        print("Nama Saya",self.nama)
        print("No Identitas",self.__no_identitas)
        print("Jumlah Tabungan",self.__jumlah_tabungan)

    def akses_method_protected(self):
        self._prtected_data()

    def akses_method_privat(self):
        self.__privat_data()

data_list = []

while True:
    print("Menu")
    print("1. Input Data")
    print("2. Menampilkan method public")
    print("3. Edit data protected")
    print("4. Tampilkan atribut protected")
    print("5. Tampilkan atribut private")
    print("0. Selesai")

    pilih = int(input("Pilih Menu Ke: "))
    if pilih == 1:
        a = input("Nama: ")    
        b = input("No Identitas: ")    
        c = input("Alamat: ")    
        d = input("Pekerjaan: ")    
        e = input("Jumlah Tabungan: ")    
        f = input("Penghasilan: ")
        data = Aflah(a,b,c,d,e,f)
        data_list.append(data)
    
    elif pilih == 2:
        print("Tampilkan method public")
        for data in data_list:
            data.public_data()

    elif pilih == 3:
        print("Edit data protected")
        if len(data_list) == 0:
            print('Belum Ada Data, Silahkan Isi data')
        else:
            no_id_edit = input('Masukan No Identitas yang akan di edit: ')
            for data in data_list:
                if data._Aflah__no_identitas == no_id_edit:
                    c2 = input("Alamat: ")
                    e2 = input("Penghasilan: ")
                    data._alamat = c2
                    data._penghasilan = e2
                    print('Data Berhasil diupdate')
                    break
            else:
                print('Tidak ada No Identitas')

    elif pilih == 4:
        print("Tampilkan atribut protected")
        for data in data_list:
            data.akses_method_protected()
    
    elif pilih == 5:
        print("Tampilkan atribut privat")
        for data in data_list:
            data.akses_method_privat()

    elif pilih == 0:
        print("Terimakasih")
        break

    else:
        print("Anda salah menginputkan")