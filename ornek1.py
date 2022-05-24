#PROJECT EULER 1.SORU
#1000'den küçük olan ve 3'e veya 5'e bölünen bütün sayıların toplamı kaçtır?
def check(x):
    if x % 3 == 0 or x % 5 == 0:
        return True
    else:
        return False

sum = 0

for i in range(1,1000):
    if check(i) == True:
        sum += i

print(sum)

#4.SATIR: Sorulan sayının üçe veya beşe bölünüp bölünmediğini kontrol ediyoruz. 

"""OR KULLANIMI:
Verilen iki durumdan birinin doğru olması yeterlidir.
TRUE or TRUE = TRUE
TRUE or FALSE = TRUE
FALSE or FALSE = FALSE
"""
"""AND KULLANIMI:
Verilen iki durumdan her ikisinin de doğru olması gerekir.
TRUE and TRUE = TRUE
FALSE and TRUE = FALSE
FALSE and FALSE  = FALSE 
"""