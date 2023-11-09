class Menu:
    def __init__(self, nama_makanan, harga_makanan, nama_minumam, harga_minimam):
        self.nama_makanan = nama_makanan
        self.harga_makanan = harga_makanan
        self.nama_minumam = nama_minumam
        self.harga_minumam = harga_minimam

    def list_menu(self):
        print("Nama Makanan",self.nama_makanan)
        print("Harga Makanan: ",self.harga_makanan)
        print("Nama Minumam : ",self.nama_minumam)
        print("Harga Minumam: ",self.harga_minumam)