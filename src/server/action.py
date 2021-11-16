#!/usr/bin/python3
# -*- coding: utf-8 -*-

## @package action
# COURS   : EDF4REPA - IED - Paris 8
# PROJET  : consMaster2
# AUTEUR  : David Calmeille - 11299110@foad.iedparis8.net - L2
# FICHIER : action.py
# CONTENU : fonctions utilisateur: creation, identification, suppression, listing.
#           fonctions exercices: creation, suppression, loading.
# VERSION : 0.2
# LICENCE : GNU

from database import *
from codes import *
import json
from traceback import print_exc

class Action:

    def __init__(self, myString):
        self.myString = myString
        self.resultat = ''
        self.droit = 3  # anonymous usage
        ## Verifie si la chaine est au format JSON
        try:
            self.myJson = json.loads(myString)
        except Exception as e:
            print_exc(limit=3)
            self.resultat = '{"status":"error","code":"E_AJS","description":"'+ str(e) +'"}'
            return

        userExists = self.userExist()

        # Va executer l'action desirer
        try:
            getattr(Action,self.myJson["action"])(self)
        except Exception as e:
            print_exc(limit=3)
            self.resultat = '{"status":"error","code":"E_AGA","description":"'+ str(e) +'"}'


    def userExist(self):
        #TODO: ajouter une gestion plus fine des erreurs ?
        try:
            session = Session()
            res = session.query(User). \
                        filter(User.nickname == self.myJson["nickname"]). \
                        filter(User.password == self.myJson["password"]).all()
            session.commit()
            
            self.id = res[0].id
            self.droit = res[0].droit
            session.close()
            return True
        except Exception:
            print_exc(limit=2)
            return False


    #////////////////////////////////////////////////////////////////////////////
    #     UTILISATEUR
    #////////////////////////////////////////////////////////////////////////////

    def creatUser(self):  # Creation d'un nouvel utilisateur
        if self.droit == 0:
            droit = self.myJson["data"]["droit"]
        else:
            droit = 2  # par défaut, simple etudiant

        try:
            session = Session()
            res = session.query(User).filter(User.nickname == self.myJson["data"]["nickname"]).first()
            if res:
                self.resultat =  '{"status":"error","code":"E_AUC","description":"utilisateur deja existant"}'
            else:
                data = self.myJson["data"]
                new_user = User(data["nickname"], data.get("nom"), data.get("prenom"), data["email"], data["password"], droit)
                session.add(new_user)
                session.commit()
                insertId = str(new_user.id)
                session.close()
                self.resultat = '{"status":"success","code":"S_AUC","data":{"id":'+insertId+'}}'
        except Exception as e:
            print_exc(limit=3)
            self.resultat =  '{"status":"error","code":"E_AUC","description":"'+ str(e) +'"}'


    def identUser(self):  # Identification d'un utilisateur
        try:
            session = Session()
            res = session.query(User). \
                    filter(User.nickname == self.myJson["data"]["nickname"]). \
                    filter(User.password == self.myJson["data"]["password"]).all()
            session.commit()

            ident = str(res[0].id)
            session.close()
            self.resultat =  '{"status":"success","code":"S_AUI","data":{"id":'+ident+'}}'
        except Exception as e:
            print_exc(limit=3)
            if len(res) == 0:
                self.resultat =  '{"status":"error","code":"E_AUI","description":"utilisateur inexistant"}'
            else:
                self.resultat =  '{"status":"error","code":"E_AUI","description":"'+ str(e) +'"}'


    def delUser(self):  # Suppression d'un utilisateur avec son id
        if self.droit == 0:
            try:
                session = Session()
                res = session.query(User).filter(User.id==self.myJson["data"]["id"]).first()
                session.delete(res)
                session.commit()
                session.close()
                self.resultat =  '{"status":"success","code":"S_AUD","data":{"id":'+str(self.myJson["data"]["id"])+'}}'
            except Exception as e:
                print_exc(limit=3)
                self.resultat =  '{"status":"error","code":"E_AUD","description":"'+ str(e) +'"}'
        else:
            self.resultat =  '{"status":"error","code":"E_AUO","description":"'+ E_AUO +'"}'


    def delMyUser(self):  # Suppression d'un utilisateur avec nickname et password
          try:
              session = Session()
              res = session.query(User). \
                  filter(User.nickname == self.myJson["data"]["nickname"]). \
                  filter(User.password == self.myJson["data"]["password"]).first()
              if res:
                  session.delete(res)
                  session.commit()
                  session.close()
                  self.resultat =  '{"status":"success","code":"S_AUM","data":{"nickname":"'+str(self.myJson["data"]["nickname"])+'"}}'
              else:
                  self.resultat =  '{"status":"error","code":"E_AUM","description":"'+ E_AUM +'"}'
          except Exception as e:
              print_exc(limit=3)
              self.resultat =  '{"status":"error","code":"E_AUM","description":"'+ str(e) +'"}'


    def listUser(self):  # listing des utilisateurs
        if self.droit <= 1:
            try:
                session = Session()
                q = session.query(User)
                for item, value in self.myJson["data"].items():
                    if item == "id":
                        q = q.filter(User.id==value)
                    else:
                        q = q.filter(getattr(User, item).like("%%%s%%" % value))
                session.commit()
                response = json.dumps([{"id": item.id, "nom": item.nom, "prenom": item.prenom, "email": item.email} 
						for item in q])
                session.close()
                self.resultat =  '{"status":"success","code":"S_AUL","data":'+ response + '}'
            except Exception as e:
                print_exc(limit=3)
                self.resultat =  '{"status":"error","code":"E_AUL","description":"'+ str(e) +'"}'
        else:
            self.resultat =  '{"status":"error","code":"E_AUO","description":"'+ E_AUO +'"}'


    #////////////////////////////////////////////////////////////////////////////
    #     EXERCICES
    #////////////////////////////////////////////////////////////////////////////

    def creatExo(self):  # Creation d'un nouvel exercice
        if self.droit == 0:
            try:
                session = Session()
                data = self.myJson["data"]
                new_exo = Exercice(data["name"], data["type"], data["level"], data["raw"])
                session.add(new_exo)
                session.commit()
                insertId = str(new_exo.id)
                session.close()
                self.resultat =  '{"status":"success","code":"S_AEC","data":{"id":'+insertId+'}}'
            except Exception as e:
                print_exc(limit=3)
                self.resultat =  '{"status":"error","code":"E_AEC","description":"'+ str(e) +'"}'
        else:
            self.resultat =  '{"status":"error","code":"E_AUO","description":"'+ E_AUO +'"}'


    def loadExo(self):  # Loading des exercices
        #TODO: exiger le droit 2 ?
        try:
            session = Session()
            q = session.query(Exercice)
            for item, value in self.myJson["data"].items():
                if item == "id":
                    q = q.filter(Exercice.id == value)
                else:
                    q = q.filter(getattr(Exercice, item).like("%%%s%%" % value))
            session.commit()
            response = json.dumps([{'id': item.id, 'raw': item.raw} for item in q])
            session.close()
            self.resultat =  '{"status":"success","code":"S_AEL","data":'+ response +'}'
        except Exception as e:
            print_exc(limit=3)
            self.resultat =  '{"status":"error","code":"E_AEL","description":"'+ str(e) +'"}'

    def listExoId(self):  # Loading des exercices
        #TODO: exiger le droit 2 ?
        try:
            session = Session()
            q = session.query(Exercice)
            session.commit()
            response = json.dumps([item.id for item in q])
            session.close()
            self.resultat =  '{"status":"success","code":"S_AEL","data":'+ response +'}'
        except Exception as e:
            print_exc(limit=3)
            self.resultat =  '{"status":"error","code":"E_AEL","description":"'+ str(e) +'"}'


    def delExo(self):  # Suppression d'un exercice
        if self.droit == 0:
            try:
                session = Session()
                res = session.query(Exercice).filter(Exercice.id==self.myJson["data"]["id"]).first()
                session.delete(res)
                session.commit()
                session.close()
                self.resultat =  '{"status":"success","code":"S_AED","data":{"id":'+str(self.myJson["data"]["id"])+'}}'
            except Exception as e:
                print_exc(limit=3)
                self.resultat =  '{"status":"error","code":"E_AED","description":"'+ str(e) +'"}'
        else:
            self.resultat =  '{"status":"error","code":"E_AUO","description":"'+ E_AUO +'"}'


    #////////////////////////////////////////////////////////////////////////////
    #     SOUMISSION
    #////////////////////////////////////////////////////////////////////////////

    def creatSubm(self):  # Creation d'une nouvelle soumission
        if self.droit <= 2:
            try:
                session = Session()
                data = self.myJson["data"]
                new_soum = Soumission(self.id, data["exo_id"], data["soumission"])
                session.add(new_soum)
                session.commit()
                insertId = str(new_soum.id)
                session.close()
                self.resultat =  '{"status":"success","code":"S_ASC","data":{"id":'+insertId+'}}'
            except Exception as e:
                print_exc(limit=3)
                self.resultat =  '{"status":"error","code":"E_ASC","description":"'+ str(e) +'"}'
        else:
            self.resultat =  '{"status":"error","code":"E_AUO","description":"'+ E_AUO +'"}'


    def listSubm(self):  # listing des soumissions
        if self.droit == 0:
            try:
                session = Session()
                data = self.myJson["data"]

                q = session.query(Soumission)
                if "exo_id" in data:
                    q = q.join(Exercice).\
                            filter(Exercice.id == data["exo_id"])
                if "nickname" in data:
                    q = q.join(User).\
                            filter(User.nickname == data["nickname"])
                q = q.all()
                
                #TODO: si les 2 parmètres manquent, renvoyer une erreur
                #else:
                #    self.resultat =  '{"status":"error","code":"E_ASL","description":"commande incorrecte"}'
                #    return

                session.commit()
                response = json.dumps([{"nickname": item.user.nickname, "soumission": item.soumission, "exo_id": item.exo_id} for item in q])
                # print(response)
                session.close()
                self.resultat =  '{"status":"success","code":"S_ASL","data":'+ response +'}'
                
            except Exception as e:
                print_exc(limit=3)
                self.resultat =  '{"status":"error","code":"E_ASL","description":"'+ str(e) +'"}'
        
        else:
            self.resultat =  '{"status":"error","code":"E_AUO","description":"'+ E_AUO +'"}'

