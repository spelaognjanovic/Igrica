import tkinter as tk

slovenska_abeceda = ['A', 'B', 'C', 'Č', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'T', 'U', 'V', 'Z', 'Ž']


okno = tk.Tk()
okno.resizable(width=False, height=False)#uporabnik ne more spreminjati velikosti okna
okno.geometry('{}x{}'.format(800, 600)) 


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
def narisi_crte(beseda):
    st_crk = len(beseda)
    x = -15
    for i in range(st_crk):
        x+=35
        slika.create_polygon(x,515,x,517,x+20,517,x+20,515)


# Funkcijo. ki vzame kot argument besedo in crko
#in nato izpiše/izriše črke na črto
def izpisi_crko(beseda, crka):
    global poteza #Pomeni, da spremenljivka živi
    #zunaj funkcije in ta funkcija jo uporablja
    st_uganjenih =0
    print(beseda)
    print(crka)
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
        self.gumb.grid(row = i, column = j)

    def izpisi(self):
        izpisi_crko(self.beseda,slovenska_abeceda[5*self.i + self.j])#crka je ko klikneš
        #se ko pritisneš da gumb ostane noter stisnjen
        
        

#gumbi za abecedo          
class Gumbi:
    def __init__(self,okno, beseda):
        self.okvir = tk.Frame(okno)
        seznam_gumbov = []
        for i in range(5):
            for j in range(5):
                seznam_gumbov.append(Gumb(i,j,self.okvir,beseda))
        self.okvir.place(relx=0.7, rely=0.4)
        
        
    
    
    



 #še pokliči funkcijo

nova_igra()
gumbi = Gumbi(okno,'AVTOMOBIL')
narisi_crte('AVTOMOBIL')




tk.mainloop()
    



#https://www.tutorialspoint.com/python/tk_button.htm

        
        
        
        
    


