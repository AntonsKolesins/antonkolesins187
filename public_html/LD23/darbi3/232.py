#Fails 231.py
#Autors: Antons Kolesins
from PythonMagick import Image


bilde =Image("16x16", "#00FF00")

# Izveidojam mainigos x un y
x=y=0
#Uzstaada objekta 'bilde' x,y pixela kraasu
bilde.pixelColor( x,y, "#eeff22")

# 3x3 pixels palielina liidz 200x200
bilde.scale ("200x200")

#Objektu 'bilde' ieraksta failaa
bilde.write("232.png")
