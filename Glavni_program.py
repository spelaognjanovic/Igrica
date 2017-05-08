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
        
    
    turtle.pu()


#Funkcija, ki nariše toliko črt kot ima beseda dolžino
#(x1,y1) Začetna pozicija črt
# d- dolžina ene črte
#Funkcija dobi dvignjen kuli in pusti dvignjenega

def crte(n, x1, y1, d):
    for i in range(n): # naredimo n korakov od 0 do n-1
        turtle.goto(x1, y1)
        turtle.pd()
        turtle.seth(0)
        turtle.forward(d)
        turtle.pu()
        x1 += d+20

#Naslednjic kar se je treba lotit je risanje crk..
#na i-to mesto ti nariše znak
#def risi_scrko(znak, i, x1, y1, d) i-indeks kero crko risemo..
        
        
        
        
    


