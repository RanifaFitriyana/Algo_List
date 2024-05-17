import exercase

while True:
    exercase.tampilan() 
    print("================================================")
    pilihan = input("Masukkan pilihan anda : ")
    print("================================================")

    if pilihan == '1':
        exercase.tambah_data()
    elif pilihan == '2':
        exercase.hapus_data()
    elif pilihan == '3':
        exercase.tampil_data()