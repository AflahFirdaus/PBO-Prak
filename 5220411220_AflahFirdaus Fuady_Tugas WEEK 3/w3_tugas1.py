class Chef:
    def __init__(self, nama_chef, id_chef, email_chef):
        self.nama_chef = nama_chef
        self.id_chef = id_chef
        self.email_chef = email_chef

    def data_chef(self):
        print("Nama Chef",self.nama_chef)
        print("Id Chef",self.id_chef)
        print("Tugas",self.email_chef)
