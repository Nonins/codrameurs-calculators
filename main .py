import pygame
import time
import json

class main():

    def __init__(self):
        print("---chargement---")
        pygame.init()
        self.launched=True
        self.surface = pygame.display.set_mode((400,550),pygame.NOFRAME)
        self.surface.fill((255,255,255))
        self.nb_1=""
        self.operateur=""
        self.nb_2=""
        self.res= ""
        self.Erreur= "Error"
        self.point = 0
        self.point1 = 0
        self.Deplacer = 10
        self.btn_relacher=True
        with open("cord_btn.json") as f:
            self.coorde_btn = json.load(f)
        self.police=pygame.font.SysFont("arial",60)
        self.res_text=self.police.render("",True,(10,95,69))
        self.stade_calcule=1
        pygame.display.set_caption("Codrameur's calculators ")
        print("---chargement ruessie---")

    def menu(self):
        #code du menu
        bandeau=pygame.image.load("texture.png")
        bandeau.convert()
        self.launched = True
        while self.launched:
        #boc principale
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.btn_relacher=True
                if event.type==pygame.MOUSEBUTTONDOWN and self.btn_relacher==True:
                    for x in range(20):
                        y=str(x+1)
                        if self.coorde_btn[y]["x1"]<event.pos[0]:
                            if self.coorde_btn[y]["y1"]<event.pos[1]:
                                if self.coorde_btn[y]["x2"]>event.pos[0]:
                                    if self.coorde_btn[y]["y2"]>event.pos[1]:
                                        self.btn_relacher=False
                                        self.btn_presser(y)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.Deplacer_droite()
                    if event.key == pygame.K_LEFT:
                        self.Deplacer_gauche()
            self.surface.blit(bandeau,(0,0))
            self.surface.blit(self.res_text,(self.Deplacer,100)) 
            pygame.display.flip() 
            pygame.display.set_mode((400,550),pygame.NOFRAME)
    
    def btn_presser(self, btn):
        e=self.coorde_btn[btn]["id"]
        if e =="res":
            if self.nb_1 == "" or self.nb_2 == "":
                return
            self.calculer()
            self.arrondir()
            self.res_text=self.police.render(str(self.res),True,(10,95,69))
            self.nb_1 = self.res
            self.nb_2 = ""
            self.stade_calcule=3
            self.point = 0
            self.point1 = 0
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
                self.res_text=self.police.render(str(self.nb_1)+str(self.operateur)+str(self.nb_2),True,(10,95,69))
                return
            self.res_text=self.police.render(str(self.nb_1)+str(self.operateur)+str(self.nb_2),True,(10,95,69))
            return
        elif e == "quit":
             self.launched=False 
        else:
            if self.stade_calcule==1:
                self.nb_1=self.nb_1+e
            elif self.stade_calcule==2:    
                self.nb_2=self.nb_2+e
            elif self.stade_calcule==3:
                self.nb_2=""
                self.nb_1=e
                self.operateur=""
                self.point = 1
                if self.nb_1 == ".":
                    self.nb_1 = "0."
                self.res_text=self.police.render(self.nb_1,True,(10,95,69))
                self.stade_calcule=1
                return
        self.res_text=self.police.render(str(self.nb_1)+str(self.operateur)+str(self.nb_2),True,(10,95,69))

    def calculer(self):
        self.nb_1=float(self.nb_1)
        self.nb_2=float(self.nb_2)
       
        if self.operateur == "+":
            self.res = self.nb_1+self.nb_2
            return self.res
        if self.operateur == "-":
            self.res = self.nb_1-self.nb_2
            return self.res
        if self.operateur == "X":
            self.res = self.nb_1*self.nb_2
            return self.res
        if self.operateur == "/" and self.nb_2 == 0:
            return self.Erreur
        if self.operateur == "/":
            self.res = self.nb_1/self.nb_2
            return self.res
    
    def arrondir(self):
        split_res = str(self.res).split(".")
        if len(split_res) == 1:
            return

        nb_apres_virgule = 0
        split_nb_1 = str(self.nb_1).split(".")
        if len(split_nb_1) > 1:
            nb_apres_virgule_nb_1 = len(split_nb_1[1])
            if nb_apres_virgule < nb_apres_virgule_nb_1:
                nb_apres_virgule = nb_apres_virgule_nb_1

        split_nb_2 = str(self.nb_2).split(".")
        if len(split_nb_2) > 1:
            nb_apres_virgule_nb_2 = len(split_nb_2[1])
            if nb_apres_virgule < nb_apres_virgule_nb_2:
                nb_apres_virgule = nb_apres_virgule_nb_2

        self.res = round(self.res, nb_apres_virgule)
        if int(self.res) == self.res:
            self.res = int(self.res)
    def Deplacer_droite(self):
        self.Deplacer-=4
    def Deplacer_gauche(self):
        self.Deplacer+=4

instance=main()
instance.menu()
