from Kalkulator import kalkulator
from Gajian import penggajian
from Nilai import inputnilai
from Pembayaran import pembayaran2
import getpass


def iduser():
    
    print("""""""""""""""""""""""""""""""""""""""""""")
    print("SILAKAN LOGIN USER PROGRAM DASHBOARD ANDA")
    print("""""""""""""""""""""""""""""""""""""""""""")
    user = input("username :")
    passw = getpass.getpass("Masukan Sandi :")
    if  user=="tomi" and passw == "123":
        print("Anda Telah Login" )
    else:
        print( "Username atau Password Anda Salah" )
        exit()
iduser()
def start():
    
    print("""""""""""""""""""""""""""""""""""""")
    print("SELAMAT DATANG DI PROGRAM DATA DASHBOARD")
    print("""""""""""""""""""""""""""""""""""""") 
    print("FORM DAHSBOARD")
    print("A. PENILAIAN")
    print("B. GAJI")
    print("C. PEMBAYARAN")
    print("D. KAKULATOR")
    pilih = input ("\n Silakan Pilih Data Dashboard : ")
    if   pilih == 'B' :
         penggajian()
    elif pilih == 'A' :
         inputnilai()
    elif pilih == 'C' :
         pembayaran2()
    elif pilih == 'D' :
         kalkulator()     
    else :
        print ("Data yang diminta tidak ditemukan")
    tambahan()
    
def tambahan() :
    
    tambah = input ("Kembali Ke Dahsboard (y/t)? ")
    if tambah == 'y' :
        start()
    else :
        import Akhir
start()
    
