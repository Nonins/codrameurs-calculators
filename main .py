import pygame
import time
import json
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
        self.point = 0
        self.point1 = 0
        self.btn_relacher=True
        with open("cord_btn.json") as f:
            self.coorde_btn = json.load(f)
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
                                        self.btn_presser(y)
            self.surface.blit(bandeau,(0,0))
            self.surface.blit(self.res_text,(10,100)) 
            pygame.display.flip() 
            pygame.display.set_mode((400,550),pygame.NOFRAME)
    
    def btn_presser(self, btn):
        e=self.coorde_btn[btn]["id"]
        if e =="res":
            if self.nb_1 == "" or self.nb_2 == "":
                return
            self.res_text=self.police.render(self.calculer(),True,(10,95,69))
            self.nb_1 = self.res
            self.nb_2 = ""
            self.point = 0
            self.point1 = 0
            self.stade_calcule=3
            return
        elif e =="X" or e=="/" or e=="+" or e=="-" :
            if self.nb_1 == "":
                return
            self.operateur=e 
            self.stade_calcule=2
        elif e == None :
            self.nb_1=""
            self.nb_2=""
            self.operateur=""
            self.Erreur=""
            self.point= 0
            self.point1 = 0
            self.stade_calcule=1
        elif e == "." and self.stade_calcule == 1 :
            self.point += 1
            if self.point >= 2:
                return
            self.nb_1 = str(self.nb_1)
            self.nb_1 = self.nb_1+e
            if self.nb_1 == ".":
                self.nb_1 = "0."
                self.res_text=self.police.render(self.nb_1,True,(10,95,69))
                return
            self.res_text=self.police.render(self.nb_1,True,(10,95,69))
            return
        elif e == "." and self.stade_calcule == 2 :
            self.point1 += 1
            if self.point1 >= 2:
                return
            self.nb_2 = str(self.nb_2)
            self.nb_2 = self.nb_2+e
            if self.nb_2 == ".":
                self.nb_2 = "0."
                self.res_text=self.police.render(self.nb_2,True,(10,95,69))
                return
            self.res_text=self.police.render(self.nb_2,True,(10,95,69))
            return 
        else :
            print('nb')
            if self.stade_calcule==1:
                self.nb_1=self.nb_1+e
            elif self.stade_calcule==2:    
                self.nb_2=self.nb_2+e
            elif self.stade_calcule==3:
                self.nb_2=""
                self.nb_1=e
                self.operateur=""
                self.res_text=self.police.render(self.nb_1,True,(10,95,69))
                self.stade_calcule=1
                return
        self.res_text=self.police.render(str(self.nb_1)+str(self.operateur)+str(self.nb_2),True,(10,95,69))

    def calculer(self):
        self.nb_1=float(self.nb_1)
        if int(self.nb_1) == self.nb_1:
            self.nb_1=int(self.nb_1)
        
        self.nb_2=float(self.nb_2)
        if int(self.nb_2) == self.nb_2:
            self.nb_2=int(self.nb_2)
        
        if self.operateur == "+":
            self.res = str(self.nb_1+self.nb_2)
            return str(self.nb_1+self.nb_2)
        elif self.operateur == "-":
            self.res = str(self.nb_1-self.nb_2)
            return str(self.nb_1-self.nb_2)
        elif self.operateur == "X":
            self.res = str(self.nb_1*self.nb_2)
            return str(self.nb_1*self.nb_2)
        elif self.operateur == "/" and str(self.nb_2) == "0":
            return self.Erreur
        elif self.operateur == "/":
            self.res = str(self.nb_1/self.nb_2)
            return str(self.nb_1/self.nb_2)

instance=main()
instance.menu()
