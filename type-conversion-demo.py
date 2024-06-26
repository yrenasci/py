#2.gün float-str-hesaplama-veri

"""
daire alanı : πr²
daire çevresi : 2πr
* yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız 
(r : 3.14)
"""
"""pi = 3.14
r = float(input("yarı çap :")) #yarıçap
alan = pi * (r ** 2)
cevre = 2 * pi * r

print("alan" , alan)
print("çevre:" , cevre)""" #örnekti tekrar yapacağım

pi = 3.14
r = float(input("yarı çap: "))
alan = pi * (r ** 2)
print(type(alan))

cevre = 2 * pi * r
print(type(cevre))

"""print("alan:", alan)
print("çevre:", cevre)

"""
print("alan: "+ str(alan) + "çevre: "+ str(cevre))

