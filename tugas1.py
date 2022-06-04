import psycopg2
import os

def show_menu():
    os.system('clear')
    print(" aplikasi pengiriman invoice")
    print(" tekan 1 ")
    print(" tekan 2")
    print(" tekan3")
    select_menu = int(input("masukan angka"))

    connection = psycopg2.connect(user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
    database="bigdatacilsy")

    cur = connection.cursor()
    if select_menu == 1:
        a = '''SELECT "invoiceID" from awal_tahun'''
        cur.execute(a)
        awal_tahun = cur.fetchall()
        for hasil in awal_tahun:
            print("terima kasih telah melakukan pembayaran pada invoice "+hasil[0])
    elif (select_menu == 2):
        a = '''SELECT "invoiceID" from akhir_tahun'''
        cur.execute(a)
        akhir = cur.fetchall()
        for hasil in akhir:
            print("terima kasih telah melakukan pembayaran pada invoice"+hasil[0])
    elif (select_menu == 3):
        a = '''SELECT "invoiceID" from belum'''
        cur.execute(a)
        awal_tahun = cur.fetchall()
        for hasil in awal_tahun:
            print("terima kasih telah melakukan pembayaran pada invoice"+hasil[0])
    elif (select_menu==0):
        exit()
def back():
    show_menu() 

if __name__== '__main__':
    show_menu()