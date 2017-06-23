import tkinter as tk

slovenska_abeceda = ['A', 'B', 'C', 'Č', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'Š', 'T', 'U', 'V', 'Z', 'Ž']
        
        
    
        
import random
def izberi_besedo():
    sez =[]
    beseda = ''
    with open('besednjak.txt') as dat:
        for vrstica in dat:
            if vrstica != '' and vrstica[-1] == '\n':
                vrstica = vrstica[:-1]
            if vrstica != '':
                sez.append(vrstica)
        beseda = random.choice(sez)
    return beseda               
        
class Gumb:
    def  __init__(self,okno,i,j):#i,j sta koordinati od 1-5
        self.gumb = tk.Button(okno,text=slovenska_abeceda[5*i + j])
        self.gumb.configure(width = 2, height = 1) #font = tkFont.Font(family='Arial', size=36, weight='bold'))
        self.gumb.place(x = 300 + 30*i,y= 50+ 30*j)
        self.i = i
        self.j = j

    def nastavi(self,beseda): #vsi gumbi rabijo poznat besedo
        self.beseda = beseda
        self.gumb.configure(command = self.izpisi)

    def izpisi(self):
        igra.izpisi_crko(slovenska_abeceda[5*self.i + self.j])
        self.gumb.configure(state="disabled")
                       

class Vislice:
    def __init__(self,okno):
        self.slika = tk.Canvas(okno,width=500,height=800)
        self.slika.place(x=-40, y=-120)
        self.gumb_nov_zacetek = tk.Button(okno, text='Nova igra',command=self.nova_igra)
        self.gumb_nov_zacetek.place(x=300, y=250)
        self.gumb_nov_zacetek.configure(width=20)
        self.seznam_gumbov = []
        for i in range(5):
            for j in range(5):
                self.seznam_gumbov.append(Gumb(okno,i,j))
        self.aktivno = False
            
    def vislice(self,n): #n bo najvec 10
        if n == 1:
            self.slika.create_polygon(150,305,150,310,250,310,250,305,fill='brown')
        if n == 2:
            self.slika.create_polygon(200,180,200,310,205,310,205,180,fill='brown')
        if n == 3:
            self.slika.create_polygon(115,175,115,180,205,180,205,175,fill='brown')
        if n == 4:
            self.slika.create_polygon(110,175,110,200,115,200,115,175,fill='brown')
        if n == 5:
            self.slika.create_oval(101,200,123,220,fill='yellow')#vneseš 1. in 3. koordinato
        if n == 6:
            self.slika.create_polygon(103,222,103,260,122,260,122,222,fill='red')
        if n == 7:
            self.slika.create_polygon(103,222,75,228,80,238,103,235,fill='red')
            x=224
            self.slika.create_polygon(x-103,222,x-75,228,x-80,238,x-103,235,fill='red')
        if n == 8:
            self.slika.create_polygon(103,260,95,300,108,300,118,260,fill='blue')
            x=224
            self.slika.create_polygon(x-103,260,x-95,300,x-108,300,x-118,260,fill='blue')

            
    def narisi_crte(self):
        st_crk = len(self.beseda)
        x = 50
        for i in range(st_crk):
            x+=35
            self.slika.create_polygon(x,515,x,517,x+20,517,x+20,515)

    # Funkcijo. ki vzame kot argument besedo in crko
    #in nato izpiše/izriše črke na črto
    def izpisi_crko(self,crka):
        if self.aktivno== False:
            return None
        st_uganjenih =0
        for i in range(len(self.beseda)):       
            if self.beseda[i].upper() == crka.upper():
                st_uganjenih +=1
                self.slika.create_text(95 + i*35, 505, text=crka.upper())
        self.uganjeni +=st_uganjenih
        if self.uganjeni == len(self.beseda):
             self.slika.create_text(280, 430, text='ZMAGALI STE!',font=('Arial',20))
             for i in range(25):
                 self.seznam_gumbov[i].gumb.configure(state="disabled")                 
             self.aktivno = False
                    
        if st_uganjenih == 0:
            self.poteza +=1      
            self.vislice(self.poteza)
            if self.poteza == 8:
                self.slika.create_text(280, 430, text='IZGUBILI STE!',font=('Arial',20))
                self.slika.create_text(280, 455, text='Iskana beseda je bila {0}'.format(self.beseda))
                for i in range(25):
                    self.seznam_gumbov[i].gumb.configure(state="disabled") 
                self.aktivno = False
                

    def nova_igra(self):
        self.slika.delete('all')
        self.beseda = izberi_besedo()
        for i in range(25):
             self.seznam_gumbov[i].gumb.configure(state="normal")
             self.seznam_gumbov[i].nastavi(self.beseda)
       
        self.narisi_crte()
        self.poteza = 0
        self.uganjeni = 0
        self.aktivno = True

        
okno = tk.Tk()
okno.resizable(width=False, height=False)#uporabnik ne more spreminjati velikosti okna
okno.geometry('550x500') 
#še pokliči funkcijo
igra = Vislice(okno)


tk.mainloop()
    
#https://www.tutorialspoint.com/python/tk_button.htm
