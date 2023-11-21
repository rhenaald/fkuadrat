#fungsi untuk pengurangan dan pertambahan
def kurang(a,b):
    hasil = a-b
    return hasil
def tambah(a,b):
    hasil = a+b
    return hasil

saldo = 20000000
saldo_terpakai = 0
pin = int(input("masukan pin anda :"))

#input pin jika benar maka program jalan,jika salah program tidak jalan
if pin == 123 :
    print('|===============|')
    print('|  1.indonesia  |')
    print('|   2.iggris    |')
    print("|===============|")
    bahasa = int(input("pilih bahasa :")) #memilih bahasa yang akan digunakan
    if bahasa == 1 :
        pilih_transaksi = 0
        while pilih_transaksi <= 5 : #pengulangan pertama
            print('\n|===============|')
            print('|   1.transfer  |')
            print('| 2.tarik tunai |')
            print('| 3.setor tunai |')
            print('|  4.cek saldo  |')
            print('|    5.keluar   |')
            print("|===============|")
            pilih_transaksi = int(input('Pilih transaksi : '))
            while pilih_transaksi <= 5 : #pengulangan 2 sesuai inputan,jika inputan melebihi batas maka tidak jalan
                if pilih_transaksi == 1 :
                    #fungsi transfer (indonesia)
                    def transfer (saldo,saldo_terpakai):
                        print ("\n ======== Transfer ========")
                        rekening = input("masukan rekening yang dituju : ")
                        nominal = int(input("masukan nominal :"))
                        print ("=================")
                        if nominal < saldo:
                            print("transaksi berhasil")
                            print("rekening tujuan {rekening}")
                            print(f"jumlah transfer {nominal}")
                            print("")
                            print("sisa saldo = ",kurang(saldo,nominal))
                            saldo_terpakai = tambah(saldo_terpakai,nominal)
                            print ("=================")

                        elif nominal > saldo:
                            print ("saldo anda tidak mencukupi")
                            print ("=================")
                        return saldo_terpakai
                    #penggunaan fungsi transfer
                    saldo_terpakai = transfer (saldo,saldo_terpakai)
                    saldo=kurang(saldo,saldo_terpakai)

                elif pilih_transaksi == 2 :
                    #fungsi tarik tunai
                    def tarik (saldo,saldo_terpakai):
                        print ("\n ======== Tarik tunai ========")
                        print ("1. Rp.100.000")
                        print ("2. Rp.300.000")
                        print ("3. Rp.500.000")
                        print ("4. Rp.1.000.000")
                        angka = int(input("pilih nominal 1/2/3/4 : "))
                        if angka == 1 :
                            nominal = 100000
                            if nominal < saldo :
                                print ("transaksi berhasil")
                            else :
                                print ("saldo anda tidak mencukupi")
                        elif angka == 2 :
                            nominal = 300000
                            if nominal < saldo :
                                print ("transaksi berhasil")
                            else :
                                print ("saldo anda tidak mencukupi")
                        elif angka == 3 :
                            nominal = 500000
                            if nominal < saldo :
                                print ("transaksi berhasil")
                            else :
                                print ("saldo anda tidak mencukupi")
                        elif angka == 4 :
                            nominal = 1000000
                            if nominal < saldo :
                                print ("transaksi berhasil")
                            else :
                                print ("saldo anda tidak mencukupi")
                            saldo_terpakai = tambah(saldo_terpakai,nominal)
                            saldo = kurang(saldo,saldo_terpakai)
                        else :
                            print("pilihan tidak tersedia")
                        return saldo_terpakai
                    
                    #penggunaan fungsi tarik tunai
                    saldo_terpakai = tarik (saldo,saldo_terpakai)
                    saldo = kurang(saldo,saldo_terpakai)
                elif pilih_transaksi == 3 :
                    print ("\n ======== setor tunai ========")
                    #fungsi setor tunai
                    def setor(saldo,saldo_terpakai):
                        setor = int(input ("masukan nominal setor tunai : "))
                        if setor >= 0 :
                            saldo = tambah(saldo,setor) 
                            print("setor tunai berhasil")
                            print (f"saldo = {saldo}")
                        else :
                            ('masukan nominal dengan benar')
                        return saldo
                    
                    #penggunaan fungsi setor tunai
                    saldo = setor(saldo,saldo_terpakai)
                elif pilih_transaksi == 4 :
                    print ("\n ======== saldo ========")
                    print (saldo)
                elif pilih_transaksi == 5 :
                    pilih_transaksi = 6

                #pengkondisian untuk melakukan transaksi lagi atau tidak
                lagi = input ("\nlakukan transaksi lagi?(y/n):")  
                if lagi == "y":
                    break #break memberhentikan pengulangan ked-2,dan kembali ke pengulangan yang ke-1
                elif lagi == "n":
                    pilih_transaksi = 7
                
    if bahasa == 2 :
        pilih_transaksi = 0
        while pilih_transaksi <= 5 : #pengulangan pertama
            print('\n|==================|')
            print('|   1.transfer      |')
            print('| 2.cash withdrawal |')
            print('|     3.deposit     |')
            print('|  4.balance check  |')
            print('|      5.exit       |')
            print("|===================|")
            pilih_transaksi = int(input('select transaction : '))
            while pilih_transaksi <= 5 : #pengulangan 2 sesuai inputan,jika inputan melebihi batas maka tidak jalan
                if pilih_transaksi == 1 :
                    print ("\n ======== Transfer ========")
                    #fungsi transfer -inggris
                    def transfer2 (saldo,saldo_terpakai):
                        rekening = input("Enter the intended account : ")
                        nominal = int(input("input nominal :"))
                        print ("=================")
                        if nominal < saldo:
                            print("Successful transaction")
                            print("Destination Account {rekening}")
                            print(f"Transfer amount {nominal}")
                            print("")
                            print("Remaining balance = ",kurang(saldo,nominal))
                            saldo_terpakai = tambah(saldo_terpakai,nominal)
                            
                            print ("=================")

                        elif nominal > saldo:
                            print ("Your balance is insufficient")
                            print ("=================")
                        return saldo_terpakai
                    
                    #penggunaan fungsi transfer inggris
                    saldo_terpakai = transfer2(saldo,saldo_terpakai)
                    saldo = kurang(saldo,saldo_terpakai)

                elif pilih_transaksi == 2 :
                    print ("\n ======== Cash withdrawl ========")
                    #fungsi withdrawl 
                    def withdrawal(saldo,saldo_terpakai):
                        print ("1. Rp.100.000")
                        print ("2. Rp.300.000")
                        print ("3. Rp.500.000")
                        print ("4. Rp.1.000.000")
                        angka = int(input("sellect nominal 1/2/3/4 : "))
                        if angka == 1 :
                            nominal = 100000
                            if nominal < saldo :
                                print ("Successful transaction")
                            else :
                                print ("Your balance is insufficient")
                        elif angka == 2 :
                            nominal = 300000
                            if nominal < saldo :
                                print ("Successful transaction")
                            else :
                                print ("Your balance is insufficient")
                        elif angka == 3 :
                            nominal = 500000
                            if nominal < saldo :
                                print ("Successful transaction")
                            else :
                                print ("Your balance is insufficient")
                        elif angka == 4 :
                            nominal = 1000000
                            if nominal < saldo :
                                print ("Successful transaction")
                            else :
                                print ("Your balance is insufficient")
                        else :
                            print("option is not available")
                        saldo_terpakai = tambah(saldo_terpakai,nominal)
                        return saldo_terpakai
                    
                    #penggunaan fungsi withdrawl
                    saldo_terpakai = withdrawal(saldo,saldo_terpakai)
                    saldo = kurang(saldo,saldo_terpakai)

                elif pilih_transaksi == 3 :
                    print ("\n ======== Deposit ========")
                    #fungsi deposit
                    def deposit (saldo) :
                        setor = int(input ("input the cash deposit amount : "))
                        if setor >= 0 :
                            saldo = tambah(saldo,setor) 
                            print("succesful cash deposit")
                            print (f"balance = {saldo}")
                        else :
                            ('input the nominal correctly')
                        return saldo
                    #penggunaan fungsi deposit
                    saldo = deposit (saldo)
                elif pilih_transaksi == 4 :
                    print ("\n ======== balance ========")
                    print (f"balance = {saldo}")

                elif pilih_transaksi == 5 :
                    pilih_transaksi = 6
                
                lagi = input ("\nmake another transaction?(y/n):")  
                if lagi == "y":
                    break
                elif lagi == "n":
                    pilih_transaksi = 7
    