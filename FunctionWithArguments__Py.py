#Fungsi dengan argumen sederhana
def Siswa(Nama):
    print("Siswa ini bernama : ", Nama)

Siswa('Rizky Khapidsyah')

#Fungsi dengan menggunakan keywords arguments
def Guru(Nama, Pelajaran):
    print("Guru ini bernama    : ", Nama)
    print("Mengajar Pelajaran  : ", Pelajaran)

Guru('Rizky Khapidsyah', 'Pemrograman')
Guru(Nama = 'Rizky Khapidsyah', Pelajaran = 'Dasar-Dasar Pemrograman')

#Fungsi dengan menggunakan default arguments
def PenjagaSekolah(Nama, Shift = 'Malam', Galak = 'Tidak'):
    print('Penjaga Sekolah ini bernama   : ', Nama)
    print('Shift Jam Kerja               : ', Shift)
    print('Galak?                        :', Galak)

PenjagaSekolah('Rusdi')
PenjagaSekolah('Mawar', Shift = 'Siang')
PenjagaSekolah('Mesem', Galak = 'Iya')
PenjagaSekolah(Shift = 'Malam', Galak = 'Iya') #Akan Menghasilkan error karena tidak terisi nya parameter Nama (wajib) pada function, sementara dua parameter lainnya (Shift dan Galak) hanya opsional (boleh diisi boleh tidak)

#NB: Untuk menjalankan program, silahkan beri tanda comment (#) pada awal baris terakhir. Baris terakhir sengaja dibuat error agar mudah dipahami penyebabnya.