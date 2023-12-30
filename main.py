import sys
import os
from cryptography.fernet import Fernet
import mysql.connector
from PyQt5.QtWidgets import *
from ui_ui_version_7_18 import Ui_MainWindow
from formm import Ui_Form_2
from login import Ui_Form
from PyQt5 import QtWidgets, QtGui, QtCore, QtPrintSupport
from classes_database_1_2 import *
from PyQt5.QtChart import QPieSlice, QValueAxis

row_number_montant = 0
''' This is the MainWindow class '''


class MainWindow(QMainWindow):
    maxAxis = 1000
    data1 = []
    data2 = []
    data3 = []

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, [10, 15, 29, 2, 13, 12, 15, 1, 2, 13, 12, 15, 1])
        ##Main Buttons
        self.ui.deconnexion.clicked.connect(lambda: self.deconnection())
        ## MENU
        ########################################################################
        self.ui.personnels_interne.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.affich_personnel_interne))
        self.ui.Externe.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Affiche_externe))
        self.ui.documents.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.affich_gestion_documents))
        self.ui.marchandise_emballages.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_marchandices_amballage))
        self.ui.transport_livraison.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.affich_transport_livraison))
        self.ui.pays_unite_monetaire.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_pays_monnaie))
        self.ui.dossiers_2.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.affichDossier))
        self.ui.client_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.afficheClientMenu))
        self.ui.client_menu.clicked.connect(lambda: self.affiche_client())
        self.ui.statistiques.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.statistics))
        ## documents
        ########################################################################
        self.ui.dossiers_2.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.affichDossier))
        self.ui.dossiers_2.clicked.connect(lambda: self.affiche_dossier(self.ui.comboBox.currentText()))
        self.ui.dossiers_2.click()
        self.ui.fichiers_2.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.afficheFichier))
        self.ui.fichiers_2.clicked.connect(lambda: self.affiche_fichier())
        self.ui.client_menu.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.afficheClientMenu))
        self.ui.afficheClient_2.clicked.connect(lambda: self.affiche_client())
        #      self.ui.dossiers_2.clicked.connect(lambda: self.affiche_dossier(self.ui.filtre_gestion.currentText()))
        # ----------------------------------------------------------------------------
        self.ui.bon_de_sortie.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.AfficheBonSortie))
        self.ui.bon_de_sortie.clicked.connect(lambda: self.affiche_bon_sortie())
        self.ui.bon_de_visite.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.AfficheBonvisite))
        self.ui.bon_de_visite.clicked.connect(lambda: self.affiche_bon_visite())
        # clientFormulaire
        self.ui.ajouterClientMenu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.formClient))
        self.ui.supprimer.clicked.connect(lambda : self.supprimerClient())
        # document formulaire
        self.ui.ajouter_gestion_document.clicked.connect(lambda: self.gestion_document())
        # recherche
        self.ui.rechercherClientMenu.textChanged.connect(lambda: self.recherch_client())
        self.ui.rechercher_gestion_document.textChanged.connect(lambda: self.recherch_Documents())
        # insertion
        self.ui.enregistrer_client.clicked.connect(lambda: self.inserer_client())
        self.ui.enregistrer_bon_de_sortie.clicked.connect(lambda: self.inserBon_Sortie())
        self.ui.enregistrer_bon_visite.clicked.connect(lambda: self.inserBon_visite())
        self.ui.enregistrerfichier.clicked.connect(lambda: self.inserer_Fichier())
        self.ui.enregistrer_dossier.clicked.connect(lambda: self.inserer_dossier())
        self.ui.parcourir.clicked.connect(lambda : self.EFiles())
        # modification tables
        self.ui.modifierClientMenu.clicked.connect(lambda: self.modifier_client())
        self.ui.modifier_gestion_document.clicked.connect(lambda: self.docum_modification())
        # Suppression
        self.ui.supprimer_gestion_document.clicked.connect(lambda: self.suprimer_document())
        # Fermeture
        self.ui.pushButton_2.clicked.connect(lambda: self.fermer_dossier())

        # PAYS ET UNITE MONETAIRE
        self.ui.ajouter_pays_monnaie.clicked.connect(lambda: self.ajouterPaysOrMonnaie())
        self.ui.enregistrer_pays.clicked.connect(lambda: self.insererPays())
        self.ui.pays_unite_monetaire.clicked.connect(lambda: self.afficherPays())
        self.ui.pays_unite_monetaire.clicked.connect(lambda: self.afficherMonnaie())
        self.ui.enregistrer_monnaie.clicked.connect(lambda: self.insererMonnaie())
        self.ui.monnaie_button_pays_monnaie.clicked.connect(
            lambda: self.ui.stackedWidget_6.setCurrentWidget(self.ui.afficheMaonnaie))
        self.ui.pays_button_pays_monnaie.clicked.connect(
            lambda: self.ui.stackedWidget_6.setCurrentWidget(self.ui.affichePays))
        self.ui.supprimer_pays_monnaie.clicked.connect(lambda: self.supprimerPaysMonnaie())
        self.ui.modifier_pays_monnaie.clicked.connect(lambda: self.modifierPaysMonnaie())
        self.ui.rechercher_pays_monnaie.textChanged.connect(lambda: self.recherchePaysMonnaie())

        # Personnel interne
        self.ui.personnels_interne.clicked.connect(lambda: self.affiche_utilisateur())
        self.ui.utilisateur_button_personnel_interne.clicked.connect(
            lambda: self.ui.stackedWidget_4.setCurrentWidget(self.ui.affichUtilisateur))
        self.ui.utilisateur_button_personnel_interne.clicked.connect(lambda: self.affiche_utilisateur())
        self.ui.declarant_button_personnel_interne.clicked.connect(
            lambda: self.ui.stackedWidget_4.setCurrentWidget(self.ui.afficheDeclarent))
        self.ui.declarant_button_personnel_interne.clicked.connect(lambda: self.affiche_declarant())
        # insertion
        self.ui.ajouter_personnel_interne.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.gestion_formulaire_interne()))
        self.ui.enregistrer_user.clicked.connect(lambda: self.insererUser())
        self.ui.enregistrer_declarent.clicked.connect(lambda: self.insererDeclarant())
        # modification
        self.ui.modifier_personnel_interne.clicked.connect(lambda: self.modifier_interne())
        # recherche
        self.ui.rechercher_personnel_interne.textChanged.connect(lambda: self.recherche_interne())
        # supprimer
        self.ui.supprimer_personnel_interne.clicked.connect(lambda: self.supprimer_interne())

        # EXTERNE
        # AFFICHAGE
        self.ui.Externe.clicked.connect(lambda: self.affiche_douanier())
        self.ui.dounier_button_externe.clicked.connect(
            lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.afficheDouanier))
        self.ui.dounier_button_externe.clicked.connect(lambda: self.affiche_douanier())
        self.ui.expert_button_externe.clicked.connect(
            lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.affiche_expert))
        self.ui.expert_button_externe.clicked.connect(lambda: self.affiche_expert())
        self.ui.representant_button_externe.clicked.connect(
            lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.affiche_representant))
        self.ui.representant_button_externe.clicked.connect(lambda: self.affiche_representant())
        # formulaire
        self.ui.ajouter_externe.clicked.connect(lambda: self.gestion_externe())
        # insertion
        self.ui.enregistrer_douanier.clicked.connect(lambda: self.inserer_douanier())
        self.ui.enregistrer_expert.clicked.connect(lambda: self.inserer_expert())
        self.ui.enregistrer_representant.clicked.connect(lambda: self.inserer_representant())
        # modification
        self.ui.modifier_externe.clicked.connect(lambda: self.modifier_externe())
        # recherche
        self.ui.rechercher_externe.textChanged.connect(lambda: self.recherche_externe())
        # supprimer
        self.ui.supprimer_externe.clicked.connect(lambda: self.supprimer_externe())

        # marchandises et emballages
        # affichage
        self.ui.marchandise_emballages.clicked.connect(lambda: self.affiche_emballage())
        self.ui.marchandise_button.clicked.connect(
            lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.afficheMarchandise))
        self.ui.marchandise_button.clicked.connect(lambda: self.affiche_marchandise())
        self.ui.nature_button.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.afficheNature))
        self.ui.nature_button.clicked.connect(lambda: self.affiche_nature_marchandise())
        self.ui.emballage_button.clicked.connect(
            lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.afficheEmballage))
        self.ui.emballage_button.clicked.connect(lambda: self.affiche_emballage())
        self.ui.designation_button.clicked.connect(
            lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.afficheDesignation))
        self.ui.designation_button.clicked.connect(lambda: self.affiche_designation())
        # formulaire
        self.ui.ajouter_marchandise_embalage.clicked.connect(lambda: self.gestion_marchandise_emballage())
        # insertion
        self.ui.enregistrer_marchandice.clicked.connect(lambda: self.inserer_marchandise())
        self.ui.enregistrer_nature_marchandice.clicked.connect(lambda: self.inserer_nature_marchandise())
        self.ui.enregistrer_emballage.clicked.connect(lambda: self.inserer_emballage())
        self.ui.enregistrer_designation.clicked.connect(lambda: self.inserer_designation())
        # modifier
        self.ui.modifier_marchandise_embalage.clicked.connect(lambda: self.gestion_modifier_marchandise_emballage())
        # recherche
        self.ui.rechercher_marchandise_embalage.textChanged.connect(
            lambda: self.gestion_recherche_marchandise_emballage())
        # supprimer
        self.ui.supprimer_marchandise_embalage.clicked.connect(lambda: self.gestion_supprimer_marchandise_emballage())

        # transport/livraison
        # affichage
        self.ui.transport_livraison.clicked.connect(lambda: self.affiche_inter())
        self.ui.chauffeur_button.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.afficheChauffeur))
        self.ui.chauffeur_button.clicked.connect(lambda: self.affiche_chauffeur())
        self.ui.Camions_button.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.afficheCAmion))
        self.ui.Camions_button.clicked.connect(lambda: self.affiche_camion())
        self.ui.four_button.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.affichFournisseur))
        self.ui.four_button.clicked.connect(lambda: self.affiche_four())
        self.ui.inter_button.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.affichIntermediaire))
        self.ui.inter_button.clicked.connect(lambda: self.affiche_inter())
        # formulaire
        self.ui.ajouter_transport_livraison.clicked.connect(lambda: self.gestion_transport_livraison())
        # insertion
        self.ui.eregistrer_camion.clicked.connect(lambda: self.inserer_camion())
        self.ui.enregistrer_chauffeur.clicked.connect(lambda: self.inserer_chauffeur())
        self.ui.enregistrer_fournisseur.clicked.connect(lambda: self.inserer_four())
        self.ui.enregistrer_intermediaire.clicked.connect(lambda: self.inserer_inter())
        # modifier
        self.ui.modifier_transport_livraison.clicked.connect(lambda: self.gestion_modifier_transport_livraison())
        # recherche
        self.ui.rechercher_transport_livraison.textChanged.connect(
            lambda: self.gestion_rechercher_transport_livraison())
        # supprimer
        self.ui.supprimer_transpor_livraison.clicked.connect(
            lambda: self.gestion_supprimer_transport_livraison())

        # stat
        self.ui.statistiques.clicked.connect(lambda: self.setDataGA())
        self.ui.gain_annuel_exemple.clicked.connect(
            lambda: self.ui.stackedWidget_8.setCurrentWidget(self.ui.gain_annuel))
        self.ui.activite_mensuel_exemple.clicked.connect(
            lambda: self.ui.stackedWidget_8.setCurrentWidget(self.ui.activite_mensuel))
        self.ui.repartition_dossier_par_pay_exemple.clicked.connect(
            lambda: self.ui.stackedWidget_8.setCurrentWidget(self.ui.repartition_dossier_par_pay))
        self.ui.gain_annuel_exemple.clicked.connect(lambda: self.setDataGA())
        self.ui.repartition_dossier_par_pay_exemple.clicked.connect(lambda: self.setDataRDP())
        self.ui.activite_mensuel_exemple.clicked.connect(lambda: self.setDataAM())

        # TOOLTIP(AIDE POP UP)
        # bouttons supprimer
        self.ui.supprimer_marchandise_embalage.setToolTip("Supprimer l'élement selectionné du tableau")
        self.ui.supprimer_transpor_livraison.setToolTip("Supprimer l'élement selectionné du tableau")
        self.ui.supprimer_personnel_interne.setToolTip("Supprimer l'élement selectionné du tableau")
        self.ui.supprimer_externe.setToolTip("Supprimer l'élement selectionné du tableau")
        self.ui.supprimer_pays_monnaie.setToolTip("Supprimer l'élement selectionné du tableau")
        self.ui.supprimer_gestion_document.setToolTip("Supprimer l'élement selectionné du tableau")
        self.ui.supprimerFactures.setToolTip("Supprimer l'élement selectionné du tableau")
        self.ui.supprimer.setToolTip("Supprimer l'élement selectionné du tableau")
        # bouttons modifier
        self.ui.modifier_marchandise_embalage.setToolTip("Appliquer les changements à l'élement modifié du tableau")
        self.ui.modifier_personnel_interne.setToolTip("Appliquer les changements à l'élement modifié du tableau")
        self.ui.modifier_externe.setToolTip("Appliquer les changements à l'élement modifié du tableau")
        self.ui.modifier_transport_livraison.setToolTip("Appliquer les changements à l'élement modifié du tableau")
        self.ui.modifier_pays_monnaie.setToolTip("Appliquer les changements à l'élement modifié du tableau")
        self.ui.modifier_gestion_document.setToolTip("Appliquer les changements à l'élement modifié du tableau")
        self.ui.modifierFacturesMenu.setToolTip("Appliquer les changements à l'élement modifié du tableau")
        self.ui.modifierClientMenu.setToolTip("Appliquer les changements à l'élement modifié du tableau")
        self.ui.pushButton_2.setToolTip("Fermer (archiver) le dossier selectionné")
        # bouttons ajoouter
        self.ui.ajouter_marchandise_embalage.setToolTip("Ajouter un élément à la table")
        self.ui.ajouter_personnel_interne.setToolTip("Ajouter un élément à la table")
        self.ui.ajouter_externe.setToolTip("Ajouter un élément à la table")
        self.ui.ajouter_transport_livraison.setToolTip("Ajouter un élément à la table")
        self.ui.ajouter_pays_monnaie.setToolTip("Ajouter un élément à la table")
        self.ui.ajouter_gestion_document.setToolTip("Ajouter un élément à la table")
        self.ui.ajouterFacturesMenu.setToolTip("Ajouter un élément à la table")
        self.ui.ajouterClientMenu.setToolTip("Ajouter un élément à la table")
        # rechercher
        self.ui.rechercher_marchandise_embalage.setToolTip("rechercher dans le tableau affiché")
        self.ui.rechercher_personnel_interne.setToolTip("rechercher dans le tableau affiché")
        self.ui.rechercher_externe.setToolTip("rechercher dans le tableau affiché")
        self.ui.rechercher_transport_livraison.setToolTip("rechercher dans le tableau affiché")
        self.ui.rechercher_pays_monnaie.setToolTip("rechercher dans le tableau affiché")
        self.ui.rechercher_gestion_document.setToolTip("rechercher dans le tableau affiché")
        self.ui.rechercherfacturesMenu.setToolTip("rechercher dans le tableau affiché")
        self.ui.rechercherClientMenu.setToolTip("rechercher dans le tableau affiché")
        # affichage
        # march et emballage
        self.ui.marchandise_button.setToolTip("afficher la table contenant toutes les marchandises")
        self.ui.emballage_button.setToolTip("afficher la table contenant tous les emballages")
        self.ui.nature_button.setToolTip("afficher la table contenant toutes les natures de la marchandise")
        self.ui.designation_button.setToolTip("afficher la table contenant toutes les designations")
        # transports livraison
        self.ui.chauffeur_button.setToolTip("afficher la table contenant tous les chauffeurs")
        self.ui.Camions_button.setToolTip("afficher la table contenant tous les camions")
        self.ui.four_button.setToolTip("afficher la table contenant tous les fournisseurs")
        self.ui.inter_button.setToolTip("afficher la table contenant tous les intermediaires")
        # client
        self.ui.afficheClient_2.setToolTip("afficher la table contenant tous les clients")
        # perso interne
        self.ui.utilisateur_button_personnel_interne.setToolTip("afficher la table contenant tous les utilisateurs")
        self.ui.declarant_button_personnel_interne.setToolTip("afficher la table contenant tous les declarants")
        # externe
        self.ui.dounier_button_externe.setToolTip("afficher la table contenant tous les douaniers")
        self.ui.representant_button_externe.setToolTip("afficher la table contenant tous les représentants")
        self.ui.expert_button_externe.setToolTip("afficher la table contenant tous les experts")
        # documents
        self.ui.dossiers_2.setToolTip("afficher la table contenant tous les dossiers")
        self.ui.fichiers_2.setToolTip("afficher la table contenant tous les fichiers")
        self.ui.bon_de_visite.setToolTip("afficher la table contenant tous les bons de visite")
        self.ui.bon_de_sortie.setToolTip("afficher la table contenant tous les bons de sortie")
        # pays monnaie
        self.ui.pays_button_pays_monnaie.setToolTip("afficher la table contenant tous les pays")
        self.ui.monnaie_button_pays_monnaie.setToolTip("afficher la table contenant toutes les monnaies")
        # factures
        self.ui.afficheFactures_2.setToolTip("Mettre à jour la table contenant toutes les factures")
        # FACTURATION
        # affichage
        self.ui.facturation.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.affichageFactures))
        self.ui.facturation.clicked.connect(lambda: self.affiche_facture())
        self.ui.afficheFactures_2.clicked.connect(lambda: self.affiche_facture())
        self.ui.ajouterFacturesMenu.clicked.connect(lambda: self.affiche_design_factures())
        self.ui.buttonAjouterFormFact.clicked.connect(lambda: self.remplir_table_montants())
        # modification
        self.ui.modifierFacturesMenu.clicked.connect(lambda: self.modifier_facture())
        # recherche
        self.ui.rechercherfacturesMenu.textChanged.connect(
            lambda: self.rechercher_factures())
        self.ui.lineEdit_3.textChanged.connect(
            lambda: self.recherche_designation_dans_facture())
        # supprimer
        self.ui.supprimerFactures.clicked.connect(lambda: self.supprimer_facture())
        # ajouter
        self.ui.ajouterFacturesMenu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.formFacture))
        self.ui.calculerFacture.clicked.connect(lambda: self.calculerFacture())
        self.ui.ImprimerFacture.clicked.connect(lambda: self.imprimerFacture())
        self.ui.enregistrer_facture.clicked.connect(lambda: self.enregistrerFacteur())
        # imprimer
        self.ui.pushButton_3.clicked.connect(lambda: self.imprimerFactTable())
        self.ui.exporter_gestion_document.clicked.connect(lambda: self.gestion_des_impressions())

        ########################################## CLOSING ########################################################################
        self.ui.close_18.clicked.connect(lambda: self.closeMonnaiePays())
        self.ui.close_20.clicked.connect(lambda: self.closeMonnaiePays())
        self.ui.close_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.affichageFactures))
        self.ui.close_8.clicked.connect(lambda: self.closeTransLivraison())
        self.ui.pushButton.clicked.connect(lambda: self.closeTransLivraison())
        self.ui.close_15.clicked.connect(lambda: self.closeTransLivraison())
        self.ui.close_16.clicked.connect(lambda: self.closeTransLivraison())
        self.ui.close_17.clicked.connect(lambda: self.closeMarchandiseEmballages())
        self.ui.close_19.clicked.connect(lambda: self.closeMarchandiseEmballages())
        self.ui.close_13.clicked.connect(lambda: self.closeMarchandiseEmballages())
        self.ui.pushButton_6.clicked.connect(lambda: self.closeMarchandiseEmballages())
        self.ui.close_10.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.afficheClientMenu))
        self.ui.close_11.clicked.connect(lambda: self.closeInterne())
        self.ui.close_21.clicked.connect(lambda: self.closeInterne())
        self.ui.close_12.clicked.connect(lambda: self.closeExterne())
        self.ui.close_14.clicked.connect(lambda: self.closeExterne())
        self.ui.pushButton_10.clicked.connect(lambda: self.closeExterne())
        self.ui.pushButton_8.clicked.connect(lambda: self.closeDocument())
        self.ui.close.clicked.connect(lambda: self.closeDocument())
        self.ui.close_4.clicked.connect(lambda: self.closeDocument())
        self.ui.close_6.clicked.connect(lambda: self.closeDocument())
        self.ui.documents.click()

        ###############################################AUTO COMPLETE###################################
        # chauffeur in bon de sortie
        '''
        sql = "select nom from personne where type='chauffeur'"
        cur.execute(sql)
        self.result_chauffeur = cur.fetchall()
        # self.wordList_declarant = [''.join(str(i)) for i in self.result_declarent]
        self.wordList_chauffeur = ["%s " % x for x in self.result_chauffeur]
        completer_chauffeur_dc = QCompleter(self.wordList_chauffeur)
        self.ui.lineEdit_8.setCompleter(completer_chauffeur_dc)
        self.ui.lineEdit_8.editingFinished.connect(lambda: self.update_chauffeur())'''

        # Camion in bon de sortie
        '''
        sql = "select matricule from camion"
        cur.execute(sql)
        self.result_matricule = cur.fetchall()
        self.wordList_matricule = ["%s " % x for x in self.result_matricule]
        completer_matricule_dc = QCompleter(self.wordList_matricule)
        self.ui.matricule.setCompleter(completer_matricule_dc)'''

        # Client in doossier
        sql = "select nom_client from client"
        cur.execute(sql)
        self.result_client = cur.fetchall()
        self.wordList_client = [''.join(i) for i in self.result_client]
        completer_client_dc = QCompleter(self.wordList_client)
        self.ui.nom_client_2.setCompleter(completer_client_dc)

        # Fournisseur in doossier
        sql = "select nom_fournisseur from fournisseur"
        cur.execute(sql)
        self.result_fourn = cur.fetchall()
        self.wordList_fourn = [''.join(i) for i in self.result_fourn]
        completer_fournisseur_dc = QCompleter(self.wordList_fourn)
        self.ui.numero_fournisseur.setCompleter(completer_fournisseur_dc)

        # pay in doossier
        sql = "select nom_pays from pays"
        cur.execute(sql)
        self.result_pays = cur.fetchall()
        self.wordList_pays = [''.join(i) for i in self.result_pays]
        completer_pays_dc = QCompleter(self.wordList_pays)
        self.ui.nom_pays.setCompleter(completer_pays_dc)
        self.ui.nom_pays.editingFinished.connect(lambda: self.update_id_pays())

        # numero_fichier in doossier
        sql = "select id_fichier from fichier"
        cur.execute(sql)
        self.result_fichier = cur.fetchall()
        # self.wordList_fichier = [''.join(str(i)) for i in self.result_fichier]
        self.wordList_fichier = ["%s " % x for x in self.result_fichier]
        completer_fichier_dc = QCompleter(self.wordList_fichier)
        self.ui.numero_fichier.setCompleter(completer_fichier_dc)

        # declarent in doossier
        sql = "select nom from personne where type=\"declarant\""
        cur.execute(sql)
        self.result_declarent = cur.fetchall()
        # self.wordList_declarant = [''.join(str(i)) for i in self.result_declarent]
        self.wordList_declarant = ["%s " % x for x in self.result_declarent]
        completer_declarent_dc = QCompleter(self.wordList_declarant)
        self.ui.lineEdit.setCompleter(completer_declarent_dc)
        self.ui.lineEdit.editingFinished.connect(lambda: self.update_declarant())

        # code_monnaie in dossier
        sql = "select code_monnaie from monnaie"
        cur.execute(sql)
        self.result_monnaie = cur.fetchall()
        self.wordList_monnaie = [''.join(i) for i in self.result_monnaie]
        completer_monnaie = QCompleter(self.wordList_monnaie)
        self.ui.code_monnaie.setCompleter(completer_monnaie)

    def EFiles(self):
        fname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.chemin_form.setText(fname)

    def supprimerClient(self):
        try:
            message = QMessageBox.question(self, "Suppression", "Êtes-vous sûr de supprimer cet élément ?",
                                           QMessageBox.Yes | QMessageBox.No)
            if (message == QMessageBox.Yes):
                id = self.ui.tableClienMenu.item(self.ui.tableClienMenu.currentRow(), 0).text()
                Client.supprimerClient(id)
            self.affiche_client()
        except:
            pass

    def update_id_pays(self):
        try:
            sql = 'select code_pays from pays where nom_pays=%s'
            cur.execute(sql, (self.ui.nom_pays.text(),))
            result = cur.fetchone()
            self.ui.id_pays.setText(str(result[0]))
        except:
            pass

    def update_declarant(self):
        try:
            sql = "select id,prenom from personne where nom=\"{}\"".format(self.ui.nom_declarent.text().rstrip())
            cur.execute(sql)
            result = cur.fetchall()
            print(result)
            self.ui.numero_declarant.setText(str(result[0][0]))
            self.ui.prenom_declaren.setText(str(result[0][1]))
        except:
            pass
    # IMPRESSION_BON_SORTIE
    def enregistrerBs(self):
        try:
            column = self.ui.tableBonSortie.columnCount()
            row = self.ui.tableBonSortie.currentRow()
            n_dosier = self.ui.tableBonSortie.item(row, 0).text()
            nbon = self.ui.tableBonSortie.item(row, 1).text()
            dat = self.ui.tableBonSortie.item(row, 2).text()
            pc = self.ui.tableBonSortie.item(row, 3).text()
            chauf = self.ui.tableBonSortie.item(row, 4).text()
            matricule = self.ui.tableBonSortie.item(row, 5).text()
            fact = open("Bondesortie/Bon{}_Dossier{}.txt".format(nbon, n_dosier), "w")
            fact.write("                            Bon de Sortie\n\n\n\n")
            fact.write("Num Dossier : {}              ".format(n_dosier))
            fact.write("Num Bon de sortie : {}\n\n".format(nbon))
            fact.write("Date : {}            ".format(dat))
            fact.write("Pc : {}\n\n".format(pc))
            fact.write("Matricule : {}       ".format(matricule))
            fact.write("Chauffeur : {} \n\n\n".format(chauf))
            fact.close()

            return 0, nbon, n_dosier
        except:
            essage = QMessageBox.warning(self, "Erreur", "Aucun Dossier n'est selectionner ")
            return -1, 0, 0

    def imprimerBs(self):
        ret = self.enregistrerBs()
        if ret[0] == 0:
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
            dialog = QtPrintSupport.QPrintDialog(printer, self)
            if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
                screen = open("Bondesortie/Bon{}_Dossier{}.txt".format(ret[1], ret[2]))
                doc = QtGui.QTextDocument(screen.read())
                doc.print_(printer)
                self.ui.stackedWidget.setCurrentWidget(self.ui.affich_gestion_documents)
                message = QMessageBox.information(self, "Avec succès!", "Le bon de sortie Nº" + str(ret[1]) + " a été enregistrer dans le dossier {Bons de sortie}")

    # IMPRESSION_BON_SORTIE
    def gestion_des_impressions(self):
        if (self.ui.stackedWidget_2.currentWidget() == self.ui.affichDossier):
            message = QMessageBox.warning(self, "Remarque", "L'option d'impression est seulement valable pour les bons.")
        elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonSortie):
            self.imprimerBs()
        elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonvisite):
            self.imprimerBv()
        else:
            message = QMessageBox.warning(self, "Remarque","L'option d'impression est seulement valable pour les bons.")


    def enregistrerBv(self):
        try:
            column = self.ui.tableBonVisite.columnCount()
            row = self.ui.tableBonVisite.currentRow()
            n_dosier = self.ui.tableBonVisite.item(row, 0).text()
            nbon = self.ui.tableBonVisite.item(row, 1).text()
            dat = self.ui.tableBonVisite.item(row, 2).text()
            pc = self.ui.tableBonVisite.item(row, 3).text()
            douan = self.ui.tableBonVisite.item(row, 4).text()
            bur_douane = self.ui.tableBonVisite.item(row, 5).text()
            fact = open("Bondevisite/Bon{}_Dossier{}.txt".format(nbon, n_dosier), "w")
            fact.write("                            Bon de Visite\n\n\n\n")
            fact.write("Num Dossier : {}                ".format(n_dosier))
            fact.write("Num Bon de visite : {}\n\n".format(nbon))
            fact.write("Date : {}\n\n".format(dat))
            fact.write("Pc : {}                  ".format(pc))
            fact.write("Bureau de douane : {} \n\n\n".format(douan))
            fact.write("Douanier : {} \n\n\n".format(bur_douane))
            fact.close()

            return 0,nbon, n_dosier
        except:
            essage = QMessageBox.warning(self, "Erreur", "Il existe des champs vides ou le bon de visite n'existe pas ")
            return -1, 0, 0

    def imprimerBv(self):
        ret = self.enregistrerBv()
        if ret[0] == 0:
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
            dialog = QtPrintSupport.QPrintDialog(printer, self)
            if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
                screen = open("Bondevisite/Bon{}_Dossier{}.txt".format(ret[1], ret[2]))
                doc = QtGui.QTextDocument(screen.read())
                doc.print_(printer)
                self.ui.stackedWidget.setCurrentWidget(self.ui.affich_gestion_documents)
                message = QMessageBox.information(self, "Avec succès!", "Le bon de visite Nº" + str(ret[1]) + " a été enregistrer dans le dossier {Bons de visite}")


    # CALCULER ET IMPRESSION ET ENREGISTREMENT DES FACTURES
    def __get_info_facture(self):
        info = []
        info.append(self.ui.tva.text())
        info.append(self.ui.date_3.text())
        info.append(self.ui.numero_dossier_3.text())
        info.append(self.ui.droitTimbre.text())
        info.append(self.ui.totaldebours.text())
        info.append(self.ui.totalPrestation.text())
        info.append(self.ui.montantTotal.text())
        info.append(self.ui.etat_paiement_3.currentText())
        info.append(self.ui.mod_paiement_3.text())
        Fact = Factur(int(info[2]), self.ui.date_3.date().toPyDate(), float(info[0]), float(info[5]), float(info[4]),
                      float(info[3]), info[7], info[8])
        info.append(Fact.get_id_facture())
        sql = "SELECT id_client FROM dossier WHERE id_dossier = %s "
        cur.execute(sql, (int(info[2]),))
        info.append(cur.fetchone()[0])
        return info

    def enregistrerFacteur(self):
        try:
            info = self.__get_info_facture()
            fact = open("Factures/Fact_D{}_F{}.txt".format(info[2], info[9]), "w")
            fact.write("                            Facture\n\n\n\n")
            fact.write("Num Facture : {}                ".format(info[9]))
            fact.write("Date : {}\n\n".format(info[1]))
            fact.write("Client : {}                 ".format(info[10]))
            fact.write("Num Dossier : {}\n\n".format(info[2]))
            fact.write("TVA : {} %                  ".format(info[0]))
            fact.write("Droit de Timbre : {} DA\n\n\n".format(info[3]))
            fact.write("                         Designations : \n\n")
            for i in range(self.ui.designationMontantTable.rowCount()):
                fact.write("{}- {} ...... Debours : {} DA ...... Prestation : {} DA\n\n".format(
                    i + 1, self.ui.designationMontantTable.item(i, 0).text(),
                    self.ui.designationMontantTable.item(i, 1).text()
                    , self.ui.designationMontantTable.item(i, 2).text()
                ))
            fact.write("\n\n")
            fact.write("Total Debours : {} DA\n\n".format(info[4]))
            fact.write("Total Prestation : {} DA\n\n".format(info[5]))
            fact.write("Total : {} DA".format(info[6]))
            fact.close()

            return 0, info[2], info[9]
        except:
            essage = QMessageBox.warning(self, "Erreur", "il existe des champs vides ou dossier n'existe pas ")
            return -1, 0, 0

    def imprimerFacture(self):
        ret = self.enregistrerFacteur()
        if ret[0] == 0:
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
            dialog = QtPrintSupport.QPrintDialog(printer, self)
            if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
                screen = open("Factures/Fact_D{}_F{}.txt".format(ret[1], ret[2]))
                doc = QtGui.QTextDocument(screen.read())
                doc.print_(printer)
                self.ui.stackedWidget.setCurrentWidget(self.ui.affichageFactures)

    def imprimerFactTable(self):
        id = self.ui.tableClienMenu_3.item(self.ui.tableClienMenu_3.currentRow(), 0).text()
        idDossier = self.ui.tableClienMenu_3.item(self.ui.tableClienMenu_3.currentRow(), 1).text()
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        dialog = QtPrintSupport.QPrintDialog(printer, self)
        if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            screen = open("Factures/Fact_D{}_F{}.txt".format(idDossier, id))
            doc = QtGui.QTextDocument(screen.read())
            doc.print_(printer)
            self.ui.stackedWidget.setCurrentWidget(self.ui.affichageFactures)

    def calculerFacture(self):
        try:
            debour = 0.0
            prestation = 0.0
            for i in range(self.ui.designationMontantTable.rowCount()):
                debour = debour + float(self.ui.designationMontantTable.item(i, 1).text())
                prestation = prestation + float(self.ui.designationMontantTable.item(i, 2).text())
            self.ui.totaldebours.setText(str(debour))
            self.ui.totalPrestation.setText(str(prestation))
            self.ui.montantTotal.setText(str(debour + prestation + prestation * int(self.ui.tva.text()) / 100))
        except:
            essage = QMessageBox.warning(self, "Erreur",
                                         "Les données que vous avez saisi ne peuvent pas être calculer !!" \
                                         + "\nveuillez verfier les champs (TVA,Prestations,Debours)")

    # STAT FUNCTIONS
    def setDataGA(self):
        sql = "SELECT id_dossier from dossier WHERE" \
              + " date_ouverture BETWEEN %s AND %s "
        self.data1 = []
        for i in range(1, 13):
            date_1 = "{}-{}-01".format(datetime.now().year, i)
            if i == 2:
                date_2 = "{}-{}-29".format(datetime.now().year, i)
            elif i == 8 or ((i < 8) and (i % 2 == 1)) or ((i > 8) and (i % 2 == 0)):
                date_2 = "{}-{}-31".format(datetime.now().year, i)
            else:
                date_2 = "{}-{}-30".format(datetime.now().year, i)
            try:
                cur.execute(sql, (date_1, date_2))
                self.data1.append(len(cur.fetchall()))
            except:
                print("you wrong")
        self.ui.chart1.axisY().setMax(max(self.data1) + 3)
        for i, n in enumerate(self.data1):
            self.ui.set0.replace(i, n)

    def setDataRDP(self):
        sql = "SELECT * FROM pays"
        cur.execute(sql)
        self.data2 = []
        sql = "SELECT COUNT(id_dossier) AS 'COUNT(dossier)' FROM dossier WHERE id_pays=%s"
        for pay in cur.fetchall():
            cur.execute(sql, (pay[0],))
            self.data2.append((pay[1], cur.fetchone()[0]))
            sorted(self.data2, key=lambda x: x[1])
        self.ui.series2.clear()
        for i, n in self.data2[0:5]:
            self.ui.series2.append(i, n)
        try:
            slice = QPieSlice()
            slice = self.ui.series2.slices()[self.data2.index(max(self.data2, key=lambda x: x[1]))]
            slice.setExploded(True)
            slice.setLabelVisible(True)
            slice.setPen(QtGui.QPen(QtCore.Qt.green, self.data2.index(max(self.data2))))
            slice.setBrush(QtCore.Qt.green)
        except:
            pass;

    def setDataAM(self):
        self.ui.series3.clear()
        sql = "SELECT total_prestation,total_debours,TVA from faacturess WHERE" \
              + " faacturess.date BETWEEN %s AND %s "
        self.ui.chart3.axisY().setMax(500)
        for i in range(1, 13):
            date_1 = "{}-{}-01".format(datetime.now().year, i)
            if i == 2:
                date_2 = "{}-{}-29".format(datetime.now().year, i)
            elif i == 8 or ((i < 8) and (i % 2 == 1)) or ((i > 8) and (i % 2 == 0)):
                date_2 = "{}-{}-31".format(datetime.now().year, i)
            else:
                date_2 = "{}-{}-30".format(datetime.now().year, i)
            try:
                cur.execute(sql, (date_1, date_2))
                res = cur.fetchall()

            except:
                print("you wrong")
            # print(max([int(x[0]+x[1]) for x in res])
            self.ui.series3.append(i - 1, sum(x[0] + x[1] + x[1] * x[2] / 100 for x in res))
            self.setMaxChart(res)

    def setMaxChart(self, res):
        if len(res) != 0:
            m = max([int(x[0] + x[1] + x[1] * x[2] / 100 + 1000) for x in res])
            if m > self.maxAxis:
                self.maxAxis = m
            axisY = QValueAxis()
            axisY.setRange(0, self.maxAxis + 1000)
            self.ui.chart3.setAxisY(axisY, self.ui.series3)

    # CLOSE FUNCTIONS
    def closeDocument(self):
        if (self.ui.stackedWidget.currentWidget() == self.ui.formDossier):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affich_gestion_documents)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.affichDossier)
            self.affiche_dossier(self.ui.comboBox.currentText())
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formfichier):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affich_gestion_documents)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.afficheFichier)
            self.affiche_fichier()
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formBonSortie):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affich_gestion_documents)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.AfficheBonSortie)
            self.affiche_bon_sortie()
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formBonVisite):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affich_gestion_documents)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.AfficheBonvisite)
            self.affiche_bon_visite()

    def closeExterne(self):
        if (self.ui.stackedWidget.currentWidget() == self.ui.formDouanier):
            self.ui.stackedWidget.setCurrentWidget(self.ui.Affiche_externe)
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.afficheDouanier)
            self.affiche_douanier()
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formExpert):
            self.ui.stackedWidget.setCurrentWidget(self.ui.Affiche_externe)
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.affiche_expert)
            self.affiche_expert()
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formRepresentant):
            self.ui.stackedWidget.setCurrentWidget(self.ui.Affiche_externe)
            self.ui.stackedWidget_7.setCurrentWidget(self.ui.affiche_representant)
            self.affiche_representant()

    def closeInterne(self):
        if (self.ui.stackedWidget.currentWidget() == self.ui.formUser):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affich_personnel_interne)
            self.ui.stackedWidget_4.setCurrentWidget(self.ui.affichUtilisateur)
            self.affiche_utilisateur()
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formDeclarent):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affich_personnel_interne)
            self.ui.stackedWidget_4.setCurrentWidget(self.ui.afficheDeclarent)
            self.affiche_declarant()

    def closeTransLivraison(self):
        if (self.ui.stackedWidget.currentWidget() == self.ui.formCamion):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affich_transport_livraison)
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.afficheCAmion)
            self.affiche_camion()
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formChauffeur):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affich_transport_livraison)
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.afficheChauffeur)
            self.affiche_chauffeur()
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formFournisseur):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affich_transport_livraison)
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.affichFournisseur)
            self.affiche_four()
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formIntermediaire):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affich_transport_livraison)
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.affichIntermediaire)
            self.affiche_inter()

    def closeMonnaiePays(self):
        if (self.ui.stackedWidget.currentWidget() == self.ui.formPays):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_pays_monnaie)
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.affichePays)
            self.afficherPays()
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formMonnaie):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_pays_monnaie)
            self.ui.stackedWidget_6.setCurrentWidget(self.ui.afficheMaonnaie)
            self.afficherMonnaie()

    def closeMarchandiseEmballages(self):
        if (self.ui.stackedWidget.currentWidget() == self.ui.formEmballage):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_marchandices_amballage)
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.afficheEmballage)
            self.affiche_emballage()
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formDesigniation):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_marchandices_amballage)
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.afficheDesignation)
            self.affiche_designation()
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formNaturemarchandice):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_marchandices_amballage)
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.afficheNature)
            self.affiche_nature_marchandise()
        elif (self.ui.stackedWidget.currentWidget() == self.ui.formMarchandice):
            self.ui.stackedWidget.setCurrentWidget(self.ui.affiche_marchandices_amballage)
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.afficheMarchandise)
            self.affiche_marchandise()

    ##################################################### Facutre ########################################################
    def affiche_facture(self):
        sql = "select * from faacturess"
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableClienMenu_3.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableClienMenu_3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                # print(column_number)
                self.ui.tableClienMenu_3.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def modifier_facture(self):
        message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            try:
                idDossier = self.ui.tableClienMenu_3.item(self.ui.tableClienMenu_3.currentRow(), 1).text()
                date = self.ui.tableClienMenu_3.item(self.ui.tableClienMenu_3.currentRow(), 2).text()
                totprest = self.ui.tableClienMenu_3.item(self.ui.tableClienMenu_3.currentRow(), 4).text()
                tva = self.ui.tableClienMenu_3.item(self.ui.tableClienMenu_3.currentRow(), 3).text()
                totdebour = self.ui.tableClienMenu_3.item(self.ui.tableClienMenu_3.currentRow(), 5).text()
                droitT = self.ui.tableClienMenu_3.item(self.ui.tableClienMenu_3.currentRow(), 6).text()
                etatP = self.ui.tableClienMenu_3.item(self.ui.tableClienMenu_3.currentRow(), 7).text()
                modeP = self.ui.tableClienMenu_3.item(self.ui.tableClienMenu_3.currentRow(), 8).text()
                id = self.ui.tableClienMenu_3.item(self.ui.tableClienMenu_3.currentRow(), 0).text()
                Factur.modifier_une_facture(id, idDossier, date, tva, totprest, totdebour, droitT, etatP, modeP)
            except:
                message = QMessageBox.warning(self, "Erreur",
                                              "Les données que vous avez saisi ne peuvent pas être insérées!")
        self.ui.afficheFactures_2.click()

    def supprimer_facture(self):
        message = QMessageBox.question(self, "Suppression", "Êtes-vous sûr de supprimer cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            id = self.ui.tableClienMenu_3.item(self.ui.tableClienMenu_3.currentRow(), 0).text()
            Factur.supprimer_facture(id)
        self.ui.afficheFactures_2.click()

    def affiche_design_factures(self):
        sql = "select type,nom_designation from designation"
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def remplir_table_montants(self):
        try:
            column = self.ui.tableWidget.columnCount()
            row = self.ui.tableWidget.currentRow()
            nom_design = self.ui.tableWidget.item(row, 1).text()
            result = [(nom_design, 0, 0)]
            for row_number, row_data in enumerate(result):
                self.ui.designationMontantTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.designationMontantTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            pass

    def rechercher_factures(self):
        id = self.ui.rechercherfacturesMenu.text()
        sql = "SELECT * FROM faacturess WHERE id LIKE '%{}%' ORDER BY id LIMIT 25".format(
            id)
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableClienMenu_3.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableClienMenu_3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableClienMenu_3.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def recherche_designation_dans_facture(self):
        id = self.ui.lineEdit_3.text()
        sql = "SELECT nom_designation FROM designation WHERE nom_designation LIKE '%{}%' ORDER BY nom_designation LIMIT 25".format(
            id)
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    ##################################################### Client ########################################################
    def modifier_client(self):
        message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            try:
                column = self.ui.tableClienMenu.columnCount()
                row = self.ui.tableClienMenu.currentRow()
                nom_cl = self.ui.tableClienMenu.item(row, 0).text()
                observ = self.ui.tableClienMenu.item(row, 5).text()
                mail = self.ui.tableClienMenu.item(row, 4).text()
                tel = self.ui.tableClienMenu.item(row, 6).text()
                adrs = self.ui.tableClienMenu.item(row, 2).text()
                n_rc = self.ui.tableClienMenu.item(row, 7).text()
                n_succ = self.ui.tableClienMenu.item(row, 9).text()
                nis = self.ui.tableClienMenu.item(row, 10).text()
                artcl = self.ui.tableClienMenu.item(row, 11).text()
                exp_rc = self.ui.tableClienMenu.item(row, 13).text()
                exp_mnd = self.ui.tableClienMenu.item(row, 12).text()
                codepstl = self.ui.tableClienMenu.item(row, 1).text()
                mondt = self.ui.tableClienMenu.item(row, 14).text()
                nif = self.ui.tableClienMenu.item(row, 8).text()
                stt_judrq = self.ui.tableClienMenu.item(row, 3).text()
                Client.modifieClient(nom_cl, codepstl, adrs, stt_judrq, mail, observ, tel, n_rc, nif, n_succ, nis,
                                     artcl,
                                     exp_rc, exp_mnd, mondt)
            except:
                message = QMessageBox.warning(self, "Erreur",
                                              "Les données que vous avez saisi ne peuvent pas être insérées!")
        self.affiche_client()

    def recherch_client(self):
        nom = self.ui.rechercherClientMenu.text()
        sql = "SELECT * FROM client WHERE nom_client LIKE '%{}%'  ORDER BY nom_client LIMIT 25".format(nom)
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableClienMenu.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableClienMenu.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableClienMenu.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def affiche_client(self):

        try:
            sql = "select * from client"
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableClienMenu.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableClienMenu.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableClienMenu.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            print("Error")

    def inserer_client(self):
        try:
            nom_cl = self.ui.nom_client.text()
            mail = self.ui.email.text()
            tel = self.ui.numro_tlf.text()
            adrs = self.ui.addresse.text()
            n_rc = self.ui.rc.text()
            n_succ = self.ui.succursale.text()
            nis = self.ui.nic.text()
            artcl = self.ui.article_imposition.text()
            exp_rc = self.ui.expiration_rc.text()
            exp_mnd = self.ui.expiration_mandat.text()
            codepstl = self.ui.code_postal.text()
            mondt = self.ui.numero_mandat.text()
            nif = self.ui.nif.text()
            stt_judrq = self.ui.statut_jurdique.text()
            cl1 = Client(nom_cl, int(codepstl), adrs, stt_judrq, mail, "an observation", tel, n_rc, nif, n_succ,
                         nis, artcl, datetime.now(), datetime.now(), mondt)
            message = QMessageBox.information(self, "Avec succès!",
                                              "Le client " + nom_cl +  " a été enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    ##################################################### Documents ########################################################
    def modifier_dossier(self):
        message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            try:
                column = self.ui.tableDossier.columnCount()
                row = self.ui.tableDossier.currentRow()
                id_dos = self.ui.tableDossier.item(row, 0).text()
                nm_client_d = self.ui.tableDossier.item(row, 1).text()
                nmdeclr = self.ui.tableDossier.item(row, 2).text()
                dateOuverture = self.ui.tableDossier.item(row, 3).text()
                dt_arrv = self.ui.tableDossier.item(row, 4).text()
                dt_ferm = self.ui.tableDossier.item(row, 5).text()
                navire = ""
                navire += self.ui.tableDossier.item(row, 6).text()
                nb_conteneur = ""
                nb_conteneur += self.ui.tableDossier.item(row, 7).text()
                statusDossier = ""
                statusDossier += self.ui.tableDossier.item(row, 8).text()
                nb_ctn = int(nb_conteneur)
                n_fourn = self.ui.tableDossier.item(row, 9).text()
                nm_pays = self.ui.tableDossier.item(row, 10).text()
                ntrans = self.ui.tableDossier.item(row, 11).text()
                ttr_trans = self.ui.tableDossier.item(row, 12).text()
                nomport = self.ui.tableDossier.item(row, 13).text()
                sg = self.ui.tableDossier.item(row, 14).text()
                li_entrepo = self.ui.tableDossier.item(row, 15).text()
                observ = self.ui.tableDossier.item(row, 16).text()
                natrdossier = self.ui.tableDossier.item(row, 17).text()
                gros = self.ui.tableDossier.item(row, 18).text()
                artcl = self.ui.tableDossier.item(row, 19).text()
                cod_mon = self.ui.tableDossier.item(row, 20).text()
                numfiche = self.ui.tableDossier.item(row, 21).text()
                Dossier.modifierDossier(id_dos, nm_client_d, dt_arrv, dt_arrv, dt_ferm, nb_ctn, statusDossier, n_fourn,
                                        nmdeclr, nm_pays, ntrans, ttr_trans, navire, nomport, sg, li_entrepo, observ,
                                        natrdossier, gros, artcl, cod_mon, numfiche)
            except:
                message = QMessageBox.warning(self, "Erreur",
                                              "Les données que vous avez saisi ne peuvent pas être insérées!")
        self.affiche_dossier(self.ui.comboBox.currentText())

    def modifierBon_Sortie(self):
        message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            try:
                column = self.ui.tableBonSortie.columnCount()
                row = self.ui.tableBonSortie.currentRow()
                n_dosier = self.ui.tableBonSortie.item(row, 0).text()
                nbon = self.ui.tableBonSortie.item(row, 1).text()
                dat = self.ui.tableBonSortie.item(row, 2).text()
                pc = self.ui.tableBonSortie.item(row, 3).text()
                chauf = self.ui.tableBonSortie.item(row, 4).text()
                matricule = self.ui.tableBonSortie.item(row, 5).text()
                BonSortie.modifieBonSortie(n_dosier, nbon, dat, pc, matricule, chauf)
            except:
                message = QMessageBox.warning(self, "Erreur",
                                              "Les données que vous avez saisi ne peuvent pas être insérées!")

    def modifeirBon_visite(self):
        message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            try:
                column = self.ui.tableBonVisite.columnCount()
                row = self.ui.tableBonVisite.currentRow()
                n_dosier = ""
                if (self.ui.tableBonVisite.item(row, 0) and self.ui.tableBonVisite.item(row, 0).text()):
                    n_dosier += self.ui.tableBonVisite.item(row, 0).text()
                else:
                    n_dosier += "Null"
                nbon = self.ui.tableBonVisite.item(row, 1).text()
                dat = self.ui.tableBonVisite.item(row, 2).text()
                pc = self.ui.tableBonVisite.item(row, 3).text()
                douan = self.ui.tableBonVisite.item(row, 4).text()
                bur_douane = self.ui.tableBonVisite.item(row, 5).text()
                BonVisite.modifieBonVisite(n_dosier, nbon, dat, pc, bur_douane, douan)
            except:
                message = QMessageBox.warning(self, "Erreur",
                                              "Les données que vous avez saisi ne peuvent pas être insérées!")

    def modifier_Fichier(self):
        message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            try:
                column = self.ui.tableFichier.columnCount()
                row = self.ui.tableFichier.currentRow()
                idFichier = self.ui.tableFichier.item(row, 0).text()
                chemin = self.ui.tableFichier.item(row, 1).text()
                Fichier.modifier_une_fichier(int(idFichier), chemin)
            except:
                message = QMessageBox.warning(self, "Erreur",
                                              "Les données que vous avez saisi ne peuvent pas être insérées!")

    def docum_modification(self):
        message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            if (self.ui.stackedWidget_2.currentWidget() == self.ui.affichDossier):
                self.modifier_dossier()
            elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonSortie):
                self.modifierBon_Sortie()
            elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonvisite):
                self.modifeirBon_visite()
            else:
                self.modifier_Fichier()
        if (self.ui.stackedWidget_2.currentWidget() == self.ui.affichDossier):
            self.affiche_dossier(self.ui.comboBox.currentText())
        elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonSortie):
            self.affiche_bon_sortie()
        elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonvisite):
            self.affiche_bon_visite()
        else:
            self.affiche_fichier()

    def recherch_Documents(self):
        mot = self.ui.rechercher_gestion_document.text()
        if (self.ui.stackedWidget_2.currentWidget() == self.ui.affichDossier):
            sql = "SELECT * FROM dossier WHERE id_dossier LIKE '%{}%'  ORDER BY id_dossier LIMIT 25".format(mot)
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableDossier.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableDossier.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableDossier.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonSortie):
            sql = "SELECT * FROM bon_sortie WHERE id_dossier LIKE '%{}%'  ORDER BY id_dossier LIMIT 25".format(mot)
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableBonSortie.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableBonSortie.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableBonSortie.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonvisite):
            sql = "SELECT * FROM bon_visite WHERE id_dossier LIKE '%{}%'  ORDER BY id_dossier LIMIT 25".format(mot)
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableBonVisite.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableBonVisite.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableBonVisite.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else:
            sql = "SELECT * FROM fichier WHERE id_fichier LIKE '%{}%'  ORDER BY id_fichier LIMIT 25".format(mot)
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableFichier.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableFichier.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableFichier.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def affiche_dossier(self, filter):
        if (filter == "Tout"):
            sql = "select * from dossier"
        elif (filter == "Archivés"):
            sql = "select * from dossier where dossier.statut_dossier= \"Archivé\" "
        else:
            sql = "select * from dossier where  dossier.statut_dossier= \"En cours\" "
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableDossier.setRowCount(0)
        for row_number, row_data in enumerate(result):
            # print(row_number)
            self.ui.tableDossier.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                # print(column_number)
                self.ui.tableDossier.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def affiche_bon_sortie(self):
        sql = "select bon.id_dossier,bon.num_bon,bon.date_Bon,bon.pc,bon_sortie.id_chauffeur,bon_sortie.matricule from bon,bon_sortie Where bon.id_dossier=bon_sortie.id_dossier;"
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableBonSortie.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableBonSortie.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableBonSortie.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def affiche_bon_visite(self):
        sql = "select bon.id_dossier,bon.num_bon,bon.date_Bon,bon.pc,bon_visite.id_douanier,bon_visite.bureau_douane from bon,bon_visite Where bon.id_dossier=bon_visite.id_dossier;"
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableBonVisite.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableBonVisite.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableBonVisite.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def affiche_fichier(self):
        sql = "select * from fichier"
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableFichier.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableFichier.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableFichier.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def gestion_document(self):
        if (self.ui.stackedWidget_2.currentWidget() == self.ui.affichDossier):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formDossier)
        elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonSortie):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formBonSortie)
        elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonvisite):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formBonVisite)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.formfichier)

    def inserBon_Sortie(self):
        try:
            n_dosier = self.ui.numero_dossier_4.text()
            nbon = self.ui.numero_bon.text()
            dat = self.ui.date_4.date().toPyDate()
            pc = self.ui.pc.text()
            matricule = self.ui.matricule.text()
            chauf = self.ui.lineEdit_8.text()
            bs = BonSortie(int(n_dosier), int(nbon), dat, pc, int(chauf), int(matricule))
            message = QMessageBox.information(self, "Avec succès!",
                                              "Le bon de sortie Nº " + nbon + " a été enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def inserBon_visite(self):
        try:
            n_dosier = self.ui.numero_dossier_6.text()
            nbon = self.ui.numero_bon_3.text()
            dat = self.ui.date_6.date().toPyDate()
            pc = self.ui.pc_3.text()
            bur_douane = self.ui.lineEdit_10.text()
            douan = self.ui.douanier.text()
            bvs = BonVisite(int(n_dosier), int(nbon), dat, pc,int(douan), bur_douane)
            message = QMessageBox.information(self, "Avec succès!",
                                              "Le bon de sortie Nº " + nbon + " a été enregistré")

        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def inserer_dossier(self):
        try:
            nm_client_d = self.ui.nom_client_2.text()
            numfiche = self.ui.numero_fichier.text()
            nmdeclr = self.ui.numero_declarant.text()
            stt_dossier = self.ui.statut_dossier.currentText()
            natrdossier = self.ui.nature_dossier.currentText()
            n_fourn = self.ui.numero_fournisseur.text()
            nm_pays = self.ui.nom_pays.text()
            cod_mon = self.ui.code_monnaie.text()
            nvr = self.ui.navire.text()
            ttr_trans = self.ui.titre_transport.text()
            li_entrepo = self.ui.lieu_entreposage.text()
            artcl = self.ui.article.text()
            dt_arrv = self.ui.date_arrive.date().toPyDate()
            dt_oouvrtr = self.ui.date_ouverture.date().toPyDate()
            observ = self.ui.observation.toPlainText()
            idpay = self.ui.id_pays.text()
            nomport = self.ui.nom_port.text()
            nb_ctn = self.ui.nb_conteneur.text()
            ntrans = self.ui.num_transport.text()
            gros = self.ui.gros_4.text()
            sg = self.ui.sg_4.text()
            ds = Dossier(nm_client_d, dt_oouvrtr, dt_arrv, int(nb_ctn), stt_dossier, n_fourn, int(nmdeclr), int(idpay),
                         ntrans, ttr_trans, nvr, nomport, sg, li_entrepo, observ, natrdossier, gros, artcl, cod_mon,
                         int(numfiche))
            if self.ui.checkbox_creationDossierArchivage.isChecked():
                os.mkdir("Dossiersdarchivage/{}".format(ds.getIdDossier()))
                f = Fichier("Dossiersdarchivage/{}".format(ds.getIdDossier()))

            message = QMessageBox.information(self, "Avec succès!",
                                              "Le dossier Nº " + str(ds.getIdDossier()) + " a été bien enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def inserer_Fichier(self):
        try:
            fich = Fichier(self.ui.chemin_form.text())
            message = QMessageBox.information(self, "Avec succès!",
                                              "Le fichier Nº " + str(fich.get_id_fichier()) + " a été enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def suprimer_document(self):
        message = QMessageBox.question(self, "Suppression", "Êtes-vous sûr de supprimer cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            if (self.ui.stackedWidget_2.currentWidget() == self.ui.affichDossier):
                id = int(self.ui.tableDossier.item(self.ui.tableDossier.currentRow(), 0).text())
                Dossier.supprimerDossier(id)
                self.affiche_dossier(self.ui.comboBox.currentText())
            elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonSortie):
                id = int(self.ui.tableBonSortie.item(self.ui.tableBonSortie.currentRow(), 0).text())
                # BonSortie.
                self.affiche_bon_sortie()
            elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonvisite):
                id = int(self.ui.tableBonVisite.item(self.ui.tableBonVisite.currentRow(), 0).text())
                # BonVisite.
                self.affiche_bon_visite()
            else:
                id = int(self.ui.tableFichier.item(self.ui.tableFichier.currentRow(), 0).text())
                Fichier.supprimer_fichier(id)
                self.affiche_fichier()
        if (self.ui.stackedWidget_2.currentWidget() == self.ui.affichDossier):
            self.affiche_dossier(self.ui.comboBox.currentText())
        elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonSortie):
            self.affiche_bon_sortie()
        elif (self.ui.stackedWidget_2.currentWidget() == self.ui.AfficheBonvisite):
            self.affiche_bon_visite()
        else:
            self.affiche_fichier()

    def fermer_dossier(self):
        try:
            if (self.ui.stackedWidget_2.currentWidget() == self.ui.affichDossier):
                column = self.ui.tableDossier.columnCount()
                row = self.ui.tableDossier.currentRow()
                id_dos = self.ui.tableDossier.item(row, 0).text()
                Dossier.fermerDossier(id_dos)
        except:
            pass

    ############################################ Monnaie et Pays ######################################################
    def ajouterPaysOrMonnaie(self):
        if (self.ui.stackedWidget_6.currentWidget() == self.ui.affichePays):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formPays)
            self.afficherPays()
        elif (self.ui.stackedWidget_6.currentWidget() == self.ui.afficheMaonnaie):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formMonnaie)
            self.afficherMonnaie()

    def insererPays(self):
        try:
            nom = self.ui.nom_9.text()
            code = self.ui.code_2.text()
            pays = Pays(code, nom)
            message = QMessageBox.information(self, "Avec succès!",
                                              "Le pays du code " + code + " a été enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def afficherPays(self):
        sql = "select * from Pays ORDER BY code_pays LIMIT 25"
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tablePays.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tablePays.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tablePays.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def insererMonnaie(self):
        try:
            nom = self.ui.nom_pays_2.text()
            code = self.ui.code.text()
            mn = Monnaie(code, nom)
            message = QMessageBox.information(self, "Avec succès!",
                                              "La monnaie du code " + code + " a été enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def afficherMonnaie(self):
        sql = "select * from Monnaie LIMIT 25"
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableMonnaie.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableMonnaie.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableMonnaie.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def supprimerPaysMonnaie(self):
        message = QMessageBox.question(self, "Suppression", "Êtes-vous sûr de supprimer cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            if (self.ui.stackedWidget_6.currentWidget() == self.ui.affichePays):
                code = int(self.ui.tablePays.item(self.ui.tablePays.currentRow(), 0).text())
                Pays.supprimer_pay(code)
                self.afficherPays()
            elif (self.ui.stackedWidget_6.currentWidget() == self.ui.afficheMaonnaie):
                code = self.ui.tableMonnaie.item(self.ui.tableMonnaie.currentRow(), 0).text()
                print("here")
                Monnaie.supprimer_monnaie(code)
                print("here")
                self.afficherMonnaie()

    def modifierPaysMonnaie(self):
        message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            if (self.ui.stackedWidget_6.currentWidget() == self.ui.affichePays):
                try:
                    code = self.ui.tablePays.item(self.ui.tablePays.currentRow(), 0).text()
                    nom_pays = self.ui.tablePays.item(self.ui.tablePays.currentRow(), 1).text()
                    Pays.modifier_pays(int(code), nom_pays)
                    self.ui.pays_unite_monetaire.click()
                except:
                    message = QMessageBox.warning(self, "Erreur",
                                                  "Les données que vous avez saisi ne peuvent pas être insérées!")
            elif (self.ui.stackedWidget_6.currentWidget() == self.ui.afficheMaonnaie):
                try:
                    code = self.ui.tableMonnaie.item(self.ui.tableMonnaie.currentRow(), 0).text()
                    pays = self.ui.tableMonnaie.item(self.ui.tableMonnaie.currentRow(), 1).text()
                    Monnaie.modifier_monnaie(code, pays)
                except:
                    message = QMessageBox.warning(self, "Erreur",
                                                  "Les données que vous avez saisi ne peuvent pas être insérées!")
        self.ui.pays_unite_monetaire.click()

    def recherchePaysMonnaie(self):
        id = self.ui.rechercher_pays_monnaie.text()
        if (self.ui.stackedWidget_6.currentWidget() == self.ui.affichePays):
            sql = "SELECT code_pays,nom_pays FROM pays WHERE code_pays LIKE '%{}%' ORDER BY code_pays LIMIT 25".format(
                id)
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tablePays.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tablePays.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tablePays.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        elif (self.ui.stackedWidget_6.currentWidget() == self.ui.afficheMaonnaie):
            sql = "SELECT code_monnaie, nom_pay FROM Monnaie WHERE code_monnaie LIKE '%{}%' ORDER BY code_monnaie LIMIT 25".format(
                id)
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableMonnaie.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableMonnaie.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableMonnaie.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    ##################################### Transport et livraison ########################################################
    def gestion_supprimer_transport_livraison(self):
        message = QMessageBox.question(self, "Suppresion", "Êtes-vous sûr de supprimer cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            if (self.ui.stackedWidget_3.currentWidget() == self.ui.afficheCAmion):
                self.supprimer_camion()
                self.affiche_camion()
            elif (self.ui.stackedWidget_3.currentWidget() == self.ui.afficheChauffeur):
                self.supprimer_chauffeur()
                self.affiche_chauffeur()
            elif (self.ui.stackedWidget_3.currentWidget() == self.ui.affichFournisseur):
                self.supprimer_four()
                self.affiche_four()
            elif (self.ui.stackedWidget_3.currentWidget() == self.ui.affichIntermediaire):
                self.supprimer_inter()
                self.affiche_inter()

    def supprimer_camion(self):
        id = int(self.ui.tableCamion.item(self.ui.tableCamion.currentRow(), 0).text())
        Camion.supprimer_Camion(id)

    def supprimer_chauffeur(self):
        id = int(self.ui.tableChauffeur_2.item(self.ui.tableChauffeur_2.currentRow(), 0).text())
        Chauffeur.supprimerPersonne(id)

    def supprimer_four(self):
        id = self.ui.tableFournisseur.item(self.ui.tableFournisseur.currentRow(), 0).text()
        Fournisseur.supprimer_Fournisseur(id)

    def supprimer_inter(self):
        id = self.ui.tableIntermediaire.item(self.ui.tableIntermediaire.currentRow(), 0).text()
        Intermediaire.supprimer_intermediaire(id)

    def gestion_rechercher_transport_livraison(self):
        if (self.ui.stackedWidget_3.currentWidget() == self.ui.afficheCAmion):
            self.rechercher_camion()
        elif (self.ui.stackedWidget_3.currentWidget() == self.ui.afficheChauffeur):
            self.rechercher_chauffeur()
        elif (self.ui.stackedWidget_3.currentWidget() == self.ui.affichFournisseur):
            self.rechercher_four()
        elif (self.ui.stackedWidget_3.currentWidget() == self.ui.affichIntermediaire):
            self.rechercher_inter()

    def rechercher_chauffeur(self):
        id = self.ui.rechercher_transport_livraison.text()
        sql = "SELECT chauffeur.id_chauffeur,personne.nom,personne.prenom,personne.date_de_naissance,personne.tele FROM personne,chauffeur WHERE (chauffeur.id_chauffeur = personne.id AND chauffeur.id_chauffeur LIKE '%{}%') ORDER BY id_chauffeur LIMIT 25".format(
            id)
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableChauffeur_2.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableChauffeur_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableChauffeur_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def rechercher_camion(self):
        id = self.ui.rechercher_transport_livraison.text()
        sql = "SELECT * FROM camion WHERE matricule LIKE '%{}%' ORDER BY matricule LIMIT 25".format(
            id)
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableCamion.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableCamion.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableCamion.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def rechercher_four(self):
        id = self.ui.rechercher_transport_livraison.text()
        sql = "SELECT * FROM fournisseur WHERE nom_fournisseur LIKE '%{}%' ORDER BY nom_fournisseur LIMIT 25".format(
            id)
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableFournisseur.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableFournisseur.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableFournisseur.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def rechercher_inter(self):
        id = self.ui.rechercher_transport_livraison.text()
        sql = "SELECT * FROM intermediaire WHERE nom_inter LIKE '%{}%' ORDER BY nom_inter LIMIT 25".format(
            id)
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableIntermediaire.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableIntermediaire.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableIntermediaire.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def gestion_modifier_transport_livraison(self):
        if (self.ui.stackedWidget_3.currentWidget() == self.ui.afficheCAmion):
            message = QMessageBox.warning(self, "Modification", "Vous pouvez pas modifier cet élément")
            self.affiche_camion()
        elif (self.ui.stackedWidget_3.currentWidget() == self.ui.afficheChauffeur):
            message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                           QMessageBox.Yes | QMessageBox.No)
            if (message == QMessageBox.Yes):
                self.modifier_chauffeur()
            self.affiche_chauffeur()
        elif (self.ui.stackedWidget_3.currentWidget() == self.ui.affichFournisseur):
            message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                           QMessageBox.Yes | QMessageBox.No)
            if (message == QMessageBox.Yes):
                self.modifier_four()
            self.affiche_four()
        elif (self.ui.stackedWidget_3.currentWidget() == self.ui.affichIntermediaire):
            message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                           QMessageBox.Yes | QMessageBox.No)
            if (message == QMessageBox.Yes):
                self.modifier_inter()
            self.affiche_inter()

    def modifier_inter(self):
        try:
            column = self.ui.tableIntermediaire.columnCount()
            row = self.ui.tableIntermediaire.currentRow()
            nominter = self.ui.tableIntermediaire.item(row, 0).text()
            newtype = self.ui.tableIntermediaire.item(row, 1).text()
            Intermediaire.modifier_intermediaire(nominter, nominter, newtype)
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Les données que vous avez saisi ne peuvent pas être insérées!")

    def modifier_four(self):
        try:
            column = self.ui.tableFournisseur.columnCount()
            row = self.ui.tableFournisseur.currentRow()
            nom_four = self.ui.tableFournisseur.item(row, 0).text()
            adr = self.ui.tableFournisseur.item(row, 1).text()
            Fournisseur.modifier_Fournisseur(nom_four, nom_four, adr)
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Les données que vous avez saisi ne peuvent pas être insérées!")

    def modifier_chauffeur(self):
        try:
            column = self.ui.tableChauffeur_2.columnCount()
            row = self.ui.tableChauffeur_2.currentRow()
            id = self.ui.tableChauffeur_2.item(row, 0).text()
            newNom = self.ui.tableChauffeur_2.item(row, 1).text()
            newPrenom = self.ui.tableChauffeur_2.item(row, 2).text()
            newDate = self.ui.tableChauffeur_2.item(row, 3).text()
            newTel = self.ui.tableChauffeur_2.item(row, 4).text()
            print(id, newNom, newTel, newDate, newPrenom)
            Chauffeur.modifierChauffeur(int(id), newNom, newPrenom, newDate, newTel)
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Les données que vous avez saisi ne peuvent pas être insérées!")

    def affiche_chauffeur(self):
        try:
            sql = "select chauffeur.id_chauffeur,personne.nom,personne.prenom,personne.date_de_naissance,personne.tele from chauffeur,personne WHERE personne.id = chauffeur.id_chauffeur;"
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableChauffeur_2.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableChauffeur_2.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableChauffeur_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            print("Error")

    def affiche_camion(self):
        try:
            sql = "select * from camion"
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableCamion.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableCamion.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableCamion.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            print("Error")

    def affiche_four(self):
        try:
            sql = "select * from fournisseur"
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableFournisseur.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableFournisseur.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableFournisseur.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            print("Error")

    def affiche_inter(self):
        try:
            sql = "select * from intermediaire"
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableIntermediaire.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableIntermediaire.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableIntermediaire.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            print("Error")

    def gestion_transport_livraison(self):
        if (self.ui.stackedWidget_3.currentWidget() == self.ui.afficheChauffeur):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formChauffeur)
        elif (self.ui.stackedWidget_3.currentWidget() == self.ui.afficheCAmion):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formCamion)
        elif (self.ui.stackedWidget_3.currentWidget() == self.ui.affichFournisseur):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formFournisseur)
        elif (self.ui.stackedWidget_3.currentWidget() == self.ui.affichIntermediaire):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formIntermediaire)

    def inserer_chauffeur(self):
        try:
            nom = self.ui.nom.text()
            prenom = self.ui.prenom.text()
            datenaiss = self.ui.date_8.date()
            datenaiss2 = datenaiss.toPyDate()
            tele = self.ui.numro_tlf.text()
            chauf = Chauffeur(nom, prenom, datenaiss2, tele)
            message = QMessageBox.information(self, "Avec succès!",
                                              "Le chauffeur " + str(chauf.getIdChauffeur()) + " a été enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def inserer_camion(self):
        try:
            matriculee = self.ui.matricule_3.text()
            cam = Camion(matriculee, )
            message = QMessageBox.information(self, "Avec succès!",
                                              "Le camion de matricule " + matriculee + " a été enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def inserer_four(self):
        try:
            nomfourn = self.ui.nom_7.text()
            adrs = self.ui.addresse_2.text()
            four = Fournisseur(nomfourn, adrs)
            message = QMessageBox.information(self, "Avec succès!",
                                              "Le fournisseur " + nomfourn + " a été enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def inserer_inter(self):
        try:
            nom_intr = self.ui.nom_8.text()
            typ = self.ui.type_3.text()
            intermediairee = Intermediaire(nom_intr, typ)
            message = QMessageBox.information(self, "Avec succès!",
                                              "L'intermidiare " + nom_intr + " a été enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    ####################3##################### Marchandise et Emballage ####################################################
    def gestion_supprimer_marchandise_emballage(self):
        message = QMessageBox.question(self, "Suppression", "Êtes-vous sûr de supprimer cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            if (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheEmballage):
                self.supprimer_emballage()
            elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheMarchandise):
                self.supprimer_marchandise()
            elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheNature):
                self.supprimer_nature()
            elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheDesignation):
                self.supprimer_designation()
        if (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheEmballage):
            self.affiche_emballage()
        elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheNature):
            self.affiche_nature_marchandise()
        elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheMarchandise):
            self.affiche_marchandise()
        elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheDesignation):
            self.affiche_designation()

    def supprimer_marchandise(self):
        id = int(self.ui.tableMarchandice.item(self.ui.tableMarchandice.currentRow(), 0).text())
        marchandise.supprimerMarchandise(id)

    def supprimer_emballage(self):
        id = self.ui.tableEmbalage.item(self.ui.tableEmbalage.currentRow(), 0).text()
        emballage.supprimerEmballage(id)

    def supprimer_nature(self):
        id = self.ui.tableNatureMarch.item(self.ui.tableNatureMarch.currentRow(), 0).text()
        Nature_Marchandise.supprimer_nature_marchandise(id)

    def supprimer_designation(self):
        id = self.ui.tableDesigniation.item(self.ui.tableDesigniation.currentRow(), 0).text()
        Designation.supprimer_designation(id)

    def gestion_recherche_marchandise_emballage(self):
        if (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheEmballage):
            self.recherche_emballage()
        elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheMarchandise):
            self.recherche_marchandise()
        elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheNature):
            self.recherche_nature()
        elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheDesignation):
            self.recherche_designation()

    def recherche_marchandise(self):
        id = self.ui.rechercher_marchandise_embalage.text()
        sql = "SELECT id_marchandise,poids,num_facture,nature,montant,id_dossier,id_emballage,description FROM marchandise WHERE id_marchandise LIKE '%{}%' ORDER BY id_marchandise LIMIT 25".format(
            id)
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableMarchandice.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableMarchandice.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableMarchandice.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def recherche_emballage(self):
        id = self.ui.rechercher_marchandise_embalage.text()
        sql = "SELECT id_emballage,genre,type,pieds,id_dossier FROM emballage WHERE id_emballage LIKE '%{}%' ORDER BY id_emballage LIMIT 25".format(
            id)
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableEmbalage.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableEmbalage.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableEmbalage.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def recherche_nature(self):
        id = self.ui.rechercher_marchandise_embalage.text()
        sql = "SELECT nature FROM nature_marchandise WHERE nature LIKE '%{}%' ORDER BY nature LIMIT 25".format(
            id)
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableNatureMarch.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableNatureMarch.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableNatureMarch.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def recherche_designation(self):
        id = self.ui.rechercher_marchandise_embalage.text()
        sql = "SELECT nom_designation,type,id_marchandise FROM designation WHERE nom_designation LIKE '%{}%' ORDER BY nom_designation LIMIT 25".format(
            id)
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableDesigniation.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableDesigniation.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableDesigniation.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def gestion_modifier_marchandise_emballage(self):
        if (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheEmballage):
            message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                           QMessageBox.Yes | QMessageBox.No)
            if (message == QMessageBox.Yes):
                self.modifier_emballage()
            self.affiche_emballage()
        elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheMarchandise):
            message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                           QMessageBox.Yes | QMessageBox.No)
            if (message == QMessageBox.Yes):
                self.modifier_marchandise()
            self.affiche_marchandise()
        elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheNature):
            message = QMessageBox.warning(self, "Modification", "Vous pouvez pas modifier cet élément")
            self.affiche_nature_marchandise()
        elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheDesignation):
            message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                           QMessageBox.Yes | QMessageBox.No)
            if (message == QMessageBox.Yes):
                self.modifier_designation()
            self.affiche_designation()

    def modifier_marchandise(self):
        try:
            column = self.ui.tableMarchandice.columnCount()
            row = self.ui.tableMarchandice.currentRow()
            id_marchandise = self.ui.tableMarchandice.item(row, 0).text()
            poids = self.ui.tableMarchandice.item(row, 1).text()
            num_fac = self.ui.tableMarchandice.item(row, 2).text()
            nat = self.ui.tableMarchandice.item(row, 3).text()
            montant = self.ui.tableMarchandice.item(row, 4).text()
            id_doss = self.ui.tableMarchandice.item(row, 5).text()
            emba = self.ui.tableMarchandice.item(row, 6).text()
            descr = self.ui.tableMarchandice.item(row, 7).text()
            marchandise.modifier_marchandise(id_marchandise, poids, num_fac, nat, montant, id_doss, emba, descr)
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Les données que vous avez saisi ne peuvent pas être insérées!")

    def modifier_emballage(self):
        try:
            column = self.ui.tableEmbalage.columnCount()
            row = self.ui.tableEmbalage.currentRow()
            id_emballage = self.ui.tableEmbalage.item(row, 0).text()
            new_genre = self.ui.tableEmbalage.item(row, 1).text()
            new_type = self.ui.tableEmbalage.item(row, 2).text()
            new_pieds = self.ui.tableEmbalage.item(row, 3).text()
            id_doss = self.ui.tableEmbalage.item(row, 4).text()
            emballage.modifier_emballage(id_emballage, new_genre, new_type, new_pieds, id_doss)
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Les données que vous avez saisi ne peuvent pas être insérées!")

    def modifier_designation(self):
        try:
            column = self.ui.tableDesigniation.columnCount()
            row = self.ui.tableDesigniation.currentRow()
            nom_designation = self.ui.tableDesigniation.item(row, 0).text()
            new_type = self.ui.tableDesigniation.item(row, 1).text()
            new_id_march = self.ui.tableDesigniation.item(row, 2).text()
            Designation.modifier_designation(nom_designation, new_type, new_id_march)
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Les données que vous avez saisi ne peuvent pas être insérées!")

    def affiche_marchandise(self):
        try:
            sql = "select * from marchandise"
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableMarchandice.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableMarchandice.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    # print(column_number)
                    self.ui.tableMarchandice.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            print("Error")

    def affiche_nature_marchandise(self):
        try:
            sql = "select * from nature_marchandise"
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableNatureMarch.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableNatureMarch.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    # print(column_number)
                    self.ui.tableNatureMarch.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            print("Error")

    def affiche_emballage(self):
        try:
            sql = "select * from emballage"
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableEmbalage.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableEmbalage.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    # print(column_number)
                    self.ui.tableEmbalage.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            print("Error")

    def affiche_designation(self):
        try:
            sql = "select * from designation"
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableDesigniation.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableDesigniation.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    # print(column_number)
                    self.ui.tableDesigniation.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            print("Error")

    def gestion_marchandise_emballage(self):
        if (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheEmballage):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formEmballage)
        elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheMarchandise):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formMarchandice)
        elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheNature):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formNaturemarchandice)
        elif (self.ui.stackedWidget_5.currentWidget() == self.ui.afficheDesignation):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formDesigniation)

    def inserer_marchandise(self):
        try:
            poids = self.ui.poids.text()
            num_fac = self.ui.numfacture.text()
            nat = self.ui.nature.text()
            montant = self.ui.montant.text()
            id_doss = self.ui.numdossier.text()
            emba = self.ui.emballage.text()
            descr = self.ui.description.toPlainText()
            march1 = marchandise(int(poids), num_fac, nat, int(montant), int(id_doss), int(emba), descr)
            message = QMessageBox.information(self, "Avec succès!",
                                              "Cette marchandise a été bien enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")



    def inserer_nature_marchandise(self):
        try:
            nature = self.ui.nature_2.text()
            natmarch = Nature_Marchandise(nature, )
            message = QMessageBox.information(self, "Avec succès!",
                                             nature + " a été enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def inserer_emballage(self):
        try:
            idemb = self.ui.id_emballge_edit.text()
            genre = self.ui.genre.text()
            typee = self.ui.type_2.text()
            pieds = self.ui.pieds.text()
            iddossier = self.ui.numero_dossier_8.text()
            emb = emballage(idemb, genre, typee, pieds, int(iddossier))
            message = QMessageBox.information(self, "Avec succès!",
                                              "L'emballage Nº " + idemb + " a été bien enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def inserer_designation(self):
        try:
            nomdes = self.ui.nom_4.text()
            typedes = self.ui.type.text()
            idmarcha = self.ui.num_marchandise.text()
            des = Designation(nomdes, typedes, int(idmarcha))
            message = QMessageBox.information(self, "Avec succès!",
                                              "La désignation " + nomdes + " a été enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    ############################## Deconnection ########################################################################
    def deconnection(self):
        app.quit()
        open("cookies.txt", 'w').close()

    ############################## Ineternes ########################################################################
    def supprimer_interne(self):
        message = QMessageBox.question(self, "Suppression", "Êtes-vous sûr de suppression cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            if (self.ui.stackedWidget_4.currentWidget() == self.ui.afficheDeclarent):
                id = int(self.ui.tableDeclarent.item(self.ui.tableDeclarent.currentRow(), 0).text())
                Declarant.supprimerPersonne(id)
            elif (self.ui.stackedWidget_4.currentWidget() == self.ui.affichUtilisateur):
                id = int(self.ui.tableUtilisateur.item(self.ui.tableUtilisateur.currentRow(), 0).text())
                Utilisateur.supprimerPersonne(id)
        if (self.ui.stackedWidget_4.currentWidget() == self.ui.afficheDeclarent):
            self.affiche_declarant()
        elif (self.ui.stackedWidget_4.currentWidget() == self.ui.affichUtilisateur):
            self.affiche_utilisateur()

    def recherche_interne(self):
        id = self.ui.rechercher_personnel_interne.text()
        if (self.ui.stackedWidget_4.currentWidget() == self.ui.afficheDeclarent):
            sql = "SELECT personne.id,personne.nom,personne.prenom,personne.date_de_naissance,personne.tele FROM Personne WHERE nom LIKE '%{}%' AND type='declarant' ORDER BY id LIMIT 25".format(
                id)
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableDeclarent.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableDeclarent.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableDeclarent.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        elif (self.ui.stackedWidget_4.currentWidget() == self.ui.affichUtilisateur):
            sql = "SELECT personne.id,personne.nom,personne.prenom,personne.date_de_naissance,personne.tele FROM Personne WHERE nom LIKE '%{}%' AND type='utilisateur' ORDER BY id LIMIT 25".format(
                id)
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.tableUtilisateur.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableUtilisateur.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableUtilisateur.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def modifier_interne(self):
        message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            if (self.ui.stackedWidget_4.currentWidget() == self.ui.afficheDeclarent):
                try:
                    nom = self.ui.tableDeclarent.item(self.ui.tableDeclarent.currentRow(), 1).text()
                    prenom = self.ui.tableDeclarent.item(self.ui.tableDeclarent.currentRow(), 2).text()
                    tele = self.ui.tableDeclarent.item(self.ui.tableDeclarent.currentRow(), 4).text()
                    dateDeNaissance = self.ui.tableDeclarent.item(self.ui.tableDeclarent.currentRow(), 3).text()
                    id = self.ui.tableDeclarent.item(self.ui.tableDeclarent.currentRow(), 0).text()
                    Declarant.modifierDeclarant(int(id), nom, prenom, dateDeNaissance, tele)
                except:
                    message = QMessageBox.warning(self, "Erreur",
                                                  "Les données que vous avez saisi ne peuvent pas être insérées!")
            elif (self.ui.stackedWidget_4.currentWidget() == self.ui.affichUtilisateur):
                try:
                    nom = self.ui.tableUtilisateur.item(self.ui.tableUtilisateur.currentRow(), 1).text()
                    prenom = self.ui.tableUtilisateur.item(self.ui.tableUtilisateur.currentRow(), 2).text()
                    tele = self.ui.tableUtilisateur.item(self.ui.tableUtilisateur.currentRow(), 4).text()
                    dateDeNaissance = self.ui.tableUtilisateur.item(self.ui.tableUtilisateur.currentRow(), 3).text()
                    id = self.ui.tableUtilisateur.item(self.ui.tableUtilisateur.currentRow(), 0).text()
                    pw = self.ui.tableUtilisateur.item(self.ui.tableUtilisateur.currentRow(), 5).text()
                    Utilisateur.modifierUtilisateur(int(id), nom, prenom, dateDeNaissance, tele, pw)
                except:
                    message = QMessageBox.warning(self, "Erreur",
                                                  "Les données que vous avez saisi ne peuvent pas être insérées!")
        if (self.ui.stackedWidget_4.currentWidget() == self.ui.afficheDeclarent):
            self.affiche_declarant()
        elif (self.ui.stackedWidget_4.currentWidget() == self.ui.affichUtilisateur):
            self.affiche_utilisateur()

    def gestion_formulaire_interne(self):
        if (self.ui.stackedWidget_4.currentWidget() == self.ui.afficheDeclarent):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formDeclarent)
        elif (self.ui.stackedWidget_4.currentWidget() == self.ui.affichUtilisateur):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formUser)

    def insererUser(self):
        try:
            nom = self.ui.nom_11.text()
            prenom = self.ui.prenom_7.text()
            tele = self.ui.tel_4.text()
            passwd = self.ui.passw.text()
            dateDeNaissance = self.ui.date_11.date().toPyDate()
            user = Utilisateur(nom, prenom, dateDeNaissance, tele, passwd)
            message = QMessageBox.information(self, "Avec succès!",
                                              "L'utilisateur " + str(user.getIdUtilisateur()) + " a été enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def insererDeclarant(self):
        try:
            nom = self.ui.nom_3.text()
            prenom = self.ui.prenom_3.text()
            tele = self.ui.numero_tlf_2.text()
            dateDeNaissance = self.ui.date_10.date().toPyDate()
            declarant = Declarant(nom, prenom, dateDeNaissance, tele)
            num = declarant.getIdDeclarant()
            message = QMessageBox.information(self, "Avec succès!",
                                              "Le déclarant Nº" + str(num) + " a été bien enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Il y a des champs vides ou les données ne sont pas compatibles!")

    def affiche_declarant(self):
        sql = "select personne.id,personne.nom,personne.prenom,personne.date_de_naissance,personne.tele from personne,declarant Where personne.id=declarant.idDeclarant ORDER BY Personne.id LIMIT 25"
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableDeclarent.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableDeclarent.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableDeclarent.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def affiche_utilisateur(self):
        sql = "select personne.id,personne.nom,personne.prenom,personne.date_de_naissance,personne.tele,utilisateur.password from personne,utilisateur Where personne.id=utilisateur.id_utilisateur;"
        cur.execute(sql)
        result = cur.fetchall()
        self.ui.tableUtilisateur.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableUtilisateur.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableUtilisateur.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    ############################## Externes ########################################################################
    def affiche_douanier(self):
        try:
            sql = "select personne.id,personne.nom,personne.prenom,personne.tele,personne.date_de_naissance from personne,douanier WHERE personne.id=douanier.id_douanier"
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.table_douanier.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.table_douanier.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.table_douanier.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            print("Error")

    def affiche_expert(self):
        try:
            sql = "select personne.id,personne.nom,personne.prenom,personne.tele,personne.date_de_naissance,expert.domaine from personne,expert WHERE personne.id=expert.id_expert"
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.table_expert.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.table_expert.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.table_expert.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            print("Error")

    def affiche_representant(self):
        try:
            sql = "select personne.id,personne.nom,personne.prenom,personne.tele,personne.date_de_naissance,representant.id_client from personne,representant WHERE personne.id=representant.id_representant"
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.table_representant.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.table_representant.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.table_representant.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            print("Error")

    def inserer_douanier(self):
        try:
            nom = self.ui.nom_5.text()
            prenom = self.ui.prenom_4.text()
            datenaiss = self.ui.dateEdit.date().toPyDate()
            tele = self.ui.tel.text()
            douanier = Douanier(nom, prenom, datenaiss, tele)
            message = QMessageBox.information(self, "Avec succès!",
                                              "Le déclarant Nº" + str(douanier.getIdDouanier()) + " a été bien enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Les données que vous avez saisi ne peuvent pas être insérées!")

    def inserer_expert(self):
        try:
            nom = self.ui.nom_6.text()
            prenom = self.ui.prenom_5.text()
            datenaiss = self.ui.dateEdit_2.date().toPyDate()
            tele = self.ui.tel_2.text()
            domaine = self.ui.domaine.text()
            expert = Expert(nom, prenom, datenaiss, tele, domaine)
            message = QMessageBox.information(self, "Avec succès!",
                                              "Le déclarant Nº" + str(expert.getIdExpert()) + " a été bien enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Les données que vous avez saisi ne peuvent pas être insérées!")

    def inserer_representant(self):
        try:
            nom = self.ui.nom_10.text()
            prenom = self.ui.prenom_6.text()
            datenaiss = self.ui.date_nec.date().toPyDate()
            tele = self.ui.tel_3.text()
            nomclient = self.ui.nom_client_3.text()
            representant = Representant(nom, prenom, datenaiss, tele, nomclient)
            message = QMessageBox.information(self, "Avec succès!",
                                              "Le déclarant Nº" + str(representant.getIdRepresentant()) + " a été bien enregistré")
        except:
            message = QMessageBox.warning(self, "Erreur",
                                          "Les données que vous avez saisi ne peuvent pas être insérées!")

    def recherche_externe(self):
        id = self.ui.rechercher_externe.text()
        if (self.ui.stackedWidget_7.currentWidget() == self.ui.afficheDouanier):
            sql = "SELECT personne.id,personne.nom,personne.prenom,personne.date_de_naissance,personne.tele FROM Personne WHERE nom LIKE '%{}%' AND type='douanier' ORDER BY id LIMIT 25".format(
                id)
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.table_douanier.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.table_douanier.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.table_douanier.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        elif (self.ui.stackedWidget_7.currentWidget() == self.ui.affiche_expert):
            sql = "SELECT personne.id,personne.nom,personne.prenom,personne.date_de_naissance,personne.tele FROM Personne WHERE nom LIKE '%{}%' AND type='expert' ORDER BY id LIMIT 25".format(
                id)
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.table_expert.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.table_expert.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.table_expert.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        elif (self.ui.stackedWidget_7.currentWidget() == self.ui.affiche_representant):
            sql = "SELECT personne.id,personne.nom,personne.prenom,personne.tele,personne.date_de_naissance,representant.id_client FROM Personne,representant WHERE personne.nom LIKE '%{}%' AND personne.id=representant.id_representant ORDER BY id LIMIT 25".format(
                id)
            cur.execute(sql)
            result = cur.fetchall()
            self.ui.table_representant.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.table_representant.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.table_representant.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def supprimer_externe(self):
        message = QMessageBox.question(self, "Suppression", "Êtes-vous sûr de supprimer cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            if (self.ui.stackedWidget_7.currentWidget() == self.ui.afficheDouanier):
                id = int(self.ui.table_douanier.item(self.ui.table_douanier.currentRow(), 0).text())
                Douanier.supprimerPersonne(id)
            elif (self.ui.stackedWidget_7.currentWidget() == self.ui.affiche_expert):
                id = int(self.ui.table_expert.item(self.ui.table_expert.currentRow(), 0).text())
                Expert.supprimerPersonne(id)
            elif (self.ui.stackedWidget_7.currentWidget() == self.ui.affiche_representant):
                id = int(self.ui.table_representant.item(self.ui.table_representant.currentRow(), 0).text())
                Representant.supprimerPersonne(id)
        if (self.ui.stackedWidget_7.currentWidget() == self.ui.afficheDouanier):
            self.affiche_douanier()
        elif (self.ui.stackedWidget_7.currentWidget() == self.ui.affiche_expert):
            self.affiche_expert()
        elif (self.ui.stackedWidget_7.currentWidget() == self.ui.affiche_representant):
            self.affiche_representant()

    def modifier_externe(self):
        message = QMessageBox.question(self, "Modification", "Êtes-vous sûr de modifier cet élément ?",
                                       QMessageBox.Yes | QMessageBox.No)
        if (message == QMessageBox.Yes):
            if (self.ui.stackedWidget_7.currentWidget() == self.ui.afficheDouanier):
                try:
                    row = self.ui.table_douanier.currentRow()
                    nom = self.ui.table_douanier.item(row, 1).text()
                    prenom = self.ui.table_douanier.item(row, 2).text()
                    tele = self.ui.table_douanier.item(row, 3).text()
                    dateDeNaissance = self.ui.table_douanier.item(row, 4).text()
                    id = self.ui.table_douanier.item(row, 0).text()
                    Douanier.modifierDouanier(int(id), nom, prenom, dateDeNaissance, tele)
                except:
                    message = QMessageBox.warning(self, "Erreur",
                                                  "Les données que vous avez saisi ne peuvent pas être insérées!")
            elif (self.ui.stackedWidget_7.currentWidget() == self.ui.affiche_expert):
                try:
                    row = self.ui.table_expert.currentRow()
                    nom = self.ui.table_expert.item(row, 1).text()
                    prenom = self.ui.table_expert.item(row, 2).text()
                    tele = self.ui.table_expert.item(row, 3).text()
                    dateDeNaissance = self.ui.table_expert.item(row, 4).text()
                    id = self.ui.table_expert.item(row, 0).text()
                    domaine = self.ui.table_expert.item(row, 5).text()
                    Expert.modifierExpert(id, nom, prenom, dateDeNaissance, tele, domaine)
                except:
                    message = QMessageBox.warning(self, "Erreur",
                                                  "Les données que vous avez saisi ne peuvent pas être insérées!")
            else:
                try:
                    row = self.ui.table_representant.currentRow()
                    nom = self.ui.table_representant.item(row, 1).text()
                    prenom = self.ui.table_representant.item(row, 2).text()
                    tele = self.ui.table_representant.item(row, 3).text()
                    dateDeNaissance = self.ui.table_representant.item(row, 4).text()
                    id = self.ui.table_representant.item(row, 0).text()
                    id_client = self.ui.table_representant.item(row, 5).text()
                    Representant.modifierRepresentant(id, nom, prenom, dateDeNaissance, tele, id_client)
                except:
                    message = QMessageBox.warning(self, "Erreur",
                                                  "Les données que vous avez saisi ne peuvent pas être insérées!")
        if (self.ui.stackedWidget_7.currentWidget() == self.ui.afficheDouanier):
            self.affiche_douanier()
        elif (self.ui.stackedWidget_7.currentWidget() == self.ui.affiche_expert):
            self.affiche_expert()
        elif (self.ui.stackedWidget_7.currentWidget() == self.ui.affiche_representant):
            self.affiche_representant()

    def gestion_externe(self):
        if (self.ui.stackedWidget_7.currentWidget() == self.ui.afficheDouanier):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formDouanier)
        elif (self.ui.stackedWidget_7.currentWidget() == self.ui.affiche_expert):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formExpert)
        elif (self.ui.stackedWidget_7.currentWidget() == self.ui.affiche_representant):
            self.ui.stackedWidget.setCurrentWidget(self.ui.formRepresentant)


''' This is the Login Form class '''


class Login(QtWidgets.QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(504, 500)
        self.ui.connecter_4.clicked.connect(lambda: self.se_connecter(window))

    def se_connecter(self, window):
        try:
            id = int(self.ui.tel_8.text())
        except:
            id = 0
        pw = self.ui.mdp_4.text()
        if Utilisateur.login(id, pw):
            window.close()
            window = MainWindow()
            window.ui.welcome_user.setText("   Bienvenu " + Utilisateur.getName(id) + " !")
            window.showMaximized()
            f = open("cookies.txt", 'w')
            cord1 = str(id)
            key = Fernet.generate_key()
            fernet = Fernet(key)
            f.write(key.decode() + '\n')
            f.write(fernet.encrypt(cord1.encode()).decode() + '\n')
            f.close()
        else:
            self.ui.tel_8.setStyleSheet("color: rgb(0,0,0);\n"
                                        "border: 1.3px solid rgb(255, 0,0);\n"
                                        "font-size: 14px;")
            self.ui.mdp_4.setStyleSheet("color: rgb(0,0,0);\n"
                                        "border: 1.3px solid rgb(255,0, 0);\n"
                                        "font-size: 14px;")

class Setting(QtWidgets.QDialog):
    def __init__(self):
        super(Setting, self).__init__()
        self.ui = Ui_Form_2()
        self.ui.setupUi(self)
        self.ui.connecter_4.clicked.connect(lambda : self.valideBDD())

    def valideBDD(self):
        try:
            import subprocess
            bdd = self.ui.tel_8.text()
            ip = self.ui.lineEdit_2.text()
            user = self.ui.lineEdit.text()
            pw = self.ui.mdp_4.text()
            db = mysql.connector.connect(user=user, password=pw,
                                         host=ip, database=bdd)
            st = open("settings.txt","w")
            st.write(bdd+'\n')
            st.write(ip+'\n')
            st.write(user+'\n')
            st.write(pw+'\n')
            st.close()
            os.system("python classes_database_1_2.py")
            self.close()
            subprocess.call("python main.py",shell=True)
        except:
            self.ui.tel_8.setStyleSheet("color: rgb(0,0,0);\n"
                                        "border: 1.3px solid rgb(255, 0,0);\n"
                                        "font-size: 14px;")
            self.ui.mdp_4.setStyleSheet("color: rgb(0,0,0);\n"
                                        "border: 1.3px solid rgb(255,0, 0);\n"
                                        "font-size: 14px;")
            self.ui.lineEdit.setStyleSheet("color: rgb(0,0,0);\n"
                                        "border: 1.3px solid rgb(255, 0,0);\n"
                                        "font-size: 14px;")
            self.ui.lineEdit_2.setStyleSheet("color: rgb(0,0,0);\n"
                                        "border: 1.3px solid rgb(255,0, 0);\n"
                                        "font-size: 14px;")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    settings = open("settings.txt", 'a+')
    cookies = open("cookies.txt", 'a+')
    file_size = os.stat('settings.txt').st_size

    if file_size == 0:
        window = Setting()
        window.show()
    else:
        file_size = os.stat('cookies.txt').st_size
        if file_size == 0:
            window = Login()
            window.show()
        else:
            window = MainWindow()
            cookies.seek(0)
            fernet = Fernet(cookies.readline()[0:-1].encode())
            cord1 = fernet.decrypt(cookies.readline()[0:-1].encode()).decode()
            window.ui.welcome_user.setText("Bienvenu " + Utilisateur.getName(int(cord1)) + " !")
            window.showMaximized()

    cookies.close()
    settings.close()
    sys.exit(app.exec_())