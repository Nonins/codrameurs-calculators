#un calculatrice
import pygame
import time
class main():
    def __init__(self):
        print("---chargement---")
        pygame.init()
        self.surface = pygame.display.set_mode((400,550),pygame.NOFRAME)
        self.surface.fill((255,255,255))
        self.nb_1=""
        self.operateur=""
        self.nb_2=""
        self.res= ""
        self.Erreur= "Error"
        self.btn_relacher=True
        self.coorde_btn={
            "1":{
                "x1":0,
                "y1":180,
                "x2":100,
                "y2":245,
                "id":None 
            },
            "2":{
                "x1":100,
                "y1":180,
                "x2":200,
                "y2":245,
                "id":None 
            },
            "3":{
                "x1":200,
                "y1":180,
                "x2":300,
                "y2":245,
                "id":None 
            },
            "4":{
                "x1":300,
                "y1":180,
                "x2":400,
                "y2":245,
                "id":"/"
            },
            "5":{
                "x1":0,
                "y1":245,
                "x2":100,
                "y2":310,
                "id":"7" 
            },
            "6":{
                "x1":100,
                "y1":245,
                "x2":200,
                "y2":310,
                "id":"8" 
            },
            "7":{
                "x1":200,
                "y1":245,
                "x2":300,
                "y2":310,
                "id":"9" 
            },
            "8":{
                "x1":300,
                "y1":245,
                "x2":400,
                "y2":310,
                "id":"X"
            },
            "9":{
                "x1":0,
                "y1":310,
                "x2":100,
                "y2":375,
                "id":"4" 
            },
            "10":{
                "x1":100,
                "y1":310,
                "x2":200,
                "y2":375,
                "id":"5"
            },
            "11":{
                "x1":200,
                "y1":310,
                "x2":300,
                "y2":375,
                "id":"6"
            },
            "12":{
                "x1":300,
                "y1":310,
                "x2":400,
                "y2":375,
                "id":"-"
            },
            "13":{
                "x1":0,
                "y1":375,
                "x2":100,
                "y2":440,
                "id":"1" 
            },
            "14":{
                "x1":100,
                "y1":375,
                "x2":200,
                "y2":440,
                "id":"2" 
            },
            "15":{
                "x1":200,
                "y1":375,
                "x2":300,
                "y2":440,
                "id":"3"
            },
            "16":{
                "x1":300,
                "y1":375,
                "x2":400,
                "y2":440,
                "id":"+"
            },
            "17":{
                "x1":0,
                "y1":440,
                "x2":0,
                "y2":505,
                "id":None 
                },
            "18":{
                "x1":100,
                "y1":440,
                "x2":200,
                "y2":505,
                "id":"0" 
                },
            "19":{
                "x1":200,
                "y1":440,
                "x2":400,
                "y2":505,
                "id":"res"
                },
        
        
        }
        self.coorde_btn_event:{
            "QUITTER":{
                "x1":300,
                "y1":57,
                "x2":387,
                "y2":75,
            },
        }
        self.police=pygame.font.SysFont("arial",60)
        self.res_text=self.police.render("",True,(10,95,69))
        self.stade_calcule=1
        pygame.display.set_caption("Codrameur's calculators ")
        print("---chargement ruessie---")
    def menu(self):
        #code du menu
        bandeau=pygame.image.load("textur.png")
        bandeau.convert()
        def btn_presser(btn):
            e=self.coorde_btn[btn]["id"]
            if e =="res":
                self.res_text=self.police.render(calculer(),True,(10,95,69))
                return
            elif e =="X" or e=="/" or e=="+" or e=="-" :
                self.operateur=e 
                self.stade_calcule=2
            elif e == None :
                self.nb_1=""
                self.nb_2=""
                self.operateur=""
                self.res =self.nb_1
                self.Erreur
            else :
                print('nb')
                if self.stade_calcule==1:
                    self.nb_1=self.nb_1+e
                elif self.stade_calcule==2:       
                    self.nb_2=self.nb_2+e
            self.res_text=self.police.render(str(self.nb_1)+str(self.operateur)+str(self.nb_2),True,(10,95,69))
        def calculer():
            self.nb_1=int(self.nb_1)
            self.nb_2=int(self.nb_2)
            self.nb_2=int(self.nb_1*2)
            if not self.nb_2:
                print("test")
            if self.operateur == "+":
                return str(self.nb_1+self.nb_2)
            elif self.operateur == "-":
                return str(self.nb_1-self.nb_2)
            elif self.operateur == "X":
                return str(self.nb_1*self.nb_2)
            elif self.operateur == "/" and str(self.nb_2) == "0":
                str(self.Erreur) =="Erreur"
                return str(self.Erreur)
            elif self.operateur == "/":
                return str(self.nb_1/self.nb_2)
        launched = True
        while launched:
        #boc principale
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched=False
                if event.type == pygame.MOUSEBUTTONUP:
                    self.btn_relacher=True
                if event.type==pygame.MOUSEBUTTONDOWN and self.btn_relacher==True:
                    for x in range(19):
                        y=str(x+1)
                        if self.coorde_btn[y]["x1"]<event.pos[0]:
                            if self.coorde_btn[y]["y1"]<event.pos[1]:
                                if self.coorde_btn[y]["x2"]>event.pos[0]:
                                    if self.coorde_btn[y]["y2"]>event.pos[1]:
                                        self.btn_relacher=False
                                        btn_presser(y)                  
            self.surface.blit(bandeau,(0,0))
            self.surface.blit(self.res_text,(10,100)) 
            pygame.display.flip() 
            pygame.display.set_mode((400,550),pygame.NOFRAME)
instance=main()
instance.menu()
