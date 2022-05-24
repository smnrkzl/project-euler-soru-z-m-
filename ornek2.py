#PROJECT EULER 2.SORU 2.ÇÖZÜM
#4 milyondan küçük ve çift olan fibonacci sayılarının toplamı kaçtır?

a = 1
b = 2

sum = 2
while True:
    c = a + b
    a = b
    b = c

    if c % 2 == 0:
        sum += c
    
    if c > 4000000:
        break

print(sum)


#WHİLE DÖNGÜSÜNÜN ÇÖZÜMÜ
"""
11.SATIR: a = 1 ve b = 2 olduğu için 11.satırdaki işlemin sonucu 3 olacak ve a = b , b = c olduğu için a ve b sayıları dört milyona kadar artmaya devam edecek.
a = 1 , b = 2, c = 3
a = 2 , b = 3 , c = 5
a = 3 , b = 5 , c = 8
9.SATIR : sum = 2 dememizin sebebi ise soruda da belirttiğimiz gibi çift olan sayıların toplamı istenmişti bizden ve ilk tanımladığımız sayılardan da sadece 2 çift sayı olduğu için toplamı 2'den başlattık.
15.SATIR: 2 ile bölümü sonucunda kalanı sıfır olan yani çift olan sayıları bulmaya çalışıyoruz bu if yapısında.
18.SATIR: Soruda bizden 4000000'dan küçük sayılar istenmişti. Bu satırdaki if yapısında da c sayısının 4000000'dan büyük olduğunda döngünün durmasını istiyoruz. Bu durumda c, 4000000 sayısını geçmemiş oluyor.
"""
#BREAK ifadesi döngüyü sonlandırır
"""
BREAK:
list = [1, 2, 3, 4, 5, 6] 

for i in liste:
     if i == 3:
        break    
     print(i)
SONUÇ:
1
2

"""



