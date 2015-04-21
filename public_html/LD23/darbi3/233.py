#Fails 231.py
#Autors: Antons Kolesins
from PythonMagick import Image


bilde =Image("33x33", "#00FF00")

# Izveidojam mainigos x un y

#Uzstaada objekta 'bilde' x,y pixela kraasu

bilde.pixelColor( 1,2, "#eeff23")
bilde.pixelColor( 1,3, "#eeff23")
bilde.pixelColor( 1,4, "#eeff23")
bilde.pixelColor( 1,5, "#eeff23")
bilde.pixelColor( 2,1, "#eeff23")
bilde.pixelColor( 3,1, "#eeff23")
bilde.pixelColor( 4,1, "#eeff23")
bilde.pixelColor( 4,3, "#eeff23")
bilde.pixelColor( 5,5, "#eeff23")
bilde.pixelColor( 5,4, "#eeff23")
bilde.pixelColor( 5,3, "#eeff23")
bilde.pixelColor( 5,2, "#eeff23")
bilde.pixelColor( 2,3, "#eeff23")
bilde.pixelColor( 3,3, "#eeff23")



bilde.pixelColor( 7,1, "#eeff23")
bilde.pixelColor( 7,2, "#eeff23")
bilde.pixelColor( 7,3, "#eeff23")
bilde.pixelColor( 7,4, "#eeff23")
bilde.pixelColor( 7,5, "#eeff23")
bilde.pixelColor( 8,3, "#eeff23")
bilde.pixelColor( 9,4, "#eeff23")
bilde.pixelColor( 9,2, "#eeff23")
bilde.pixelColor( 10,1, "#eeff23")
bilde.pixelColor( 10,5, "#eeff23")



bilde.pixelColor( 10,10, "#eeff23")
bilde.pixelColor( 10,11, "#eeff23")
bilde.pixelColor( 10,12, "#eeff23")
bilde.pixelColor( 10,13, "#eeff23")
bilde.pixelColor( 10,14, "#eeff23")
bilde.pixelColor( 13,10, "#eeff23")
bilde.pixelColor( 13,11, "#eeff23")
bilde.pixelColor( 13,12, "#eeff23")
bilde.pixelColor( 13,13, "#eeff23")
bilde.pixelColor( 13,14, "#eeff23")
bilde.pixelColor( 7,14, "#eeff23")
bilde.pixelColor( 8,15 , "#eeff23")
bilde.pixelColor( 9,16, "#eeff23")
bilde.pixelColor( 10,17, "#eeff23")
bilde.pixelColor( 11,17, "#eeff23")
bilde.pixelColor( 12,17, "#eeff23")
bilde.pixelColor( 13,17, "#eeff23")
bilde.pixelColor( 14,16, "#eeff23")
bilde.pixelColor( 15,15, "#eeff23")
bilde.pixelColor( 16,14, "#eeff23")




# 3x3 pixels palielina liidz 200x200
bilde.scale ("500x500")

#Objektu 'bilde' ieraksta failaa
bilde.write("233.png") 



