
def penggajian() :
    from texttable import Texttable
    table = Texttable ()
    no = 0
    nama = []
    jabatan = []
    gaji = []
    jawab = "y"

    print ("""""""""""""""""""""""""""""""""""""")
    print ( "SISTEM PENGGAJIAN" )
    print ("""""""""""""""""""""""""""""""""""""")  

    while (jawab == 'y'):
        nama.append(input("Masukan Nama: "))
        jab = input("Jabatan : ")
        jabatan.append(jab)
        if  (jab == 'Guru') :
            gaji.append(300000)
            jawab = input("\nTambah Lagi Data? ")
            
        elif (jab == 'Admin') :
            gaji.append(200000)
            jawab = input("\nTambah Lagi Data? ")
            
        elif (jab == 'Satpam') :
            gaji.append(500000)
            jawab = input("\nTambah Lagi Data : ")
            
        else:
            print("Pekerjaan yang dicari tidak ditemukan")
            jawab = input("\nTambah Lagi Data : ")
        no += 1
  
    for i in range (no):
            table.add_rows([['No','Nama','Jabatan','Gaji'],
                            [i+1, nama[i],jabatan[i],gaji[i]]])                      
    print(table.draw())

