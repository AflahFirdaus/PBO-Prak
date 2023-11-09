class UTY:
    def __init__(self, id , nama, alamat):
        self._id = id
        self.nama = nama
        self.alamat = alamat

    def perkenalan(self):
        print('Perkenalkan Nama Saya', self.nama,'alamat di', self.alamat)

class Student(UTY):
    def __init__(self, id, nama, alamat, prodi, angkatan, ip):
        super().__init__(id, nama, alamat)
        self.prodi = prodi
        self._angkatan = angkatan
        self.__ip = ip

    @property
    def angkatan(self):
        return self._angkatan
    
    @angkatan.setter
    def angkatan(self, y):
        if (y < 2017):
            y = 2017
        elif (y > 2023):
            y = 2023
        else:
            self._angkatan = y
    
    @property
    def ip(self):
        return self.__ip
    
    @ip.setter
    def ip(self, y):
        if (y > 4.0):
            self.__ip = 4.0
            print('IP tidak Bisa lebih dari 4.0')

        elif (y < 0):
            self.__ip = 0
            print('IP Tidak Bisa Negatif')

        else:
            self.__ip = y

    def perkenalan_student(self):
        self.perkenalan()
        print('Saya berasal dari prodi', self.prodi,'angkatan', self.angkatan)

    def perkenalan_private_student(self):
        self.perkenalan
        print('Ip saya saat ini',self.__ip)

class Dosen(UTY):
    def __init__(self, id, nama, alamat, homebase, keahlian, gaji):
        super().__init__(id, nama, alamat)
        self.homebase = homebase
        self.keahlian = keahlian
        self.__gaji = gaji
        
    @property
    def gaji(self, y):
        return self.__gaji
    
    @gaji.setter
    def gaji(self, y):
        if (y < 0):
            print('Input Gaji Salah')

        else:
            self.__gaji = y


    def perkenalan_dosen(self):
        self.perkenalan()
        print('Nama ',self.nama,'Alamat ',self.alamat,'Homebase ',self.homebase,'Keahlian ', self.keahlian,)

    def perkenalan_dosen_private(self):
        self.perkenalan
        print('Gaji ',self.__gaji)


class Tendik(UTY):
    def __init__(self, id, nama, alamat, unitKerja, gaji):
        super().__init__(id, nama, alamat)
        self.unitKerja = unitKerja
        self.__gaji = gaji

    def perkenalan_tendik(self):
        self.perkenalan()
        print('Nama ',self.nama,'Alamat ',self.alamat,'Unit Kerja ',self.unitKerja)

    def perkenalan_tendik_private(self):
        self.perkenalan
        print('Gaji ',self.__gaji)