a = input ("Digite um valor para o cateto a:")
a = float (a)
b = input ("Digite um valor para o cateto b:")
b = float (b)

import math

hipotenusa = math.sqrt (a**2 + b**2)

print ("A hipotenusa é:" , hipotenusa)