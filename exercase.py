barang = []

def tampilan():
    print("Selamat Datang di Program Manajemen Stok Barang!")
    print("Pilihan :")
    print("1. Tambah data barang")
    print("2. Hapus data barang")
    print("3. Tampilkan data barang")
    print("4. Keluar")
  

def tambah_data():
    nama = str(input("Masukkan Nama Barang : "))
    stok = int(input("Masukkan Stok Barang : "))
    barang_new = {'nama' : nama, 'stok' : stok}
    barang.append(barang_new)
    print("---------- Data Berhasil Ditambahkan ----------")
    print("\n")

def hapus_data():
    hapus = int(input("Hapus Data Index Ke = "))
    barang.pop(hapus) 
    print("----------- Data Berhasil Dihapus ------------")
    print("\n")

def tampil_data():
    print("\n------------------ Data Barang ------------------")
    for i in barang:
        print('-',i['nama'],'--> Stok : ',i['stok'])
    print("-------------------------------------------------")
    print("\n")



     