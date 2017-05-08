import turtle

# Funkcija, ki nariše n-ti korak vislic, kjer je n med 1 in 11.
#Kordinate nožišča vislic so točno (x0,y0).
#Funkcija dobi dvignjen kuli in ga tudi na koncu pusti dvignjenga.

def vislice(n,x0,y0):
    if n == 1:
        turtle.goto(x0-20, y0)
        turtle.pd()
        turtle.seth(0)
        turtle.forward(40)
    elif n == 2:
        turtle.goto(x0,y0)
        turtle.seth(90)
        turtle.pd()
        turtle.forward(200)
    elif n == 3:
        

    
    turtle.pu()


