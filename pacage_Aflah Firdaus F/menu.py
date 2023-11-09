from w5_1 import UTY
from w5_1 import Student
from w5_1 import Dosen
from w5_1 import Tendik
import os

while True:
    os.system('cls')
    print('Menu Pilihan')
    print('1. Input Data Mahasiswa')
    print('2. Input Data Dosen')
    print('3. Input Data Tendik')
    print('4. Cetak Data Siswa')
    print('5. Cetak Data Dosen')
    print('6. Cetak Data Tendik')
    print('0. Selseai')

    pilih = int(input('Pilih Menu: '))
    if pilih == 1:
        print('Isi Data Mahasiswa')
        a = input('Masukan NPM: ')
        b = input('Masukan Nama: ')
        c = input('Masukan Alamat: ')
        d = input('Masukan Program Studi: ')
        e = int(input('Masukan Angkatan: '))
        f = float(input('Masukan IP: '))
        while f > 4.0 or f <= 0:
            print('IP yang diinputkan tidak sesuai')
            f = float(input('Masukan IP: '))
        mhs1 = Student(a,b,c,d,0,0)
        mhs1.angkatan = e
        mhs1.ip = f

    elif pilih == 2:
        print('Isi Data Dosen')
        a1 = input('Masukan Id: ')
        b1 = input('Masukan Nama: ')
        c1 = input('Masukan Alamat: ')
        d1 = input('Masukan Homebase: ')
        e1 = input('Masukan Keahlian: ')
        f1 = int(input('Masukan Gaji: '))
        while f1 <= 0:
            print('Gaji yang diinputkan tidak sesuai')
            f1 = float(input('Masukan Gaji: '))
        dosen1 = Dosen(a1,b1,c1,d1,e1,0)
        dosen1.gaji = f1
    
    elif pilih == 3:
        print('Isi Data Tendik')
        a2 = input('Masukan Id:')
        b2 = input('Masukan Nama: ')
        c2 = input('Masukan Alamat: ')
        d2 = input('Masukan Unit Kerja: ')
        e2 = input('Masukan Gaji: ')
        tendik1 = Tendik(a2,b2,c2,d2,e2)


    elif pilih == 4:
        print('Cetak Data Mahasiswa')
        mhs1.perkenalan_student()
        mhs1.perkenalan_private_student()
    
    elif pilih == 5:
        print('cetak Data Dosen')
        dosen1.perkenalan_dosen()
        dosen1.perkenalan_dosen_private()

    elif pilih == 6:
        print('Cetak Data Tendik')
        tendik1.perkenalan_tendik()
        tendik1.perkenalan_tendik_private()

    elif pilih == 0:
        print('Terimakasih')
        break

    else:
        print('Anda Salah Pilih Menu')
    print('Tekan[Enter]Untuk Lanjut..')
    os.system('pause')
