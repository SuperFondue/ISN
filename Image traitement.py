import os
from PIL import Image

#Vérification
rep_cour=os.getcwd()
if rep_cour!="C:\Documents and Settings\Administrateur\Bureau\ISN/trait_img":
    
    os.chdir("C:\Documents and Settings\Administrateur\Bureau\ISN/trait_img")
    print(os.getcwd())

print("Tout est en ordre!")

#Paramètres de l'image + son affichage
nom_image=("img_base.pgm")
img_in=Image.open(nom_image)
print("Nom de l'image :",nom_image)
print("Format de l'image :",img_in.format)
print("Taille de l'image :",img_in.size)
print("Mode de l'image :",img_in.mode)
#img_in.show()

#Création d'une copie nb
taille=img_in.size
col=taille[0]
lgn=taille[1]

img_out=Image.new(img_in.mode,img_in.size)
y=0
x=0
while (x<col):
    while(y<lgn):
        p=img_in.getpixel((x,y))
        if p<175:
            img_out.putpixel((x,y),p)
        else:
             img_out.putpixel((x,y),255)
        y=y+1
        p=0
    y=0
    x=x+1

nom_copie_image=("img_copie.pgm")

img_out.save(nom_copie_image)
img_in_1=Image.open(nom_copie_image)
#img_in_1.show()



#Création d'une copie négatif
img_out=Image.new(img_in.mode,img_in.size)
y=0
x=0
while (x<col):
    while(y<lgn):
        p=img_in.getpixel((x,y))
        p=255-p
        img_out.putpixel((x,y),p)
        y=y+1
        p=0
    y=0
    x=x+1

nom_copie_image=("img_copie_negatif.pgm")

img_out.save(nom_copie_image)
img_in_2=Image.open(nom_copie_image)
#img_in_2.show()



#Création d'une copie réduction
img_out=Image.new(img_in.mode,(int(col/2)+1,int(lgn/2)+1))
y=0
x=0
y1=0
x1=0

while (x<col):
    while(y<lgn):
        p=img_in.getpixel((x,y))
        img_out.putpixel((x1,y1),p)
        y=y+2
        y1=y1+1
        p=0
    y1=0
    y=0
    x1=x1+1
    x=x+2

nom_copie_image=("img_copie_reduc.pgm")

img_out.save(nom_copie_image)
img_in_3=Image.open(nom_copie_image)
#img_in_3.show()



#Création d'une copie réduction
img_out=Image.new(img_in.mode,img_in.size)
y=0
x=0
y1=0
x1=0

while (x<col):
    while(y<lgn):
        p=img_in.getpixel((x,y))
        img_out.putpixel((x1+int(col/2),y1),p)
        img_out.putpixel((x1,y1+int(lgn/2)),p)
        img_out.putpixel((x1,y1),p)
        img_out.putpixel((x1+int(col/2),y1+int(lgn/2)),p)
        y=y+2
        y1=y1+1
        p=0
    y1=0
    y=0
    x1=x1+1
    x=x+2

nom_copie_image=("img_copie_photomaton.pgm")

img_out.save(nom_copie_image)
img_in_4=Image.open(nom_copie_image)
#img_in_4.show()



#Création d'une copie effet de bord
img_out=Image.new(img_in.mode,img_in.size)
y=1
x=1

while (x<col-1):
    while(y<lgn-1):
        b=img_in.getpixel((x+1,y),p)
        c=img_in.getpixel((x,y+1),p)
        d=img_in.getpixel((x-1,y),p)
        e=img_in.getpixel((x,y-1),p)

        t=((b-d)**2+(c-e)**2)**0.5

        if t>25:
            p=255
        else:
            p=0

        b=img_out.putpixel((x,y),p)
        
        y=y+1
        p=0
    y=0
    x=x+1

nom_copie_image=("img_copie_effetbord.pgm")

img_out.save(nom_copie_image)
img_in_5=Image.open(nom_copie_image)
img_in_5.show()
