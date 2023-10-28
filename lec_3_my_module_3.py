from lec_3_my_module_0 import earth_mass as em
from lec_3_my_module import gravity_constant as G
from lec_3_my_module_1 import sigma_steff_bolc as sigma
 
g = 500 * G / 10**2
print(g)
 
x = em * G * sigma
print(x)