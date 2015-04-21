#Fails 231.py
#Autors: Antons Kolesins
from PythonMagick import Image


img = open ( "sun.jpg")

# Izveidojam mainigos x un y

#Uzstaada objekta 'bilde' x,y pixela kraasu

img[0].size[1]    # resolution x
img[0].size[2]


img.scale ("300x300")

#Objektu 'bilde' ieraksta failaa
img.write("999.png") 



