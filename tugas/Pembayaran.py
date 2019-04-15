from texttable import Texttable
def pembayaran2():
    table= Texttable ()
    jawab1 = "y"
    no=0
    name=[]
    nim=[]
    kelas=[]
    membayar_semester=[]
    membayar_seminar=[]
    membayar_kas=[]
    membayar_uts=[]
    membayar_uas=[]
    admin=[]
    
    
    print ("""""""""""""""""""""""""""""""""""""")
    print ( "JALUR PEMBAYARAN UAS & UTS " )
    print ("""""""""""""""""""""""""""""""""""""")  
    
    while(jawab1 == "y"):
        nama=(input("Masukan Nama  : "))
        nim=(input("Masukan NIM   : "))
        kelas=(input("Masukan Kelas: "))
        pilih = (input("Apakah anda ingin membayar semester (y/t) ? "))
        if pilih == 'y':
            membayar_semester =int(input("untuk berapa bulan ? "))
            d_membayar_semester = 'membayar_SEMESTER'
            membayar_semester=550000*membayar_semester
        else :
            sem_ = ''
            sem=0   
        pilih = (input("ingin membayar UTS (y/t) ? "))
        if  pilih == 'y':
            membayar_uts =int(input("untuk berapa bulan ? "))
            d_membayar_uts  = 'membayar_UTS'
            membayar_uts=300000*membayar_uts
        else :
            membayar_uts_ = ''
            membayar_uts=0          
        pilih = (input("ingin membayar UAS (y/t) ? "))
        if  pilih == 'y':
            membayar_uas =int(input("untuk berapa bulan ? "))
            d_membayar_uas  = 'membayar_UAS'
            membayar_uas=200000*membayar_uas
        else :
            membayar_uas_ = ''
            membayar_uas=0      
        pilih = (input("ingin membayar seminar sebesar 150000 (y/t) ? "))
        if  pilih == 'y':
            membayar_seminar  = 'membayar_seminar'
            membayar_seminar=150000
        else :
            membayar_seminar = ''
            membayar_seminar=0
        pilih = (input("ingin bayar KAS Bulanan sebesar 25000 (y/t) ? "))
        if  pilih == 'y':
            membayar_kas  = 'membayar_KAS'
            membayar_kas=25000
        else :
            membayar_kas = ''
            membayar_kas=0
        pilih = (input("Anda akan dikenakan admin sebesar 10000 (y/t) ? "))
        if  pilih == 'y':
            admin  = 'ADMIN'
            admin=10000
        else :
            admin = ''
            admin=0

        total_bayar = membayar_semester+membayar_seminar+membayar_kas+membayar_uts+membayar_uas+admin
        table.add_rows([['NAMA','NIM','KELAS','SEMESTER','SEMINAR','KAS','UTS','UAS','TOTAL'],
                        [nama ,nim ,kelas ,membayar_semester , membayar_seminar  ,  membayar_kas  , membayar_uts  , membayar_uas,total_bayar  ]])
        print("")
        print("")
        print("")
        print("Total Rincian Yang Dibayar")     
        print (table.draw())
        jawab1 = input("\n  Tambahkan Data Pembayaran (y/t)? ") ; print("")
