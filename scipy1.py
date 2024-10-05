
# Math Constants

from pyparsing import alphas
from scipy.constants import pi, golden_ratio

print(f'\nPi: {pi}')
print(f'\nGolden ration: {golden_ratio}')

# Physical constants

from scipy.constants import m_n, Avogadro

print(f'\nMass of Neutron: {m_n}')
print(f'\nAvogadros Number: {Avogadro}')

from scipy.constants import physical_constants

print(f'\nAlpha Particle Mass: {physical_constants["alpha particle mass"]}') 

# # Printing all a-z Physical constants 
# for key,value in physical_constants.items():
#     print(f'{key} : {value}')


from scipy.constants import kilo

print(f'\nKilo: {kilo}')