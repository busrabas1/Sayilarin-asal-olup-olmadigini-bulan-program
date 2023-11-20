x=0
sayi=int(input("sayi giriniz"))
for c in range(2,sayi):
    if sayi % c == 0:
        x=x+1
        break
if x== 0:
    print("sayi asal")
else:
    print("sayi asal değil")
