def inputbil():
    bilangan = int(input("masukkan bilangan: "))
    return bilangan
def idr_eur():
    konv = bil//19.348
    print(f"{konv:,.0f}")
def eur_idr():
    konve = bil*19.348
    print(f"{konve:,.3f}")
    
print("1. IDR - EUR")
print("2. EUR - IDR")
pil = input("masukkan pilihan anda: ")
bil = inputbil()
if pil=="1":
    idr_eur()
elif pil=="2":
    eur_idr()
