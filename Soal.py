teks = open("Data.txt", mode="r") #membuka file teks dengan mode read

list_teks = teks.readlines()  #menjadikan variabel sebagai program list
list_teks.insert(2, 'Matakuliah favoritnya addalah "Algo"\n') #Menyelipkan string ke dalam index 2

teks = open("Data.txt", mode="w") #membuka file teks dengan mode write
for t in list_teks: #menjadikan "t" sebagai variabel yang suda ada dalam  variabel list_teks
    teks.write(t) #kemudian methode write digunakan untuk menuliskan list pada variabel list_teks ke dalam file
    
teks.close() #menutup sesi dari file