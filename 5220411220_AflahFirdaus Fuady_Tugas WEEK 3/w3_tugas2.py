class Pelayan:
    def __init__(self, nama_pelayan, id_pelayan, email_pelayan):
        self.nama_pelayan = nama_pelayan
        self.id_pelayan = id_pelayan
        self.email_pelayan = email_pelayan

    def data_pelayan(self):
        print("Nama Pelayan: ",self.nama_pelayan)
        print("Id Pelayan: ",self.id_pelayan)
        print("Email: ",self.email_pelayan)