
import mysql.connector
from datetime import *
try:
    f = open("settings.txt","r")
    bdd=f.readline().replace('\n','')
    ip=f.readline().replace('\n','')
    user=f.readline().replace('\n','')
    pw=f.readline().replace('\n','')
    db=mysql.connector.connect(user=user, password=pw,
                                   host=ip, database=bdd)
    cur= db.cursor()
except:
    db = None
    cur = None

try:
    cur.execute("CREATE TABLE IF NOT EXISTS fichier(id_fichier INT PRIMARY KEY AUTO_INCREMENT,"
                "chemin VARCHAR(100))")
    cur.execute('CREATE TABLE IF NOT EXISTS Client(nom_client VARCHAR(50) PRIMARY KEY,code_postal INT' \
                + ',adresse VARCHAR(50),statut_juridique VARCHAR(30),email VARCHAR(30)' \
                + ',observation VARCHAR(100),tel VARCHAR(20),num_rc VARCHAR(30),num_nif VARCHAR(30)' \
                + ',num_succurale VARCHAR(30),num_nis VARCHAR(30),num_article_imp VARCHAR(30),date_exp_rc DATE' \
                + ',date_exp_mandat DATE,num_mandat VARCHAR(30))')
    cur.execute('CREATE TABLE IF NOT EXISTS Personne(id INT PRIMARY KEY AUTO_INCREMENT,' \
                + 'nom VARCHAR(20),prenom VARCHAR(20),date_de_naissance DATE,tele VARCHAR(20),type VARCHAR(20))')
    cur.execute('CREATE TABLE IF NOT EXISTS Expert(id_expert INT PRIMARY KEY,domaine VARCHAR(20),' \
                + 'FOREIGN KEY (id_expert) REFERENCES Personne(id) ON DELETE CASCADE)')
    cur.execute('CREATE TABLE IF NOT EXISTS Utilisateur(id_utilisateur INT PRIMARY KEY,password VARCHAR(20),' \
                + 'FOREIGN KEY (id_utilisateur) REFERENCES Personne(id) ON DELETE CASCADE)')
    cur.execute('CREATE TABLE IF NOT EXISTS Chauffeur(id_chauffeur INT PRIMARY KEY,' \
                + 'FOREIGN KEY (id_chauffeur) REFERENCES Personne(id) ON DELETE CASCADE)')
    cur.execute('CREATE TABLE IF NOT EXISTS Douanier(id_douanier INT PRIMARY KEY,' \
                + 'FOREIGN KEY (id_douanier) REFERENCES Personne(id) ON DELETE CASCADE)')
    cur.execute('CREATE TABLE IF NOT EXISTS declarant(idDeclarant INT PRIMARY KEY,' \
                + 'FOREIGN KEY (idDeclarant) REFERENCES Personne(id) ON DELETE CASCADE)')
    cur.execute('CREATE TABLE IF NOT EXISTS Representant(id_representant INT PRIMARY KEY,id_client VARCHAR(50),' \
                + 'FOREIGN KEY (id_representant) REFERENCES Personne(id) ON DELETE CASCADE,' \
                + 'FOREIGN KEY (id_client) REFERENCES Client(nom_client) ON DELETE CASCADE)')
    cur.execute("CREATE TABLE IF NOT EXISTS Monnaie(code_monnaie VARCHAR(20) PRIMARY KEY ,nom_pay VARCHAR(20) )")
    cur.execute("CREATE TABLE IF NOT EXISTS Nature_Marchandise(nature VARCHAR(20) PRIMARY KEY   )")
    sql_inter = 'CREATE TABLE IF NOT EXISTS intermediaire(nom_inter VARCHAR(20) PRIMARY KEY' \
                + ',type VARCHAR(20))'
    cur.execute(sql_inter)
    sql_fourn = 'CREATE TABLE IF NOT EXISTS fournisseur(nom_fournisseur VARCHAR(20) PRIMARY KEY' \
                + ',adresse VARCHAR(20))'
    cur.execute(sql_fourn)
    sql_pays = 'CREATE TABLE IF NOT EXISTS pays(code_pays INT PRIMARY KEY, nom_pays VARCHAR(20))'
    cur.execute(sql_pays)
    cur.execute("CREATE TABLE IF NOT EXISTS dossier(id_dossier INT PRIMARY KEY AUTO_INCREMENT, id_client VARCHAR(20), "
                "id_declarant INT,date_ouverture DATETIME,date_arrivee DATETIME,date_fermeture DATETIME,navire VARCHAR(20),"
                "nb_conteneurs INT,statut_dossier ENUM('Archivé', 'En cours'),id_four VARCHAR(20),id_pays INT,"
                "id_comp_trans VARCHAR(20) ,titre_trans VARCHAR(20),nom_port VARCHAR(20),SG VARCHAR(20),"
                "id_lieu_entrepot VARCHAR(20),observation VARCHAR(100),nature_dossier ENUM('Import', 'Export'),"
                "gros VARCHAR(20),article VARCHAR(20),code_monnaie VARCHAR(10),id_fichiers INT,"
                "FOREIGN KEY (id_client) REFERENCES client (nom_client) ON DELETE CASCADE,"
                "FOREIGN KEY (id_four) REFERENCES fournisseur (nom_fournisseur) ON DELETE CASCADE,"
                "FOREIGN KEY (id_pays) REFERENCES pays (code_pays) ON DELETE CASCADE,"
                "FOREIGN KEY (code_monnaie) REFERENCES monnaie (code_monnaie) ON DELETE CASCADE,"
                "FOREIGN KEY (id_fichiers) REFERENCES fichier (id_fichier) ON DELETE CASCADE,"
                "FOREIGN KEY (id_declarant) REFERENCES declarant (idDeclarant) ON DELETE CASCADE,"
                "FOREIGN KEY (id_comp_trans) REFERENCES intermediaire (nom_inter) ON DELETE CASCADE)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Faacturess(id INT PRIMARY KEY AUTO_INCREMENT ,idDossier INT, date DATETIME ,TVA FLOAT, total_prestation FLOAT,  total_debours FLOAT ,droit_timbre INT,"
        " etat_paiement VARCHAR(20), mode_paiement VARCHAR(20), FOREIGN KEY (idDossier) REFERENCES Dossier (id_dossier) ON DELETE SET NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS Camion (matricule BIGINT PRIMARY KEY   )")
    cur.execute("CREATE TABLE IF NOT EXISTS Bon(id_dossier INT,type VARCHAR(20)" \
                + ",num_bon VARCHAR(30),date_bon DATE ,pc VARCHAR(30)" \
                + ",PRIMARY KEY (id_dossier,type) , FOREIGN KEY (id_dossier) REFERENCES dossier(id_dossier) ON DELETE CASCADE)")

    cur.execute("CREATE TABLE IF NOT EXISTS bon_sortie(id_dossier INT PRIMARY KEY" \
                + ",id_chauffeur INT ,matricule BIGINT" \
                + ",FOREIGN KEY (id_chauffeur) REFERENCES chauffeur(id_chauffeur) ON DELETE SET NULL" \
                + ",FOREIGN KEY (matricule) REFERENCES camion(matricule) ON DELETE SET NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS bon_visite(id_dossier INT PRIMARY KEY" \
                + ",id_douanier INT ,bureau_douane VARCHAR(30)" \
                + ",FOREIGN KEY (id_douanier) REFERENCES douanier(id_douanier) ON DELETE SET NULL" \
                + ",FOREIGN KEY (bureau_douane) REFERENCES intermediaire(nom_inter) ON DELETE SET NULL)")

    cur.execute("CREATE TABLE IF NOT EXISTS emballage(id_emballage INT ,"
                "genre VARCHAR(20),type VARCHAR(20),pieds VARCHAR(20), id_dossier INT,"
                "PRIMARY KEY(id_emballage,id_dossier),"
                "FOREIGN KEY (id_dossier) REFERENCES dossier (id_dossier) ON DELETE CASCADE)")

    cur.execute("CREATE TABLE IF NOT EXISTS marchandise (id_marchandise INT PRIMARY KEY,"
                "poids FLOAT, num_facture VARCHAR(20), nature VARCHAR(20), montant FLOAT,"
                "id_dossier INT, id_emballage INT,description VARCHAR(50),"
                "FOREIGN KEY (id_emballage) REFERENCES emballage(id_emballage) ON DELETE CASCADE,"
                "FOREIGN KEY (id_dossier) REFERENCES dossier (id_dossier) ON DELETE CASCADE)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Designation(nom_designation VARCHAR(20) PRIMARY KEY ,type VARCHAR(20),id_marchandise INT ,FOREIGN KEY (id_marchandise) REFERENCES marchandise (id_marchandise) ON DELETE SET NULL  )")

except:
    pass

'''_____________________________Fichier________________________________________'''
'''****************************************************************************'''

'''cur.execute("CREATE TABLE IF NOT EXISTS Faacturess(id INT PRIMARY KEY AUTO_INCREMENT ,idDossier INT, date DATETIME ,TVA FLOAT, total_prestation FLOAT,  total_debours FLOAT ,droit_timbre INT, etat_paiement VARCHAR(20), mode_paiment VARCHAR(20) )")'''


class Fichier:

    def __init__(self, chemin):
        self.__id_fichier = 0
        self.__chemin=chemin
        self.inserer_un_fichier()

    '''__________setters and getters____________'''

    def set_id_fichier(self, attribute_id):
        self.__id_fichier = attribute_id

    def get_id_fichier(self):
        return self.__id_fichier

    def get_tuple_fichier(self):
        return(self.__idDossier,self.__chemin)

    ''' _____________ insertion __________________'''

    def inserer_un_fichier(self):
        sql = 'INSERT INTO Fichier(chemin) VALUES(%s)'
        cur.execute(sql, (self.__chemin,))
        self.set_id_fichier(cur.lastrowid)
        db.commit()

    '''_______________ static methods _________________'''
    @staticmethod
    def recherche_fichier(id):
        sql = 'SELECT * FROM Fichier WHERE id_fichier=%s'
        cur.execute(sql, (id,))
        res = cur.fetchone()
        return res

    @staticmethod
    def fichier_existe(id):
        sql = 'SELECT * FROM Fichier WHERE id_fichier= %s'
        cur.execute(sql, (id,))
        res = cur.fetchone()
        if res is None:
            return False
        else:
            return True

    @staticmethod
    def modifier_une_fichier(idFichier,chemain):
        sql = 'UPDATE Fichier SET chemin=%s WHERE id_fichier=%s'
        cur.execute(sql,(chemain,idFichier))
        db.commit()

    @staticmethod
    def supprimer_fichier(id):
        sql = 'DELETE FROM Fichier WHERE id_fichier=%s'
        cur.execute(sql, (id,))
        db.commit()






'''=====================Client===================='''



class Client:
    def __init__(self,nomClient,codePostal,adresse,statutJuridique,email,observation,tel,numRC
                 ,numNIF,numSuccurale,numNIS,numArticleImp,dateExpRC,dateExpMandat,numMandat):
        self.__nomClient=nomClient
        self.__codePostal=codePostal
        self.__adresse=adresse
        self.__statutJuridique=statutJuridique
        self.__email=email
        self.__observation=observation
        self.__tel=tel
        self.__numRC=numRC
        self.__numNIF=numNIF
        self.__numSuccurale=numSuccurale
        self.__numNIS=numNIS
        self.__numArticleImp=numArticleImp
        self.__dateExpRC=dateExpRC
        self.__dateExpMandat=dateExpMandat
        self.__numMandat=numMandat
        self.insererClient()

    def insererClient(self):
        sql='INSERT INTO client VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        info=(self.__nomClient,self.__codePostal,self.__adresse,self.__statutJuridique
              ,self.__email,self.__observation,self.__tel,self.__numRC,self.__numNIF
              ,self.__numSuccurale,self.__numNIS,self.__numArticleImp,self.__dateExpRC
              ,self.__dateExpMandat,self.__numMandat)
        cur.execute(sql,info)
        db.commit()

    '''==================== Getters and Setters================='''
    def setNomClient(self,nomClient):
        self.__nomClient=nomClient
    def getNomClient(self):
        return self.__nomClient

    '''====================== Static Methods===================='''
    @staticmethod
    def rechClient(nomClient):
        sql='SELECT * FROM Client WHERE nom_client=%s'
        cur.execute(sql,(nomClient,))
        return cur.fetchone()

    @staticmethod
    def existeClient(nomClient):
        sql = 'SELECT nom_client FROM Client WHERE nom_client=%s'
        cur.execute(sql, (nomClient,))
        res=cur.fetchone()
        if res is None:
            return False
        else:
            return True

    @staticmethod
    def modifieClient(nomClient,codePostal,adresse,statutJuridique,email,observation,tel,numRC
                 ,numNIF,numSuccurale,numNIS,numArticleImp,dateExpRC,dateExpMandat,numMandat):
        sql='UPDATE client SET code_postal=%s,adresse=%s,statut_juridique=%s'\
        +',email=%s,observation=%s,tel=%s,num_rc=%s,num_nif=%s,num_succurale=%s,num_nis=%s'\
        +',num_article_imp=%s,date_exp_rc=%s,date_exp_mandat=%s,num_mandat=%s WHERE nom_client=%s'
        info=(codePostal,adresse,statutJuridique,email,observation,tel,numRC
                 ,numNIF,numSuccurale,numNIS,numArticleImp,dateExpRC,dateExpMandat,numMandat,nomClient)
        cur.execute(sql,info)
        db.commit()

    @staticmethod
    def supprimerClient(id):
        sql = 'DELETE FROM client WHERE nom_client =%s'
        cur.execute(sql,(id,))
        db.commit()

'''==============================Personne==========================='''



class Personne:
    def __init__(self, nom, prenom, datedenaissance, tele, type):
        self.__id = 0
        self.__nom = nom
        self.__prenom = prenom
        self.__dateDeNaissance = datedenaissance
        self.__tele = tele
        self.__type = type
        self.insererCettePersonne()

    def insererCettePersonne(self):
        sql = 'INSERT INTO Personne(nom,prenom,date_de_naissance,tele,type)' \
              + 'VALUES(%s,%s,%s,%s,%s)'
        cur.execute(sql, (self.__nom, self.__prenom, self.__dateDeNaissance, self.__tele, self.__type))
        db.commit()
        self.__id = cur.lastrowid

    '''==================== Getters and Setters================='''

    def getId(self):
        return self.__id

    def setId(self, attribute_id):
        self.__id = attribute_id

    @staticmethod
    def getName(id):
        sql='SELECT nom FROM personne WHERE id=%s'
        cur.execute(sql,(id,))
        return cur.fetchone()[0]


    '''====================== Static Methods===================='''

    @staticmethod
    def modifierPersonne(id, newNom, newPrenom, newDateDeNaissance, newTele,type):
        sql = 'UPDATE Personne SET nom=%s,prenom=%s,date_de_naissance=%s,tele=%s WHERE id=%s AND type=%s'
        cur.execute(sql, (newNom, newPrenom, newDateDeNaissance, newTele, id,type))
        db.commit()

    @staticmethod
    def rech(id):
        sql = 'SELECT * FROM Personne WHERE id=%s'
        cur.execute(sql, (id,))
        res = cur.fetchone()
        return res

    @staticmethod
    def supprimerPersonne(id):
        sql="DELETE FROM Personne WHERE id=%s"
        cur.execute(sql,(id,))
        db.commit()

'''=====================Expert===================='''



class Expert(Personne):
    def __init__(self, nom, prenom, dateDeNaissance, tele, domaine):
        super().__init__(nom, prenom, dateDeNaissance, tele,'expert')
        self.__idExpert = self.getId()
        self.__domaine = domaine
        self.insererCetExpert()

    def insererCetExpert(self):
        sql = 'INSERT INTO Expert VALUES(%s,%s)'
        cur.execute(sql, (self.__idExpert, self.__domaine))
        db.commit()

    '''==================== Getters and Setters================='''

    def getIdExpert(self):
        return self.__idExpert

    '''====================== Static Methods===================='''

    @staticmethod
    def rechExpert(id):
        sql = 'SELECT domaine FROM Expert WHERE id_expert=%s'
        cur.execute(sql, (id,))
        res= cur.fetchone()
        if res is None:
            return res
        else:
            res_=Personne.rech(id)+res
            return res_

    @staticmethod
    def existeExpert(id):
        sql = 'SELECT id_expert FROM Expert WHERE id_expert=%s'
        cur.execute(sql, (id,))
        res = cur.fetchone()
        if res is None:
            return False
        else:
            return True

    @staticmethod
    def modifierExpert(id, newNom, newPrenom, newDateDeNaissance, newTele, newDomaine):
        sql = 'UPDATE Expert SET domaine=%s WHERE id_expert=%s'
        cur.execute(sql, (newDomaine, id))
        db.commit()
        Personne.modifierPersonne(id,newNom,newPrenom,newDateDeNaissance,newTele,'expert')




'''=====================Utilisateur===================='''



class Utilisateur(Personne):
    def __init__(self, nom, prenom, dateDeNaissance, tele, password):
        super().__init__(nom, prenom, dateDeNaissance, tele, 'utilisateur')
        self.__idUtilisateur = self.getId()
        self.__password = password
        self.insererCetUtilisateur()

    def insererCetUtilisateur(self):
        sql = 'INSERT INTO Utilisateur VALUES(%s,%s)'
        cur.execute(sql, (self.__idUtilisateur, self.__password))
        db.commit()


    '''==================== Getters and Setters ================='''

    def getIdUtilisateur(self):
        return self.__idUtilisateur

    '''==================== Static Methods ================='''

    @staticmethod
    def rechUtilisateur(id):
        sql = 'SELECT password FROM Utilisateur WHERE id_utilisateur=%s'
        cur.execute(sql, (id,))
        res = cur.fetchone()
        if res is None:
            return res
        else:
            sql = 'SELECT * FROM Personne WHERE id=%s'
            cur.execute(sql, (id,))
            res_ = cur.fetchone() + res
            return res_

    @staticmethod
    def modifierUtilisateur(id, newNom, newPrenom, newDateDeNaissance, newTele, newPassword):
        sql = 'UPDATE Utilisateur SET password=%s WHERE id_utilisateur=%s'
        cur.execute(sql, (newPassword, id))
        db.commit()
        Personne.modifierPersonne(id,newNom,newPrenom,newDateDeNaissance,newTele,'utilisateur')

    @staticmethod
    def login(id,pw):
        sql ='SELECT * FROM utilisateur WHERE id_utilisateur=%s AND password=%s'
        cur.execute(sql,(id,pw))
        if cur.fetchone() is None:
            return False
        else:
            return True



'''=====================Chauffeur===================='''



class Chauffeur(Personne):
    def __init__(self, nom, prenom, dateDeNaissance, tele):
        super().__init__(nom, prenom, dateDeNaissance, tele, 'chauffeur')
        self.__idChauffeur = self.getId()
        self.insererCeChauffeur()

    def insererCeChauffeur(self):
        sql = 'INSERT INTO Chauffeur VALUES(%s)'
        cur.execute(sql, (self.__idChauffeur,))
        db.commit()

    '''==================== Getters and Setters================='''

    def getIdChauffeur(self):
        return self.__idChauffeur

    '''====================== Static Methods===================='''

    @staticmethod
    def rechChaffeur(id):
        sql = "SELECT * FROM personne WHERE id=%s AND type='chauffeur'"
        cur.execute(sql, (id,))
        return cur.fetchone()

    @staticmethod
    def modifierChauffeur(id, newNom, newPrenom, newDateDeNaissance, newTele):
        sql = "UPDATE Personne SET nom=%s,prenom=%s,date_de_naissance=%s tele=%s WHERE id=%s AND type='chauffeur'"
        cur.execute(sql, (newNom, newPrenom, newDateDeNaissance, newTele, id))



'''=====================Douanier===================='''


class Douanier(Personne):
    def __init__(self, nom, prenom, dateDeNaissance, tele):
        super().__init__(nom, prenom, dateDeNaissance, tele,'douanier')
        self.__idDouanier = self.getId()
        self.insererCeDouanier()

    def insererCeDouanier(self):
        sql = 'INSERT INTO Douanier VALUES(%s)'
        cur.execute(sql, (self.__idDouanier,))
        db.commit()

    '''==================== Getters and Setters================='''

    def getIdDouanier(self):
        return self.__idDouanier

    '''====================== Static Methods===================='''

    @staticmethod
    def rechDouanier(id):
        sql = "SELECT * FROM personne WHERE id=%s AND type='douanier'"
        cur.execute(sql, (id,))
        return cur.fetchone()

    @staticmethod
    def modifierDouanier(id, newNom, newPrenom, newDateDeNaissance, newTele):
        Personne.modifierPersonne(id,newNom,newPrenom,newDateDeNaissance,newTele,'douanier')

'''=====================Declarant===================='''


class Declarant(Personne):
    def __init__(self, nom, prenom, dateDeNaissance, tele):
        super().__init__(nom, prenom, dateDeNaissance, tele,'declarant')
        self.__idDeclarant = self.getId()
        self.insererCeDeclarant()

    def insererCeDeclarant(self):
        sql = 'INSERT INTO Declarant VALUES(%s)'
        cur.execute(sql, (self.__idDeclarant,))
        db.commit()

    '''==================== Getters and Setters================='''

    def getIdDeclarant(self):
        return self.__idDeclarant

    '''====================== Static Methods===================='''

    @staticmethod
    def rechDeclarant(id):
        sql = "SELECT * FROM personne WHERE id=%s AND type='declarant'"
        cur.execute(sql, (id,))
        return cur.fetchone()

    @staticmethod
    def modifierDeclarant(id, newNom, newPrenom, newDateDeNaissance, newTele):
        Personne.modifierPersonne(id,newNom,newPrenom,newDateDeNaissance,newTele,'declarant')
    '''    sql = "UPDATE Personne SET nom=%s,prenom=%s,date_de_naissance=%s tele=%s WHERE id=%s AND type='declarant'"
        cur.execute(sql, (newNom, newPrenom, newDateDeNaissance, newTele, id))
        db.commit()'''



'''=====================Representant===================='''

class Representant(Personne):
    def __init__(self, nom, prenom, dateDeNaissance, tele, id_client):
        super().__init__(nom, prenom, dateDeNaissance, tele, 'representant')
        self.__idRepresentant = self.getId()
        self.__idClient = id_client
        self.insererCeRepresentant()

    def insererCeRepresentant(self):
        sql = 'INSERT INTO Representant VALUES(%s,%s)'
        if Client.existeClient(self.__idClient):
            cur.execute(sql, (self.__idRepresentant, self.__idClient))
            db.commit()
        else:
            print("ERROR Client doesnt exist")

    '''==================== Getters and Setters================='''

    def getIdRepresentant(self):
        return self.__idRepresentant

    '''====================== Static Methods===================='''

    @staticmethod
    def rechRepresentant(id):
        sql = 'SELECT id_client FROM Representant WHERE id_representant=%s'
        cur.execute(sql, (id,))
        res = cur.fetchone()
        if res is None:
            return res
        else:
            res_ =  Personne.rech(id) +res
            return res_

    @staticmethod
    def modifierRepresentant(id, newNom, newPrenom, newDateDeNaissance, newTele, id_client):
        sql = 'UPDATE representant SET id_client=%s WHERE id_representant=%s'
        cur.execute(sql, (id_client, id))
        db.commit()
        Personne.modifierPersonne(id,newNom,newPrenom,newDateDeNaissance,newTele,'representant')






'''_____________________________Monnaie________________________________________'''
'''****************************************************************************'''


class Monnaie:
    def __init__(self, code_monnaie, nom_pay):
        self.__code_monnaie = code_monnaie
        self.__nom_pay = nom_pay
        self.inserer_monnaie()

    '''__________setters and getters____________'''

    def set_id_monnaie(self, attribute_id):
        self.__code_monnaie = attribute_id

    def get_id_monnaie(self):
        return self.__code_monnaie

    def get_tuple_monnaie(self):
        return (self.__nom_pay)

    '''___________insertion____________'''

    def inserer_monnaie(self):
        sql = 'INSERT INTO Monnaie(code_monnaie,nom_pay)' \
              + 'VALUES(%s,%s)'
        cur.execute(sql, (self.__code_monnaie,self.__nom_pay))
        db.commit()

    '''___________static methods----------'''

    @staticmethod
    def recherche_monnaie(code_monnaie):
        sql = 'SELECT * FROM Monnaie WHERE code_monnaie = %s'
        cur.execute(sql, (code_monnaie,))
        res = cur.fetchone()
        return res

    @staticmethod
    def modifier_monnaie(code_monnaie, new_nom_pay):
        sql = 'UPDATE Monnaie SET code_monnaie=%s, nom_pay=%s WHERE code_monnaie =%s'
        cur.execute(sql, (code_monnaie,new_nom_pay,code_monnaie))
        db.commit()
    @staticmethod
    def supprimer_monnaie(code_monnaie):
        sql = 'DELETE FROM Monnaie WHERE code_monnaie=%s'
        cur.execute(sql, (code_monnaie,))
        db.commit()


'''_____________________________Nature_Marchandise________________________________________'''
'''****************************************************************************'''



class Nature_Marchandise:
    def __init__(self, nature):
        self.__nature = nature
        self.inserer_nature_marchandise()

    '''__________setters and getters____________'''

    def set_id_marchandise(self, attribute_id):
        self.__nature = attribute_id
    def get_id_marchandise(self):
        return self.__nature

    def get_tuple_marchandise(self):
        return (self.__nature, )

    '''___________insertion___________'''

    def inserer_nature_marchandise(self):
        sql = 'INSERT INTO Nature_Marchandise(nature)' \
              + 'VALUES(%s)'
        cur.execute(sql, (self.__nature,))
        db.commit()

    '''____________static methods_________'''

    @staticmethod
    def recherche_nature_marchandise(nature):
        sql = 'SELECT * FROM Nature_Marchandise WHERE nature=%s'
        cur.execute(sql, (nature,))
        res = cur.fetchone()
        return res

    @staticmethod
    def modifier_nature_marchandise(nature, new_nature):
        sql = 'UPDATE nature SET nature=%s WHERE nature=%s '
        cur.execute(sql, (new_nature, nature))
        db.commit()

    @staticmethod
    def supprimer_nature_marchandise(nature):
        sql = 'DELETE  FROM Nature_Marchandise WHERE nature=%s'
        cur.execute(sql, (nature,))
        db.commit()


'''_____________________________Intermediaire________________________________________'''
'''****************************************************************************'''








class Intermediaire:
    def __init__(self,nom_intr,typ):
        self.__nom_inter=nom_intr
        self.__type=typ
        self.inserer_intermediaire()

    '''__________ setters and getters ____________'''

    def get_nom_inter(self):
        return self.__nom_inter
    def get_type(self):
        return self.__type

    def set_infos(self, n_nominter, n_type):
        self.__nom_inter = n_nominter
        self.__type = n_type

    '''__________ static_methods ____________'''

    @staticmethod
    def existe_intermediaire(nintern):
        sql = 'SELECT nom_inter FROM Intermediaire WHERE nom_inter=%s'
        cur.execute(sql, (nintern,))
        res = cur.fetchone()
        if res is None:
            return False
        else:
            return True
    @staticmethod
    def rech_intermediaire(nom_inter):
        sql='SELECT * FROM Intermediaire WHERE nom_inter =%s'
        cur.execute(sql,(nom_inter,))
        res=cur.fetchone()
        return res

    def inserer_intermediaire(self):
        self.__sql='INSERT INTO intermediaire(nom_inter,type)'\
                   +' VALUES (%s,%s)'
        cur.execute(self.__sql,(self.__nom_inter,self.__type))
        db.commit()
    @staticmethod
    def modifier_intermediaire(a_intr,n_intr,n_type):
        sql='UPDATE Intermediaire SET nom_inter=%s,type=%s WHERE nom_inter=%s '
        cur.execute(sql,(n_intr,n_type,a_intr))
        db.commit()
    @staticmethod
    def supprimer_intermediaire(inter):
        sql = 'DELETE FROM intermediaire WHERE nom_inter=%s'
        cur.execute(sql,(inter,))
        db.commit()




'''_____________________________Fournisseur________________________________________'''
'''****************************************************************************'''




class Fournisseur:
    def __init__(self,nomfourn,adrs):
        self.nom_fournisseur=nomfourn
        self.adresse=adrs
        self.inserer()


    '''_____________ setters and getters __________________________'''

    def get_nomfourn(self):
        return self.nom_fournisseur

    def get_adaress(self):
        return self.adresse

    def set_infos(self,n_nomfourn,n_adresse):
        self.nom_fournisseur=n_nomfourn
        self.adresse=n_adresse


    '''__________________ static methods _____________________'''


    @staticmethod
    def existe_fournisseur(nfourn):
        sql = 'SELECT nom_fournisseur FROM Fournisseur WHERE nom_fournisseur=%s'
        cur.execute(sql,(nfourn,))
        res = cur.fetchone()
        if res is None:
            return False
        else:
            return True


    @staticmethod
    def rech_Fournisseur(nom_four):
        sql='SELECT * FROM Fournisseur WHERE nom_fournisseur =%s'
        cur.execute(sql,(nom_four,))
        res=cur.fetchone()
        return res

    def inserer(self):
        self.__sql='INSERT INTO Fournisseur(nom_fournisseur,adresse)'\
                   +' VALUES (%s,%s)'
        cur.execute(self.__sql,(self.nom_fournisseur,self.adresse))
        db.commit()

    @staticmethod
    def modifier_Fournisseur(a_fourn,n_fourn,n_adr):
        sql='UPDATE Fournisseur SET nom_fournisseur=%s,adresse=%s WHERE nom_fournisseur=%s '
        cur.execute(sql,(n_fourn,n_adr,a_fourn))
        db.commit()

    @staticmethod
    def supprimer_Fournisseur(fourn):
        sql = 'DELETE FROM Fournisseur WHERE nom_fournisseur=%s'
        cur.execute(sql,(fourn,))
        db.commit()



'''_____________________________Pays________________________________________'''
'''****************************************************************************'''



class Pays:
    def __init__(self,codePays,nomPays):
        self.__code_pays=codePays
        self.__nom_pays=nomPays
        self.inserer_pays()


    '''_______________setters and getters______________'''


    def get_idpays(self):
        return self.__code_pays
    def get_nompays(self):
        return self.__nom_pays
    def set_pays(self,pay):
        self.__nom_pays=pay

    '''______________insertion___________________'''

    def inserer_pays(self):
        self.__sql='INSERT INTO pays(code_pays,nom_pays) VALUES (%s,%s)'
        cur.execute(self.__sql,(self.__code_pays,self.__nom_pays))
        db.commit()

    '''_________________Static methods______________________'''

    @staticmethod
    def rech_pays(id):
        sql='SELECT * FROM pays WHERE code_pays=%s'
        cur.execute(sql,(id,))
        res=cur.fetchone()
        return res

    @staticmethod
    def modifier_pays(code,nom):
        sql='UPDATE pays SET code_pays=%s, nom_pays=%s WHERE code_pays=%s'
        cur.execute(sql,(code,nom,code))
        db.commit()

    @staticmethod
    def supprimer_pay(pays):
        sql = 'DELETE FROM pays WHERE code_pays=%s'
        cur.execute(sql,(pays,))
        db.commit()

    @staticmethod
    def existe_pay(pay):
        sql = 'SELECT nom_pays FROM pays WHERE code_payss=%s'
        cur.execute(sql,(pay,))
        res = cur.fetchone()
        if res is None:
            return False
        else:
            return True


'''-------------------------------------Dossier---------------------------'''

class Dossier:
    # Constructeur
    def __init__(self, idClient, dateOuverture, dateArrive, nbConteneur,
                 statutDossier, idFour, idDeclarant, idPays, idCompTrans, titreTrans, navire, nomPort,
                 SG, idLieuEntrepot, observation, natureDossier, gros, article, codeMonnaie, idFichiers):
        self.__id_dossier = 0
        self.__idClient = idClient
        self.__dateOuverture = dateOuverture
        self.__dateArrive = dateArrive
        self.__dateFermeture = None
        self.__idFour = idFour
        self.__nbConteneur = nbConteneur
        self.__idCompTrans = idCompTrans
        self.__statutDossier = statutDossier
        self.__titreTrans = titreTrans
        self.__gros = gros
        self.__article = article
        self.__idDeclarant = idDeclarant
        self.__idFour = idFour
        self.__navire = navire
        self.__nomPort = nomPort
        self.__SG = SG
        self.__idLieuEntrepot = idLieuEntrepot
        self.__observation = observation
        self.__natureDossier = natureDossier
        self.__idPays = idPays
        self.__codeMonnaie = codeMonnaie
        self.__idFichiers = idFichiers
        self.insererCeDossier()

    # Getters and Setters
    def setIDdossier(self, id):
        self.__id_dossier = id

    def setStatutDossier(self, statutDossier):
        self.__statutDossier = statutDossier

    def setDateFermeture(self, dateFermeture):
        self.__dateFermeture = dateFermeture

    def setDateOuverture(self, dateOuverture):
        self.__dateOuverture = dateOuverture

    def getIdDossier(self):
        return self.__id_dossier
    def getTupleDossier(self):
        return (self.__idClient,self.__idDeclarant, self.__dateOuverture, self.__dateArrive,
                self.__dateFermeture, self.__navire,self.__nbConteneur,self.__statutDossier,self.__idFour,self.__idPays,
                self.__idCompTrans,self.__titreTrans,self.__nomPort,self.__SG,self.__idLieuEntrepot,self.__observation,
                self.__natureDossier,self.__gros, self.__article, self.__codeMonnaie, self.__idFichiers)
    # Méthodes pour ce dossier (l'objet lui meme)
    def insererCeDossier(self):
        sql = "INSERT INTO dossier (id_client,id_declarant,date_ouverture,"\
            "date_arrivee,date_fermeture,navire,"\
            "nb_conteneurs,statut_dossier,id_four,id_pays,"\
            "id_comp_trans,titre_trans,nom_port,SG,"\
            "id_lieu_entrepot,observation ,nature_dossier,"\
            "gros ,article ,code_monnaie ,id_fichiers) "\
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        cur.execute(sql,self.getTupleDossier())
        self.setIDdossier(cur.lastrowid)
        db.commit()

    def existeCeDossier(self):
        sql = 'SELECT * FROM dossier WHERE id_dossier = {}'.format(self.getIdDossier())
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return False
        else:
            return True

    def modifierCeDossier(self):
        sql = "UPDATE dossier SET id_client= %s,id_declarant=%s, date_ouverture= %s, date_arrivee=%s, date_fermeture=%s," \
              "navire=%s,nb_conteneurs=%s, statut_dossier=%s, id_four=%s, id_pays=%s," \
              "id_comp_trans=%s, titre_trans=%s, nom_port=%s," \
              "SG = %s, id_lieu_entrepot = %s, observation = %s, nature_dossier = %s, gros=%s," \
              "article = %s, code_monnaie=%s,id_fichiers=%s WHERE id_dossier={}".format(self.getIdDossier())
        cur.execute(sql, self.getTupleDossier())
        db.commit()

    def fermerCeDossier(self):
        date = datetime.now()
        sql = "UPDATE dossier SET date_fermeture = '{}', statut_dossier = 'Archivé' WHERE id_dossier = {}".format(date,self.getIdDossier())
        cur.execute(sql)
        db.commit()
        self.setStatutDossier("Archivé")
        self.setDateFermeture(date)

    def ouvrirCeDossier(self):
        date = datetime.now()
        sql = "UPDATE dossier SET date_ouverture = '{}', statut_dossier = 'En cours' WHERE id_dossier = {}".format(date,self.getIdDossier())
        cur.execute(sql)
        db.commit()
        self.setStatutDossier("En cours")
        self.setDateOuverture(date)

    def supprimerCeDossier(self):
        sql = 'DELETE FROM dossier WHERE id_dossier = {}'.format(self.getIdDossier())
        cur.execute(sql)
        self.setIDdossier(0)
        db.commit()

    # Méthodes statiques

    @staticmethod
    def rechercherDossier(id):
        sql = 'SELECT * FROM dossier WHERE id_dossier = {}'.format(id)
        cur.execute(sql)
        res = cur.fetchone()
        return res

    @staticmethod
    def modifierDossier(id, idClient, dateOuverture, dateArrive, dateFermeture, nbConteneur,
                        statutDossier, idFour, idDeclarant, idPays, idCompTrans, titreTrans, navire, nomPort,
                        SG, idLieuEntrepot, observation, natureDossier, gros, article,code_monnaie,id_fichiers):
        sql = 'UPDATE dossier SET id_client= %s, date_ouverture= %s, date_arrivee=%s, date_fermeture=%s, ' \
              + 'nb_conteneurs=%s, statut_dossier=%s, id_four=%s, id_declarant=%s, id_pays=%s,' \
              + ' id_comp_trans=%s, titre_trans=%s, navire=%s, nom_port=%s,' \
                'SG = %s, id_lieu_entrepot = %s, observation = %s, nature_dossier = %s, gros=%s,' \
                'article = %s,code_monnaie=%s,id_fichiers=%s WHERE id_dossier={}'.format(id)
        cur.execute(sql, (idClient, dateOuverture, dateArrive, dateFermeture, nbConteneur,
                          statutDossier, idFour, idDeclarant, idPays, idCompTrans, titreTrans, navire, nomPort,
                          SG, idLieuEntrepot, observation, natureDossier, gros, article,code_monnaie,id_fichiers))
        db.commit()

    @staticmethod
    def existerDossier(id):
        sql = 'SELECT id_dossier FROM dossier WHERE id_dossier =%s'
        cur.execute(sql,(id,))
        result = cur.fetchone()
        if result is None:
            return False
        else:
            return True

    @staticmethod
    def supprimerDossier(id):
        sql = 'DELETE FROM dossier WHERE id_dossier = {}'.format(id)
        cur.execute(sql)
        db.commit()

    @staticmethod
    def fermerDossier(id):
        date = datetime.now()
        sql = "UPDATE dossier SET date_fermeture = '{}', statut_dossier = 'Archivé' WHERE id_dossier = {}".format(date, id)
        cur.execute(sql)
        db.commit()

    @staticmethod
    def ouvrirDossier(id):
        date = datetime.now()
        sql = "UPDATE dossier SET date_ouverture = '{}', statut_dossier = 'En cours' WHERE id_dossier = {}".format(date, id)
        cur.execute(sql)
        db.commit()



'''_____________________________Facture________________________________________'''
'''****************************************************************************'''





class Factur:

    def __init__(self, idDossier, date, TVA, total_prestation, total_debours, droit_timbre, etat_paiement, mode_paiement):
        self.__id = 0
        self.__idDossier = idDossier
        self.__date = date
        self.__TVA = TVA
        self.__total_prestation = total_prestation
        self.__total_debours = total_debours
        self.__droit_timbre = droit_timbre
        self.__etat_paiement = etat_paiement
        self.__mode_paiement = mode_paiement
        self.inserer_une_facture()

    '''__________setters and getters____________'''

    def set_id_facture(self, attribute_id):
        self.__id = attribute_id

    def get_id_facture(self):
        return self.__id

    def get_tuple_facture(self):
        return(self.__idDossier, self.__date, self.__TVA, self.__total_prestation, self.__total_debours, self.__droit_timbre, self.__etat_paiement, self.__mode_paiement)

    ''' _____________ insertion __________________'''

    def inserer_une_facture(self):
        sql = 'INSERT INTO Faacturess(idDossier,date,TVA,total_prestation,total_debours,droit_timbre,etat_paiement,mode_paiement) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql, (self.__idDossier, self.__date, self.__TVA, self.__total_prestation, self.__total_debours, self.__droit_timbre, self.__etat_paiement, self.__mode_paiement))
        self.set_id_facture(cur.lastrowid)
        db.commit()

    '''_______________ static methods _________________'''
    @staticmethod
    def recherche_facture(id):
        sql = 'SELECT * FROM Faacturess WHERE id=%s'
        cur.execute(sql, (id,))
        res = cur.fetchone()
        return res

    @staticmethod
    def facture_existe(id):
        sql = 'SELECT * FROM Faacturess WHERE id= %s'
        cur.execute(sql, (id,))
        res = cur.fetchone()
        if res is None:
            return False
        else:
            return True

    @staticmethod
    def modifier_une_facture(id, idDossier, date, tva, totprest, totdebours, droitT, etat, mode):
        sql = 'UPDATE Faacturess SET idDossier=%s, date=%s, TVA=%s, total_prestation=%s, total_debours=%s, droit_timbre=%s, etat_paiement=%s, mode_paiement=%s WHERE id=%s'
        cur.execute(sql, (idDossier, date, tva, totprest, totdebours, droitT, etat, mode, id))
        db.commit()

    @staticmethod
    def supprimer_facture(id):
        sql = 'DELETE FROM Faacturess WHERE id=%s'
        cur.execute(sql, (id,))
        db.commit()


'''_____________________________Camion________________________________________'''
'''****************************************************************************'''




class Camion:
    def __init__(self, matricule):
        self.__matricule = matricule
        self.inserer_matricule()

    '''__________setters and getters____________'''

    def set_matricule(self, attribute_id):
        self.__matricule = attribute_id

    def get_matricule(self):
        return self.__matricule

    def get_tuple_camion(self):
        return (self.__matricule,)

    '''___________insertion___________'''

    def inserer_matricule(self):
        sql = 'INSERT INTO Camion(matricule)' \
              + 'VALUES(%s)'
        cur.execute(sql, (self.__matricule,))
        db.commit()

    '''____________static methods_________'''

    @staticmethod
    def recherche_Camion(matricule):
        sql = 'SELECT * FROM Camion WHERE matricule=%s'
        cur.execute(sql, (matricule,))
        res = cur.fetchone()
        return res

    @staticmethod
    def modifier_Camion(matricule, new_matricule):
        sql = 'UPDATE Camion SET matricule=%s WHERE matricule=%s '
        cur.execute(sql, (new_matricule, matricule))
        db.commit()

    @staticmethod
    def supprimer_Camion(matricule):
        sql = 'DELETE FROM Camion WHERE matricule=%s'
        cur.execute(sql, (matricule,))
        db.commit()


'''===========================Class Bon========================'''



class Bon:
    def __init__(self,idDossier,type,numBon,dateBon,pc):
        self.__idDossier=idDossier
        self.__type=type
        self.__numBon=numBon
        self.__dateBon=dateBon
        self.__pc=pc
        self.insererBon()

    def insererBon(self):
        if Dossier.existerDossier(self.__idDossier):
            sql="INSERT INTO BON VALUES(%s,%s,%s,%s,%s)"
            info=(self.__idDossier,self.__type,self.__numBon,self.__dateBon,self.__pc)
            cur.execute(sql,info)
            db.commit()
        else:
            print("ERROR idDossier doesnt existe")

    @staticmethod
    def rechBon(id,type):
        sql="SELECT * FROM Bon WHERE id=%s AND type=%s"
        cur.execute(sql,(id,type))
        res=cur.fetchone()
        return res

    @staticmethod
    def modifieBon(id,type,newNumBon,newDateBon,newPC):
        sql="UPDATE Bon SET num_bon=%s,date_bon=%s,pc=%s WHERE id_dossier=%s AND type=%s"
        cur.execute(sql,(newNumBon,newDateBon,newPC,id,type))
        db.commit()



class BonSortie(Bon):
    def __init__(self,idDossier,numBon,dateBon,pc,idChauffeur,matricule):
        super().__init__(idDossier, 'sortie', numBon, dateBon, pc)
        self.__idDossier=idDossier
        self.__idChauffeur=idChauffeur
        self.__matricule=matricule
        self.insererBonSortie()

    def insererBonSortie(self):
        sql = "INSERT INTO Bon_sortie VALUES(%s,%s,%s)"
        cur.execute(sql, (self.__idDossier, self.__idChauffeur, self.__matricule))
        db.commit()


    @staticmethod
    def rechBonSortie(id):
        sql="SELECT id_chauffeur,matricule FROM Bon_sortie WHERE id_dossier=%s"
        cur.execute(sql,(id,))
        res=cur.fetchone()
        if res in None:
            return res
        else:
            res_=Bon.rechBon(id,'sortie') + res
            return res_

    @staticmethod
    def modifieBonSortie(idDossier,newNumBon,newDateBon,newPC,newMatricule,newIdChauffeur):
        sql = "UPDATE Bon_sortie SET id_chauffeur=%s , matricule=%s WHERE id_Dossier=%s"
        cur.execute(sql,(newIdChauffeur,newMatricule,idDossier))
        db.commit()
        Bon.modifieBon(idDossier,'sortie',newNumBon,newDateBon,newPC)



class BonVisite(Bon):
    def __init__(self, idDossier, numBon, dateBon, pc, idDouanier, idBureauDouane):
        super().__init__(idDossier, 'visite', numBon, dateBon, pc)
        self.__idDossier = idDossier
        self.__idDouanier = idDouanier
        self.__idBureauDouane = idBureauDouane
        self.insererBonVisite()

    def insererBonVisite(self):
        sql = "INSERT INTO Bon_visite VALUES(%s,%s,%s)"
        cur.execute(sql, (self.__idDossier, self.__idDouanier, self.__idBureauDouane))
        db.commit()

    @staticmethod
    def rechBonVisite(id):
        sql = "SELECT id_douanier,bureau_douane FROM Bon_visite WHERE id_dossier=%s"
        cur.execute(sql, (id,))
        res = cur.fetchone()
        if res in None:
            return res
        else:
            res_ = Bon.rechBon(id, 'visite') + res
            return res_

    @staticmethod
    def modifieBonVisite(idDossier, newNumBon, newDateBon, newPC, newIdBureauDouane, newIdDouanier):
        sql = "UPDATE Bon_visite SET id_douanier=%s , bureau_douane=%s WHERE id_Dossier=%s"
        cur.execute(sql, (newIdDouanier, newIdBureauDouane, idDossier))
        db.commit()
        Bon.modifieBon(idDossier, 'visite', newNumBon, newDateBon, newPC)




class marchandise:
    def __init__(self, id_marchandise, poids, num_facture,
                 nature, montant, id_dossier, id_emballage, description):
        self.__id_marchandise = id_marchandise
        self.__poids = poids
        self.__num_facture = num_facture
        self.__nature = nature
        self.__montant = montant
        self.__id_dossier = id_dossier
        self.__id_emballage = id_emballage
        self.__description = description
        self.inserer_marchandise()

    def inserer_marchandise(self):
        sql = 'INSERT INTO marchandise(id_marchandise,poids,num_facture,nature,montant,id_dossier,id_emballage,description)' \
              + 'VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql, (
        self.__id_marchandise, self.__poids, self.__num_facture, self.__nature, self.__montant, self.__id_dossier,
        self.__id_emballage, self.__description))
        db.commit()

    def update_marchandise(self):
        sql = 'UPDATE marchandise SET poids=%s,num_facture=%s,nature=%s,montant=%s,id_dossier=%s,id_emballage=%s,description=%s WHERE id_marchandise=%s'
        cur.execute(sql, (
        self.__poids, self.__num_facture, self.__nature, self.__montant, self.__id_dossier, self.__id_emballage,
        self.__description, self.__id_marchandise))
        db.commit()

    @staticmethod
    def modifier_marchandise(id_marchandise, new_poids, new_num_facture, new_nature, new_montant, new_id_dossier,
                             new_id_emballage, new_description):
        sql = 'UPDATE marchandise SET poids=%s,num_facture=%s,nature=%s,montant=%s,id_dossier=%s,id_emballage=%s,description=%s WHERE id_marchandise=%s'
        cur.execute(sql, (
        new_poids, new_num_facture, new_nature, new_montant, new_id_dossier, new_id_emballage, new_description,
        id_marchandise))
        db.commit()

    @staticmethod
    def rech_marchandise(id_marchandise):
        sql = 'SELECT * FROM marchandise WHERE id_marchandise=%s'
        cur.execute(sql, (id_marchandise,))
        res = cur.fetchone()
        return res

    def get_poids(self):
        return self.__poids

    def set_poids(self, poids):
        self.__poids = poids


class emballage:
    def __init__(self, id_emballage, genre, typee, pieds, id_dossier):
        self.__id_emballage = id_emballage
        self.__genre = genre
        self.__type = typee
        self.__pieds = pieds
        self.__id_dossier = id_dossier
        self.inserer_emballage()

    def inserer_emballage(self):
        sql = 'INSERT INTO emballage(id_emballage,genre,type,pieds,id_dossier)' \
              + 'VALUES(%s,%s,%s,%s,%s)'
        cur.execute(sql, (self.__id_emballage, self.__genre, self.__type, self.__pieds, self.__id_dossier))
        db.commit()

    def update_emballage(self):
        sql = 'UPDATE emballage SET genre=%s,type=%s,pieds=%s WHERE (id_emballage=%s AND id_dossier =%s)'
        cur.execute(sql, (self.__genre, self.__type, self.__pieds, self.__id_emballage, self.__id_dossier))
        db.commit()

    @staticmethod
    def modifier_emballage(id_emballage, new_genre, new_typee, new_pieds, id_dossier):
        sql = 'UPDATE emballage SET genre=%s,type=%s,pieds=%s WHERE (id_emballage=%s AND id_dossier =%s)'
        cur.execute(sql, (new_genre, new_typee, new_pieds, id_emballage, id_dossier))
        db.commit()

    @staticmethod
    def rech_emballage(id_emballage):
        sql = 'SELECT * FROM emballage WHERE id_emballage=%s'
        cur.execute(sql, (id_emballage,))
        res = cur.fetchone()
        return res

    def set_genre(self, genre):
        self.__genre = genre



'''_____________________________Designation________________________________________'''
'''****************************************************************************'''



class Designation:
    def __init__(self,nomDesignation, type,idMarchandise):
        self.__nom_designation = nomDesignation
        self.__type = type
        self.__idMarchandise=idMarchandise
        self.inserer_designation()

    '''__________setters and getters____________'''

    def set_nom_desifnation(self, attribute_nom):
        self.__nom_designation = attribute_nom

    def get_nom_designation(self):
        return self.__nom_designation

    def get_tuple_designation(self):
        return(self.__nom_designation,self.__type,self.__idMarchandise)

    '''___________insertion_____________'''

    def inserer_designation(self):
        sql = 'INSERT INTO Designation(nom_designation,type,id_marchandise)' \
              + 'VALUES(%s,%s, %s)'
        cur.execute(sql, (self.__nom_designation,self.__type,self.__idMarchandise))
        db.commit()

    '''____________static methods___________'''

    @staticmethod
    def recherche_designation(nom_designation):
        sql = 'SELECT * FROM Designation WHERE nom_designation=%s'
        cur.execute(sql, (nom_designation,))
        res = cur.fetchone()
        return res

    @staticmethod
    def modifier_designation(nom_designation, newType, newidMarchandise):
        sql = 'UPDATE pays SET type=%s , id_marchandise=%s WHERE nom_designation=%s '
        cur.execute(sql, (newType, newidMarchandise, nom_designation))
        db.commit()

    @staticmethod
    def supprimer_designation(nom_designation):
        sql = 'DELETE FROM Designation WHERE nom_designation=%s'
        cur.execute(sql, (nom_designation,))
        db.commit()
"""
####### insertion des exemples dans la db

c = Client('samir',16004,'oued smar','SARL','samir@mail.com','this is an observation',
           213677777777,15,20,12,13,15,datetime.now(),datetime.now(),'this is num mondat')
c = Client('said',16004,'oued smar','SARL','said@mail.com','this is an observation',
           213677777777,15,20,12,13,15,datetime.now(),datetime.now(),'this is num mondat')
c = Client('fouad',16004,'oued smar','SARL','fouad@mail.com','this is an observation',
           213677777777,15,20,12,13,15,datetime.now(),datetime.now(),'this is num mondat')
four = Fournisseur('ali','beb ezouar')
four = Fournisseur('omar','beb ezouar')
four = Fournisseur('wail','beb ezouar')
dec = Declarant('dallou','houssine',datetime.now(),788888888)
dec = Declarant('balla','ourida',datetime.now(),788888888)
dec = Declarant('fouzra','melissa',datetime.now(),788888888)
pays = Pays(12,'Turkie')
pays = Pays(13,'chine')
pays = Pays(15,'espagne')
int = Intermediaire('1er intermediaire','type inter')
int = Intermediaire('2e intermediaire','type inter')
int = Intermediaire('3e intermediaire','type inter')
cm = Monnaie('eur','espagne')
cm = Monnaie('dollar','etats unis')
fich = Fichier('c:\drive\ffolder')
fich = Fichier("d:\folder\fich")

d= Dossier('samir',datetime.now(),datetime.now(),15,'En cours','ali',1,12,'1er intermediaire',
           'titretrans','navire','port','this is SG',
           'lieu entrepot','this is observation','Import','gros','this is an article','eur',1)
d= Dossier('fouad',datetime.now(),datetime.now(),15,'En cours','omar',1,13,'2e intermediaire',
           'titretrans','navire','port','this is SG',
           'lieu entrepot','this is observation','Import','gros','this is an article','dollar',1)
d= Dossier('said',datetime.now(),datetime.now(),15,'En cours','wail',1,15,'3e intermediaire',
           'titretrans','navire','port','this is SG',
           'lieu entrepot','this is observation','Import','gros','this is an article','dollar',1)
doua = Douanier('dhawat','djamel',datetime.now(),544444444)
doua = Douanier('daki','jawad',datetime.now(),55555555)
bv= BonVisite(1,1,datetime.now(),'pc05',4,'2e intermediaire')
bv= BonVisite(2,1,datetime.now(),'pc05',5,'3e intermediaire')
c= Chauffeur('ali','jamel',datetime.now(),566666666)
c= Chauffeur('mourad','jameli',datetime.now(),544444444)
camion = Camion(1690812345)
camion = Camion(2390512345)
bs = BonSortie(3,1,datetime.now(),'assus',6,1690812345)
bs = BonSortie(2,15,datetime.now(),'hjks',7,2390512345)
emb = emballage(1,'genre emb','type emb','pieds emb',1)
emb = emballage(2,'genre emb','type emb','pieds emb',2)
marcha = marchandise(1,800,'numfact','naturemar',63.5,1,1,'this is a description')
marcha = marchandise(2,800,'numfact','naturemar',63.5,3,2,'this is a description')
design = Designation('design1','type design',1)
design = Designation('design2','type design',2)
exp = Expert('hayani','mohamed',datetime.now(),798989898,'un domaine')
exp = Expert('bacha','fouzia',datetime.now(),674747474,'un domaine')
facture = Factur(2,datetime.now(),198.35,55.23,25.23,154,'payé','carte')
facture = Factur(3,datetime.now(),200.35,99.77,24.58,154,'non payé','liquide')
repr = Representant('adimi','dania',datetime.now(),788998899,'fouad')
repr = Representant('fouzari','ryma',datetime.now(),788998899,'said')
user = Utilisateur('adjal','mehdi',datetime.now(),566446644,'pass')
user = Utilisateur('benraya','aymen',datetime.now(),566446644,'123564')
user = Utilisateur('marya','mitiche',datetime.now(),566446644,'pass2008')
natma = Nature_Marchandise('nature march01')
natma = Nature_Marchandise('nature march02')
d= Dossier('7amid',datetime.now(),datetime.now(),15,'En cours','ali',1,12,'1er intermediaire',
           'titretrans','navire','port','this is SG',
           'lieu entrepot','this is observation','Import','gros','this is an article','eur',2)
"""
