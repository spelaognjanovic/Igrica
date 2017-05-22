import tkinter as tk

slovenska_abeceda = ['A', 'B', 'C', 'Č', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'T', 'U', 'V', 'Z', 'Ž']


okno = tk.Tk()
okno.resizable(width=False, height=False)#uporabnik ne more spreminjati velikosti okna
okno.geometry('{}x{}'.format(800, 600)) 


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

poteza = 0

#Funkcija, ki nariše vislice
slika = tk.Canvas(okno,width=500,height=800)
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
        slika.create_oval(2,200,22,220)#vneseš 1. in 3. koordinato
    if n == 6:
        slika.create_polygon(11,220,11,270,13,270,13,220)
    if n == 7:
        slika.create_polygon(0,200,0,202,11,237,11,235)
    if n == 8:
        slika.create_polygon(13,235,13,237,28,202,28,200)
    if n == 9:
        slika.create_polygon(0,300,0,302,11,270,11,268)
    if n == 10:
        slika.create_polygon(13,268,13,270,24,302,24,300)
    
slika.pack()

#Funkcija, ki nariše št. črt
def narici_crte(beseda):
    st_crk = len(beseda)
    x = -15
    for i in range(st_crk):
        x+=35
        slika.create_polygon(x,515,x,517,x+20,517,x+20,515)


# Funkcijo. ki vzame kot argument besedo in crko
#in nato izpiše/izriše črke na črto
def izpisi_crko(beseda, crka):
    global poteza #Poeni, da spremenljivka živi
    #zunaj funkcije in ta funkcija jo uporablja
    st_uganjenih =0
    for i in range(len(beseda)):       
        if beseda[i] == crka:
            st_uganjenih +=1
            slika.create_text(30 + i*35, 505, text=crka.upper())
    if st_uganjenih == 0:
        poteza +=1      
        vislice(poteza)
        
class Gumb:
    def  __init__(self,i ,j, okvir, beseda ):#i,j sta koordinati od 1-500
        self.gumb = tk.Button(okvir, text=slovenska_abeceda[5*i + j], command = self.izpisi)
        self.beseda = beseda
        self.i = i #vsak gumb se more zavedat na kateri koordinati je
        self.j= j

    def izpisi(self):
        izpisi_crko(self.beseda,slovenska_abeceda[5*self.i + self.j])#crka je ko klikneš
        #se ko pritisneš da gumb ostane noter stisnjenS
        
        

#gumbi za abecedo          
class Gumbi:
    def __init__:
        
        
    
    
    



postavi_abecedo() #še pokliči funkcijo
nova_igra()

narici_crte('avtomobil')
izpisi_crko('avtomobil', 'a')
izpisi_crko('avtomobil', 'o')
izpisi_crko('avtomobil', 'š')
izpisi_crko('avtomobil', 'đ')


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
        
        
        
        
    


