#PROJECT EULER 2.SORU 1.ÇÖZÜM
#4 milyondan küçük ve çift olan fibonacci sayılarının toplamı kaçtır?

fibonacci = list()

fibonacci.append(1)
fibonacci.append(2)

i = 2 

while True:
    if fibonacci[i-1] + fibonacci[i-2] < 4000000:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        i += 1
    else:
        break

sum = 0
for i in fibonacci:
    if i % 2 == 0:
       sum += 1

print(sum)

#6-7: listenin ilk iki elemanını listeye ekledik
#i'yi 2'den başlattık çünkü altıncı ve yedinci satırdan sıfırıncı ve birinci elemanı ekledik.
"""
listelerde eleman sayımı sıfır ile başlar.
ornek = [elma, armut, portakal]
0.eleman => elma
1.eleman => armut 
2.eleman => portakal

"""

#CONTİNUE ifadesi döngü içerisinde kullanıldığında ilgili koşul işletilmeden bir sonraki duruma geçilir
"""
CONTİNUE:
list = [1, 2, 3, 4, 5, 6] 

for i in liste:
     if İ == 4:
        continue
     
     print(i)
SONUÇ: 
1
2
3
5
6
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