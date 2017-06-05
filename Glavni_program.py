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
        self.gumb.place(x = 300 + 30*i,y= 50+ 30*j)
        self.i = i
        self.j = j

    def nastavi(self,beseda):
        self.beseda = beseda
        self.gumb.configure(command = self.izpisi)

    def izpisi(self):
        igra.izpisi_crko(slovenska_abeceda[5*self.i + self.j])
        self.gumb.configure(state="disabled")
                       

class Vislice:
    def __init__(self,okno):
        self.gumb_nov_zacetek = tk.Button(okno, text='Nova igra',command=self.nova_igra)
        self.gumb_nov_zacetek.place(relx=0.73, rely=0.3)
        self.slika = tk.Canvas(okno,width=500,height=800)
        self.slika.place(x=10, y=10)
        self.seznam_gumbov = []
        for i in range(5):
            for j in range(5):
                self.seznam_gumbov.append(Gumb(okno,i,j))
        self.aktivno = False
            
    def vislice(self,n): #n bo najvec 10
        if n == 1:
            self.slika.create_polygon(50,305,50,310,150,310,150,305)
        if n == 2:
            self.slika.create_polygon(100,180,100,310,105,310,105,180)
        if n == 3:
            self.slika.create_polygon(10,175,10,180,105,180,105,175)
        if n == 4:
            self.slika.create_polygon(5,175,5,200,10,200,10,175)
        if n == 5:
            self.slika.create_oval(2,200,22,220)#vneseš 1. in 3. koordinato
        if n == 6:
            self.slika.create_polygon(11,220,11,270,13,270,13,220)
        if n == 7:
            self.slika.create_polygon(0,200,0,202,11,237,11,235)
        if n == 8:
            self.slika.create_polygon(13,235,13,237,28,202,28,200)
        if n == 9:
            self.slika.create_polygon(0,300,0,302,11,270,11,268)
        if n == 10:
            self.slika.create_polygon(13,268,13,270,24,302,24,300)

            
    def narisi_crte(self):
        st_crk = len(self.beseda)
        x = -15
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
                self.slika.create_text(30 + i*35, 505, text=crka.upper())
        print(st_uganjenih)
        print(self.beseda)
        print(crka)
        self.uganjeni +=st_uganjenih
        if self.uganjeni == len(self.beseda):
             self.slika.create_text(60, 400, text='ZMAGALI STE!')
             for i in range(25):
                 self.seznam_gumbov[i].gumb.configure(state="disabled")                 
             self.aktivno = False
                    
        if st_uganjenih == 0:
            self.poteza +=1      
            self.vislice(self.poteza)
            if self.poteza == 10:
                self.slika.create_text(60, 400, text='IZGUBILI STE!')
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
okno.geometry('{}x{}'.format(800, 600)) 
#še pokliči funkcijo
igra = Vislice(okno)


tk.mainloop()
    
#https://www.tutorialspoint.com/python/tk_button.htm
