def kalkulator():
   print ("""""""""""""""""""""""""""""""""""""")
   print ( "SISTEM KALKULATOR" )
   print ("""""""""""""""""""""""""""""""""""""")
   
   jawab = "y"
   while (jawab == 'y'):
      def penjumblahan(x, y):
         return x + y
      def pengurangan(x, y):
         return x - y
      def perkalian(x, y):
         return x * y
      def pembagian(x, y):
         return x / y
      print("Pilih Operasi.")
      print("1.Jumlah")
      print("2.Kurang")
      print("3.Kali")
      print("4.Bagi")
      kategori = input("Masukkan pilihan(1 OF 4): ")
      num1 = int(input("Masukkan bilangan pertama: "))
      num2 = int(input("Masukkan bilangan kedua: "))
      if kategori == '1':
         print(num1,"+",num2,"=", penjumblahan(num1,num2))
         jawab = input("\nTambah Lagi Data? ")
      elif kategori == '2':
         print(num1,"-",num2,"=", pengurangan(num1,num2))
         jawab = input("\nTambah Lagi Data? ")
      elif kategori == '3':
         print(num1,"*",num2,"=", perkalian(num1,num2))
         jawab = input("\nTambah Lagi Data? ")
      elif kategori == '4':
         print(num1,"/",num2,"=", pembagian(num1,num2))
         jawab = input("\nTambah Lagi Data? ")
      else:
         print("Input salah")
         jawab = input("\nTambah Lagi Data? ")

