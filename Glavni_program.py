import tkinter as tk

slovenska_abeceda = ['A', 'B', 'C', 'Č', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'T', 'U', 'V', 'Z', 'Ž']


okno = tk.Tk()
okno.resizable(width=False, height=False)#uporabnik ne more spreminjati velikosti okna
okno.geometry('{}x{}'.format(700, 500)) 


#Funkcija,ki bo postavila gumbe
def postavi_abecedo():  
    gumbi = tk.Frame(okno) #okvir za vseh 25 gumbov #frame navidezno polje
    
    for i in range(5):
        for j in range(5):
            gumb = tk.Button(gumbi, text=slovenska_abeceda[5*i + j])
            gumb.grid(row = i, column = j)
    gumbi.place(relx=0.7, rely=0.4)


#Še Gumb za začetek nove igre          
def nova_igra():
    gumb_nov_zacetek = tk.Button(okno, text='Nova igra')
    gumb_nov_zacetek.place(relx=0.73, rely=0.3)



#Funkcija, ki nariše vislice
slika = tk.Canvas(okno,width=400,height=500)
def vislice(n): #n bo najvec 10, torej 10 možnosti za ugib črk, drugače se izrišejo vislice
    if n == 1:
        slika.create_polygon(50,305,50,310,150,310,150,305)
    if n == 2:
        slika.create_polygon(100,180,100,310,105,310,105,180)
    if n == 3:
        slika.create_polygon(10,175,10,180,105,180,105,175)
    if n == 4:
        slika.create_polygon(5,175,5,200,10,200,10,175)
    if n == 5:
        slika.create_oval(2,200,25,225)#vneseš 1. in 3. koordinato


    
slika.pack()

#Funkcija, ki presteje stevilo crk v besedi
#def st_crk(beseda): #lahko še narandom izberemo besedo
    #st_crk = beseda.count

#Funkcija, ki nariše št. črt
#def narici_crte(st_crk):
    

postavi_abecedo() #še pokliči funkcijo
nova_igra()
vislice(1)
vislice(2)
vislice(3)
vislice(4)
vislice(5)
tk.mainloop()
    




#https://www.tutorialspoint.com/python/tk_button.htm

#import turtle

# Funkcija, ki nariše n-ti korak vislic, kjer je n med 1 in 11.
#Kordinate nožišča vislic so točno (x0,y0).
#Funkcija dobi dvignjen kuli in ga tudi na koncu pusti dvignjenga.

#def vislice(n,x0,y0):
 #   if n == 1:
  #      turtle.goto(x0-20, y0)
   #     turtle.pd()
    #    turtle.seth(0)
     #   turtle.forward(40)
    #elif n == 2:
     #   turtle.goto(x0,y0)
      #  turtle.seth(90)
       # turtle.pd()
        #turtle.forward(200)
        
    
   # turtle.pu()


#Funkcija, ki nariše toliko črt kot ima beseda dolžino
#(x1,y1) Začetna pozicija črt
# d- dolžina ene črte
#Funkcija dobi dvignjen kuli in pusti dvignjenega

#def crte(n, x1, y1, d):
 #   for i in range(n): # naredimo n korakov od 0 do n-1
  #      turtle.goto(x1, y1)
   #     turtle.pd()
    #    turtle.seth(0)
     #   turtle.forward(d)
      #  turtle.pu()
       # x1 += d+20

#Naslednjic kar se je treba lotit je risanje crk..
#na i-to mesto ti nariše znak
#def risi_scrko(znak, i, x1, y1, d) i-indeks kero crko risemo..
        
        
        
        
    


