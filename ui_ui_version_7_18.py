# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_version_7_18WYZEKA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject,QRect, QSize, Qt,QDate)
from PyQt5.QtGui import (QBrush, QColor,QCursor, QFont,QIcon,QPainter)
from PyQt5.QtWidgets import *
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis\
        ,QPieSeries,QLineSeries,QValueAxis


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,data1):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1198, 868)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setWindowIcon(QIcon("assets/logo.jpg"))
        MainWindow.setStyleSheet(u"@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;400&display=swap');")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;400&display=swap');")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMinimumSize(QSize(0, 55))
        self.top_bar.setMaximumSize(QSize(16777215, 55))
        self.top_bar.setStyleSheet(u"background-color: white;\n"
"border-bottom: 1px solid #eeeeee;\n"
"font-size: 16px;")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_button = QPushButton(self.top_bar)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setMinimumSize(QSize(250, 55))
        self.menu_button.setMaximumSize(QSize(250, 220))
        self.menu_button.setStyleSheet(u"border: none;\n"
"background-color: rgb(57, 195, 221);\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 22px;\n"
"")

        self.horizontalLayout.addWidget(self.menu_button)

        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spacer)

        self.welcome_user = QLabel(self.top_bar)
        self.welcome_user.setObjectName(u"welcome_user")
        self.welcome_user.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.welcome_user)

        self.horizontalSpacer_3 = QSpacerItem(7, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.settings = QPushButton(self.top_bar)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(25, 25))
        self.settings.setMaximumSize(QSize(25, 25))
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u"assets/setting-lines.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon)

        self.horizontalLayout.addWidget(self.settings)

        self.horizontalSpacer_2 = QSpacerItem(7, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.deconnexion = QPushButton(self.top_bar)
        self.deconnexion.setObjectName(u"deconnexion")
        self.deconnexion.setMinimumSize(QSize(25, 25))
        self.deconnexion.setMaximumSize(QSize(25, 25))
        self.deconnexion.setCursor(QCursor(Qt.PointingHandCursor))
        self.deconnexion.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u"assets/turn-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deconnexion.setIcon(icon1)

        self.horizontalLayout.addWidget(self.deconnexion)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"QFrame {\n"
"	font-family: 'Montserrat', sans-serif;\n"
"	font-size: 20px;\n"
"	color: #090A0B;\n"
"}\n"
"")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_list_container = QFrame(self.content)
        self.menu_list_container.setObjectName(u"menu_list_container")
        self.menu_list_container.setMinimumSize(QSize(250, 0))
        self.menu_list_container.setMaximumSize(QSize(250, 16777215))
        self.menu_list_container.setStyleSheet(u"background-color: #353946;\n"
"font-size: 15px;")
        self.menu_list_container.setFrameShape(QFrame.NoFrame)
        self.menu_list_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu_list_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_list = QFrame(self.menu_list_container)
        self.menu_list.setObjectName(u"menu_list")
        self.menu_list.setMinimumSize(QSize(250, 0))
        self.menu_list.setMaximumSize(QSize(250, 16777215))
        self.menu_list.setStyleSheet(u"QFrame {\n"
"	background-color: #353946;\n"
"}\n"
"QPushButton {\n"
"	border: 1px solid #353946;\n"
"	padding: 15px 0px 15px 0px;\n"
"	background-color: #353946;\n"
"	color: #eeeeee;\n"
"	font-size: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 47, 58);\n"
"	border-left: 5px solid #00BAFF;\n"
"}\n"
"\n"
"\n"
"")
        self.menu_list.setFrameShape(QFrame.NoFrame)
        self.menu_list.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_list)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.statistiques = QPushButton(self.menu_list)
        self.statistiques.setObjectName(u"statistiques")
        self.statistiques.setMinimumSize(QSize(250, 0))
        self.statistiques.setMaximumSize(QSize(250, 16777215))
        self.statistiques.setCursor(QCursor(Qt.PointingHandCursor))
        self.statistiques.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.statistiques, 0, Qt.AlignLeft)

        self.client_menu = QPushButton(self.menu_list)
        self.client_menu.setObjectName(u"client_menu")
        self.client_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.client_menu.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.client_menu)

        self.personnels_interne = QPushButton(self.menu_list)
        self.personnels_interne.setObjectName(u"personnels_interne")
        self.personnels_interne.setMinimumSize(QSize(250, 0))
        self.personnels_interne.setMaximumSize(QSize(250, 16777215))
        self.personnels_interne.setCursor(QCursor(Qt.PointingHandCursor))
        self.personnels_interne.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.personnels_interne, 0, Qt.AlignLeft)

        self.Externe = QPushButton(self.menu_list)
        self.Externe.setObjectName(u"Externe")
        self.Externe.setMinimumSize(QSize(250, 0))
        self.Externe.setMaximumSize(QSize(250, 16777215))
        self.Externe.setCursor(QCursor(Qt.PointingHandCursor))
        self.Externe.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.Externe, 0, Qt.AlignLeft)

        self.documents = QPushButton(self.menu_list)
        self.documents.setObjectName(u"documents")
        self.documents.setMinimumSize(QSize(250, 0))
        self.documents.setMaximumSize(QSize(250, 16777215))
        self.documents.setCursor(QCursor(Qt.PointingHandCursor))
        self.documents.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.documents, 0, Qt.AlignLeft)

        self.marchandise_emballages = QPushButton(self.menu_list)
        self.marchandise_emballages.setObjectName(u"marchandise_emballages")
        self.marchandise_emballages.setMinimumSize(QSize(250, 0))
        self.marchandise_emballages.setMaximumSize(QSize(250, 16777215))
        self.marchandise_emballages.setCursor(QCursor(Qt.PointingHandCursor))
        self.marchandise_emballages.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.marchandise_emballages, 0, Qt.AlignLeft)

        self.transport_livraison = QPushButton(self.menu_list)
        self.transport_livraison.setObjectName(u"transport_livraison")
        self.transport_livraison.setMinimumSize(QSize(250, 0))
        self.transport_livraison.setMaximumSize(QSize(250, 16777215))
        self.transport_livraison.setCursor(QCursor(Qt.PointingHandCursor))
        self.transport_livraison.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.transport_livraison, 0, Qt.AlignLeft)

        self.pays_unite_monetaire = QPushButton(self.menu_list)
        self.pays_unite_monetaire.setObjectName(u"pays_unite_monetaire")
        self.pays_unite_monetaire.setMinimumSize(QSize(250, 0))
        self.pays_unite_monetaire.setMaximumSize(QSize(250, 16777215))
        self.pays_unite_monetaire.setCursor(QCursor(Qt.PointingHandCursor))
        self.pays_unite_monetaire.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pays_unite_monetaire)

        self.facturation = QPushButton(self.menu_list)
        self.facturation.setObjectName(u"facturation")
        self.facturation.setCursor(QCursor(Qt.PointingHandCursor))
        self.facturation.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.facturation)


        self.verticalLayout_2.addWidget(self.menu_list, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.menu_list_container)

        self.content_frame = QFrame(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.content_frame)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, -1)
        self.scroll_area = QScrollArea(self.content_frame)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"QScrollBar:vertical {             \n"
"    border: 1px solid #e5ebf0;\n"
"   	background:white;\n"
"    width:10px;    \n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle{\n"
"     background: rgb(213, 213, 213);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line{\n"
"     background: black;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line{\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"     stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 931, 868))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_57 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.formFacture = QWidget()
        self.formFacture.setObjectName(u"formFacture")
        self.formFacture.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.formFacture)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.fatcture = QFrame(self.formFacture)
        self.fatcture.setObjectName(u"fatcture")
        self.fatcture.setMinimumSize(QSize(0, 300))
        self.fatcture.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.fatcture.setFrameShape(QFrame.NoFrame)
        self.fatcture.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.fatcture)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_3 = QFrame(self.fatcture)
        self.ajouter_et_close_3.setObjectName(u"ajouter_et_close_3")
        self.ajouter_et_close_3.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_3.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_3.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.ajouter_et_close_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.ajouter_3 = QLabel(self.ajouter_et_close_3)
        self.ajouter_3.setObjectName(u"ajouter_3")
        self.ajouter_3.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;\n"
"font-size:20px;")

        self.horizontalLayout_6.addWidget(self.ajouter_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.close_3 = QPushButton(self.ajouter_et_close_3)
        self.close_3.setObjectName(u"close_3")
        self.close_3.setMinimumSize(QSize(25, 25))
        self.close_3.setMaximumSize(QSize(25, 25))
        self.close_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_3.setStyleSheet(u"border: none;")
        icon2 = QIcon()
        icon2.addFile(u"assets/cancel (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_3.setIcon(icon2)
        self.close_3.setIconSize(QSize(14, 14))

        self.horizontalLayout_6.addWidget(self.close_3)


        self.verticalLayout_8.addWidget(self.ajouter_et_close_3)

        self.frame_5 = QFrame(self.fatcture)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 300))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.frame_5.setFont(font)
        self.frame_5.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(1)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(15, 15, 30, -1)
        self.label_117 = QLabel(self.frame_5)
        self.label_117.setObjectName(u"label_117")

        self.gridLayout_4.addWidget(self.label_117, 16, 1, 1, 1)

        self.label_116 = QLabel(self.frame_5)
        self.label_116.setObjectName(u"label_116")

        self.gridLayout_4.addWidget(self.label_116, 14, 1, 1, 1)

        self.totaldebours = QLineEdit(self.frame_5)
        self.totaldebours.setObjectName(u"totaldebours")
        self.totaldebours.setMinimumSize(QSize(0, 30))
        self.totaldebours.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.totaldebours, 15, 2, 1, 1)

        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 15, 1, 1, 1)

        self.verticalSpacer_50 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_50, 4, 1, 1, 5)

        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"border: 1px solid rgb(238, 238, 238);\n"
"column-width: 100px;")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(31)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(128)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(22)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.tableWidget, 7, 5, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 17, 0, 1, 1)

        self.mod_paiement_3 = QLineEdit(self.frame_5)
        self.mod_paiement_3.setObjectName(u"mod_paiement_3")
        self.mod_paiement_3.setMinimumSize(QSize(0, 30))
        self.mod_paiement_3.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_4.addWidget(self.mod_paiement_3, 2, 5, 1, 1)

        self.numero_dossier_3 = QLineEdit(self.frame_5)
        self.numero_dossier_3.setObjectName(u"numero_dossier_3")
        self.numero_dossier_3.setMinimumSize(QSize(0, 30))
        self.numero_dossier_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.numero_dossier_3, 0, 2, 1, 1)

        self.designationMontantTable = QTableWidget(self.frame_5)
        if (self.designationMontantTable.columnCount() < 3):
            self.designationMontantTable.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.designationMontantTable.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.designationMontantTable.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.designationMontantTable.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.designationMontantTable.setObjectName(u"designationMontantTable")
        self.designationMontantTable.setLayoutDirection(Qt.LeftToRight)
        self.designationMontantTable.setStyleSheet(u"border: 1px solid rgb(238, 238, 238);\n"
"column-width: 100px;\n"
"")
        self.designationMontantTable.setFrameShape(QFrame.NoFrame)
        self.designationMontantTable.horizontalHeader().setCascadingSectionResizes(False)
        self.designationMontantTable.horizontalHeader().setMinimumSectionSize(300)
        self.designationMontantTable.horizontalHeader().setDefaultSectionSize(300)
        self.designationMontantTable.horizontalHeader().setHighlightSections(True)
        self.designationMontantTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.designationMontantTable.horizontalHeader().setStretchLastSection(True)
        self.designationMontantTable.verticalHeader().setMinimumSectionSize(50)
        self.designationMontantTable.verticalHeader().setDefaultSectionSize(50)
        self.designationMontantTable.verticalHeader().setHighlightSections(True)
        self.designationMontantTable.verticalHeader().setProperty("showSortIndicator", False)
        self.designationMontantTable.verticalHeader().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.designationMontantTable, 7, 1, 1, 3)

        self.etat_paiement_3 = QComboBox(self.frame_5)
        self.etat_paiement_3.addItem("")
        self.etat_paiement_3.addItem("")
        self.etat_paiement_3.setObjectName(u"etat_paiement_3")
        self.etat_paiement_3.setMinimumSize(QSize(0, 30))
        self.etat_paiement_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.etat_paiement_3, 2, 2, 1, 1)

        self.label_date_ouver_3 = QLabel(self.frame_5)
        self.label_date_ouver_3.setObjectName(u"label_date_ouver_3")

        self.gridLayout_4.addWidget(self.label_date_ouver_3, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)

        self.date_3 = QDateEdit(self.frame_5)
        self.date_3.setObjectName(u"date_3")
        self.date_3.setMinimumSize(QSize(0, 30))
        self.date_3.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(13)
        self.date_3.setFont(font1)
        self.date_3.setDate(QDate(2021, 1, 1))

        self.gridLayout_4.addWidget(self.date_3, 0, 5, 1, 1)

        self.tva = QLineEdit(self.frame_5)
        self.tva.setObjectName(u"tva")
        self.tva.setMinimumSize(QSize(0, 30))
        self.tva.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.tva, 3, 2, 1, 1)

        self.label_date_ferm_3 = QLabel(self.frame_5)
        self.label_date_ferm_3.setObjectName(u"label_date_ferm_3")
        self.label_date_ferm_3.setStyleSheet(u"padding-left:2px;")

        self.gridLayout_4.addWidget(self.label_date_ferm_3, 2, 3, 1, 1)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"padding-left:2px;")

        self.gridLayout_4.addWidget(self.label_13, 3, 3, 1, 1)

        self.label_date_arr_3 = QLabel(self.frame_5)
        self.label_date_arr_3.setObjectName(u"label_date_arr_3")
        self.label_date_arr_3.setStyleSheet(u"padding-left:2px;")

        self.gridLayout_4.addWidget(self.label_date_arr_3, 0, 3, 1, 1)

        self.montantTotal = QLineEdit(self.frame_5)
        self.montantTotal.setObjectName(u"montantTotal")
        self.montantTotal.setMinimumSize(QSize(0, 30))
        self.montantTotal.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.montantTotal, 16, 2, 1, 1)

        self.droitTimbre = QLineEdit(self.frame_5)
        self.droitTimbre.setObjectName(u"droitTimbre")
        self.droitTimbre.setMinimumSize(QSize(0, 30))
        self.droitTimbre.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.droitTimbre, 3, 5, 1, 1)

        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 3, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(3, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 7, 4, 1, 1)

        self.totalPrestation = QLineEdit(self.frame_5)
        self.totalPrestation.setObjectName(u"totalPrestation")
        self.totalPrestation.setMinimumSize(QSize(0, 30))
        self.totalPrestation.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.totalPrestation, 14, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_9, 8, 1, 1, 5)

        self.frame_27 = QFrame(self.frame_5)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_27, 9, 2, 1, 2)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.calculerFacture = QPushButton(self.frame_4)
        self.calculerFacture.setObjectName(u"calculerFacture")
        self.calculerFacture.setMinimumSize(QSize(125, 35))
        self.calculerFacture.setMaximumSize(QSize(125, 35))
        self.calculerFacture.setCursor(QCursor(Qt.PointingHandCursor))
        self.calculerFacture.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(255, 0, 0);\n"
"border: 1px solid  rgb(255, 0, 0);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 66, 66);\n"
"border: 1px solid rgb(255, 66, 66);\n"
"}\n"
"")

        self.horizontalLayout_64.addWidget(self.calculerFacture)

        self.ImprimerFacture = QPushButton(self.frame_4)
        self.ImprimerFacture.setObjectName(u"ImprimerFacture")
        self.ImprimerFacture.setMinimumSize(QSize(125, 35))
        self.ImprimerFacture.setMaximumSize(QSize(125, 35))
        self.ImprimerFacture.setCursor(QCursor(Qt.PointingHandCursor))
        self.ImprimerFacture.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(25, 215, 110);\n"
"border: 1px solid rgb(25, 215, 110);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(26, 236, 117);\n"
"border: 1px solidrgb(26, 236, 117);\n"
"}\n"
"")

        self.horizontalLayout_64.addWidget(self.ImprimerFacture)

        self.enregistrer_facture = QPushButton(self.frame_4)
        self.enregistrer_facture.setObjectName(u"enregistrer_facture")
        self.enregistrer_facture.setMinimumSize(QSize(125, 35))
        self.enregistrer_facture.setMaximumSize(QSize(125, 35))
        self.enregistrer_facture.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_facture.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.horizontalLayout_64.addWidget(self.enregistrer_facture)


        self.gridLayout_4.addWidget(self.frame_4, 17, 3, 1, 3)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 35))
        self.frame_2.setMaximumSize(QSize(16777215, 35))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.buttonAjouterFormFact = QPushButton(self.frame_2)
        self.buttonAjouterFormFact.setObjectName(u"buttonAjouterFormFact")
        self.buttonAjouterFormFact.setMinimumSize(QSize(30, 30))
        self.buttonAjouterFormFact.setMaximumSize(QSize(30, 30))
        self.buttonAjouterFormFact.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonAjouterFormFact.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(25, 215, 110);\n"
"border: 1px solid rgb(25, 215, 110);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(26, 236, 117);\n"
"border: 1px solidrgb(26, 236, 117);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"assets/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonAjouterFormFact.setIcon(icon3)

        self.horizontalLayout_57.addWidget(self.buttonAjouterFormFact)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(30, 30))
        self.pushButton_4.setMaximumSize(QSize(30, 30))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 0, 4);\n"
"border: 1px solid rgb(255, 0, 4);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 66, 66);\n"
"border: 1px solid rgb(255, 66, 66);\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"assets/minus-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)

        self.horizontalLayout_57.addWidget(self.pushButton_4)

        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_3.setStyleSheet(u"")

        self.horizontalLayout_57.addWidget(self.lineEdit_3)


        self.gridLayout_4.addWidget(self.frame_2, 5, 5, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_10, 6, 5, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)


        self.verticalLayout_5.addWidget(self.fatcture)

        self.stackedWidget.addWidget(self.formFacture)
        self.formfichier = QWidget()
        self.formfichier.setObjectName(u"formfichier")
        self.horizontalLayout_54 = QHBoxLayout(self.formfichier)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.page_container_23 = QFrame(self.formfichier)
        self.page_container_23.setObjectName(u"page_container_23")
        self.page_container_23.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_23.setFrameShape(QFrame.NoFrame)
        self.page_container_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.page_container_23)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close = QFrame(self.page_container_23)
        self.ajouter_et_close.setObjectName(u"ajouter_et_close")
        self.ajouter_et_close.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.ajouter_et_close)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.ajouter = QLabel(self.ajouter_et_close)
        self.ajouter.setObjectName(u"ajouter")
        self.ajouter.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_13.addWidget(self.ajouter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.close = QPushButton(self.ajouter_et_close)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(25, 25))
        self.close.setMaximumSize(QSize(25, 25))
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        self.close.setStyleSheet(u"border: none;")
        self.close.setIcon(icon2)
        self.close.setIconSize(QSize(14, 14))

        self.horizontalLayout_13.addWidget(self.close)


        self.verticalLayout_58.addWidget(self.ajouter_et_close)

        self.frame_3 = QFrame(self.page_container_23)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 225))
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit, QTextEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(15, 15, 30, -1)
        self.frame_32 = QFrame(self.frame_3)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 40))
        self.frame_32.setMaximumSize(QSize(16777215, 50))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.parcourir = QPushButton(self.frame_32)
        self.parcourir.setObjectName(u"parcourir")
        self.parcourir.setMinimumSize(QSize(125, 35))
        self.parcourir.setMaximumSize(QSize(125, 35))
        self.parcourir.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(25, 215, 110);\n"
"border: 1px solid rgb(25, 215, 110);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(26, 236, 117);\n"
"border: 1px solidrgb(26, 236, 117);\n"
"}\n"
"")

        self.horizontalLayout_93.addWidget(self.parcourir)

        self.enregistrerfichier = QPushButton(self.frame_32)
        self.enregistrerfichier.setObjectName(u"enregistrerfichier")
        self.enregistrerfichier.setMinimumSize(QSize(125, 35))
        self.enregistrerfichier.setMaximumSize(QSize(125, 35))
        self.enregistrerfichier.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrerfichier.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.horizontalLayout_93.addWidget(self.enregistrerfichier)


        self.gridLayout_2.addWidget(self.frame_32, 2, 0, 1, 3, Qt.AlignRight|Qt.AlignTop)

        self.chemin_form = QLineEdit(self.frame_3)
        self.chemin_form.setObjectName(u"chemin_form")
        self.chemin_form.setMinimumSize(QSize(0, 30))
        self.chemin_form.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.chemin_form, 1, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 0))
        self.label_11.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)


        self.verticalLayout_58.addWidget(self.frame_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_58.addItem(self.verticalSpacer_2)


        self.horizontalLayout_54.addWidget(self.page_container_23)

        self.stackedWidget.addWidget(self.formfichier)
        self.formBonSortie = QWidget()
        self.formBonSortie.setObjectName(u"formBonSortie")
        self.verticalLayout_10 = QVBoxLayout(self.formBonSortie)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.bonSortie = QFrame(self.formBonSortie)
        self.bonSortie.setObjectName(u"bonSortie")
        self.bonSortie.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.bonSortie.setFrameShape(QFrame.NoFrame)
        self.bonSortie.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bonSortie)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_4 = QFrame(self.bonSortie)
        self.ajouter_et_close_4.setObjectName(u"ajouter_et_close_4")
        self.ajouter_et_close_4.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_4.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_4.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.ajouter_et_close_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ajouter_4 = QLabel(self.ajouter_et_close_4)
        self.ajouter_4.setObjectName(u"ajouter_4")
        self.ajouter_4.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_7.addWidget(self.ajouter_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.close_4 = QPushButton(self.ajouter_et_close_4)
        self.close_4.setObjectName(u"close_4")
        self.close_4.setMinimumSize(QSize(25, 25))
        self.close_4.setMaximumSize(QSize(25, 25))
        self.close_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_4.setStyleSheet(u"border: none;")
        self.close_4.setIcon(icon2)
        self.close_4.setIconSize(QSize(14, 14))

        self.horizontalLayout_7.addWidget(self.close_4)


        self.verticalLayout_9.addWidget(self.ajouter_et_close_4)

        self.frame_6 = QFrame(self.bonSortie)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 300))
        self.frame_6.setFont(font)
        self.frame_6.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit, QTextEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(1)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setContentsMargins(15, 15, 30, -1)
        self.pc = QLineEdit(self.frame_6)
        self.pc.setObjectName(u"pc")
        self.pc.setMinimumSize(QSize(0, 30))
        self.pc.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.pc, 4, 2, 1, 3)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 5, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 14, 0, 1, 1)

        self.matricule = QLineEdit(self.frame_6)
        self.matricule.setObjectName(u"matricule")
        self.matricule.setMinimumSize(QSize(0, 30))
        self.matricule.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.matricule, 5, 4, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_6)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 30))
        self.lineEdit_8.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.lineEdit_8, 5, 2, 1, 1)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 3, 1, 1, 1)

        self.numero_bon = QLineEdit(self.frame_6)
        self.numero_bon.setObjectName(u"numero_bon")
        self.numero_bon.setMinimumSize(QSize(0, 30))
        self.numero_bon.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.numero_bon, 2, 2, 1, 3)

        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 2, 1, 1, 1)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label, 0, 1, 1, 1)

        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 4, 1, 1, 1)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 5, 3, 1, 1)

        self.numero_dossier_4 = QLineEdit(self.frame_6)
        self.numero_dossier_4.setObjectName(u"numero_dossier_4")
        self.numero_dossier_4.setMinimumSize(QSize(0, 30))
        self.numero_dossier_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.numero_dossier_4, 0, 2, 1, 3)

        self.enregistrer_bon_de_sortie = QPushButton(self.frame_6)
        self.enregistrer_bon_de_sortie.setObjectName(u"enregistrer_bon_de_sortie")
        self.enregistrer_bon_de_sortie.setMinimumSize(QSize(125, 35))
        self.enregistrer_bon_de_sortie.setMaximumSize(QSize(125, 35))
        self.enregistrer_bon_de_sortie.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_bon_de_sortie.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.enregistrer_bon_de_sortie, 13, 4, 1, 1, Qt.AlignRight)

        self.date_4 = QDateEdit(self.frame_6)
        self.date_4.setObjectName(u"date_4")
        self.date_4.setMinimumSize(QSize(0, 30))
        self.date_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.date_4, 3, 2, 1, 3)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.verticalSpacer_8 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)


        self.verticalLayout_10.addWidget(self.bonSortie)

        self.stackedWidget.addWidget(self.formBonSortie)
        self.modBonSortie = QWidget()
        self.modBonSortie.setObjectName(u"modBonSortie")
        self.horizontalLayout_9 = QHBoxLayout(self.modBonSortie)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.stackedWidget.addWidget(self.modBonSortie)
        self.formBonVisite = QWidget()
        self.formBonVisite.setObjectName(u"formBonVisite")
        self.verticalLayout_13 = QVBoxLayout(self.formBonVisite)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.page_container_2 = QFrame(self.formBonVisite)
        self.page_container_2.setObjectName(u"page_container_2")
        self.page_container_2.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_2.setFrameShape(QFrame.NoFrame)
        self.page_container_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.page_container_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_6 = QFrame(self.page_container_2)
        self.ajouter_et_close_6.setObjectName(u"ajouter_et_close_6")
        self.ajouter_et_close_6.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_6.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_6.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.ajouter_et_close_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.ajouter_6 = QLabel(self.ajouter_et_close_6)
        self.ajouter_6.setObjectName(u"ajouter_6")
        self.ajouter_6.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_10.addWidget(self.ajouter_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.close_6 = QPushButton(self.ajouter_et_close_6)
        self.close_6.setObjectName(u"close_6")
        self.close_6.setMinimumSize(QSize(25, 25))
        self.close_6.setMaximumSize(QSize(25, 25))
        self.close_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_6.setStyleSheet(u"border: none;")
        self.close_6.setIcon(icon2)
        self.close_6.setIconSize(QSize(14, 14))

        self.horizontalLayout_10.addWidget(self.close_6)


        self.verticalLayout_12.addWidget(self.ajouter_et_close_6)

        self.frame_8 = QFrame(self.page_container_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 300))
        self.frame_8.setFont(font)
        self.frame_8.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit, QTextEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setLineWidth(1)
        self.gridLayout_7 = QGridLayout(self.frame_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(10)
        self.gridLayout_7.setContentsMargins(15, 15, 30, -1)
        self.pc_3 = QLineEdit(self.frame_8)
        self.pc_3.setObjectName(u"pc_3")
        self.pc_3.setMinimumSize(QSize(0, 30))
        self.pc_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.pc_3, 4, 2, 1, 3)

        self.label_25 = QLabel(self.frame_8)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_7.addWidget(self.label_25, 5, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_11, 14, 0, 1, 1)

        self.douanier = QLineEdit(self.frame_8)
        self.douanier.setObjectName(u"douanier")
        self.douanier.setMinimumSize(QSize(0, 30))
        self.douanier.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.douanier, 5, 4, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_8)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 30))
        self.lineEdit_10.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.lineEdit_10, 5, 2, 1, 1)

        self.label_26 = QLabel(self.frame_8)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_7.addWidget(self.label_26, 3, 1, 1, 1)

        self.numero_bon_3 = QLineEdit(self.frame_8)
        self.numero_bon_3.setObjectName(u"numero_bon_3")
        self.numero_bon_3.setMinimumSize(QSize(0, 30))
        self.numero_bon_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.numero_bon_3, 2, 2, 1, 3)

        self.label_27 = QLabel(self.frame_8)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_7.addWidget(self.label_27, 2, 1, 1, 1)

        self.label_28 = QLabel(self.frame_8)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.label_28, 0, 1, 1, 1)

        self.label_29 = QLabel(self.frame_8)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_7.addWidget(self.label_29, 4, 1, 1, 1)

        self.label_30 = QLabel(self.frame_8)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_7.addWidget(self.label_30, 5, 3, 1, 1)

        self.numero_dossier_6 = QLineEdit(self.frame_8)
        self.numero_dossier_6.setObjectName(u"numero_dossier_6")
        self.numero_dossier_6.setMinimumSize(QSize(0, 30))
        self.numero_dossier_6.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.numero_dossier_6, 0, 2, 1, 3)

        self.enregistrer_bon_visite = QPushButton(self.frame_8)
        self.enregistrer_bon_visite.setObjectName(u"enregistrer_bon_visite")
        self.enregistrer_bon_visite.setMinimumSize(QSize(125, 35))
        self.enregistrer_bon_visite.setMaximumSize(QSize(125, 35))
        self.enregistrer_bon_visite.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_bon_visite.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.enregistrer_bon_visite, 13, 4, 1, 1, Qt.AlignRight)

        self.date_6 = QDateEdit(self.frame_8)
        self.date_6.setObjectName(u"date_6")
        self.date_6.setMinimumSize(QSize(0, 30))
        self.date_6.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.date_6, 3, 2, 1, 3)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_12)


        self.verticalLayout_13.addWidget(self.page_container_2)

        self.stackedWidget.addWidget(self.formBonVisite)
        self.modBonVisite = QWidget()
        self.modBonVisite.setObjectName(u"modBonVisite")
        self.horizontalLayout_12 = QHBoxLayout(self.modBonVisite)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.stackedWidget.addWidget(self.modBonVisite)
        self.formCamion = QWidget()
        self.formCamion.setObjectName(u"formCamion")
        self.horizontalLayout_15 = QHBoxLayout(self.formCamion)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.page_container_4 = QFrame(self.formCamion)
        self.page_container_4.setObjectName(u"page_container_4")
        self.page_container_4.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_4.setFrameShape(QFrame.NoFrame)
        self.page_container_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.page_container_4)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_8 = QFrame(self.page_container_4)
        self.ajouter_et_close_8.setObjectName(u"ajouter_et_close_8")
        self.ajouter_et_close_8.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_8.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_8.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.ajouter_et_close_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.ajouter_8 = QLabel(self.ajouter_et_close_8)
        self.ajouter_8.setObjectName(u"ajouter_8")
        self.ajouter_8.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_14.addWidget(self.ajouter_8)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.close_8 = QPushButton(self.ajouter_et_close_8)
        self.close_8.setObjectName(u"close_8")
        self.close_8.setMinimumSize(QSize(25, 25))
        self.close_8.setMaximumSize(QSize(25, 25))
        self.close_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_8.setStyleSheet(u"border: none;")
        self.close_8.setIcon(icon2)
        self.close_8.setIconSize(QSize(14, 14))

        self.horizontalLayout_14.addWidget(self.close_8)


        self.verticalLayout_15.addWidget(self.ajouter_et_close_8)

        self.frame_10 = QFrame(self.page_container_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 100))
        self.frame_10.setMaximumSize(QSize(16777215, 100))
        self.frame_10.setFont(font)
        self.frame_10.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit, QTextEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_10.setLineWidth(1)
        self.gridLayout_9 = QGridLayout(self.frame_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(10)
        self.gridLayout_9.setContentsMargins(15, 15, 30, -1)
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_15, 8, 0, 1, 1)

        self.eregistrer_camion = QPushButton(self.frame_10)
        self.eregistrer_camion.setObjectName(u"eregistrer_camion")
        self.eregistrer_camion.setMinimumSize(QSize(125, 35))
        self.eregistrer_camion.setMaximumSize(QSize(125, 35))
        self.eregistrer_camion.setCursor(QCursor(Qt.PointingHandCursor))
        self.eregistrer_camion.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.eregistrer_camion, 7, 2, 1, 1, Qt.AlignRight)

        self.matricule_3 = QLineEdit(self.frame_10)
        self.matricule_3.setObjectName(u"matricule_3")
        self.matricule_3.setMinimumSize(QSize(0, 30))
        self.matricule_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_9.addWidget(self.matricule_3, 0, 2, 1, 1)

        self.label_37 = QLabel(self.frame_10)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_9.addWidget(self.label_37, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_10)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_16)


        self.horizontalLayout_15.addWidget(self.page_container_4)

        self.stackedWidget.addWidget(self.formCamion)
        self.modCamion = QWidget()
        self.modCamion.setObjectName(u"modCamion")
        self.horizontalLayout_17 = QHBoxLayout(self.modCamion)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.stackedWidget.addWidget(self.modCamion)
        self.formChauffeur = QWidget()
        self.formChauffeur.setObjectName(u"formChauffeur")
        self.horizontalLayout_19 = QHBoxLayout(self.formChauffeur)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.page_container_6 = QFrame(self.formChauffeur)
        self.page_container_6.setObjectName(u"page_container_6")
        self.page_container_6.setMinimumSize(QSize(0, 0))
        self.page_container_6.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_6.setFrameShape(QFrame.NoFrame)
        self.page_container_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.page_container_6)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_10 = QFrame(self.page_container_6)
        self.ajouter_et_close_10.setObjectName(u"ajouter_et_close_10")
        self.ajouter_et_close_10.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_10.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_10.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.ajouter_et_close_10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.ajouter_10 = QLabel(self.ajouter_et_close_10)
        self.ajouter_10.setObjectName(u"ajouter_10")
        self.ajouter_10.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_18.addWidget(self.ajouter_10)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_13)

        self.pushButton = QPushButton(self.ajouter_et_close_10)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(25, 25))
        self.pushButton.setMaximumSize(QSize(25, 25))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border: none;")
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_18.addWidget(self.pushButton)


        self.verticalLayout_17.addWidget(self.ajouter_et_close_10)

        self.frame_12 = QFrame(self.page_container_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 260))
        self.frame_12.setMaximumSize(QSize(16777215, 260))
        self.frame_12.setFont(font)
        self.frame_12.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setLineWidth(1)
        self.gridLayout_11 = QGridLayout(self.frame_12)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setVerticalSpacing(10)
        self.gridLayout_11.setContentsMargins(15, 15, 30, -1)
        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_19, 8, 0, 1, 1)

        self.label_39 = QLabel(self.frame_12)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_11.addWidget(self.label_39, 1, 0, 1, 1)

        self.prenom = QLineEdit(self.frame_12)
        self.prenom.setObjectName(u"prenom")
        self.prenom.setMinimumSize(QSize(0, 30))
        self.prenom.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.prenom, 1, 1, 1, 1)

        self.nom = QLineEdit(self.frame_12)
        self.nom.setObjectName(u"nom")
        self.nom.setMinimumSize(QSize(0, 30))
        self.nom.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_11.addWidget(self.nom, 0, 1, 1, 1)

        self.enregistrer_chauffeur = QPushButton(self.frame_12)
        self.enregistrer_chauffeur.setObjectName(u"enregistrer_chauffeur")
        self.enregistrer_chauffeur.setMinimumSize(QSize(125, 35))
        self.enregistrer_chauffeur.setMaximumSize(QSize(125, 35))
        self.enregistrer_chauffeur.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_chauffeur.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_11.addWidget(self.enregistrer_chauffeur, 7, 1, 1, 1, Qt.AlignRight)

        self.label_40 = QLabel(self.frame_12)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_11.addWidget(self.label_40, 3, 0, 1, 1)

        self.label_41 = QLabel(self.frame_12)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_11.addWidget(self.label_41, 0, 0, 1, 1)

        self.label_42 = QLabel(self.frame_12)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_11.addWidget(self.label_42, 2, 0, 1, 1)

        self.numro_tlf = QLineEdit(self.frame_12)
        self.numro_tlf.setObjectName(u"numro_tlf")
        self.numro_tlf.setMinimumSize(QSize(0, 30))
        self.numro_tlf.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.numro_tlf, 2, 1, 1, 1)

        self.date_8 = QDateEdit(self.frame_12)
        self.date_8.setObjectName(u"date_8")
        self.date_8.setMinimumSize(QSize(0, 30))
        self.date_8.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.date_8, 3, 1, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_12)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_20)


        self.horizontalLayout_19.addWidget(self.page_container_6)

        self.stackedWidget.addWidget(self.formChauffeur)
        self.modChauffeur = QWidget()
        self.modChauffeur.setObjectName(u"modChauffeur")
        self.horizontalLayout_21 = QHBoxLayout(self.modChauffeur)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.stackedWidget.addWidget(self.modChauffeur)
        self.formClient = QWidget()
        self.formClient.setObjectName(u"formClient")
        self.horizontalLayout_23 = QHBoxLayout(self.formClient)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.page_container_8 = QFrame(self.formClient)
        self.page_container_8.setObjectName(u"page_container_8")
        self.page_container_8.setMinimumSize(QSize(0, 800))
        self.page_container_8.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_8.setFrameShape(QFrame.NoFrame)
        self.page_container_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.page_container_8)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_12 = QFrame(self.page_container_8)
        self.ajouter_et_close_12.setObjectName(u"ajouter_et_close_12")
        self.ajouter_et_close_12.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_12.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_12.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.ajouter_et_close_12)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.ajouter_12 = QLabel(self.ajouter_et_close_12)
        self.ajouter_12.setObjectName(u"ajouter_12")
        self.ajouter_12.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_22.addWidget(self.ajouter_12)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_15)

        self.close_10 = QPushButton(self.ajouter_et_close_12)
        self.close_10.setObjectName(u"close_10")
        self.close_10.setMinimumSize(QSize(25, 25))
        self.close_10.setMaximumSize(QSize(25, 25))
        self.close_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_10.setStyleSheet(u"border: none;")
        self.close_10.setIcon(icon2)
        self.close_10.setIconSize(QSize(14, 14))

        self.horizontalLayout_22.addWidget(self.close_10)


        self.verticalLayout_19.addWidget(self.ajouter_et_close_12)

        self.formulaire = QFrame(self.page_container_8)
        self.formulaire.setObjectName(u"formulaire")
        self.formulaire.setFont(font)
        self.formulaire.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.formulaire.setFrameShape(QFrame.NoFrame)
        self.formulaire.setFrameShadow(QFrame.Raised)
        self.formulaire.setLineWidth(1)
        self.gridLayout_13 = QGridLayout(self.formulaire)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setVerticalSpacing(10)
        self.gridLayout_13.setContentsMargins(15, 15, 30, -1)
        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_23, 20, 0, 1, 1)

        self.label_47 = QLabel(self.formulaire)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_13.addWidget(self.label_47, 5, 1, 1, 1)

        self.rc = QLineEdit(self.formulaire)
        self.rc.setObjectName(u"rc")
        self.rc.setMinimumSize(QSize(0, 30))
        self.rc.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.rc, 5, 2, 1, 1)

        self.statut_jurdique = QLineEdit(self.formulaire)
        self.statut_jurdique.setObjectName(u"statut_jurdique")
        self.statut_jurdique.setMinimumSize(QSize(0, 30))
        self.statut_jurdique.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.statut_jurdique, 5, 4, 1, 1)

        self.succursale = QLineEdit(self.formulaire)
        self.succursale.setObjectName(u"succursale")
        self.succursale.setMinimumSize(QSize(0, 30))
        self.succursale.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.succursale, 6, 2, 1, 1)

        self.nif = QLineEdit(self.formulaire)
        self.nif.setObjectName(u"nif")
        self.nif.setMinimumSize(QSize(0, 30))
        self.nif.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.nif, 6, 4, 1, 1)

        self.label_48 = QLabel(self.formulaire)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_13.addWidget(self.label_48, 5, 3, 1, 1)

        self.label_49 = QLabel(self.formulaire)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_13.addWidget(self.label_49, 6, 1, 1, 1)

        self.label_50 = QLabel(self.formulaire)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_13.addWidget(self.label_50, 6, 3, 1, 1)

        self.nom_client = QLineEdit(self.formulaire)
        self.nom_client.setObjectName(u"nom_client")
        self.nom_client.setMinimumSize(QSize(0, 30))
        self.nom_client.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.nom_client, 0, 2, 1, 3)

        self.enregistrer_client = QPushButton(self.formulaire)
        self.enregistrer_client.setObjectName(u"enregistrer_client")
        self.enregistrer_client.setMinimumSize(QSize(125, 35))
        self.enregistrer_client.setMaximumSize(QSize(125, 35))
        self.enregistrer_client.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_client.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_13.addWidget(self.enregistrer_client, 19, 4, 1, 1, Qt.AlignRight)

        self.label_51 = QLabel(self.formulaire)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_13.addWidget(self.label_51, 7, 1, 1, 1)

        self.nic = QLineEdit(self.formulaire)
        self.nic.setObjectName(u"nic")
        self.nic.setMinimumSize(QSize(0, 30))
        self.nic.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.nic, 7, 2, 1, 1)

        self.label_52 = QLabel(self.formulaire)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_13.addWidget(self.label_52, 7, 3, 1, 1)

        self.numero_mandat = QLineEdit(self.formulaire)
        self.numero_mandat.setObjectName(u"numero_mandat")
        self.numero_mandat.setMinimumSize(QSize(0, 30))
        self.numero_mandat.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.numero_mandat, 7, 4, 1, 1)

        self.expiration_mandat = QDateEdit(self.formulaire)
        self.expiration_mandat.setObjectName(u"expiration_mandat")
        self.expiration_mandat.setMinimumSize(QSize(0, 30))
        self.expiration_mandat.setMaximumSize(QSize(16777215, 30))
        self.expiration_mandat.setDate(QDate(2021, 1, 1))

        self.gridLayout_13.addWidget(self.expiration_mandat, 10, 2, 1, 3)

        self.numero_tlf = QLineEdit(self.formulaire)
        self.numero_tlf.setObjectName(u"numero_tlf")
        self.numero_tlf.setMinimumSize(QSize(0, 30))
        self.numero_tlf.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.numero_tlf, 3, 2, 1, 3)

        self.label_53 = QLabel(self.formulaire)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_13.addWidget(self.label_53, 3, 1, 1, 1)

        self.email = QLineEdit(self.formulaire)
        self.email.setObjectName(u"email")
        self.email.setMinimumSize(QSize(0, 30))
        self.email.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.email, 2, 2, 1, 3)

        self.label_54 = QLabel(self.formulaire)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_13.addWidget(self.label_54, 8, 1, 1, 1)

        self.label_55 = QLabel(self.formulaire)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_13.addWidget(self.label_55, 2, 1, 1, 1)

        self.label_56 = QLabel(self.formulaire)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"")

        self.gridLayout_13.addWidget(self.label_56, 0, 1, 1, 1)

        self.article_imposition = QLineEdit(self.formulaire)
        self.article_imposition.setObjectName(u"article_imposition")
        self.article_imposition.setMinimumSize(QSize(0, 30))
        self.article_imposition.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.article_imposition, 8, 2, 1, 3)

        self.addresse = QLineEdit(self.formulaire)
        self.addresse.setObjectName(u"addresse")
        self.addresse.setMinimumSize(QSize(0, 30))
        self.addresse.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.addresse, 4, 2, 1, 1)

        self.label_57 = QLabel(self.formulaire)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_13.addWidget(self.label_57, 4, 1, 1, 1)

        self.label_58 = QLabel(self.formulaire)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_13.addWidget(self.label_58, 4, 3, 1, 1)

        self.code_postal = QLineEdit(self.formulaire)
        self.code_postal.setObjectName(u"code_postal")
        self.code_postal.setMinimumSize(QSize(0, 30))
        self.code_postal.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_13.addWidget(self.code_postal, 4, 4, 1, 1)

        self.label_59 = QLabel(self.formulaire)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_13.addWidget(self.label_59, 10, 1, 1, 1)

        self.label_60 = QLabel(self.formulaire)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_13.addWidget(self.label_60, 9, 1, 1, 1)

        self.expiration_rc = QDateEdit(self.formulaire)
        self.expiration_rc.setObjectName(u"expiration_rc")
        self.expiration_rc.setMinimumSize(QSize(0, 30))
        self.expiration_rc.setMaximumSize(QSize(16777215, 30))
        self.expiration_rc.setFont(font1)
        self.expiration_rc.setDate(QDate(2021, 1, 1))

        self.gridLayout_13.addWidget(self.expiration_rc, 9, 2, 1, 3)


        self.verticalLayout_19.addWidget(self.formulaire)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_4)


        self.horizontalLayout_23.addWidget(self.page_container_8)

        self.stackedWidget.addWidget(self.formClient)
        self.formDeclarent = QWidget()
        self.formDeclarent.setObjectName(u"formDeclarent")
        self.horizontalLayout_25 = QHBoxLayout(self.formDeclarent)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.page_container_9 = QFrame(self.formDeclarent)
        self.page_container_9.setObjectName(u"page_container_9")
        self.page_container_9.setMinimumSize(QSize(0, 0))
        self.page_container_9.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_9.setFrameShape(QFrame.NoFrame)
        self.page_container_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.page_container_9)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_13 = QFrame(self.page_container_9)
        self.ajouter_et_close_13.setObjectName(u"ajouter_et_close_13")
        self.ajouter_et_close_13.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_13.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_13.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_13.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.ajouter_et_close_13)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.ajouter_13 = QLabel(self.ajouter_et_close_13)
        self.ajouter_13.setObjectName(u"ajouter_13")
        self.ajouter_13.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_24.addWidget(self.ajouter_13)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_16)

        self.close_11 = QPushButton(self.ajouter_et_close_13)
        self.close_11.setObjectName(u"close_11")
        self.close_11.setMinimumSize(QSize(25, 25))
        self.close_11.setMaximumSize(QSize(25, 25))
        self.close_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_11.setStyleSheet(u"border: none;")
        self.close_11.setIcon(icon2)
        self.close_11.setIconSize(QSize(14, 14))

        self.horizontalLayout_24.addWidget(self.close_11)


        self.verticalLayout_20.addWidget(self.ajouter_et_close_13)

        self.frame_14 = QFrame(self.page_container_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 250))
        self.frame_14.setFont(font)
        self.frame_14.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_14.setLineWidth(1)
        self.gridLayout_14 = QGridLayout(self.frame_14)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setVerticalSpacing(10)
        self.gridLayout_14.setContentsMargins(15, 15, 30, -1)
        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_24, 8, 0, 1, 1)

        self.label_61 = QLabel(self.frame_14)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_14.addWidget(self.label_61, 1, 0, 1, 1)

        self.prenom_3 = QLineEdit(self.frame_14)
        self.prenom_3.setObjectName(u"prenom_3")
        self.prenom_3.setMinimumSize(QSize(0, 30))
        self.prenom_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_14.addWidget(self.prenom_3, 1, 1, 1, 1)

        self.nom_3 = QLineEdit(self.frame_14)
        self.nom_3.setObjectName(u"nom_3")
        self.nom_3.setMinimumSize(QSize(0, 30))
        self.nom_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_14.addWidget(self.nom_3, 0, 1, 1, 1)

        self.enregistrer_declarent = QPushButton(self.frame_14)
        self.enregistrer_declarent.setObjectName(u"enregistrer_declarent")
        self.enregistrer_declarent.setMinimumSize(QSize(125, 35))
        self.enregistrer_declarent.setMaximumSize(QSize(125, 35))
        self.enregistrer_declarent.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_declarent.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_14.addWidget(self.enregistrer_declarent, 7, 1, 1, 1, Qt.AlignRight)

        self.label_62 = QLabel(self.frame_14)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_14.addWidget(self.label_62, 3, 0, 1, 1)

        self.label_63 = QLabel(self.frame_14)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_14.addWidget(self.label_63, 0, 0, 1, 1)

        self.label_64 = QLabel(self.frame_14)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_14.addWidget(self.label_64, 2, 0, 1, 1)

        self.numero_tlf_2 = QLineEdit(self.frame_14)
        self.numero_tlf_2.setObjectName(u"numero_tlf_2")
        self.numero_tlf_2.setMinimumSize(QSize(0, 30))
        self.numero_tlf_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_14.addWidget(self.numero_tlf_2, 2, 1, 1, 1)

        self.date_10 = QDateEdit(self.frame_14)
        self.date_10.setObjectName(u"date_10")
        self.date_10.setMinimumSize(QSize(0, 30))
        self.date_10.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_14.addWidget(self.date_10, 3, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_14)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_25)


        self.horizontalLayout_25.addWidget(self.page_container_9)

        self.stackedWidget.addWidget(self.formDeclarent)
        self.formDesigniation = QWidget()
        self.formDesigniation.setObjectName(u"formDesigniation")
        self.horizontalLayout_27 = QHBoxLayout(self.formDesigniation)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.page_container_10 = QFrame(self.formDesigniation)
        self.page_container_10.setObjectName(u"page_container_10")
        self.page_container_10.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_10.setFrameShape(QFrame.NoFrame)
        self.page_container_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.page_container_10)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_14 = QFrame(self.page_container_10)
        self.ajouter_et_close_14.setObjectName(u"ajouter_et_close_14")
        self.ajouter_et_close_14.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_14.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_14.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_14.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.ajouter_et_close_14)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.ajouter_14 = QLabel(self.ajouter_et_close_14)
        self.ajouter_14.setObjectName(u"ajouter_14")
        self.ajouter_14.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_26.addWidget(self.ajouter_14)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_17)

        self.pushButton_6 = QPushButton(self.ajouter_et_close_14)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(25, 25))
        self.pushButton_6.setMaximumSize(QSize(25, 25))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"border: none;")
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(14, 14))

        self.horizontalLayout_26.addWidget(self.pushButton_6)


        self.verticalLayout_21.addWidget(self.ajouter_et_close_14)

        self.frame_15 = QFrame(self.page_container_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 200))
        self.frame_15.setMaximumSize(QSize(16777215, 210))
        self.frame_15.setFont(font)
        self.frame_15.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit, QTextEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_15.setLineWidth(1)
        self.gridLayout_15 = QGridLayout(self.frame_15)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setVerticalSpacing(10)
        self.gridLayout_15.setContentsMargins(15, 15, 30, -1)
        self.num_marchandisedesignation = QLineEdit(self.frame_15)
        self.num_marchandisedesignation.setObjectName(u"num_marchandisedesignation")
        self.num_marchandisedesignation.setMinimumSize(QSize(0, 30))
        self.num_marchandisedesignation.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_15.addWidget(self.num_marchandisedesignation, 2, 2, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_26, 10, 0, 1, 1)

        self.enregistrer_designation = QPushButton(self.frame_15)
        self.enregistrer_designation.setObjectName(u"enregistrer_designation")
        self.enregistrer_designation.setMinimumSize(QSize(125, 35))
        self.enregistrer_designation.setMaximumSize(QSize(125, 35))
        self.enregistrer_designation.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_designation.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_15.addWidget(self.enregistrer_designation, 9, 2, 1, 1, Qt.AlignRight)

        self.label_67 = QLabel(self.frame_15)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_15.addWidget(self.label_67, 1, 0, 1, 1)

        self.nom_designation = QLineEdit(self.frame_15)
        self.nom_designation.setObjectName(u"nom_designation")
        self.nom_designation.setMinimumSize(QSize(0, 30))
        self.nom_designation.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_15.addWidget(self.nom_designation, 0, 2, 1, 1)

        self.label_65 = QLabel(self.frame_15)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_15.addWidget(self.label_65, 2, 0, 1, 1)

        self.label_66 = QLabel(self.frame_15)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_15.addWidget(self.label_66, 0, 0, 1, 1)

        self.typedesignation = QLineEdit(self.frame_15)
        self.typedesignation.setObjectName(u"typedesignation")
        self.typedesignation.setMinimumSize(QSize(0, 30))
        self.typedesignation.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_15.addWidget(self.typedesignation, 1, 2, 1, 1)


        self.verticalLayout_21.addWidget(self.frame_15)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_27)


        self.horizontalLayout_27.addWidget(self.page_container_10)

        self.stackedWidget.addWidget(self.formDesigniation)
        self.formDossier = QWidget()
        self.formDossier.setObjectName(u"formDossier")
        self.horizontalLayout_29 = QHBoxLayout(self.formDossier)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.page_container_11 = QFrame(self.formDossier)
        self.page_container_11.setObjectName(u"page_container_11")
        self.page_container_11.setMinimumSize(QSize(0, 850))
        self.page_container_11.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_11.setFrameShape(QFrame.NoFrame)
        self.page_container_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.page_container_11)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_15 = QFrame(self.page_container_11)
        self.ajouter_et_close_15.setObjectName(u"ajouter_et_close_15")
        self.ajouter_et_close_15.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_15.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_15.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_15.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.ajouter_et_close_15)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.ajouter_15 = QLabel(self.ajouter_et_close_15)
        self.ajouter_15.setObjectName(u"ajouter_15")
        self.ajouter_15.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_28.addWidget(self.ajouter_15)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_18)

        self.pushButton_8 = QPushButton(self.ajouter_et_close_15)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(25, 25))
        self.pushButton_8.setMaximumSize(QSize(25, 25))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"border: none;")
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QSize(14, 14))

        self.horizontalLayout_28.addWidget(self.pushButton_8)


        self.verticalLayout_22.addWidget(self.ajouter_et_close_15)

        self.fromulaire = QFrame(self.page_container_11)
        self.fromulaire.setObjectName(u"fromulaire")
        self.fromulaire.setFont(font)
        self.fromulaire.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.fromulaire.setFrameShape(QFrame.NoFrame)
        self.fromulaire.setFrameShadow(QFrame.Raised)
        self.fromulaire.setLineWidth(1)
        self.gridLayout_16 = QGridLayout(self.fromulaire)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setVerticalSpacing(10)
        self.gridLayout_16.setContentsMargins(15, 15, 30, -1)
        self.label_73 = QLabel(self.fromulaire)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_16.addWidget(self.label_73, 14, 3, 1, 1)

        self.label_code_monnaie = QLabel(self.fromulaire)
        self.label_code_monnaie.setObjectName(u"label_code_monnaie")

        self.gridLayout_16.addWidget(self.label_code_monnaie, 8, 1, 1, 1)

        self.enregistrer_dossier = QPushButton(self.fromulaire)
        self.enregistrer_dossier.setObjectName(u"enregistrer_dossier")
        self.enregistrer_dossier.setMinimumSize(QSize(125, 35))
        self.enregistrer_dossier.setMaximumSize(QSize(125, 35))
        self.enregistrer_dossier.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_dossier.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_16.addWidget(self.enregistrer_dossier, 22, 4, 1, 1, Qt.AlignRight)

        self.label_75 = QLabel(self.fromulaire)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_16.addWidget(self.label_75, 16, 3, 1, 1)

        self.numero_fichier = QLineEdit(self.fromulaire)
        self.numero_fichier.setObjectName(u"numero_fichier")
        self.numero_fichier.setMinimumSize(QSize(0, 30))
        self.numero_fichier.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.numero_fichier, 2, 2, 1, 3)

        self.label_74 = QLabel(self.fromulaire)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_16.addWidget(self.label_74, 14, 1, 1, 1)

        self.label_titre_transport = QLabel(self.fromulaire)
        self.label_titre_transport.setObjectName(u"label_titre_transport")

        self.gridLayout_16.addWidget(self.label_titre_transport, 12, 1, 1, 1)

        self.label_76 = QLabel(self.fromulaire)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_16.addWidget(self.label_76, 3, 1, 1, 1)

        self.numero_fournisseur = QLineEdit(self.fromulaire)
        self.numero_fournisseur.setObjectName(u"numero_fournisseur")
        self.numero_fournisseur.setMinimumSize(QSize(0, 30))
        self.numero_fournisseur.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.numero_fournisseur, 6, 2, 1, 3)

        self.label_id_trans = QLabel(self.fromulaire)
        self.label_id_trans.setObjectName(u"label_id_trans")

        self.gridLayout_16.addWidget(self.label_id_trans, 12, 3, 1, 1)

        self.date_arrive = QDateEdit(self.fromulaire)
        self.date_arrive.setObjectName(u"date_arrive")
        self.date_arrive.setMinimumSize(QSize(0, 30))
        self.date_arrive.setMaximumSize(QSize(16777215, 30))
        self.date_arrive.setFont(font1)
        self.date_arrive.setDate(QDate(2021, 1, 1))

        self.gridLayout_16.addWidget(self.date_arrive, 17, 2, 1, 3)

        self.label_n_fournisseur = QLabel(self.fromulaire)
        self.label_n_fournisseur.setObjectName(u"label_n_fournisseur")

        self.gridLayout_16.addWidget(self.label_n_fournisseur, 6, 1, 1, 1)

        self.label_date_arr_4 = QLabel(self.fromulaire)
        self.label_date_arr_4.setObjectName(u"label_date_arr_4")

        self.gridLayout_16.addWidget(self.label_date_arr_4, 17, 1, 1, 1)

        self.numero_declarant = QLineEdit(self.fromulaire)
        self.numero_declarant.setObjectName(u"numero_declarant")
        self.numero_declarant.setMinimumSize(QSize(0, 30))
        self.numero_declarant.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.numero_declarant, 3, 2, 1, 3)

        self.lineEdit = QLineEdit(self.fromulaire)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_16.addWidget(self.lineEdit, 4, 2, 1, 1)

        self.label_10 = QLabel(self.fromulaire)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(True)

        self.gridLayout_16.addWidget(self.label_10, 4, 1, 1, 1)

        self.label_72 = QLabel(self.fromulaire)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_16.addWidget(self.label_72, 2, 1, 1, 1)

        self.nature_dossier = QComboBox(self.fromulaire)
        self.nature_dossier.addItem("")
        self.nature_dossier.addItem("")
        self.nature_dossier.setObjectName(u"nature_dossier")
        self.nature_dossier.setMinimumSize(QSize(0, 30))
        self.nature_dossier.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.nature_dossier, 5, 4, 1, 1)

        self.nom_pays = QLineEdit(self.fromulaire)
        self.nom_pays.setObjectName(u"nom_pays")
        self.nom_pays.setMinimumSize(QSize(0, 30))
        self.nom_pays.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.nom_pays, 7, 2, 1, 1)

        self.lieu_entreposage = QLineEdit(self.fromulaire)
        self.lieu_entreposage.setObjectName(u"lieu_entreposage")
        self.lieu_entreposage.setMinimumSize(QSize(0, 30))
        self.lieu_entreposage.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.lieu_entreposage, 14, 2, 1, 1)

        self.label_id_pays = QLabel(self.fromulaire)
        self.label_id_pays.setObjectName(u"label_id_pays")

        self.gridLayout_16.addWidget(self.label_id_pays, 7, 3, 1, 1)

        self.navire = QLineEdit(self.fromulaire)
        self.navire.setObjectName(u"navire")
        self.navire.setMinimumSize(QSize(0, 30))
        self.navire.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.navire, 10, 2, 1, 1)

        self.observation = QTextEdit(self.fromulaire)
        self.observation.setObjectName(u"observation")
        self.observation.setStyleSheet(u"border: 1px solid rgb(238, 238, 238);")
        self.observation.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_16.addWidget(self.observation, 20, 1, 1, 4)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_28, 24, 0, 1, 1)

        self.nom_port = QLineEdit(self.fromulaire)
        self.nom_port.setObjectName(u"nom_port")
        self.nom_port.setMinimumSize(QSize(0, 30))
        self.nom_port.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.nom_port, 8, 4, 1, 1)

        self.id_pays = QLineEdit(self.fromulaire)
        self.id_pays.setObjectName(u"id_pays")
        self.id_pays.setMinimumSize(QSize(0, 30))
        self.id_pays.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.id_pays, 7, 4, 1, 1)

        self.label_nom_pays = QLabel(self.fromulaire)
        self.label_nom_pays.setObjectName(u"label_nom_pays")

        self.gridLayout_16.addWidget(self.label_nom_pays, 7, 1, 1, 1)

        self.label_date_ouver_4 = QLabel(self.fromulaire)
        self.label_date_ouver_4.setObjectName(u"label_date_ouver_4")

        self.gridLayout_16.addWidget(self.label_date_ouver_4, 18, 1, 1, 1)

        self.code_monnaie = QLineEdit(self.fromulaire)
        self.code_monnaie.setObjectName(u"code_monnaie")
        self.code_monnaie.setMinimumSize(QSize(0, 30))
        self.code_monnaie.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.code_monnaie, 8, 2, 1, 1)

        self.article = QLineEdit(self.fromulaire)
        self.article.setObjectName(u"article")
        self.article.setMinimumSize(QSize(0, 30))
        self.article.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.article, 16, 2, 1, 1)

        self.label_69 = QLabel(self.fromulaire)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_16.addWidget(self.label_69, 8, 3, 1, 1)

        self.label_70 = QLabel(self.fromulaire)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_16.addWidget(self.label_70, 19, 1, 1, 1)

        self.sg_4 = QLineEdit(self.fromulaire)
        self.sg_4.setObjectName(u"sg_4")
        self.sg_4.setMinimumSize(QSize(0, 30))
        self.sg_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.sg_4, 16, 4, 1, 1)

        self.date_ouverture = QDateEdit(self.fromulaire)
        self.date_ouverture.setObjectName(u"date_ouverture")
        self.date_ouverture.setMinimumSize(QSize(0, 30))
        self.date_ouverture.setMaximumSize(QSize(16777215, 30))
        self.date_ouverture.setDate(QDate(2021, 1, 1))

        self.gridLayout_16.addWidget(self.date_ouverture, 18, 2, 1, 3)

        self.label_71 = QLabel(self.fromulaire)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_16.addWidget(self.label_71, 5, 1, 1, 1)

        self.num_transport = QLineEdit(self.fromulaire)
        self.num_transport.setObjectName(u"num_transport")
        self.num_transport.setMinimumSize(QSize(0, 30))
        self.num_transport.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.num_transport, 12, 4, 1, 1)

        self.label_nom_client = QLabel(self.fromulaire)
        self.label_nom_client.setObjectName(u"label_nom_client")
        self.label_nom_client.setStyleSheet(u"")

        self.gridLayout_16.addWidget(self.label_nom_client, 0, 1, 1, 1)

        self.statut_dossier = QComboBox(self.fromulaire)
        self.statut_dossier.addItem("")
        self.statut_dossier.addItem("")
        self.statut_dossier.setObjectName(u"statut_dossier")
        self.statut_dossier.setMinimumSize(QSize(0, 30))
        self.statut_dossier.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.statut_dossier, 5, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.fromulaire)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_16.addWidget(self.lineEdit_2, 4, 4, 1, 1)

        self.gros_4 = QLineEdit(self.fromulaire)
        self.gros_4.setObjectName(u"gros_4")
        self.gros_4.setMinimumSize(QSize(0, 30))
        self.gros_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.gros_4, 14, 4, 1, 1)

        self.label_19 = QLabel(self.fromulaire)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.gridLayout_16.addWidget(self.label_19, 4, 3, 1, 1)

        self.nom_client_2 = QLineEdit(self.fromulaire)
        self.nom_client_2.setObjectName(u"nom_client_2")
        self.nom_client_2.setMinimumSize(QSize(0, 30))
        self.nom_client_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.nom_client_2, 0, 2, 1, 3)

        self.label_68 = QLabel(self.fromulaire)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_16.addWidget(self.label_68, 5, 3, 1, 1)

        self.lable_nb_conteneur = QLabel(self.fromulaire)
        self.lable_nb_conteneur.setObjectName(u"lable_nb_conteneur")

        self.gridLayout_16.addWidget(self.lable_nb_conteneur, 10, 3, 1, 1)

        self.nb_conteneur = QLineEdit(self.fromulaire)
        self.nb_conteneur.setObjectName(u"nb_conteneur")
        self.nb_conteneur.setMinimumSize(QSize(0, 30))
        self.nb_conteneur.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.nb_conteneur, 10, 4, 1, 1)

        self.titre_transport = QLineEdit(self.fromulaire)
        self.titre_transport.setObjectName(u"titre_transport")
        self.titre_transport.setMinimumSize(QSize(0, 30))
        self.titre_transport.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.titre_transport, 12, 2, 1, 1)

        self.label_article_4 = QLabel(self.fromulaire)
        self.label_article_4.setObjectName(u"label_article_4")

        self.gridLayout_16.addWidget(self.label_article_4, 16, 1, 1, 1)

        self.label_navire = QLabel(self.fromulaire)
        self.label_navire.setObjectName(u"label_navire")

        self.gridLayout_16.addWidget(self.label_navire, 10, 1, 1, 1)

        self.checkbox_creationDossierArchivage = QCheckBox(self.fromulaire)
        self.checkbox_creationDossierArchivage.setObjectName(u"checkbox_creationDossierArchivage")
        self.checkbox_creationDossierArchivage.setMinimumSize(QSize(0, 25))
        self.checkbox_creationDossierArchivage.setMaximumSize(QSize(16777215, 25))
        self.checkbox_creationDossierArchivage.setStyleSheet(u"background-color:white;\n"
"font-size:24px;\n"
"margin-left:5px;")

        self.gridLayout_16.addWidget(self.checkbox_creationDossierArchivage, 21, 1, 1, 4)

        self.verticalSpacer_13 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_16.addItem(self.verticalSpacer_13, 23, 4, 1, 1)


        self.verticalLayout_22.addWidget(self.fromulaire)


        self.horizontalLayout_29.addWidget(self.page_container_11)

        self.stackedWidget.addWidget(self.formDossier)
        self.formDouanier = QWidget()
        self.formDouanier.setObjectName(u"formDouanier")
        self.horizontalLayout_31 = QHBoxLayout(self.formDouanier)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.page_container_12 = QFrame(self.formDouanier)
        self.page_container_12.setObjectName(u"page_container_12")
        self.page_container_12.setMinimumSize(QSize(0, 0))
        self.page_container_12.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_12.setFrameShape(QFrame.NoFrame)
        self.page_container_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.page_container_12)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_16 = QFrame(self.page_container_12)
        self.ajouter_et_close_16.setObjectName(u"ajouter_et_close_16")
        self.ajouter_et_close_16.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_16.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_16.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_16.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.ajouter_et_close_16)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.ajouter_16 = QLabel(self.ajouter_et_close_16)
        self.ajouter_16.setObjectName(u"ajouter_16")
        self.ajouter_16.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_30.addWidget(self.ajouter_16)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_19)

        self.close_12 = QPushButton(self.ajouter_et_close_16)
        self.close_12.setObjectName(u"close_12")
        self.close_12.setMinimumSize(QSize(25, 25))
        self.close_12.setMaximumSize(QSize(25, 25))
        self.close_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_12.setStyleSheet(u"border: none;")
        self.close_12.setIcon(icon2)
        self.close_12.setIconSize(QSize(14, 14))

        self.horizontalLayout_30.addWidget(self.close_12)


        self.verticalLayout_23.addWidget(self.ajouter_et_close_16)

        self.frame_16 = QFrame(self.page_container_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 220))
        self.frame_16.setFont(font)
        self.frame_16.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_16.setLineWidth(1)
        self.gridLayout_17 = QGridLayout(self.frame_16)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setVerticalSpacing(10)
        self.gridLayout_17.setContentsMargins(15, 15, 30, -1)
        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_29, 8, 0, 1, 1)

        self.label_77 = QLabel(self.frame_16)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_17.addWidget(self.label_77, 1, 0, 1, 1)

        self.prenom_4 = QLineEdit(self.frame_16)
        self.prenom_4.setObjectName(u"prenom_4")
        self.prenom_4.setMinimumSize(QSize(0, 30))
        self.prenom_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_17.addWidget(self.prenom_4, 1, 1, 1, 1)

        self.nom_5 = QLineEdit(self.frame_16)
        self.nom_5.setObjectName(u"nom_5")
        self.nom_5.setMinimumSize(QSize(0, 30))
        self.nom_5.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_17.addWidget(self.nom_5, 0, 1, 1, 1)

        self.enregistrer_douanier = QPushButton(self.frame_16)
        self.enregistrer_douanier.setObjectName(u"enregistrer_douanier")
        self.enregistrer_douanier.setMinimumSize(QSize(125, 35))
        self.enregistrer_douanier.setMaximumSize(QSize(125, 35))
        self.enregistrer_douanier.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_douanier.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_17.addWidget(self.enregistrer_douanier, 7, 1, 1, 1, Qt.AlignRight)

        self.label_78 = QLabel(self.frame_16)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_17.addWidget(self.label_78, 3, 0, 1, 1)

        self.label_79 = QLabel(self.frame_16)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_17.addWidget(self.label_79, 0, 0, 1, 1)

        self.label_80 = QLabel(self.frame_16)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_17.addWidget(self.label_80, 2, 0, 1, 1)

        self.tel = QLineEdit(self.frame_16)
        self.tel.setObjectName(u"tel")
        self.tel.setMinimumSize(QSize(0, 30))
        self.tel.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_17.addWidget(self.tel, 2, 1, 1, 1)

        self.dateEdit = QDateEdit(self.frame_16)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 30))
        self.dateEdit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_17.addWidget(self.dateEdit, 3, 1, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_16)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_30)


        self.horizontalLayout_31.addWidget(self.page_container_12)

        self.stackedWidget.addWidget(self.formDouanier)
        self.formEmballage = QWidget()
        self.formEmballage.setObjectName(u"formEmballage")
        self.horizontalLayout_33 = QHBoxLayout(self.formEmballage)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.page_container_13 = QFrame(self.formEmballage)
        self.page_container_13.setObjectName(u"page_container_13")
        self.page_container_13.setMinimumSize(QSize(0, 0))
        self.page_container_13.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_13.setFrameShape(QFrame.NoFrame)
        self.page_container_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.page_container_13)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_17 = QFrame(self.page_container_13)
        self.ajouter_et_close_17.setObjectName(u"ajouter_et_close_17")
        self.ajouter_et_close_17.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_17.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_17.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_17.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.ajouter_et_close_17)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.ajouter_17 = QLabel(self.ajouter_et_close_17)
        self.ajouter_17.setObjectName(u"ajouter_17")
        self.ajouter_17.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_32.addWidget(self.ajouter_17)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_20)

        self.close_13 = QPushButton(self.ajouter_et_close_17)
        self.close_13.setObjectName(u"close_13")
        self.close_13.setMinimumSize(QSize(25, 25))
        self.close_13.setMaximumSize(QSize(25, 25))
        self.close_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_13.setStyleSheet(u"border: none;")
        self.close_13.setIcon(icon2)
        self.close_13.setIconSize(QSize(14, 14))

        self.horizontalLayout_32.addWidget(self.close_13)


        self.verticalLayout_24.addWidget(self.ajouter_et_close_17)

        self.frame_17 = QFrame(self.page_container_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 260))
        self.frame_17.setFont(font)
        self.frame_17.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_17.setLineWidth(1)
        self.gridLayout_18 = QGridLayout(self.frame_17)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setVerticalSpacing(10)
        self.gridLayout_18.setContentsMargins(15, 15, 30, -1)
        self.numero_dossier_8 = QLineEdit(self.frame_17)
        self.numero_dossier_8.setObjectName(u"numero_dossier_8")
        self.numero_dossier_8.setMinimumSize(QSize(0, 30))
        self.numero_dossier_8.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.numero_dossier_8, 4, 1, 1, 1)

        self.label_82 = QLabel(self.frame_17)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_18.addWidget(self.label_82, 1, 0, 1, 1)

        self.label_81 = QLabel(self.frame_17)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_18.addWidget(self.label_81, 4, 0, 1, 1)

        self.label_84 = QLabel(self.frame_17)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_18.addWidget(self.label_84, 2, 0, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_31, 9, 0, 1, 1)

        self.genre = QLineEdit(self.frame_17)
        self.genre.setObjectName(u"genre")
        self.genre.setMinimumSize(QSize(0, 30))
        self.genre.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.genre, 1, 1, 1, 1)

        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_18.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_83 = QLabel(self.frame_17)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_18.addWidget(self.label_83, 3, 0, 1, 1)

        self.type_2 = QLineEdit(self.frame_17)
        self.type_2.setObjectName(u"type_2")
        self.type_2.setMinimumSize(QSize(0, 30))
        self.type_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.type_2, 2, 1, 1, 1)

        self.enregistrer_emballage = QPushButton(self.frame_17)
        self.enregistrer_emballage.setObjectName(u"enregistrer_emballage")
        self.enregistrer_emballage.setMinimumSize(QSize(125, 35))
        self.enregistrer_emballage.setMaximumSize(QSize(125, 35))
        self.enregistrer_emballage.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_emballage.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_18.addWidget(self.enregistrer_emballage, 8, 1, 1, 1, Qt.AlignRight)

        self.pieds = QLineEdit(self.frame_17)
        self.pieds.setObjectName(u"pieds")
        self.pieds.setMinimumSize(QSize(0, 30))
        self.pieds.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.pieds, 3, 1, 1, 1)

        self.id_emballge_edit = QLineEdit(self.frame_17)
        self.id_emballge_edit.setObjectName(u"id_emballge_edit")
        self.id_emballge_edit.setMinimumSize(QSize(0, 30))
        self.id_emballge_edit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.id_emballge_edit, 0, 1, 1, 1)


        self.verticalLayout_24.addWidget(self.frame_17)

        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_32)


        self.horizontalLayout_33.addWidget(self.page_container_13)

        self.stackedWidget.addWidget(self.formEmballage)
        self.formExpert = QWidget()
        self.formExpert.setObjectName(u"formExpert")
        self.horizontalLayout_35 = QHBoxLayout(self.formExpert)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.page_container_14 = QFrame(self.formExpert)
        self.page_container_14.setObjectName(u"page_container_14")
        self.page_container_14.setMinimumSize(QSize(0, 0))
        self.page_container_14.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_14.setFrameShape(QFrame.NoFrame)
        self.page_container_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.page_container_14)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_18 = QFrame(self.page_container_14)
        self.ajouter_et_close_18.setObjectName(u"ajouter_et_close_18")
        self.ajouter_et_close_18.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_18.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_18.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_18.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.ajouter_et_close_18)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.ajouter_18 = QLabel(self.ajouter_et_close_18)
        self.ajouter_18.setObjectName(u"ajouter_18")
        self.ajouter_18.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_34.addWidget(self.ajouter_18)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_21)

        self.close_14 = QPushButton(self.ajouter_et_close_18)
        self.close_14.setObjectName(u"close_14")
        self.close_14.setMinimumSize(QSize(25, 25))
        self.close_14.setMaximumSize(QSize(25, 25))
        self.close_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_14.setStyleSheet(u"border: none;")
        self.close_14.setIcon(icon2)
        self.close_14.setIconSize(QSize(14, 14))

        self.horizontalLayout_34.addWidget(self.close_14)


        self.verticalLayout_25.addWidget(self.ajouter_et_close_18)

        self.frame_18 = QFrame(self.page_container_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 260))
        self.frame_18.setFont(font)
        self.frame_18.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_18.setLineWidth(1)
        self.gridLayout_19 = QGridLayout(self.frame_18)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setVerticalSpacing(10)
        self.gridLayout_19.setContentsMargins(15, 15, 30, -1)
        self.verticalSpacer_33 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_33, 9, 0, 1, 1)

        self.label_85 = QLabel(self.frame_18)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout_19.addWidget(self.label_85, 2, 0, 1, 1)

        self.label_86 = QLabel(self.frame_18)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_19.addWidget(self.label_86, 1, 0, 1, 1)

        self.tel_2 = QLineEdit(self.frame_18)
        self.tel_2.setObjectName(u"tel_2")
        self.tel_2.setMinimumSize(QSize(0, 30))
        self.tel_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.tel_2, 2, 1, 1, 1)

        self.prenom_5 = QLineEdit(self.frame_18)
        self.prenom_5.setObjectName(u"prenom_5")
        self.prenom_5.setMinimumSize(QSize(0, 30))
        self.prenom_5.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.prenom_5, 1, 1, 1, 1)

        self.nom_6 = QLineEdit(self.frame_18)
        self.nom_6.setObjectName(u"nom_6")
        self.nom_6.setMinimumSize(QSize(0, 30))
        self.nom_6.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.nom_6, 0, 1, 1, 1)

        self.enregistrer_expert = QPushButton(self.frame_18)
        self.enregistrer_expert.setObjectName(u"enregistrer_expert")
        self.enregistrer_expert.setMinimumSize(QSize(125, 35))
        self.enregistrer_expert.setMaximumSize(QSize(125, 35))
        self.enregistrer_expert.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_expert.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_19.addWidget(self.enregistrer_expert, 8, 1, 1, 1, Qt.AlignRight)

        self.label_87 = QLabel(self.frame_18)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_19.addWidget(self.label_87, 3, 0, 1, 1)

        self.label_88 = QLabel(self.frame_18)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_19.addWidget(self.label_88, 0, 0, 1, 1)

        self.label_89 = QLabel(self.frame_18)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_19.addWidget(self.label_89, 4, 0, 1, 1)

        self.domaine = QLineEdit(self.frame_18)
        self.domaine.setObjectName(u"domaine")
        self.domaine.setMinimumSize(QSize(0, 30))
        self.domaine.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.domaine, 4, 1, 1, 1)

        self.dateEdit_2 = QDateEdit(self.frame_18)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(0, 30))
        self.dateEdit_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_19.addWidget(self.dateEdit_2, 3, 1, 1, 1)


        self.verticalLayout_25.addWidget(self.frame_18)

        self.verticalSpacer_34 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_34)


        self.horizontalLayout_35.addWidget(self.page_container_14)

        self.stackedWidget.addWidget(self.formExpert)
        self.formFournisseur = QWidget()
        self.formFournisseur.setObjectName(u"formFournisseur")
        self.horizontalLayout_37 = QHBoxLayout(self.formFournisseur)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.page_container_15 = QFrame(self.formFournisseur)
        self.page_container_15.setObjectName(u"page_container_15")
        self.page_container_15.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_15.setFrameShape(QFrame.NoFrame)
        self.page_container_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.page_container_15)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_19 = QFrame(self.page_container_15)
        self.ajouter_et_close_19.setObjectName(u"ajouter_et_close_19")
        self.ajouter_et_close_19.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_19.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_19.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_19.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.ajouter_et_close_19)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.ajouter_19 = QLabel(self.ajouter_et_close_19)
        self.ajouter_19.setObjectName(u"ajouter_19")
        self.ajouter_19.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_36.addWidget(self.ajouter_19)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_22)

        self.close_15 = QPushButton(self.ajouter_et_close_19)
        self.close_15.setObjectName(u"close_15")
        self.close_15.setMinimumSize(QSize(25, 25))
        self.close_15.setMaximumSize(QSize(25, 25))
        self.close_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_15.setStyleSheet(u"border: none;")
        self.close_15.setIcon(icon2)
        self.close_15.setIconSize(QSize(14, 14))

        self.horizontalLayout_36.addWidget(self.close_15)


        self.verticalLayout_26.addWidget(self.ajouter_et_close_19)

        self.frame_19 = QFrame(self.page_container_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 100))
        self.frame_19.setMaximumSize(QSize(16777215, 160))
        self.frame_19.setFont(font)
        self.frame_19.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit, QTextEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_19.setLineWidth(1)
        self.gridLayout_20 = QGridLayout(self.frame_19)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setVerticalSpacing(10)
        self.gridLayout_20.setContentsMargins(15, 15, 30, -1)
        self.label_90 = QLabel(self.frame_19)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_20.addWidget(self.label_90, 1, 0, 1, 1)

        self.enregistrer_fournisseur = QPushButton(self.frame_19)
        self.enregistrer_fournisseur.setObjectName(u"enregistrer_fournisseur")
        self.enregistrer_fournisseur.setMinimumSize(QSize(125, 35))
        self.enregistrer_fournisseur.setMaximumSize(QSize(125, 35))
        self.enregistrer_fournisseur.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_fournisseur.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_20.addWidget(self.enregistrer_fournisseur, 8, 2, 1, 1, Qt.AlignRight)

        self.nom_7 = QLineEdit(self.frame_19)
        self.nom_7.setObjectName(u"nom_7")
        self.nom_7.setMinimumSize(QSize(0, 30))
        self.nom_7.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_20.addWidget(self.nom_7, 0, 2, 1, 1)

        self.label_91 = QLabel(self.frame_19)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_20.addWidget(self.label_91, 0, 0, 1, 1)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_35, 9, 0, 1, 1)

        self.addresse_2 = QLineEdit(self.frame_19)
        self.addresse_2.setObjectName(u"addresse_2")
        self.addresse_2.setMinimumSize(QSize(0, 30))
        self.addresse_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_20.addWidget(self.addresse_2, 1, 2, 1, 1)


        self.verticalLayout_26.addWidget(self.frame_19)

        self.verticalSpacer_36 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_36)


        self.horizontalLayout_37.addWidget(self.page_container_15)

        self.stackedWidget.addWidget(self.formFournisseur)
        self.formIntermediaire = QWidget()
        self.formIntermediaire.setObjectName(u"formIntermediaire")
        self.horizontalLayout_39 = QHBoxLayout(self.formIntermediaire)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.page_container_16 = QFrame(self.formIntermediaire)
        self.page_container_16.setObjectName(u"page_container_16")
        self.page_container_16.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_16.setFrameShape(QFrame.NoFrame)
        self.page_container_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.page_container_16)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_20 = QFrame(self.page_container_16)
        self.ajouter_et_close_20.setObjectName(u"ajouter_et_close_20")
        self.ajouter_et_close_20.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_20.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_20.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_20.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.ajouter_et_close_20)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.ajouter_20 = QLabel(self.ajouter_et_close_20)
        self.ajouter_20.setObjectName(u"ajouter_20")
        self.ajouter_20.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_38.addWidget(self.ajouter_20)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_23)

        self.close_16 = QPushButton(self.ajouter_et_close_20)
        self.close_16.setObjectName(u"close_16")
        self.close_16.setMinimumSize(QSize(25, 25))
        self.close_16.setMaximumSize(QSize(25, 25))
        self.close_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_16.setStyleSheet(u"border: none;")
        self.close_16.setIcon(icon2)
        self.close_16.setIconSize(QSize(14, 14))

        self.horizontalLayout_38.addWidget(self.close_16)


        self.verticalLayout_27.addWidget(self.ajouter_et_close_20)

        self.frame_20 = QFrame(self.page_container_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 100))
        self.frame_20.setMaximumSize(QSize(16777215, 160))
        self.frame_20.setFont(font)
        self.frame_20.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit, QTextEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_20.setLineWidth(1)
        self.gridLayout_21 = QGridLayout(self.frame_20)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setVerticalSpacing(10)
        self.gridLayout_21.setContentsMargins(15, 15, 30, -1)
        self.verticalSpacer_37 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_37, 9, 0, 1, 1)

        self.label_92 = QLabel(self.frame_20)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_21.addWidget(self.label_92, 1, 0, 1, 1)

        self.enregistrer_intermediaire = QPushButton(self.frame_20)
        self.enregistrer_intermediaire.setObjectName(u"enregistrer_intermediaire")
        self.enregistrer_intermediaire.setMinimumSize(QSize(125, 35))
        self.enregistrer_intermediaire.setMaximumSize(QSize(125, 35))
        self.enregistrer_intermediaire.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_intermediaire.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_21.addWidget(self.enregistrer_intermediaire, 8, 2, 1, 1, Qt.AlignRight)

        self.nom_8 = QLineEdit(self.frame_20)
        self.nom_8.setObjectName(u"nom_8")
        self.nom_8.setMinimumSize(QSize(0, 30))
        self.nom_8.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_21.addWidget(self.nom_8, 0, 2, 1, 1)

        self.label_93 = QLabel(self.frame_20)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_21.addWidget(self.label_93, 0, 0, 1, 1)

        self.type_3 = QLineEdit(self.frame_20)
        self.type_3.setObjectName(u"type_3")
        self.type_3.setMinimumSize(QSize(0, 30))
        self.type_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_21.addWidget(self.type_3, 1, 2, 1, 1)


        self.verticalLayout_27.addWidget(self.frame_20)

        self.verticalSpacer_38 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_38)


        self.horizontalLayout_39.addWidget(self.page_container_16)

        self.stackedWidget.addWidget(self.formIntermediaire)
        self.formMarchandice = QWidget()
        self.formMarchandice.setObjectName(u"formMarchandice")
        self.horizontalLayout_41 = QHBoxLayout(self.formMarchandice)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.page_container_17 = QFrame(self.formMarchandice)
        self.page_container_17.setObjectName(u"page_container_17")
        self.page_container_17.setMinimumSize(QSize(0, 800))
        self.page_container_17.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_17.setFrameShape(QFrame.NoFrame)
        self.page_container_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.page_container_17)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_21 = QFrame(self.page_container_17)
        self.ajouter_et_close_21.setObjectName(u"ajouter_et_close_21")
        self.ajouter_et_close_21.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_21.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_21.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_21.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.ajouter_et_close_21)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.ajouter_21 = QLabel(self.ajouter_et_close_21)
        self.ajouter_21.setObjectName(u"ajouter_21")
        self.ajouter_21.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_40.addWidget(self.ajouter_21)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_24)

        self.close_17 = QPushButton(self.ajouter_et_close_21)
        self.close_17.setObjectName(u"close_17")
        self.close_17.setMinimumSize(QSize(25, 25))
        self.close_17.setMaximumSize(QSize(25, 25))
        self.close_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_17.setStyleSheet(u"border: none;")
        self.close_17.setIcon(icon2)
        self.close_17.setIconSize(QSize(14, 14))

        self.horizontalLayout_40.addWidget(self.close_17)


        self.verticalLayout_28.addWidget(self.ajouter_et_close_21)

        self.frame_21 = QFrame(self.page_container_17)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFont(font)
        self.frame_21.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit, QTextEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.frame_21.setLineWidth(1)
        self.gridLayout_22 = QGridLayout(self.frame_21)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setVerticalSpacing(10)
        self.gridLayout_22.setContentsMargins(15, 15, 30, -1)
        self.enregistrer_marchandice = QPushButton(self.frame_21)
        self.enregistrer_marchandice.setObjectName(u"enregistrer_marchandice")
        self.enregistrer_marchandice.setMinimumSize(QSize(125, 35))
        self.enregistrer_marchandice.setMaximumSize(QSize(125, 35))
        self.enregistrer_marchandice.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_marchandice.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_22.addWidget(self.enregistrer_marchandice, 14, 4, 1, 1, Qt.AlignRight)

        self.numdossier = QLineEdit(self.frame_21)
        self.numdossier.setObjectName(u"numdossier")
        self.numdossier.setMinimumSize(QSize(0, 30))
        self.numdossier.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_22.addWidget(self.numdossier, 0, 2, 1, 3)

        self.label_94 = QLabel(self.frame_21)
        self.label_94.setObjectName(u"label_94")

        self.gridLayout_22.addWidget(self.label_94, 5, 1, 1, 1)

        self.label_95 = QLabel(self.frame_21)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_22.addWidget(self.label_95, 4, 3, 1, 1)

        self.description = QTextEdit(self.frame_21)
        self.description.setObjectName(u"description")
        self.description.setMinimumSize(QSize(0, 70))
        self.description.setMaximumSize(QSize(16777215, 70))
        self.description.setStyleSheet(u"margin: 0px 2px 0px 2px;")
        self.description.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_22.addWidget(self.description, 6, 1, 1, 4)

        self.label_96 = QLabel(self.frame_21)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_22.addWidget(self.label_96, 4, 1, 1, 1)

        self.emballage = QLineEdit(self.frame_21)
        self.emballage.setObjectName(u"emballage")
        self.emballage.setMinimumSize(QSize(0, 30))
        self.emballage.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_22.addWidget(self.emballage, 4, 4, 1, 1)

        self.verticalSpacer_39 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_39, 15, 0, 1, 1)

        self.label_97 = QLabel(self.frame_21)
        self.label_97.setObjectName(u"label_97")

        self.gridLayout_22.addWidget(self.label_97, 3, 1, 1, 1)

        self.poids = QLineEdit(self.frame_21)
        self.poids.setObjectName(u"poids")
        self.poids.setMinimumSize(QSize(0, 30))
        self.poids.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_22.addWidget(self.poids, 3, 4, 1, 1)

        self.label_98 = QLabel(self.frame_21)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_22.addWidget(self.label_98, 3, 3, 1, 1)

        self.numfacture = QLineEdit(self.frame_21)
        self.numfacture.setObjectName(u"numfacture")
        self.numfacture.setMinimumSize(QSize(0, 30))
        self.numfacture.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_22.addWidget(self.numfacture, 2, 2, 1, 3)

        self.montant = QLineEdit(self.frame_21)
        self.montant.setObjectName(u"montant")
        self.montant.setMinimumSize(QSize(0, 30))
        self.montant.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_22.addWidget(self.montant, 4, 2, 1, 1)

        self.label_99 = QLabel(self.frame_21)
        self.label_99.setObjectName(u"label_99")

        self.gridLayout_22.addWidget(self.label_99, 2, 1, 1, 1)

        self.label_100 = QLabel(self.frame_21)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setStyleSheet(u"")

        self.gridLayout_22.addWidget(self.label_100, 0, 1, 1, 1)

        self.nature = QLineEdit(self.frame_21)
        self.nature.setObjectName(u"nature")
        self.nature.setMinimumSize(QSize(0, 30))
        self.nature.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_22.addWidget(self.nature, 3, 2, 1, 1)


        self.verticalLayout_28.addWidget(self.frame_21)

        self.verticalSpacer_3 = QSpacerItem(20, 500, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_3)


        self.horizontalLayout_41.addWidget(self.page_container_17)

        self.stackedWidget.addWidget(self.formMarchandice)
        self.formMonnaie = QWidget()
        self.formMonnaie.setObjectName(u"formMonnaie")
        self.horizontalLayout_43 = QHBoxLayout(self.formMonnaie)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.page_container_18 = QFrame(self.formMonnaie)
        self.page_container_18.setObjectName(u"page_container_18")
        self.page_container_18.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_18.setFrameShape(QFrame.NoFrame)
        self.page_container_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.page_container_18)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_22 = QFrame(self.page_container_18)
        self.ajouter_et_close_22.setObjectName(u"ajouter_et_close_22")
        self.ajouter_et_close_22.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_22.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_22.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_22.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.ajouter_et_close_22)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.ajouter_22 = QLabel(self.ajouter_et_close_22)
        self.ajouter_22.setObjectName(u"ajouter_22")
        self.ajouter_22.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_42.addWidget(self.ajouter_22)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_25)

        self.close_18 = QPushButton(self.ajouter_et_close_22)
        self.close_18.setObjectName(u"close_18")
        self.close_18.setMinimumSize(QSize(25, 25))
        self.close_18.setMaximumSize(QSize(25, 25))
        self.close_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_18.setStyleSheet(u"border: none;")
        self.close_18.setIcon(icon2)
        self.close_18.setIconSize(QSize(14, 14))

        self.horizontalLayout_42.addWidget(self.close_18)


        self.verticalLayout_29.addWidget(self.ajouter_et_close_22)

        self.frame_22 = QFrame(self.page_container_18)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 100))
        self.frame_22.setMaximumSize(QSize(16777215, 150))
        self.frame_22.setFont(font)
        self.frame_22.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit, QTextEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_22.setLineWidth(1)
        self.gridLayout_23 = QGridLayout(self.frame_22)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setVerticalSpacing(10)
        self.gridLayout_23.setContentsMargins(15, 15, 30, -1)
        self.label_101 = QLabel(self.frame_22)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_23.addWidget(self.label_101, 1, 0, 1, 1)

        self.code = QLineEdit(self.frame_22)
        self.code.setObjectName(u"code")
        self.code.setMinimumSize(QSize(0, 30))
        self.code.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_23.addWidget(self.code, 0, 2, 1, 1)

        self.verticalSpacer_40 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_40, 9, 0, 1, 1)

        self.enregistrer_monnaie = QPushButton(self.frame_22)
        self.enregistrer_monnaie.setObjectName(u"enregistrer_monnaie")
        self.enregistrer_monnaie.setMinimumSize(QSize(125, 35))
        self.enregistrer_monnaie.setMaximumSize(QSize(125, 35))
        self.enregistrer_monnaie.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_monnaie.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_23.addWidget(self.enregistrer_monnaie, 8, 2, 1, 1, Qt.AlignRight)

        self.nom_pays_2 = QLineEdit(self.frame_22)
        self.nom_pays_2.setObjectName(u"nom_pays_2")
        self.nom_pays_2.setMinimumSize(QSize(0, 30))
        self.nom_pays_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_23.addWidget(self.nom_pays_2, 1, 2, 1, 1)

        self.label_102 = QLabel(self.frame_22)
        self.label_102.setObjectName(u"label_102")

        self.gridLayout_23.addWidget(self.label_102, 0, 0, 1, 1)


        self.verticalLayout_29.addWidget(self.frame_22)

        self.verticalSpacer_41 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_41)


        self.horizontalLayout_43.addWidget(self.page_container_18)

        self.stackedWidget.addWidget(self.formMonnaie)
        self.formNaturemarchandice = QWidget()
        self.formNaturemarchandice.setObjectName(u"formNaturemarchandice")
        self.horizontalLayout_45 = QHBoxLayout(self.formNaturemarchandice)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.page_container_19 = QFrame(self.formNaturemarchandice)
        self.page_container_19.setObjectName(u"page_container_19")
        self.page_container_19.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_19.setFrameShape(QFrame.NoFrame)
        self.page_container_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.page_container_19)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_23 = QFrame(self.page_container_19)
        self.ajouter_et_close_23.setObjectName(u"ajouter_et_close_23")
        self.ajouter_et_close_23.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_23.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_23.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_23.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.ajouter_et_close_23)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.ajouter_23 = QLabel(self.ajouter_et_close_23)
        self.ajouter_23.setObjectName(u"ajouter_23")
        self.ajouter_23.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_44.addWidget(self.ajouter_23)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_26)

        self.close_19 = QPushButton(self.ajouter_et_close_23)
        self.close_19.setObjectName(u"close_19")
        self.close_19.setMinimumSize(QSize(25, 25))
        self.close_19.setMaximumSize(QSize(25, 25))
        self.close_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_19.setStyleSheet(u"border: none;")
        self.close_19.setIcon(icon2)
        self.close_19.setIconSize(QSize(14, 14))

        self.horizontalLayout_44.addWidget(self.close_19)


        self.verticalLayout_30.addWidget(self.ajouter_et_close_23)

        self.frame_23 = QFrame(self.page_container_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 100))
        self.frame_23.setMaximumSize(QSize(16777215, 100))
        self.frame_23.setFont(font)
        self.frame_23.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit, QTextEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.frame_23.setLineWidth(1)
        self.gridLayout_24 = QGridLayout(self.frame_23)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setVerticalSpacing(10)
        self.gridLayout_24.setContentsMargins(15, 15, 30, -1)
        self.verticalSpacer_42 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_42, 8, 0, 1, 1)

        self.enregistrer_nature_marchandice = QPushButton(self.frame_23)
        self.enregistrer_nature_marchandice.setObjectName(u"enregistrer_nature_marchandice")
        self.enregistrer_nature_marchandice.setMinimumSize(QSize(125, 35))
        self.enregistrer_nature_marchandice.setMaximumSize(QSize(125, 35))
        self.enregistrer_nature_marchandice.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_nature_marchandice.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_24.addWidget(self.enregistrer_nature_marchandice, 7, 2, 1, 1, Qt.AlignRight)

        self.nature_2 = QLineEdit(self.frame_23)
        self.nature_2.setObjectName(u"nature_2")
        self.nature_2.setMinimumSize(QSize(0, 30))
        self.nature_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_24.addWidget(self.nature_2, 0, 2, 1, 1)

        self.label_103 = QLabel(self.frame_23)
        self.label_103.setObjectName(u"label_103")

        self.gridLayout_24.addWidget(self.label_103, 0, 0, 1, 1)


        self.verticalLayout_30.addWidget(self.frame_23)

        self.verticalSpacer_43 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_43)


        self.horizontalLayout_45.addWidget(self.page_container_19)

        self.stackedWidget.addWidget(self.formNaturemarchandice)
        self.formPays = QWidget()
        self.formPays.setObjectName(u"formPays")
        self.horizontalLayout_47 = QHBoxLayout(self.formPays)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.page_container_20 = QFrame(self.formPays)
        self.page_container_20.setObjectName(u"page_container_20")
        self.page_container_20.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_20.setFrameShape(QFrame.NoFrame)
        self.page_container_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.page_container_20)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_24 = QFrame(self.page_container_20)
        self.ajouter_et_close_24.setObjectName(u"ajouter_et_close_24")
        self.ajouter_et_close_24.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_24.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_24.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_24.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.ajouter_et_close_24)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.ajouter_24 = QLabel(self.ajouter_et_close_24)
        self.ajouter_24.setObjectName(u"ajouter_24")
        self.ajouter_24.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_46.addWidget(self.ajouter_24)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_27)

        self.close_20 = QPushButton(self.ajouter_et_close_24)
        self.close_20.setObjectName(u"close_20")
        self.close_20.setMinimumSize(QSize(25, 25))
        self.close_20.setMaximumSize(QSize(25, 25))
        self.close_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_20.setStyleSheet(u"border: none;")
        self.close_20.setIcon(icon2)
        self.close_20.setIconSize(QSize(14, 14))

        self.horizontalLayout_46.addWidget(self.close_20)


        self.verticalLayout_31.addWidget(self.ajouter_et_close_24)

        self.frame_24 = QFrame(self.page_container_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 100))
        self.frame_24.setMaximumSize(QSize(16777215, 150))
        self.frame_24.setFont(font)
        self.frame_24.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit, QTextEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.frame_24.setLineWidth(1)
        self.gridLayout_25 = QGridLayout(self.frame_24)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setVerticalSpacing(10)
        self.gridLayout_25.setContentsMargins(15, 15, 30, -1)
        self.label_104 = QLabel(self.frame_24)
        self.label_104.setObjectName(u"label_104")

        self.gridLayout_25.addWidget(self.label_104, 1, 0, 1, 1)

        self.enregistrer_pays = QPushButton(self.frame_24)
        self.enregistrer_pays.setObjectName(u"enregistrer_pays")
        self.enregistrer_pays.setMinimumSize(QSize(125, 35))
        self.enregistrer_pays.setMaximumSize(QSize(125, 35))
        self.enregistrer_pays.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_pays.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_25.addWidget(self.enregistrer_pays, 8, 2, 1, 1, Qt.AlignRight)

        self.verticalSpacer_44 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_25.addItem(self.verticalSpacer_44, 9, 0, 1, 1)

        self.code_2 = QLineEdit(self.frame_24)
        self.code_2.setObjectName(u"code_2")
        self.code_2.setMinimumSize(QSize(0, 30))
        self.code_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_25.addWidget(self.code_2, 1, 2, 1, 1)

        self.label_105 = QLabel(self.frame_24)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout_25.addWidget(self.label_105, 0, 0, 1, 1)

        self.nom_9 = QLineEdit(self.frame_24)
        self.nom_9.setObjectName(u"nom_9")
        self.nom_9.setMinimumSize(QSize(0, 30))
        self.nom_9.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_25.addWidget(self.nom_9, 0, 2, 1, 1)


        self.verticalLayout_31.addWidget(self.frame_24)

        self.verticalSpacer_45 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_45)


        self.horizontalLayout_47.addWidget(self.page_container_20)

        self.stackedWidget.addWidget(self.formPays)
        self.formRepresentant = QWidget()
        self.formRepresentant.setObjectName(u"formRepresentant")
        self.horizontalLayout_49 = QHBoxLayout(self.formRepresentant)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.page_container_21 = QFrame(self.formRepresentant)
        self.page_container_21.setObjectName(u"page_container_21")
        self.page_container_21.setMinimumSize(QSize(0, 0))
        self.page_container_21.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_21.setFrameShape(QFrame.NoFrame)
        self.page_container_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.page_container_21)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_25 = QFrame(self.page_container_21)
        self.ajouter_et_close_25.setObjectName(u"ajouter_et_close_25")
        self.ajouter_et_close_25.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_25.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_25.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_25.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.ajouter_et_close_25)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.ajouter_25 = QLabel(self.ajouter_et_close_25)
        self.ajouter_25.setObjectName(u"ajouter_25")
        self.ajouter_25.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_48.addWidget(self.ajouter_25)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_28)

        self.pushButton_10 = QPushButton(self.ajouter_et_close_25)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(25, 25))
        self.pushButton_10.setMaximumSize(QSize(25, 25))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"border: none;")
        self.pushButton_10.setIcon(icon2)
        self.pushButton_10.setIconSize(QSize(14, 14))

        self.horizontalLayout_48.addWidget(self.pushButton_10)


        self.verticalLayout_32.addWidget(self.ajouter_et_close_25)

        self.frame_25 = QFrame(self.page_container_21)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(16777215, 260))
        self.frame_25.setFont(font)
        self.frame_25.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.frame_25.setLineWidth(1)
        self.gridLayout_26 = QGridLayout(self.frame_25)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setVerticalSpacing(10)
        self.gridLayout_26.setContentsMargins(15, 15, 30, -1)
        self.verticalSpacer_46 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_46, 9, 0, 1, 1)

        self.label_106 = QLabel(self.frame_25)
        self.label_106.setObjectName(u"label_106")

        self.gridLayout_26.addWidget(self.label_106, 2, 0, 1, 1)

        self.label_107 = QLabel(self.frame_25)
        self.label_107.setObjectName(u"label_107")

        self.gridLayout_26.addWidget(self.label_107, 1, 0, 1, 1)

        self.tel_3 = QLineEdit(self.frame_25)
        self.tel_3.setObjectName(u"tel_3")
        self.tel_3.setMinimumSize(QSize(0, 30))
        self.tel_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_26.addWidget(self.tel_3, 2, 1, 1, 1)

        self.prenom_6 = QLineEdit(self.frame_25)
        self.prenom_6.setObjectName(u"prenom_6")
        self.prenom_6.setMinimumSize(QSize(0, 30))
        self.prenom_6.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_26.addWidget(self.prenom_6, 1, 1, 1, 1)

        self.nom_10 = QLineEdit(self.frame_25)
        self.nom_10.setObjectName(u"nom_10")
        self.nom_10.setMinimumSize(QSize(0, 30))
        self.nom_10.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_26.addWidget(self.nom_10, 0, 1, 1, 1)

        self.enregistrer_representant = QPushButton(self.frame_25)
        self.enregistrer_representant.setObjectName(u"enregistrer_representant")
        self.enregistrer_representant.setMinimumSize(QSize(125, 35))
        self.enregistrer_representant.setMaximumSize(QSize(125, 35))
        self.enregistrer_representant.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_representant.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_26.addWidget(self.enregistrer_representant, 8, 1, 1, 1, Qt.AlignRight)

        self.label_108 = QLabel(self.frame_25)
        self.label_108.setObjectName(u"label_108")

        self.gridLayout_26.addWidget(self.label_108, 3, 0, 1, 1)

        self.label_109 = QLabel(self.frame_25)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_26.addWidget(self.label_109, 0, 0, 1, 1)

        self.label_110 = QLabel(self.frame_25)
        self.label_110.setObjectName(u"label_110")

        self.gridLayout_26.addWidget(self.label_110, 4, 0, 1, 1)

        self.nom_client_3 = QLineEdit(self.frame_25)
        self.nom_client_3.setObjectName(u"nom_client_3")
        self.nom_client_3.setMinimumSize(QSize(0, 30))
        self.nom_client_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_26.addWidget(self.nom_client_3, 4, 1, 1, 1)

        self.date_nec = QDateEdit(self.frame_25)
        self.date_nec.setObjectName(u"date_nec")
        self.date_nec.setMinimumSize(QSize(0, 30))
        self.date_nec.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_26.addWidget(self.date_nec, 3, 1, 1, 1)


        self.verticalLayout_32.addWidget(self.frame_25)

        self.verticalSpacer_47 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_47)


        self.horizontalLayout_49.addWidget(self.page_container_21)

        self.stackedWidget.addWidget(self.formRepresentant)
        self.formUser = QWidget()
        self.formUser.setObjectName(u"formUser")
        self.horizontalLayout_51 = QHBoxLayout(self.formUser)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.page_container_22 = QFrame(self.formUser)
        self.page_container_22.setObjectName(u"page_container_22")
        self.page_container_22.setMinimumSize(QSize(0, 0))
        self.page_container_22.setStyleSheet(u"background-color: #eeeeee;\n"
"\n"
"")
        self.page_container_22.setFrameShape(QFrame.NoFrame)
        self.page_container_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.page_container_22)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(10, 10, -1, -1)
        self.ajouter_et_close_26 = QFrame(self.page_container_22)
        self.ajouter_et_close_26.setObjectName(u"ajouter_et_close_26")
        self.ajouter_et_close_26.setMinimumSize(QSize(0, 75))
        self.ajouter_et_close_26.setMaximumSize(QSize(16777215, 75))
        self.ajouter_et_close_26.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid #eeeeee;")
        self.ajouter_et_close_26.setFrameShape(QFrame.NoFrame)
        self.ajouter_et_close_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.ajouter_et_close_26)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.ajouter_26 = QLabel(self.ajouter_et_close_26)
        self.ajouter_26.setObjectName(u"ajouter_26")
        self.ajouter_26.setStyleSheet(u"padding-left:5px;\n"
"font-weight: light;\n"
"border-bottom: 1px solid white;")

        self.horizontalLayout_50.addWidget(self.ajouter_26)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_29)

        self.close_21 = QPushButton(self.ajouter_et_close_26)
        self.close_21.setObjectName(u"close_21")
        self.close_21.setMinimumSize(QSize(25, 25))
        self.close_21.setMaximumSize(QSize(25, 25))
        self.close_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_21.setStyleSheet(u"border: none;")
        self.close_21.setIcon(icon2)
        self.close_21.setIconSize(QSize(14, 14))

        self.horizontalLayout_50.addWidget(self.close_21)


        self.verticalLayout_33.addWidget(self.ajouter_et_close_26)

        self.frame_26 = QFrame(self.page_container_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 260))
        self.frame_26.setFont(font)
        self.frame_26.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 25 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit {\n"
"	border: 1.3px solid rgb(238, 238, 238);\n"
"	background-color: white;\n"
"	font-size: 13pt;\n"
"	color: #111217;\n"
"}\n"
"\n"
"")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.frame_26.setLineWidth(1)
        self.gridLayout_27 = QGridLayout(self.frame_26)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setVerticalSpacing(10)
        self.gridLayout_27.setContentsMargins(15, 15, 30, -1)
        self.verticalSpacer_48 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_27.addItem(self.verticalSpacer_48, 9, 0, 1, 1)

        self.label_111 = QLabel(self.frame_26)
        self.label_111.setObjectName(u"label_111")

        self.gridLayout_27.addWidget(self.label_111, 2, 0, 1, 1)

        self.label_112 = QLabel(self.frame_26)
        self.label_112.setObjectName(u"label_112")

        self.gridLayout_27.addWidget(self.label_112, 1, 0, 1, 1)

        self.tel_4 = QLineEdit(self.frame_26)
        self.tel_4.setObjectName(u"tel_4")
        self.tel_4.setMinimumSize(QSize(0, 30))
        self.tel_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_27.addWidget(self.tel_4, 2, 1, 1, 1)

        self.prenom_7 = QLineEdit(self.frame_26)
        self.prenom_7.setObjectName(u"prenom_7")
        self.prenom_7.setMinimumSize(QSize(0, 30))
        self.prenom_7.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_27.addWidget(self.prenom_7, 1, 1, 1, 1)

        self.nom_11 = QLineEdit(self.frame_26)
        self.nom_11.setObjectName(u"nom_11")
        self.nom_11.setMinimumSize(QSize(0, 30))
        self.nom_11.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_27.addWidget(self.nom_11, 0, 1, 1, 1)

        self.enregistrer_user = QPushButton(self.frame_26)
        self.enregistrer_user.setObjectName(u"enregistrer_user")
        self.enregistrer_user.setMinimumSize(QSize(125, 35))
        self.enregistrer_user.setMaximumSize(QSize(125, 35))
        self.enregistrer_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.enregistrer_user.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 2px 0px 2px 0px;\n"
"margin-top: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")

        self.gridLayout_27.addWidget(self.enregistrer_user, 8, 1, 1, 1, Qt.AlignRight)

        self.label_113 = QLabel(self.frame_26)
        self.label_113.setObjectName(u"label_113")

        self.gridLayout_27.addWidget(self.label_113, 3, 0, 1, 1)

        self.label_114 = QLabel(self.frame_26)
        self.label_114.setObjectName(u"label_114")

        self.gridLayout_27.addWidget(self.label_114, 0, 0, 1, 1)

        self.label_115 = QLabel(self.frame_26)
        self.label_115.setObjectName(u"label_115")

        self.gridLayout_27.addWidget(self.label_115, 4, 0, 1, 1)

        self.passw = QLineEdit(self.frame_26)
        self.passw.setObjectName(u"passw")
        self.passw.setMinimumSize(QSize(0, 30))
        self.passw.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_27.addWidget(self.passw, 4, 1, 1, 1)

        self.date_11 = QDateEdit(self.frame_26)
        self.date_11.setObjectName(u"date_11")
        self.date_11.setMinimumSize(QSize(0, 30))
        self.date_11.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_27.addWidget(self.date_11, 3, 1, 1, 1)


        self.verticalLayout_33.addWidget(self.frame_26)

        self.verticalSpacer_49 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_49)


        self.horizontalLayout_51.addWidget(self.page_container_22)

        self.stackedWidget.addWidget(self.formUser)
        self.affich_transport_livraison = QWidget()
        self.affich_transport_livraison.setObjectName(u"affich_transport_livraison")
        self.horizontalLayout_58 = QHBoxLayout(self.affich_transport_livraison)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.page = QWidget(self.affich_transport_livraison)
        self.page.setObjectName(u"page")
        self.page.setMinimumSize(QSize(0, 800))
        self.page.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.display_infos = QFrame(self.page)
        self.display_infos.setObjectName(u"display_infos")
        self.display_infos.setMinimumSize(QSize(0, 100))
        self.display_infos.setMaximumSize(QSize(16777215, 200))
        self.display_infos.setStyleSheet(u"background-color: white;")
        self.display_infos.setFrameShape(QFrame.NoFrame)
        self.display_infos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.display_infos)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_gestion_container = QFrame(self.display_infos)
        self.label_gestion_container.setObjectName(u"label_gestion_container")
        self.label_gestion_container.setMinimumSize(QSize(0, 50))
        self.label_gestion_container.setMaximumSize(QSize(16777215, 50))
        self.label_gestion_container.setFrameShape(QFrame.StyledPanel)
        self.label_gestion_container.setFrameShadow(QFrame.Raised)
        self.gestion = QLabel(self.label_gestion_container)
        self.gestion.setObjectName(u"gestion")
        self.gestion.setGeometry(QRect(30, 20, 511, 31))
        self.gestion.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_7.addWidget(self.label_gestion_container)

        self.options = QFrame(self.display_infos)
        self.options.setObjectName(u"options")
        self.options.setMinimumSize(QSize(0, 60))
        self.options.setMaximumSize(QSize(16777215, 60))
        self.options.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(238, 238, 238);\n"
"	padding: 3px 5px 3px 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QLineEdit {\n"
"	font-size: 16px;\n"
"}\n"
"")
        self.options.setFrameShape(QFrame.NoFrame)
        self.options.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.options)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(30, -1, 30, -1)
        self.rechercher_transport_livraison = QLineEdit(self.options)
        self.rechercher_transport_livraison.setObjectName(u"rechercher_transport_livraison")
        self.rechercher_transport_livraison.setStyleSheet(u"border: 1.5px solid rgb(238, 238, 238);\n"
"padding: 1px;")

        self.horizontalLayout_4.addWidget(self.rechercher_transport_livraison)

        self.ajouter_transport_livraison = QPushButton(self.options)
        self.ajouter_transport_livraison.setObjectName(u"ajouter_transport_livraison")
        self.ajouter_transport_livraison.setCursor(QCursor(Qt.PointingHandCursor))
        self.ajouter_transport_livraison.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")
        self.ajouter_transport_livraison.setIcon(icon3)
        self.ajouter_transport_livraison.setIconSize(QSize(12, 12))

        self.horizontalLayout_4.addWidget(self.ajouter_transport_livraison)

        self.modifier_transport_livraison = QPushButton(self.options)
        self.modifier_transport_livraison.setObjectName(u"modifier_transport_livraison")
        self.modifier_transport_livraison.setCursor(QCursor(Qt.PointingHandCursor))
        self.modifier_transport_livraison.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(51, 54, 69);\n"
"border: 1px solid rgb(51, 54, 69);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(70, 74, 95);\n"
"border: 1px solid rgb(70, 74, 95);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"assets/edit (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.modifier_transport_livraison.setIcon(icon5)
        self.modifier_transport_livraison.setIconSize(QSize(12, 12))

        self.horizontalLayout_4.addWidget(self.modifier_transport_livraison)

        self.supprimer_transpor_livraison = QPushButton(self.options)
        self.supprimer_transpor_livraison.setObjectName(u"supprimer_transpor_livraison")
        self.supprimer_transpor_livraison.setCursor(QCursor(Qt.PointingHandCursor))
        self.supprimer_transpor_livraison.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 0, 4);\n"
"border: 1px solid rgb(255, 0, 4);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 66, 66);\n"
"border: 1px solid rgb(255, 66, 66);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"assets/delete (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.supprimer_transpor_livraison.setIcon(icon6)
        self.supprimer_transpor_livraison.setIconSize(QSize(15, 15))

        self.horizontalLayout_4.addWidget(self.supprimer_transpor_livraison)


        self.verticalLayout_7.addWidget(self.options)


        self.verticalLayout_6.addWidget(self.display_infos)

        self.contain_affichage_grid_layout = QGridLayout()
        self.contain_affichage_grid_layout.setObjectName(u"contain_affichage_grid_layout")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(1500, 16777215))

        self.contain_affichage_grid_layout.addWidget(self.label_2, 3, 0, 1, 1)

        self.cute_separator = QFrame(self.page)
        self.cute_separator.setObjectName(u"cute_separator")
        self.cute_separator.setMinimumSize(QSize(0, 20))
        self.cute_separator.setMaximumSize(QSize(1210, 20))
        self.cute_separator.setStyleSheet(u"background-color: #eeeeee;")
        self.cute_separator.setFrameShape(QFrame.NoFrame)
        self.cute_separator.setFrameShadow(QFrame.Raised)

        self.contain_affichage_grid_layout.addWidget(self.cute_separator, 1, 0, 1, 1)

        self.stackedWidget_3 = QStackedWidget(self.page)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.afficheCAmion = QWidget()
        self.afficheCAmion.setObjectName(u"afficheCAmion")
        self.verticalLayout_36 = QVBoxLayout(self.afficheCAmion)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.tableCamion = QTableWidget(self.afficheCAmion)
        if (self.tableCamion.columnCount() < 1):
            self.tableCamion.setColumnCount(1)
        font2 = QFont()
        font2.setPointSize(10)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        __qtablewidgetitem5.setBackground(QColor(0, 0, 0));
        self.tableCamion.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        self.tableCamion.setObjectName(u"tableCamion")
        self.tableCamion.setEnabled(True)
        self.tableCamion.setLayoutDirection(Qt.LeftToRight)
        self.tableCamion.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 14px;\n"
"border:0.3px solid rgb(238,238,238);\n"
"")
        self.tableCamion.setFrameShape(QFrame.NoFrame)
        self.tableCamion.setFrameShadow(QFrame.Sunken)
        self.tableCamion.setLineWidth(1)
        self.tableCamion.setTextElideMode(Qt.ElideRight)
        self.tableCamion.setShowGrid(True)
        self.tableCamion.setGridStyle(Qt.CustomDashLine)
        self.tableCamion.setSortingEnabled(False)
        self.tableCamion.setWordWrap(True)
        self.tableCamion.setCornerButtonEnabled(True)
        self.tableCamion.horizontalHeader().setCascadingSectionResizes(False)
        self.tableCamion.horizontalHeader().setDefaultSectionSize(180)
        self.tableCamion.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableCamion.horizontalHeader().setStretchLastSection(True)
        self.tableCamion.verticalHeader().setCascadingSectionResizes(False)
        self.tableCamion.verticalHeader().setProperty("showSortIndicator", False)
        self.tableCamion.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_36.addWidget(self.tableCamion)

        self.stackedWidget_3.addWidget(self.afficheCAmion)
        self.affichIntermediaire = QWidget()
        self.affichIntermediaire.setObjectName(u"affichIntermediaire")
        self.horizontalLayout_59 = QHBoxLayout(self.affichIntermediaire)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.tableIntermediaire = QTableWidget(self.affichIntermediaire)
        if (self.tableIntermediaire.columnCount() < 2):
            self.tableIntermediaire.setColumnCount(2)
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.tableIntermediaire.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        self.tableIntermediaire.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        self.tableIntermediaire.setObjectName(u"tableIntermediaire")
        self.tableIntermediaire.setMaximumSize(QSize(1500, 16777215))
        self.tableIntermediaire.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 14px;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableIntermediaire.setFrameShape(QFrame.NoFrame)
        self.tableIntermediaire.setGridStyle(Qt.CustomDashLine)
        self.tableIntermediaire.setRowCount(0)
        self.tableIntermediaire.setColumnCount(2)
        self.tableIntermediaire.horizontalHeader().setMinimumSectionSize(90)
        self.tableIntermediaire.horizontalHeader().setDefaultSectionSize(180)
        self.tableIntermediaire.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableIntermediaire.horizontalHeader().setStretchLastSection(True)
        self.tableIntermediaire.verticalHeader().setCascadingSectionResizes(False)
        self.tableIntermediaire.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_59.addWidget(self.tableIntermediaire)

        self.stackedWidget_3.addWidget(self.affichIntermediaire)
        self.affichFournisseur = QWidget()
        self.affichFournisseur.setObjectName(u"affichFournisseur")
        self.horizontalLayout_60 = QHBoxLayout(self.affichFournisseur)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.tableFournisseur = QTableWidget(self.affichFournisseur)
        if (self.tableFournisseur.columnCount() < 2):
            self.tableFournisseur.setColumnCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        self.tableFournisseur.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        self.tableFournisseur.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        self.tableFournisseur.setObjectName(u"tableFournisseur")
        self.tableFournisseur.setMaximumSize(QSize(1500, 16777215))
        self.tableFournisseur.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 14px;\n"
"border:0.3px solid rgb(238,238,238);\n"
"")
        self.tableFournisseur.setRowCount(0)
        self.tableFournisseur.setColumnCount(2)
        self.tableFournisseur.horizontalHeader().setDefaultSectionSize(180)
        self.tableFournisseur.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_60.addWidget(self.tableFournisseur)

        self.stackedWidget_3.addWidget(self.affichFournisseur)
        self.afficheChauffeur = QWidget()
        self.afficheChauffeur.setObjectName(u"afficheChauffeur")
        self.horizontalLayout_79 = QHBoxLayout(self.afficheChauffeur)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.tableChauffeur_2 = QTableWidget(self.afficheChauffeur)
        if (self.tableChauffeur_2.columnCount() < 5):
            self.tableChauffeur_2.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font3);
        self.tableChauffeur_2.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font2);
        self.tableChauffeur_2.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font2);
        self.tableChauffeur_2.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font2);
        self.tableChauffeur_2.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font2);
        self.tableChauffeur_2.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.tableChauffeur_2.setObjectName(u"tableChauffeur_2")
        self.tableChauffeur_2.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 14px;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableChauffeur_2.setRowCount(0)
        self.tableChauffeur_2.setColumnCount(5)
        self.tableChauffeur_2.horizontalHeader().setDefaultSectionSize(170)

        self.horizontalLayout_79.addWidget(self.tableChauffeur_2)

        self.stackedWidget_3.addWidget(self.afficheChauffeur)

        self.contain_affichage_grid_layout.addWidget(self.stackedWidget_3, 2, 0, 1, 1)

        self.tables = QFrame(self.page)
        self.tables.setObjectName(u"tables")
        self.tables.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid white;\n"
"	padding-bottom: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 5px solid rgb(57, 195, 221);\n"
"}")
        self.tables.setFrameShape(QFrame.NoFrame)
        self.tables.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.tables)
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(30, -1, -1, 0)
        self.Camions_button = QPushButton(self.tables)
        self.Camions_button.setObjectName(u"Camions_button")
        self.Camions_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Camions_button.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.Camions_button)

        self.chauffeur_button = QPushButton(self.tables)
        self.chauffeur_button.setObjectName(u"chauffeur_button")
        self.chauffeur_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.chauffeur_button)

        self.four_button = QPushButton(self.tables)
        self.four_button.setObjectName(u"four_button")
        self.four_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.four_button.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.four_button)

        self.inter_button = QPushButton(self.tables)
        self.inter_button.setObjectName(u"inter_button")
        self.inter_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.inter_button.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.inter_button)


        self.contain_affichage_grid_layout.addWidget(self.tables, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.contain_affichage_grid_layout)


        self.horizontalLayout_58.addWidget(self.page)

        self.stackedWidget.addWidget(self.affich_transport_livraison)
        self.affich_gestion_documents = QWidget()
        self.affich_gestion_documents.setObjectName(u"affich_gestion_documents")
        self.verticalLayout_45 = QVBoxLayout(self.affich_gestion_documents)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.page_2 = QWidget(self.affich_gestion_documents)
        self.page_2.setObjectName(u"page_2")
        self.page_2.setMinimumSize(QSize(0, 800))
        self.page_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_34 = QVBoxLayout(self.page_2)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.display_infos_2 = QFrame(self.page_2)
        self.display_infos_2.setObjectName(u"display_infos_2")
        self.display_infos_2.setMinimumSize(QSize(0, 150))
        self.display_infos_2.setMaximumSize(QSize(1500, 150))
        self.display_infos_2.setStyleSheet(u"background-color: white;")
        self.display_infos_2.setFrameShape(QFrame.NoFrame)
        self.display_infos_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.display_infos_2)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_gestion_container_2 = QFrame(self.display_infos_2)
        self.label_gestion_container_2.setObjectName(u"label_gestion_container_2")
        self.label_gestion_container_2.setMinimumSize(QSize(0, 50))
        self.label_gestion_container_2.setMaximumSize(QSize(16777215, 50))
        self.label_gestion_container_2.setFrameShape(QFrame.StyledPanel)
        self.label_gestion_container_2.setFrameShadow(QFrame.Raised)
        self.gestion_2 = QLabel(self.label_gestion_container_2)
        self.gestion_2.setObjectName(u"gestion_2")
        self.gestion_2.setGeometry(QRect(30, 20, 391, 21))
        self.gestion_2.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_35.addWidget(self.label_gestion_container_2)

        self.options_2 = QFrame(self.display_infos_2)
        self.options_2.setObjectName(u"options_2")
        self.options_2.setMinimumSize(QSize(0, 60))
        self.options_2.setMaximumSize(QSize(16777215, 60))
        self.options_2.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(238, 238, 238);\n"
"	padding: 3px 5px 3px 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QLineEdit {\n"
"	font-size: 16px;\n"
"}\n"
"")
        self.options_2.setFrameShape(QFrame.NoFrame)
        self.options_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.options_2)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(30, -1, 30, -1)
        self.rechercher_gestion_document = QLineEdit(self.options_2)
        self.rechercher_gestion_document.setObjectName(u"rechercher_gestion_document")
        self.rechercher_gestion_document.setStyleSheet(u"border: 1.5px solid rgb(238, 238, 238);\n"
"padding: 1px;")

        self.horizontalLayout_52.addWidget(self.rechercher_gestion_document)

        self.comboBox = QComboBox(self.options_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"\n"
"QComboBox {\n"
"background-color: #19d76e;\n"
"border: 1px solid #19d76e;\n"
"color: white;\n"
"padding: 3px;\n"
"font-size:14px;\n"
"}\n"
"QComboBox:hover {\n"
"background-color:rgb(26, 236, 117);\n"
"border: 1px solidrgb(26, 236, 117);\n"
"}")

        self.horizontalLayout_52.addWidget(self.comboBox)

        self.ajouter_gestion_document = QPushButton(self.options_2)
        self.ajouter_gestion_document.setObjectName(u"ajouter_gestion_document")
        self.ajouter_gestion_document.setCursor(QCursor(Qt.PointingHandCursor))
        self.ajouter_gestion_document.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")
        self.ajouter_gestion_document.setIcon(icon3)
        self.ajouter_gestion_document.setIconSize(QSize(12, 12))

        self.horizontalLayout_52.addWidget(self.ajouter_gestion_document)

        self.modifier_gestion_document = QPushButton(self.options_2)
        self.modifier_gestion_document.setObjectName(u"modifier_gestion_document")
        self.modifier_gestion_document.setCursor(QCursor(Qt.PointingHandCursor))
        self.modifier_gestion_document.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(51, 54, 69);\n"
"border: 1px solid rgb(51, 54, 69);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(70, 74, 95);\n"
"border: 1px solid rgb(70, 74, 95);\n"
"}\n"
"")
        self.modifier_gestion_document.setIcon(icon5)
        self.modifier_gestion_document.setIconSize(QSize(12, 12))

        self.horizontalLayout_52.addWidget(self.modifier_gestion_document)

        self.pushButton_2 = QPushButton(self.options_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(191, 191, 191);\n"
"border: 1px solid rgb(191, 191, 191);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(209, 209, 209);\n"
"border: 1px solid rgb(209, 209, 209);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"assets/error.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon7)

        self.horizontalLayout_52.addWidget(self.pushButton_2)

        self.supprimer_gestion_document = QPushButton(self.options_2)
        self.supprimer_gestion_document.setObjectName(u"supprimer_gestion_document")
        self.supprimer_gestion_document.setCursor(QCursor(Qt.PointingHandCursor))
        self.supprimer_gestion_document.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 0, 4);\n"
"border: 1px solid rgb(255, 0, 4);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 66, 66);\n"
"border: 1px solid rgb(255, 66, 66);\n"
"}\n"
"")
        self.supprimer_gestion_document.setIcon(icon6)
        self.supprimer_gestion_document.setIconSize(QSize(15, 15))

        self.horizontalLayout_52.addWidget(self.supprimer_gestion_document)

        self.exporter_gestion_document = QPushButton(self.options_2)
        self.exporter_gestion_document.setObjectName(u"exporter_gestion_document")
        self.exporter_gestion_document.setCursor(QCursor(Qt.PointingHandCursor))
        self.exporter_gestion_document.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(25, 215, 110);\n"
"color: white;\n"
"border: 1px solid rgb(25, 215, 110);\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(26, 236, 117);\n"
"border: 1px solidrgb(26, 236, 117);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"assets/export.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exporter_gestion_document.setIcon(icon8)
        self.exporter_gestion_document.setIconSize(QSize(12, 12))

        self.horizontalLayout_52.addWidget(self.exporter_gestion_document)


        self.verticalLayout_35.addWidget(self.options_2)

        self.tables_5 = QFrame(self.display_infos_2)
        self.tables_5.setObjectName(u"tables_5")
        self.tables_5.setMinimumSize(QSize(0, 35))
        self.tables_5.setMaximumSize(QSize(16777215, 35))
        self.tables_5.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid white;\n"
"	padding-bottom: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 5px solid rgb(57, 195, 221);\n"
"}")
        self.tables_5.setFrameShape(QFrame.NoFrame)
        self.tables_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.tables_5)
        self.horizontalLayout_89.setSpacing(25)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(30, -1, -1, 0)
        self.dossiers_2 = QPushButton(self.tables_5)
        self.dossiers_2.setObjectName(u"dossiers_2")
        self.dossiers_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.dossiers_2.setStyleSheet(u"")

        self.horizontalLayout_89.addWidget(self.dossiers_2)

        self.fichiers_2 = QPushButton(self.tables_5)
        self.fichiers_2.setObjectName(u"fichiers_2")
        self.fichiers_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.fichiers_2.setStyleSheet(u"")

        self.horizontalLayout_89.addWidget(self.fichiers_2)

        self.bon_de_visite = QPushButton(self.tables_5)
        self.bon_de_visite.setObjectName(u"bon_de_visite")
        self.bon_de_visite.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_89.addWidget(self.bon_de_visite)

        self.bon_de_sortie = QPushButton(self.tables_5)
        self.bon_de_sortie.setObjectName(u"bon_de_sortie")
        self.bon_de_sortie.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_89.addWidget(self.bon_de_sortie)


        self.verticalLayout_35.addWidget(self.tables_5)


        self.verticalLayout_34.addWidget(self.display_infos_2)

        self.cute_separator_2 = QFrame(self.page_2)
        self.cute_separator_2.setObjectName(u"cute_separator_2")
        self.cute_separator_2.setMinimumSize(QSize(0, 20))
        self.cute_separator_2.setMaximumSize(QSize(16777215, 20))
        self.cute_separator_2.setStyleSheet(u"background-color: #eeeeee;")
        self.cute_separator_2.setFrameShape(QFrame.NoFrame)
        self.cute_separator_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_34.addWidget(self.cute_separator_2)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.stackedWidget_2 = QStackedWidget(self.page_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMaximumSize(QSize(2000, 16777215))
        self.affichDossier = QWidget()
        self.affichDossier.setObjectName(u"affichDossier")
        self.horizontalLayout_85 = QHBoxLayout(self.affichDossier)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.tableDossier = QTableWidget(self.affichDossier)
        if (self.tableDossier.columnCount() < 22):
            self.tableDossier.setColumnCount(22)
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font4);
        self.tableDossier.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font5);
        self.tableDossier.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font4);
        self.tableDossier.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableDossier.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(9, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(10, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(11, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(12, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font5);
        self.tableDossier.setHorizontalHeaderItem(13, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(14, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(15, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(16, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(17, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableDossier.setHorizontalHeaderItem(18, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(19, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(20, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font2);
        self.tableDossier.setHorizontalHeaderItem(21, __qtablewidgetitem36)
        self.tableDossier.setObjectName(u"tableDossier")
        self.tableDossier.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableDossier.setRowCount(0)
        self.tableDossier.setColumnCount(22)
        self.tableDossier.horizontalHeader().setDefaultSectionSize(170)

        self.horizontalLayout_85.addWidget(self.tableDossier)

        self.stackedWidget_2.addWidget(self.affichDossier)
        self.afficheFichier = QWidget()
        self.afficheFichier.setObjectName(u"afficheFichier")
        self.verticalLayout_4 = QVBoxLayout(self.afficheFichier)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableFichier = QTableWidget(self.afficheFichier)
        if (self.tableFichier.columnCount() < 2):
            self.tableFichier.setColumnCount(2)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font2);
        self.tableFichier.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font2);
        self.tableFichier.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        self.tableFichier.setObjectName(u"tableFichier")
        self.tableFichier.setMaximumSize(QSize(1500, 1500))
        self.tableFichier.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableFichier.setFrameShape(QFrame.NoFrame)
        self.tableFichier.setRowCount(0)
        self.tableFichier.horizontalHeader().setDefaultSectionSize(250)
        self.tableFichier.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.tableFichier)

        self.stackedWidget_2.addWidget(self.afficheFichier)
        self.AfficheBonSortie = QWidget()
        self.AfficheBonSortie.setObjectName(u"AfficheBonSortie")
        self.verticalLayout_51 = QVBoxLayout(self.AfficheBonSortie)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.tableBonSortie = QTableWidget(self.AfficheBonSortie)
        if (self.tableBonSortie.columnCount() < 6):
            self.tableBonSortie.setColumnCount(6)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font3);
        self.tableBonSortie.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font2);
        self.tableBonSortie.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font2);
        self.tableBonSortie.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font2);
        self.tableBonSortie.setHorizontalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font2);
        self.tableBonSortie.setHorizontalHeaderItem(4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setFont(font2);
        self.tableBonSortie.setHorizontalHeaderItem(5, __qtablewidgetitem44)
        self.tableBonSortie.setObjectName(u"tableBonSortie")
        self.tableBonSortie.setMaximumSize(QSize(1500, 16777215))
        self.tableBonSortie.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableBonSortie.setFrameShape(QFrame.NoFrame)
        self.tableBonSortie.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableBonSortie.setRowCount(0)
        self.tableBonSortie.setColumnCount(6)
        self.tableBonSortie.horizontalHeader().setDefaultSectionSize(170)

        self.verticalLayout_51.addWidget(self.tableBonSortie)

        self.stackedWidget_2.addWidget(self.AfficheBonSortie)
        self.AfficheBonvisite = QWidget()
        self.AfficheBonvisite.setObjectName(u"AfficheBonvisite")
        self.verticalLayout_52 = QVBoxLayout(self.AfficheBonvisite)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.tableBonVisite = QTableWidget(self.AfficheBonvisite)
        if (self.tableBonVisite.columnCount() < 6):
            self.tableBonVisite.setColumnCount(6)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font2);
        self.tableBonVisite.setHorizontalHeaderItem(0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFont(font2);
        self.tableBonVisite.setHorizontalHeaderItem(1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setFont(font2);
        self.tableBonVisite.setHorizontalHeaderItem(2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setFont(font2);
        self.tableBonVisite.setHorizontalHeaderItem(3, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setFont(font2);
        self.tableBonVisite.setHorizontalHeaderItem(4, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setFont(font2);
        self.tableBonVisite.setHorizontalHeaderItem(5, __qtablewidgetitem50)
        self.tableBonVisite.setObjectName(u"tableBonVisite")
        self.tableBonVisite.setEnabled(True)
        self.tableBonVisite.setMaximumSize(QSize(1500, 16777215))
        self.tableBonVisite.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableBonVisite.setFrameShape(QFrame.NoFrame)
        self.tableBonVisite.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableBonVisite.setRowCount(0)
        self.tableBonVisite.setColumnCount(6)
        self.tableBonVisite.horizontalHeader().setCascadingSectionResizes(False)
        self.tableBonVisite.horizontalHeader().setMinimumSectionSize(25)
        self.tableBonVisite.horizontalHeader().setDefaultSectionSize(170)
        self.tableBonVisite.verticalHeader().setMinimumSectionSize(25)
        self.tableBonVisite.verticalHeader().setDefaultSectionSize(25)
        self.tableBonVisite.verticalHeader().setProperty("showSortIndicator", False)
        self.tableBonVisite.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_52.addWidget(self.tableBonVisite)

        self.stackedWidget_2.addWidget(self.AfficheBonvisite)

        self.horizontalLayout_83.addWidget(self.stackedWidget_2)


        self.verticalLayout_34.addLayout(self.horizontalLayout_83)


        self.verticalLayout_45.addWidget(self.page_2)

        self.stackedWidget.addWidget(self.affich_gestion_documents)
        self.affich_personnel_interne = QWidget()
        self.affich_personnel_interne.setObjectName(u"affich_personnel_interne")
        self.horizontalLayout_63 = QHBoxLayout(self.affich_personnel_interne)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.page_10 = QWidget(self.affich_personnel_interne)
        self.page_10.setObjectName(u"page_10")
        self.page_10.setMinimumSize(QSize(0, 800))
        self.page_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_37 = QVBoxLayout(self.page_10)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.display_infos_3 = QFrame(self.page_10)
        self.display_infos_3.setObjectName(u"display_infos_3")
        self.display_infos_3.setMinimumSize(QSize(0, 150))
        self.display_infos_3.setMaximumSize(QSize(16777215, 150))
        self.display_infos_3.setStyleSheet(u"background-color: white;")
        self.display_infos_3.setFrameShape(QFrame.NoFrame)
        self.display_infos_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.display_infos_3)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_gestion_container_3 = QFrame(self.display_infos_3)
        self.label_gestion_container_3.setObjectName(u"label_gestion_container_3")
        self.label_gestion_container_3.setMinimumSize(QSize(0, 50))
        self.label_gestion_container_3.setMaximumSize(QSize(16777215, 50))
        self.label_gestion_container_3.setFrameShape(QFrame.StyledPanel)
        self.label_gestion_container_3.setFrameShadow(QFrame.Raised)
        self.gestionpersonnelintermediaire = QLabel(self.label_gestion_container_3)
        self.gestionpersonnelintermediaire.setObjectName(u"gestionpersonnelintermediaire")
        self.gestionpersonnelintermediaire.setGeometry(QRect(30, 10, 391, 31))
        self.gestionpersonnelintermediaire.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_38.addWidget(self.label_gestion_container_3)

        self.options_3 = QFrame(self.display_infos_3)
        self.options_3.setObjectName(u"options_3")
        self.options_3.setMinimumSize(QSize(0, 60))
        self.options_3.setMaximumSize(QSize(16777215, 60))
        self.options_3.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(238, 238, 238);\n"
"	padding: 3px 5px 3px 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QLineEdit {\n"
"	font-size: 16px;\n"
"}\n"
"")
        self.options_3.setFrameShape(QFrame.NoFrame)
        self.options_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.options_3)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(30, -1, 30, -1)
        self.rechercher_personnel_interne = QLineEdit(self.options_3)
        self.rechercher_personnel_interne.setObjectName(u"rechercher_personnel_interne")
        self.rechercher_personnel_interne.setStyleSheet(u"border: 1.5px solid rgb(238, 238, 238);\n"
"padding: 1px;")

        self.horizontalLayout_61.addWidget(self.rechercher_personnel_interne)

        self.ajouter_personnel_interne = QPushButton(self.options_3)
        self.ajouter_personnel_interne.setObjectName(u"ajouter_personnel_interne")
        self.ajouter_personnel_interne.setCursor(QCursor(Qt.PointingHandCursor))
        self.ajouter_personnel_interne.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")
        self.ajouter_personnel_interne.setIcon(icon3)
        self.ajouter_personnel_interne.setIconSize(QSize(12, 12))

        self.horizontalLayout_61.addWidget(self.ajouter_personnel_interne)

        self.modifier_personnel_interne = QPushButton(self.options_3)
        self.modifier_personnel_interne.setObjectName(u"modifier_personnel_interne")
        self.modifier_personnel_interne.setCursor(QCursor(Qt.PointingHandCursor))
        self.modifier_personnel_interne.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(51, 54, 69);\n"
"border: 1px solid rgb(51, 54, 69);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(70, 74, 95);\n"
"border: 1px solid rgb(70, 74, 95);\n"
"}\n"
"")
        self.modifier_personnel_interne.setIcon(icon5)
        self.modifier_personnel_interne.setIconSize(QSize(12, 12))

        self.horizontalLayout_61.addWidget(self.modifier_personnel_interne)

        self.supprimer_personnel_interne = QPushButton(self.options_3)
        self.supprimer_personnel_interne.setObjectName(u"supprimer_personnel_interne")
        self.supprimer_personnel_interne.setCursor(QCursor(Qt.PointingHandCursor))
        self.supprimer_personnel_interne.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 0, 4);\n"
"border: 1px solid rgb(255, 0, 4);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 66, 66);\n"
"border: 1px solid rgb(255, 66, 66);\n"
"}\n"
"")
        self.supprimer_personnel_interne.setIcon(icon6)
        self.supprimer_personnel_interne.setIconSize(QSize(15, 15))

        self.horizontalLayout_61.addWidget(self.supprimer_personnel_interne)


        self.verticalLayout_38.addWidget(self.options_3)

        self.tables_3 = QFrame(self.display_infos_3)
        self.tables_3.setObjectName(u"tables_3")
        self.tables_3.setMinimumSize(QSize(0, 35))
        self.tables_3.setMaximumSize(QSize(16777215, 35))
        self.tables_3.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid white;\n"
"	padding-bottom: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 5px solid rgb(57, 195, 221);\n"
"}")
        self.tables_3.setFrameShape(QFrame.NoFrame)
        self.tables_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.tables_3)
        self.horizontalLayout_62.setSpacing(25)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(30, -1, -1, 0)
        self.utilisateur_button_personnel_interne = QPushButton(self.tables_3)
        self.utilisateur_button_personnel_interne.setObjectName(u"utilisateur_button_personnel_interne")
        self.utilisateur_button_personnel_interne.setCursor(QCursor(Qt.PointingHandCursor))
        self.utilisateur_button_personnel_interne.setStyleSheet(u"")

        self.horizontalLayout_62.addWidget(self.utilisateur_button_personnel_interne)

        self.declarant_button_personnel_interne = QPushButton(self.tables_3)
        self.declarant_button_personnel_interne.setObjectName(u"declarant_button_personnel_interne")
        self.declarant_button_personnel_interne.setCursor(QCursor(Qt.PointingHandCursor))
        self.declarant_button_personnel_interne.setStyleSheet(u"")

        self.horizontalLayout_62.addWidget(self.declarant_button_personnel_interne)


        self.verticalLayout_38.addWidget(self.tables_3)


        self.verticalLayout_37.addWidget(self.display_infos_3)

        self.cute_separator_3 = QFrame(self.page_10)
        self.cute_separator_3.setObjectName(u"cute_separator_3")
        self.cute_separator_3.setMinimumSize(QSize(0, 20))
        self.cute_separator_3.setMaximumSize(QSize(16777215, 20))
        self.cute_separator_3.setStyleSheet(u"background-color: #eeeeee;")
        self.cute_separator_3.setFrameShape(QFrame.NoFrame)
        self.cute_separator_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_37.addWidget(self.cute_separator_3)

        self.contain_affichage_grid_layout_3 = QGridLayout()
        self.contain_affichage_grid_layout_3.setObjectName(u"contain_affichage_grid_layout_3")
        self.label_3 = QLabel(self.page_10)
        self.label_3.setObjectName(u"label_3")

        self.contain_affichage_grid_layout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.stackedWidget_4 = QStackedWidget(self.page_10)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.affichUtilisateur = QWidget()
        self.affichUtilisateur.setObjectName(u"affichUtilisateur")
        self.horizontalLayout_65 = QHBoxLayout(self.affichUtilisateur)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.tableUtilisateur = QTableWidget(self.affichUtilisateur)
        if (self.tableUtilisateur.columnCount() < 6):
            self.tableUtilisateur.setColumnCount(6)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font3);
        self.tableUtilisateur.setHorizontalHeaderItem(0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setFont(font2);
        self.tableUtilisateur.setHorizontalHeaderItem(1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setFont(font2);
        self.tableUtilisateur.setHorizontalHeaderItem(2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setFont(font2);
        self.tableUtilisateur.setHorizontalHeaderItem(3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setFont(font2);
        self.tableUtilisateur.setHorizontalHeaderItem(4, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setFont(font2);
        self.tableUtilisateur.setHorizontalHeaderItem(5, __qtablewidgetitem56)
        self.tableUtilisateur.setObjectName(u"tableUtilisateur")
        self.tableUtilisateur.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableUtilisateur.setRowCount(0)
        self.tableUtilisateur.setColumnCount(6)
        self.tableUtilisateur.horizontalHeader().setDefaultSectionSize(170)

        self.horizontalLayout_65.addWidget(self.tableUtilisateur)

        self.stackedWidget_4.addWidget(self.affichUtilisateur)
        self.afficheDeclarent = QWidget()
        self.afficheDeclarent.setObjectName(u"afficheDeclarent")
        self.verticalLayout_41 = QVBoxLayout(self.afficheDeclarent)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.tableDeclarent = QTableWidget(self.afficheDeclarent)
        if (self.tableDeclarent.columnCount() < 5):
            self.tableDeclarent.setColumnCount(5)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setFont(font3);
        self.tableDeclarent.setHorizontalHeaderItem(0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setFont(font2);
        self.tableDeclarent.setHorizontalHeaderItem(1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setFont(font2);
        self.tableDeclarent.setHorizontalHeaderItem(2, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setFont(font2);
        self.tableDeclarent.setHorizontalHeaderItem(3, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setFont(font2);
        self.tableDeclarent.setHorizontalHeaderItem(4, __qtablewidgetitem61)
        self.tableDeclarent.setObjectName(u"tableDeclarent")
        self.tableDeclarent.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableDeclarent.setRowCount(0)
        self.tableDeclarent.setColumnCount(5)
        self.tableDeclarent.horizontalHeader().setDefaultSectionSize(170)

        self.verticalLayout_41.addWidget(self.tableDeclarent)

        self.stackedWidget_4.addWidget(self.afficheDeclarent)

        self.contain_affichage_grid_layout_3.addWidget(self.stackedWidget_4, 1, 0, 1, 1)


        self.verticalLayout_37.addLayout(self.contain_affichage_grid_layout_3)


        self.horizontalLayout_63.addWidget(self.page_10)

        self.stackedWidget.addWidget(self.affich_personnel_interne)
        self.affiche_marchandices_amballage = QWidget()
        self.affiche_marchandices_amballage.setObjectName(u"affiche_marchandices_amballage")
        self.horizontalLayout_68 = QHBoxLayout(self.affiche_marchandices_amballage)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.page_8 = QWidget(self.affiche_marchandices_amballage)
        self.page_8.setObjectName(u"page_8")
        self.page_8.setMinimumSize(QSize(0, 800))
        self.page_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_42 = QVBoxLayout(self.page_8)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.display_infos_4 = QFrame(self.page_8)
        self.display_infos_4.setObjectName(u"display_infos_4")
        self.display_infos_4.setMinimumSize(QSize(0, 150))
        self.display_infos_4.setMaximumSize(QSize(16777215, 150))
        self.display_infos_4.setStyleSheet(u"background-color: white;")
        self.display_infos_4.setFrameShape(QFrame.NoFrame)
        self.display_infos_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.display_infos_4)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_gestion_container_4 = QFrame(self.display_infos_4)
        self.label_gestion_container_4.setObjectName(u"label_gestion_container_4")
        self.label_gestion_container_4.setMinimumSize(QSize(0, 50))
        self.label_gestion_container_4.setMaximumSize(QSize(16777215, 50))
        self.label_gestion_container_4.setFrameShape(QFrame.StyledPanel)
        self.label_gestion_container_4.setFrameShadow(QFrame.Raised)
        self.gestion_3 = QLabel(self.label_gestion_container_4)
        self.gestion_3.setObjectName(u"gestion_3")
        self.gestion_3.setGeometry(QRect(30, 0, 591, 51))
        self.gestion_3.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_43.addWidget(self.label_gestion_container_4)

        self.options_4 = QFrame(self.display_infos_4)
        self.options_4.setObjectName(u"options_4")
        self.options_4.setMinimumSize(QSize(0, 60))
        self.options_4.setMaximumSize(QSize(16777215, 60))
        self.options_4.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(238, 238, 238);\n"
"	padding: 3px 5px 3px 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QLineEdit {\n"
"	font-size: 16px;\n"
"}\n"
"")
        self.options_4.setFrameShape(QFrame.NoFrame)
        self.options_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.options_4)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(30, -1, 30, -1)
        self.rechercher_marchandise_embalage = QLineEdit(self.options_4)
        self.rechercher_marchandise_embalage.setObjectName(u"rechercher_marchandise_embalage")
        self.rechercher_marchandise_embalage.setStyleSheet(u"border: 1.5px solid rgb(238, 238, 238);\n"
"padding: 1px;")

        self.horizontalLayout_66.addWidget(self.rechercher_marchandise_embalage)

        self.ajouter_marchandise_embalage = QPushButton(self.options_4)
        self.ajouter_marchandise_embalage.setObjectName(u"ajouter_marchandise_embalage")
        self.ajouter_marchandise_embalage.setCursor(QCursor(Qt.PointingHandCursor))
        self.ajouter_marchandise_embalage.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")
        self.ajouter_marchandise_embalage.setIcon(icon3)
        self.ajouter_marchandise_embalage.setIconSize(QSize(12, 12))

        self.horizontalLayout_66.addWidget(self.ajouter_marchandise_embalage)

        self.modifier_marchandise_embalage = QPushButton(self.options_4)
        self.modifier_marchandise_embalage.setObjectName(u"modifier_marchandise_embalage")
        self.modifier_marchandise_embalage.setCursor(QCursor(Qt.PointingHandCursor))
        self.modifier_marchandise_embalage.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(51, 54, 69);\n"
"border: 1px solid rgb(51, 54, 69);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(70, 74, 95);\n"
"border: 1px solid rgb(70, 74, 95);\n"
"}\n"
"")
        self.modifier_marchandise_embalage.setIcon(icon5)
        self.modifier_marchandise_embalage.setIconSize(QSize(12, 12))

        self.horizontalLayout_66.addWidget(self.modifier_marchandise_embalage)

        self.supprimer_marchandise_embalage = QPushButton(self.options_4)
        self.supprimer_marchandise_embalage.setObjectName(u"supprimer_marchandise_embalage")
        self.supprimer_marchandise_embalage.setCursor(QCursor(Qt.PointingHandCursor))
        self.supprimer_marchandise_embalage.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 0, 4);\n"
"border: 1px solid rgb(255, 0, 4);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 66, 66);\n"
"border: 1px solid rgb(255, 66, 66);\n"
"}\n"
"")
        self.supprimer_marchandise_embalage.setIcon(icon6)
        self.supprimer_marchandise_embalage.setIconSize(QSize(15, 15))

        self.horizontalLayout_66.addWidget(self.supprimer_marchandise_embalage)


        self.verticalLayout_43.addWidget(self.options_4)

        self.tables_4 = QFrame(self.display_infos_4)
        self.tables_4.setObjectName(u"tables_4")
        self.tables_4.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid white;\n"
"	padding-bottom: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 5px solid rgb(57, 195, 221);\n"
"}")
        self.tables_4.setFrameShape(QFrame.NoFrame)
        self.tables_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.tables_4)
        self.horizontalLayout_67.setSpacing(25)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(30, -1, -1, 0)
        self.marchandise_button = QPushButton(self.tables_4)
        self.marchandise_button.setObjectName(u"marchandise_button")
        self.marchandise_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.marchandise_button.setStyleSheet(u"")

        self.horizontalLayout_67.addWidget(self.marchandise_button)

        self.nature_button = QPushButton(self.tables_4)
        self.nature_button.setObjectName(u"nature_button")
        self.nature_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.nature_button.setStyleSheet(u"")

        self.horizontalLayout_67.addWidget(self.nature_button)

        self.emballage_button = QPushButton(self.tables_4)
        self.emballage_button.setObjectName(u"emballage_button")
        self.emballage_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.emballage_button.setStyleSheet(u"")

        self.horizontalLayout_67.addWidget(self.emballage_button)

        self.designation_button = QPushButton(self.tables_4)
        self.designation_button.setObjectName(u"designation_button")
        self.designation_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_67.addWidget(self.designation_button)


        self.verticalLayout_43.addWidget(self.tables_4)


        self.verticalLayout_42.addWidget(self.display_infos_4)

        self.cute_separator_4 = QFrame(self.page_8)
        self.cute_separator_4.setObjectName(u"cute_separator_4")
        self.cute_separator_4.setMinimumSize(QSize(0, 20))
        self.cute_separator_4.setMaximumSize(QSize(16777215, 20))
        self.cute_separator_4.setStyleSheet(u"background-color: #eeeeee;")
        self.cute_separator_4.setFrameShape(QFrame.NoFrame)
        self.cute_separator_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_42.addWidget(self.cute_separator_4)

        self.contain_affichage_grid_layout_4 = QGridLayout()
        self.contain_affichage_grid_layout_4.setObjectName(u"contain_affichage_grid_layout_4")
        self.label_6 = QLabel(self.page_8)
        self.label_6.setObjectName(u"label_6")

        self.contain_affichage_grid_layout_4.addWidget(self.label_6, 1, 0, 1, 1)

        self.stackedWidget_5 = QStackedWidget(self.page_8)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.afficheEmballage = QWidget()
        self.afficheEmballage.setObjectName(u"afficheEmballage")
        self.horizontalLayout_69 = QHBoxLayout(self.afficheEmballage)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.tableEmbalage = QTableWidget(self.afficheEmballage)
        if (self.tableEmbalage.columnCount() < 5):
            self.tableEmbalage.setColumnCount(5)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setFont(font3);
        self.tableEmbalage.setHorizontalHeaderItem(0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font2);
        self.tableEmbalage.setHorizontalHeaderItem(1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setFont(font4);
        self.tableEmbalage.setHorizontalHeaderItem(2, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setFont(font2);
        self.tableEmbalage.setHorizontalHeaderItem(3, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setFont(font2);
        self.tableEmbalage.setHorizontalHeaderItem(4, __qtablewidgetitem66)
        self.tableEmbalage.setObjectName(u"tableEmbalage")
        self.tableEmbalage.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableEmbalage.setRowCount(0)
        self.tableEmbalage.setColumnCount(5)
        self.tableEmbalage.horizontalHeader().setDefaultSectionSize(170)

        self.horizontalLayout_69.addWidget(self.tableEmbalage)

        self.stackedWidget_5.addWidget(self.afficheEmballage)
        self.afficheMarchandise = QWidget()
        self.afficheMarchandise.setObjectName(u"afficheMarchandise")
        self.horizontalLayout_72 = QHBoxLayout(self.afficheMarchandise)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.tableMarchandice = QTableWidget(self.afficheMarchandise)
        if (self.tableMarchandice.columnCount() < 8):
            self.tableMarchandice.setColumnCount(8)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setFont(font3);
        self.tableMarchandice.setHorizontalHeaderItem(0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setFont(font2);
        self.tableMarchandice.setHorizontalHeaderItem(1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setFont(font2);
        self.tableMarchandice.setHorizontalHeaderItem(2, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setFont(font2);
        self.tableMarchandice.setHorizontalHeaderItem(3, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setFont(font2);
        self.tableMarchandice.setHorizontalHeaderItem(4, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setFont(font2);
        self.tableMarchandice.setHorizontalHeaderItem(5, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setFont(font2);
        self.tableMarchandice.setHorizontalHeaderItem(6, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setFont(font4);
        self.tableMarchandice.setHorizontalHeaderItem(7, __qtablewidgetitem74)
        self.tableMarchandice.setObjectName(u"tableMarchandice")
        self.tableMarchandice.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableMarchandice.setRowCount(0)
        self.tableMarchandice.setColumnCount(8)
        self.tableMarchandice.horizontalHeader().setDefaultSectionSize(170)

        self.horizontalLayout_72.addWidget(self.tableMarchandice)

        self.stackedWidget_5.addWidget(self.afficheMarchandise)
        self.afficheNature = QWidget()
        self.afficheNature.setObjectName(u"afficheNature")
        self.horizontalLayout_73 = QHBoxLayout(self.afficheNature)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.tableNatureMarch = QTableWidget(self.afficheNature)
        if (self.tableNatureMarch.columnCount() < 1):
            self.tableNatureMarch.setColumnCount(1)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setFont(font3);
        self.tableNatureMarch.setHorizontalHeaderItem(0, __qtablewidgetitem75)
        self.tableNatureMarch.setObjectName(u"tableNatureMarch")
        self.tableNatureMarch.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableNatureMarch.setFrameShape(QFrame.NoFrame)
        self.tableNatureMarch.setRowCount(0)
        self.tableNatureMarch.setColumnCount(1)
        self.tableNatureMarch.horizontalHeader().setDefaultSectionSize(170)
        self.tableNatureMarch.horizontalHeader().setStretchLastSection(True)
        self.tableNatureMarch.verticalHeader().setMinimumSectionSize(25)
        self.tableNatureMarch.verticalHeader().setDefaultSectionSize(25)
        self.tableNatureMarch.verticalHeader().setProperty("showSortIndicator", False)
        self.tableNatureMarch.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_73.addWidget(self.tableNatureMarch)

        self.stackedWidget_5.addWidget(self.afficheNature)
        self.afficheDesignation = QWidget()
        self.afficheDesignation.setObjectName(u"afficheDesignation")
        self.horizontalLayout_74 = QHBoxLayout(self.afficheDesignation)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.tableDesigniation = QTableWidget(self.afficheDesignation)
        if (self.tableDesigniation.columnCount() < 3):
            self.tableDesigniation.setColumnCount(3)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setFont(font3);
        self.tableDesigniation.setHorizontalHeaderItem(0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setFont(font2);
        self.tableDesigniation.setHorizontalHeaderItem(1, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setFont(font4);
        self.tableDesigniation.setHorizontalHeaderItem(2, __qtablewidgetitem78)
        self.tableDesigniation.setObjectName(u"tableDesigniation")
        self.tableDesigniation.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableDesigniation.setRowCount(0)
        self.tableDesigniation.setColumnCount(3)
        self.tableDesigniation.horizontalHeader().setDefaultSectionSize(170)
        self.tableDesigniation.horizontalHeader().setStretchLastSection(True)
        self.tableDesigniation.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_74.addWidget(self.tableDesigniation)

        self.stackedWidget_5.addWidget(self.afficheDesignation)

        self.contain_affichage_grid_layout_4.addWidget(self.stackedWidget_5, 0, 0, 1, 1)


        self.verticalLayout_42.addLayout(self.contain_affichage_grid_layout_4)


        self.horizontalLayout_68.addWidget(self.page_8)

        self.stackedWidget.addWidget(self.affiche_marchandices_amballage)
        self.affiche_pays_monnaie = QWidget()
        self.affiche_pays_monnaie.setObjectName(u"affiche_pays_monnaie")
        self.horizontalLayout_77 = QHBoxLayout(self.affiche_pays_monnaie)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.page_14 = QWidget(self.affiche_pays_monnaie)
        self.page_14.setObjectName(u"page_14")
        self.page_14.setMinimumSize(QSize(0, 800))
        self.page_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_46 = QVBoxLayout(self.page_14)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.display_infos_6 = QFrame(self.page_14)
        self.display_infos_6.setObjectName(u"display_infos_6")
        self.display_infos_6.setMinimumSize(QSize(0, 150))
        self.display_infos_6.setMaximumSize(QSize(16777215, 150))
        self.display_infos_6.setStyleSheet(u"background-color: white;")
        self.display_infos_6.setFrameShape(QFrame.NoFrame)
        self.display_infos_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.display_infos_6)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_gestion_container_6 = QFrame(self.display_infos_6)
        self.label_gestion_container_6.setObjectName(u"label_gestion_container_6")
        self.label_gestion_container_6.setMinimumSize(QSize(0, 50))
        self.label_gestion_container_6.setMaximumSize(QSize(16777215, 50))
        self.label_gestion_container_6.setFrameShape(QFrame.StyledPanel)
        self.label_gestion_container_6.setFrameShadow(QFrame.Raised)
        self.gestion_5 = QLabel(self.label_gestion_container_6)
        self.gestion_5.setObjectName(u"gestion_5")
        self.gestion_5.setGeometry(QRect(30, 10, 571, 41))
        self.gestion_5.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_47.addWidget(self.label_gestion_container_6)

        self.options_6 = QFrame(self.display_infos_6)
        self.options_6.setObjectName(u"options_6")
        self.options_6.setMinimumSize(QSize(0, 60))
        self.options_6.setMaximumSize(QSize(16777215, 60))
        self.options_6.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(238, 238, 238);\n"
"	padding: 3px 5px 3px 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QLineEdit {\n"
"	font-size: 16px;\n"
"}\n"
"")
        self.options_6.setFrameShape(QFrame.NoFrame)
        self.options_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.options_6)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(30, -1, 30, -1)
        self.rechercher_pays_monnaie = QLineEdit(self.options_6)
        self.rechercher_pays_monnaie.setObjectName(u"rechercher_pays_monnaie")
        self.rechercher_pays_monnaie.setStyleSheet(u"border: 1.5px solid rgb(238, 238, 238);\n"
"padding: 1px;")

        self.horizontalLayout_75.addWidget(self.rechercher_pays_monnaie)

        self.ajouter_pays_monnaie = QPushButton(self.options_6)
        self.ajouter_pays_monnaie.setObjectName(u"ajouter_pays_monnaie")
        self.ajouter_pays_monnaie.setCursor(QCursor(Qt.PointingHandCursor))
        self.ajouter_pays_monnaie.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")
        self.ajouter_pays_monnaie.setIcon(icon3)
        self.ajouter_pays_monnaie.setIconSize(QSize(12, 12))

        self.horizontalLayout_75.addWidget(self.ajouter_pays_monnaie)

        self.modifier_pays_monnaie = QPushButton(self.options_6)
        self.modifier_pays_monnaie.setObjectName(u"modifier_pays_monnaie")
        self.modifier_pays_monnaie.setCursor(QCursor(Qt.PointingHandCursor))
        self.modifier_pays_monnaie.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(51, 54, 69);\n"
"border: 1px solid rgb(51, 54, 69);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(70, 74, 95);\n"
"border: 1px solid rgb(70, 74, 95);\n"
"}\n"
"\n"
"")
        self.modifier_pays_monnaie.setIcon(icon5)
        self.modifier_pays_monnaie.setIconSize(QSize(12, 12))

        self.horizontalLayout_75.addWidget(self.modifier_pays_monnaie)

        self.supprimer_pays_monnaie = QPushButton(self.options_6)
        self.supprimer_pays_monnaie.setObjectName(u"supprimer_pays_monnaie")
        self.supprimer_pays_monnaie.setCursor(QCursor(Qt.PointingHandCursor))
        self.supprimer_pays_monnaie.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 0, 4);\n"
"border: 1px solid rgb(255, 0, 4);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 66, 66);\n"
"border: 1px solid rgb(255, 66, 66);\n"
"}\n"
"")
        self.supprimer_pays_monnaie.setIcon(icon6)
        self.supprimer_pays_monnaie.setIconSize(QSize(15, 15))

        self.horizontalLayout_75.addWidget(self.supprimer_pays_monnaie)


        self.verticalLayout_47.addWidget(self.options_6)

        self.tables_6 = QFrame(self.display_infos_6)
        self.tables_6.setObjectName(u"tables_6")
        self.tables_6.setMinimumSize(QSize(0, 32))
        self.tables_6.setMaximumSize(QSize(16777215, 32))
        self.tables_6.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid white;\n"
"	padding-bottom: 5px;\n"
"	font-size: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 5px solid rgb(57, 195, 221);\n"
"}")
        self.tables_6.setFrameShape(QFrame.NoFrame)
        self.tables_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.tables_6)
        self.horizontalLayout_76.setSpacing(25)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(30, -1, -1, 0)
        self.pays_button_pays_monnaie = QPushButton(self.tables_6)
        self.pays_button_pays_monnaie.setObjectName(u"pays_button_pays_monnaie")
        self.pays_button_pays_monnaie.setCursor(QCursor(Qt.PointingHandCursor))
        self.pays_button_pays_monnaie.setStyleSheet(u"")

        self.horizontalLayout_76.addWidget(self.pays_button_pays_monnaie)

        self.monnaie_button_pays_monnaie = QPushButton(self.tables_6)
        self.monnaie_button_pays_monnaie.setObjectName(u"monnaie_button_pays_monnaie")
        self.monnaie_button_pays_monnaie.setCursor(QCursor(Qt.PointingHandCursor))
        self.monnaie_button_pays_monnaie.setStyleSheet(u"")

        self.horizontalLayout_76.addWidget(self.monnaie_button_pays_monnaie)


        self.verticalLayout_47.addWidget(self.tables_6)


        self.verticalLayout_46.addWidget(self.display_infos_6)

        self.cute_separator_6 = QFrame(self.page_14)
        self.cute_separator_6.setObjectName(u"cute_separator_6")
        self.cute_separator_6.setMinimumSize(QSize(0, 20))
        self.cute_separator_6.setMaximumSize(QSize(16777215, 20))
        self.cute_separator_6.setStyleSheet(u"background-color: #eeeeee;")
        self.cute_separator_6.setFrameShape(QFrame.NoFrame)
        self.cute_separator_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_46.addWidget(self.cute_separator_6)

        self.contain_affichage_grid_layout_6 = QGridLayout()
        self.contain_affichage_grid_layout_6.setObjectName(u"contain_affichage_grid_layout_6")
        self.label_8 = QLabel(self.page_14)
        self.label_8.setObjectName(u"label_8")

        self.contain_affichage_grid_layout_6.addWidget(self.label_8, 1, 0, 1, 1)

        self.stackedWidget_6 = QStackedWidget(self.page_14)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.affichePays = QWidget()
        self.affichePays.setObjectName(u"affichePays")
        self.horizontalLayout_78 = QHBoxLayout(self.affichePays)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.tablePays = QTableWidget(self.affichePays)
        if (self.tablePays.columnCount() < 2):
            self.tablePays.setColumnCount(2)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setFont(font3);
        self.tablePays.setHorizontalHeaderItem(0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setFont(font2);
        self.tablePays.setHorizontalHeaderItem(1, __qtablewidgetitem80)
        self.tablePays.setObjectName(u"tablePays")
        self.tablePays.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tablePays.setRowCount(0)
        self.tablePays.setColumnCount(2)
        self.tablePays.horizontalHeader().setDefaultSectionSize(170)
        self.tablePays.horizontalHeader().setStretchLastSection(True)
        self.tablePays.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_78.addWidget(self.tablePays)

        self.stackedWidget_6.addWidget(self.affichePays)
        self.afficheMaonnaie = QWidget()
        self.afficheMaonnaie.setObjectName(u"afficheMaonnaie")
        self.verticalLayout_50 = QVBoxLayout(self.afficheMaonnaie)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.tableMonnaie = QTableWidget(self.afficheMaonnaie)
        if (self.tableMonnaie.columnCount() < 2):
            self.tableMonnaie.setColumnCount(2)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setFont(font3);
        self.tableMonnaie.setHorizontalHeaderItem(0, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setFont(font2);
        self.tableMonnaie.setHorizontalHeaderItem(1, __qtablewidgetitem82)
        self.tableMonnaie.setObjectName(u"tableMonnaie")
        self.tableMonnaie.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableMonnaie.setFrameShape(QFrame.NoFrame)
        self.tableMonnaie.setRowCount(0)
        self.tableMonnaie.setColumnCount(2)
        self.tableMonnaie.horizontalHeader().setMinimumSectionSize(200)
        self.tableMonnaie.horizontalHeader().setDefaultSectionSize(200)
        self.tableMonnaie.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableMonnaie.horizontalHeader().setStretchLastSection(True)
        self.tableMonnaie.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_50.addWidget(self.tableMonnaie)

        self.stackedWidget_6.addWidget(self.afficheMaonnaie)

        self.contain_affichage_grid_layout_6.addWidget(self.stackedWidget_6, 0, 0, 1, 1)


        self.verticalLayout_46.addLayout(self.contain_affichage_grid_layout_6)


        self.horizontalLayout_77.addWidget(self.page_14)

        self.stackedWidget.addWidget(self.affiche_pays_monnaie)
        self.Affiche_externe = QWidget()
        self.Affiche_externe.setObjectName(u"Affiche_externe")
        self.verticalLayout_44 = QVBoxLayout(self.Affiche_externe)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.page_16 = QWidget(self.Affiche_externe)
        self.page_16.setObjectName(u"page_16")
        self.page_16.setMinimumSize(QSize(0, 800))
        self.page_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_48 = QVBoxLayout(self.page_16)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.display_infos_7 = QFrame(self.page_16)
        self.display_infos_7.setObjectName(u"display_infos_7")
        self.display_infos_7.setMinimumSize(QSize(0, 150))
        self.display_infos_7.setMaximumSize(QSize(16777215, 150))
        self.display_infos_7.setStyleSheet(u"background-color: white;")
        self.display_infos_7.setFrameShape(QFrame.NoFrame)
        self.display_infos_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.display_infos_7)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_gestion_container_7 = QFrame(self.display_infos_7)
        self.label_gestion_container_7.setObjectName(u"label_gestion_container_7")
        self.label_gestion_container_7.setMinimumSize(QSize(0, 50))
        self.label_gestion_container_7.setMaximumSize(QSize(16777215, 50))
        self.label_gestion_container_7.setFrameShape(QFrame.StyledPanel)
        self.label_gestion_container_7.setFrameShadow(QFrame.Raised)
        self.gestion_6 = QLabel(self.label_gestion_container_7)
        self.gestion_6.setObjectName(u"gestion_6")
        self.gestion_6.setGeometry(QRect(30, 10, 431, 41))
        self.gestion_6.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_49.addWidget(self.label_gestion_container_7)

        self.options_7 = QFrame(self.display_infos_7)
        self.options_7.setObjectName(u"options_7")
        self.options_7.setMinimumSize(QSize(0, 60))
        self.options_7.setMaximumSize(QSize(16777215, 60))
        self.options_7.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(238, 238, 238);\n"
"	padding: 3px 5px 3px 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QLineEdit {\n"
"	font-size: 16px;\n"
"}\n"
"")
        self.options_7.setFrameShape(QFrame.NoFrame)
        self.options_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.options_7)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(30, -1, 30, -1)
        self.rechercher_externe = QLineEdit(self.options_7)
        self.rechercher_externe.setObjectName(u"rechercher_externe")
        self.rechercher_externe.setStyleSheet(u"border: 1.5px solid rgb(238, 238, 238);\n"
"padding: 1px;")

        self.horizontalLayout_80.addWidget(self.rechercher_externe)

        self.ajouter_externe = QPushButton(self.options_7)
        self.ajouter_externe.setObjectName(u"ajouter_externe")
        self.ajouter_externe.setCursor(QCursor(Qt.PointingHandCursor))
        self.ajouter_externe.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"\n"
"\n"
"")
        self.ajouter_externe.setIcon(icon3)
        self.ajouter_externe.setIconSize(QSize(12, 12))

        self.horizontalLayout_80.addWidget(self.ajouter_externe)

        self.modifier_externe = QPushButton(self.options_7)
        self.modifier_externe.setObjectName(u"modifier_externe")
        self.modifier_externe.setCursor(QCursor(Qt.PointingHandCursor))
        self.modifier_externe.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background-color: rgb(51, 54, 69);\n"
"border: 1px solid rgb(51, 54, 69);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(70, 74, 95);\n"
"border: 1px solid rgb(70, 74, 95);\n"
"}\n"
"\n"
"")
        self.modifier_externe.setIcon(icon5)
        self.modifier_externe.setIconSize(QSize(12, 12))

        self.horizontalLayout_80.addWidget(self.modifier_externe)

        self.supprimer_externe = QPushButton(self.options_7)
        self.supprimer_externe.setObjectName(u"supprimer_externe")
        self.supprimer_externe.setCursor(QCursor(Qt.PointingHandCursor))
        self.supprimer_externe.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(255, 0, 4);\n"
"border: 1px solid rgb(255, 0, 4);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 66, 66);\n"
"border: 1px solid rgb(255, 66, 66);\n"
"}\n"
"\n"
"")
        self.supprimer_externe.setIcon(icon6)
        self.supprimer_externe.setIconSize(QSize(15, 15))

        self.horizontalLayout_80.addWidget(self.supprimer_externe)


        self.verticalLayout_49.addWidget(self.options_7)

        self.tables_7 = QFrame(self.display_infos_7)
        self.tables_7.setObjectName(u"tables_7")
        self.tables_7.setMinimumSize(QSize(0, 35))
        self.tables_7.setMaximumSize(QSize(16777215, 35))
        self.tables_7.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid white;\n"
"	padding-bottom: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 5px solid rgb(57, 195, 221);\n"
"}")
        self.tables_7.setFrameShape(QFrame.NoFrame)
        self.tables_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.tables_7)
        self.horizontalLayout_81.setSpacing(25)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(30, -1, -1, 0)
        self.dounier_button_externe = QPushButton(self.tables_7)
        self.dounier_button_externe.setObjectName(u"dounier_button_externe")
        self.dounier_button_externe.setCursor(QCursor(Qt.PointingHandCursor))
        self.dounier_button_externe.setStyleSheet(u"")

        self.horizontalLayout_81.addWidget(self.dounier_button_externe)

        self.expert_button_externe = QPushButton(self.tables_7)
        self.expert_button_externe.setObjectName(u"expert_button_externe")
        self.expert_button_externe.setCursor(QCursor(Qt.PointingHandCursor))
        self.expert_button_externe.setStyleSheet(u"")

        self.horizontalLayout_81.addWidget(self.expert_button_externe)

        self.representant_button_externe = QPushButton(self.tables_7)
        self.representant_button_externe.setObjectName(u"representant_button_externe")
        self.representant_button_externe.setCursor(QCursor(Qt.PointingHandCursor))
        self.representant_button_externe.setStyleSheet(u"")

        self.horizontalLayout_81.addWidget(self.representant_button_externe)


        self.verticalLayout_49.addWidget(self.tables_7)


        self.verticalLayout_48.addWidget(self.display_infos_7)

        self.cute_separator_7 = QFrame(self.page_16)
        self.cute_separator_7.setObjectName(u"cute_separator_7")
        self.cute_separator_7.setMinimumSize(QSize(0, 20))
        self.cute_separator_7.setMaximumSize(QSize(16777215, 20))
        self.cute_separator_7.setStyleSheet(u"background-color: #eeeeee;")
        self.cute_separator_7.setFrameShape(QFrame.NoFrame)
        self.cute_separator_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_48.addWidget(self.cute_separator_7)

        self.contain_affichage_grid_layout_7 = QGridLayout()
        self.contain_affichage_grid_layout_7.setObjectName(u"contain_affichage_grid_layout_7")
        self.label_9 = QLabel(self.page_16)
        self.label_9.setObjectName(u"label_9")

        self.contain_affichage_grid_layout_7.addWidget(self.label_9, 1, 0, 1, 1)

        self.stackedWidget_7 = QStackedWidget(self.page_16)
        self.stackedWidget_7.setObjectName(u"stackedWidget_7")
        self.afficheDouanier = QWidget()
        self.afficheDouanier.setObjectName(u"afficheDouanier")
        self.horizontalLayout_71 = QHBoxLayout(self.afficheDouanier)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.table_douanier = QTableWidget(self.afficheDouanier)
        if (self.table_douanier.columnCount() < 5):
            self.table_douanier.setColumnCount(5)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setFont(font3);
        self.table_douanier.setHorizontalHeaderItem(0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setFont(font2);
        self.table_douanier.setHorizontalHeaderItem(1, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setFont(font2);
        self.table_douanier.setHorizontalHeaderItem(2, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setFont(font2);
        self.table_douanier.setHorizontalHeaderItem(3, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setFont(font2);
        self.table_douanier.setHorizontalHeaderItem(4, __qtablewidgetitem87)
        self.table_douanier.setObjectName(u"table_douanier")
        self.table_douanier.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.table_douanier.setRowCount(0)
        self.table_douanier.setColumnCount(5)
        self.table_douanier.horizontalHeader().setDefaultSectionSize(170)

        self.horizontalLayout_71.addWidget(self.table_douanier)

        self.stackedWidget_7.addWidget(self.afficheDouanier)
        self.affiche_expert = QWidget()
        self.affiche_expert.setObjectName(u"affiche_expert")
        self.horizontalLayout_70 = QHBoxLayout(self.affiche_expert)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.table_expert = QTableWidget(self.affiche_expert)
        if (self.table_expert.columnCount() < 6):
            self.table_expert.setColumnCount(6)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setFont(font3);
        self.table_expert.setHorizontalHeaderItem(0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setFont(font2);
        self.table_expert.setHorizontalHeaderItem(1, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setFont(font2);
        self.table_expert.setHorizontalHeaderItem(2, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setFont(font2);
        self.table_expert.setHorizontalHeaderItem(3, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setFont(font2);
        self.table_expert.setHorizontalHeaderItem(4, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setFont(font2);
        self.table_expert.setHorizontalHeaderItem(5, __qtablewidgetitem93)
        self.table_expert.setObjectName(u"table_expert")
        self.table_expert.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.table_expert.setRowCount(0)
        self.table_expert.setColumnCount(6)
        self.table_expert.horizontalHeader().setDefaultSectionSize(170)

        self.horizontalLayout_70.addWidget(self.table_expert)

        self.stackedWidget_7.addWidget(self.affiche_expert)
        self.affiche_representant = QWidget()
        self.affiche_representant.setObjectName(u"affiche_representant")
        self.horizontalLayout_82 = QHBoxLayout(self.affiche_representant)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.table_representant = QTableWidget(self.affiche_representant)
        if (self.table_representant.columnCount() < 6):
            self.table_representant.setColumnCount(6)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setFont(font3);
        self.table_representant.setHorizontalHeaderItem(0, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setFont(font2);
        self.table_representant.setHorizontalHeaderItem(1, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setFont(font2);
        self.table_representant.setHorizontalHeaderItem(2, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setFont(font2);
        self.table_representant.setHorizontalHeaderItem(3, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setFont(font2);
        self.table_representant.setHorizontalHeaderItem(4, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setFont(font2);
        self.table_representant.setHorizontalHeaderItem(5, __qtablewidgetitem99)
        self.table_representant.setObjectName(u"table_representant")
        self.table_representant.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.table_representant.setRowCount(0)
        self.table_representant.setColumnCount(6)
        self.table_representant.horizontalHeader().setDefaultSectionSize(170)

        self.horizontalLayout_82.addWidget(self.table_representant)

        self.stackedWidget_7.addWidget(self.affiche_representant)

        self.contain_affichage_grid_layout_7.addWidget(self.stackedWidget_7, 0, 0, 1, 1)


        self.verticalLayout_48.addLayout(self.contain_affichage_grid_layout_7)


        self.verticalLayout_44.addWidget(self.page_16)

        self.stackedWidget.addWidget(self.Affiche_externe)
        self.afficheClientMenu = QWidget()
        self.afficheClientMenu.setObjectName(u"afficheClientMenu")
        self.horizontalLayout_3 = QHBoxLayout(self.afficheClientMenu)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.page_3 = QWidget(self.afficheClientMenu)
        self.page_3.setObjectName(u"page_3")
        self.page_3.setMinimumSize(QSize(0, 800))
        self.page_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_54 = QVBoxLayout(self.page_3)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.display_infos_5 = QFrame(self.page_3)
        self.display_infos_5.setObjectName(u"display_infos_5")
        self.display_infos_5.setMinimumSize(QSize(0, 150))
        self.display_infos_5.setMaximumSize(QSize(16777215, 150))
        self.display_infos_5.setStyleSheet(u"background-color: white;")
        self.display_infos_5.setFrameShape(QFrame.NoFrame)
        self.display_infos_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.display_infos_5)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_gestion_container_5 = QFrame(self.display_infos_5)
        self.label_gestion_container_5.setObjectName(u"label_gestion_container_5")
        self.label_gestion_container_5.setMinimumSize(QSize(0, 50))
        self.label_gestion_container_5.setMaximumSize(QSize(16777215, 50))
        self.label_gestion_container_5.setFrameShape(QFrame.StyledPanel)
        self.label_gestion_container_5.setFrameShadow(QFrame.Raised)
        self.gestion_4 = QLabel(self.label_gestion_container_5)
        self.gestion_4.setObjectName(u"gestion_4")
        self.gestion_4.setGeometry(QRect(30, 10, 391, 31))
        self.gestion_4.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_55.addWidget(self.label_gestion_container_5)

        self.options_5 = QFrame(self.display_infos_5)
        self.options_5.setObjectName(u"options_5")
        self.options_5.setMinimumSize(QSize(0, 60))
        self.options_5.setMaximumSize(QSize(16777215, 60))
        self.options_5.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(238, 238, 238);\n"
"	padding: 3px 5px 3px 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QLineEdit {\n"
"	font-size: 16px;\n"
"}\n"
"")
        self.options_5.setFrameShape(QFrame.NoFrame)
        self.options_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.options_5)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(30, -1, 30, -1)
        self.rechercherClientMenu = QLineEdit(self.options_5)
        self.rechercherClientMenu.setObjectName(u"rechercherClientMenu")
        self.rechercherClientMenu.setStyleSheet(u"border: 1.5px solid rgb(238, 238, 238);\n"
"padding: 1px;")

        self.horizontalLayout_55.addWidget(self.rechercherClientMenu)

        self.ajouterClientMenu = QPushButton(self.options_5)
        self.ajouterClientMenu.setObjectName(u"ajouterClientMenu")
        self.ajouterClientMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.ajouterClientMenu.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"\n"
"")
        self.ajouterClientMenu.setIcon(icon3)
        self.ajouterClientMenu.setIconSize(QSize(12, 12))

        self.horizontalLayout_55.addWidget(self.ajouterClientMenu)

        self.modifierClientMenu = QPushButton(self.options_5)
        self.modifierClientMenu.setObjectName(u"modifierClientMenu")
        self.modifierClientMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.modifierClientMenu.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(51, 54, 69);\n"
"border: 1px solid rgb(51, 54, 69);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(70, 74, 95);\n"
"border: 1px solid rgb(70, 74, 95);\n"
"}\n"
"")
        self.modifierClientMenu.setIcon(icon5)
        self.modifierClientMenu.setIconSize(QSize(12, 12))

        self.horizontalLayout_55.addWidget(self.modifierClientMenu)

        self.supprimer = QPushButton(self.options_5)
        self.supprimer.setObjectName(u"supprimer")
        self.supprimer.setCursor(QCursor(Qt.PointingHandCursor))
        self.supprimer.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(255, 0, 4);\n"
"border: 1px solid rgb(255, 0, 4);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 66, 66);\n"
"border: 1px solid rgb(255, 66, 66);\n"
"}\n"
"\n"
"\n"
"")
        self.supprimer.setIcon(icon6)
        self.supprimer.setIconSize(QSize(15, 15))

        self.horizontalLayout_55.addWidget(self.supprimer)


        self.verticalLayout_55.addWidget(self.options_5)

        self.tables_8 = QFrame(self.display_infos_5)
        self.tables_8.setObjectName(u"tables_8")
        self.tables_8.setMinimumSize(QSize(0, 35))
        self.tables_8.setMaximumSize(QSize(16777215, 35))
        self.tables_8.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid white;\n"
"	padding-bottom: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 5px solid rgb(57, 195, 221);\n"
"}")
        self.tables_8.setFrameShape(QFrame.NoFrame)
        self.tables_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.tables_8)
        self.horizontalLayout_84.setSpacing(25)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(30, -1, -1, 0)
        self.afficheClient_2 = QPushButton(self.tables_8)
        self.afficheClient_2.setObjectName(u"afficheClient_2")
        self.afficheClient_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.afficheClient_2.setStyleSheet(u"")

        self.horizontalLayout_84.addWidget(self.afficheClient_2)


        self.verticalLayout_55.addWidget(self.tables_8)


        self.verticalLayout_54.addWidget(self.display_infos_5)

        self.cute_separator_5 = QFrame(self.page_3)
        self.cute_separator_5.setObjectName(u"cute_separator_5")
        self.cute_separator_5.setMinimumSize(QSize(0, 20))
        self.cute_separator_5.setMaximumSize(QSize(16777215, 20))
        self.cute_separator_5.setStyleSheet(u"background-color: #eeeeee;")
        self.cute_separator_5.setFrameShape(QFrame.NoFrame)
        self.cute_separator_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_54.addWidget(self.cute_separator_5)

        self.contain_affichage_grid_layout_2 = QGridLayout()
        self.contain_affichage_grid_layout_2.setObjectName(u"contain_affichage_grid_layout_2")
        self.tableClienMenu = QTableWidget(self.page_3)
        if (self.tableClienMenu.columnCount() < 15):
            self.tableClienMenu.setColumnCount(15)
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(9)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setFont(font6);
        self.tableClienMenu.setHorizontalHeaderItem(0, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(1, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setFont(font4);
        self.tableClienMenu.setHorizontalHeaderItem(2, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(3, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(4, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(5, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(6, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(7, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(8, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(9, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(10, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        __qtablewidgetitem111.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(11, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        __qtablewidgetitem112.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(12, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        __qtablewidgetitem113.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(13, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        __qtablewidgetitem114.setFont(font2);
        self.tableClienMenu.setHorizontalHeaderItem(14, __qtablewidgetitem114)
        self.tableClienMenu.setObjectName(u"tableClienMenu")
        self.tableClienMenu.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableClienMenu.setFrameShape(QFrame.NoFrame)
        self.tableClienMenu.setRowCount(0)
        self.tableClienMenu.setColumnCount(15)
        self.tableClienMenu.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClienMenu.horizontalHeader().setMinimumSectionSize(30)
        self.tableClienMenu.horizontalHeader().setDefaultSectionSize(170)
        self.tableClienMenu.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableClienMenu.horizontalHeader().setStretchLastSection(True)
        self.tableClienMenu.verticalHeader().setStretchLastSection(False)

        self.contain_affichage_grid_layout_2.addWidget(self.tableClienMenu, 0, 0, 1, 1)


        self.verticalLayout_54.addLayout(self.contain_affichage_grid_layout_2)


        self.horizontalLayout_3.addWidget(self.page_3)

        self.stackedWidget.addWidget(self.afficheClientMenu)
        self.affichageFactures = QWidget()
        self.affichageFactures.setObjectName(u"affichageFactures")
        self.horizontalLayout_53 = QHBoxLayout(self.affichageFactures)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")

        self.horizontalLayout_53.addLayout(self.verticalLayout_39)

        self.page_5 = QWidget(self.affichageFactures)
        self.page_5.setObjectName(u"page_5")
        self.page_5.setMinimumSize(QSize(0, 800))
        self.page_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_61 = QVBoxLayout(self.page_5)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.display_infos_9 = QFrame(self.page_5)
        self.display_infos_9.setObjectName(u"display_infos_9")
        self.display_infos_9.setMinimumSize(QSize(0, 150))
        self.display_infos_9.setMaximumSize(QSize(16777215, 150))
        self.display_infos_9.setStyleSheet(u"background-color: white;")
        self.display_infos_9.setFrameShape(QFrame.NoFrame)
        self.display_infos_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.display_infos_9)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_gestion_container_9 = QFrame(self.display_infos_9)
        self.label_gestion_container_9.setObjectName(u"label_gestion_container_9")
        self.label_gestion_container_9.setMinimumSize(QSize(0, 50))
        self.label_gestion_container_9.setMaximumSize(QSize(16777215, 50))
        self.label_gestion_container_9.setFrameShape(QFrame.StyledPanel)
        self.label_gestion_container_9.setFrameShadow(QFrame.Raised)
        self.gestion_8 = QLabel(self.label_gestion_container_9)
        self.gestion_8.setObjectName(u"gestion_8")
        self.gestion_8.setGeometry(QRect(30, 10, 391, 31))
        self.gestion_8.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_62.addWidget(self.label_gestion_container_9)

        self.options_9 = QFrame(self.display_infos_9)
        self.options_9.setObjectName(u"options_9")
        self.options_9.setMinimumSize(QSize(0, 60))
        self.options_9.setMaximumSize(QSize(16777215, 60))
        self.options_9.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(238, 238, 238);\n"
"	padding: 3px 5px 3px 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QLineEdit {\n"
"	font-size: 16px;\n"
"}\n"
"")
        self.options_9.setFrameShape(QFrame.NoFrame)
        self.options_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.options_9)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(30, -1, 30, -1)
        self.rechercherfacturesMenu = QLineEdit(self.options_9)
        self.rechercherfacturesMenu.setObjectName(u"rechercherfacturesMenu")
        self.rechercherfacturesMenu.setStyleSheet(u"border: 1.5px solid rgb(238, 238, 238);\n"
"padding: 1px;")

        self.horizontalLayout_87.addWidget(self.rechercherfacturesMenu)

        self.ajouterFacturesMenu = QPushButton(self.options_9)
        self.ajouterFacturesMenu.setObjectName(u"ajouterFacturesMenu")
        self.ajouterFacturesMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.ajouterFacturesMenu.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(57, 195, 221);\n"
"border: 1px solid rgb(57, 195, 221);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 206, 231);\n"
"border: 1px solid rgb(60, 206, 231);\n"
"}\n"
"")
        self.ajouterFacturesMenu.setIcon(icon3)
        self.ajouterFacturesMenu.setIconSize(QSize(12, 12))

        self.horizontalLayout_87.addWidget(self.ajouterFacturesMenu)

        self.modifierFacturesMenu = QPushButton(self.options_9)
        self.modifierFacturesMenu.setObjectName(u"modifierFacturesMenu")
        self.modifierFacturesMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.modifierFacturesMenu.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(51, 54, 69);\n"
"border: 1px solid rgb(51, 54, 69);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(70, 74, 95);\n"
"border: 1px solid rgb(70, 74, 95);\n"
"}\n"
"\n"
"")
        self.modifierFacturesMenu.setIcon(icon5)
        self.modifierFacturesMenu.setIconSize(QSize(12, 12))

        self.horizontalLayout_87.addWidget(self.modifierFacturesMenu)

        self.supprimerFactures = QPushButton(self.options_9)
        self.supprimerFactures.setObjectName(u"supprimerFactures")
        self.supprimerFactures.setCursor(QCursor(Qt.PointingHandCursor))
        self.supprimerFactures.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(255, 0, 4);\n"
"border: 1px solid rgb(255, 0, 4);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 66, 66);\n"
"border: 1px solid rgb(255, 66, 66);\n"
"}\n"
"\n"
"")
        self.supprimerFactures.setIcon(icon6)
        self.supprimerFactures.setIconSize(QSize(15, 15))

        self.horizontalLayout_87.addWidget(self.supprimerFactures)

        self.pushButton_3 = QPushButton(self.options_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(25, 215, 110);\n"
"color: white;\n"
"border: 1px solid rgb(25, 215, 110);\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(26, 236, 117);\n"
"border: 1px solidrgb(26, 236, 117);\n"
"}")
        self.pushButton_3.setIcon(icon8)

        self.horizontalLayout_87.addWidget(self.pushButton_3)


        self.verticalLayout_62.addWidget(self.options_9)

        self.tables_10 = QFrame(self.display_infos_9)
        self.tables_10.setObjectName(u"tables_10")
        self.tables_10.setMinimumSize(QSize(0, 35))
        self.tables_10.setMaximumSize(QSize(16777215, 35))
        self.tables_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.tables_10.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid white;\n"
"	padding-bottom: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 5px solid rgb(57, 195, 221);\n"
"}")
        self.tables_10.setFrameShape(QFrame.NoFrame)
        self.tables_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.tables_10)
        self.horizontalLayout_88.setSpacing(25)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(30, -1, -1, 0)
        self.afficheFactures_2 = QPushButton(self.tables_10)
        self.afficheFactures_2.setObjectName(u"afficheFactures_2")
        self.afficheFactures_2.setStyleSheet(u"")

        self.horizontalLayout_88.addWidget(self.afficheFactures_2)


        self.verticalLayout_62.addWidget(self.tables_10)


        self.verticalLayout_61.addWidget(self.display_infos_9)

        self.cute_separator_9 = QFrame(self.page_5)
        self.cute_separator_9.setObjectName(u"cute_separator_9")
        self.cute_separator_9.setMinimumSize(QSize(0, 20))
        self.cute_separator_9.setMaximumSize(QSize(16777215, 20))
        self.cute_separator_9.setStyleSheet(u"background-color: #eeeeee;")
        self.cute_separator_9.setFrameShape(QFrame.NoFrame)
        self.cute_separator_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_61.addWidget(self.cute_separator_9)

        self.contain_affichage_grid_layout_9 = QGridLayout()
        self.contain_affichage_grid_layout_9.setObjectName(u"contain_affichage_grid_layout_9")
        self.tableClienMenu_3 = QTableWidget(self.page_5)
        if (self.tableClienMenu_3.columnCount() < 9):
            self.tableClienMenu_3.setColumnCount(9)
        __qtablewidgetitem115 = QTableWidgetItem()
        __qtablewidgetitem115.setFont(font3);
        self.tableClienMenu_3.setHorizontalHeaderItem(0, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        __qtablewidgetitem116.setFont(font2);
        self.tableClienMenu_3.setHorizontalHeaderItem(1, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        __qtablewidgetitem117.setFont(font4);
        self.tableClienMenu_3.setHorizontalHeaderItem(2, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        __qtablewidgetitem118.setFont(font2);
        self.tableClienMenu_3.setHorizontalHeaderItem(3, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        __qtablewidgetitem119.setFont(font2);
        self.tableClienMenu_3.setHorizontalHeaderItem(4, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        __qtablewidgetitem120.setFont(font2);
        self.tableClienMenu_3.setHorizontalHeaderItem(5, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        __qtablewidgetitem121.setFont(font2);
        self.tableClienMenu_3.setHorizontalHeaderItem(6, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        __qtablewidgetitem122.setFont(font2);
        self.tableClienMenu_3.setHorizontalHeaderItem(7, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        __qtablewidgetitem123.setFont(font2);
        self.tableClienMenu_3.setHorizontalHeaderItem(8, __qtablewidgetitem123)
        self.tableClienMenu_3.setObjectName(u"tableClienMenu_3")
        self.tableClienMenu_3.setStyleSheet(u"font-family:'Montserrat', sans-serif;\n"
"font-size: 10pt;\n"
"border:0.3px solid rgb(238,238,238);")
        self.tableClienMenu_3.setRowCount(0)
        self.tableClienMenu_3.setColumnCount(9)
        self.tableClienMenu_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClienMenu_3.horizontalHeader().setMinimumSectionSize(30)
        self.tableClienMenu_3.horizontalHeader().setDefaultSectionSize(170)
        self.tableClienMenu_3.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableClienMenu_3.horizontalHeader().setStretchLastSection(True)
        self.tableClienMenu_3.verticalHeader().setStretchLastSection(False)

        self.contain_affichage_grid_layout_9.addWidget(self.tableClienMenu_3, 0, 0, 1, 1)


        self.verticalLayout_61.addLayout(self.contain_affichage_grid_layout_9)


        self.horizontalLayout_53.addWidget(self.page_5)

        self.stackedWidget.addWidget(self.affichageFactures)
        self.statistics = QWidget()
        self.statistics.setObjectName(u"statistics")
        self.horizontalLayout_92 = QHBoxLayout(self.statistics)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.frame = QFrame(self.statistics)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #fff;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 35))
        self.frame_28.setMaximumSize(QSize(16777215, 60))
        self.frame_28.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid white;\n"
"	padding-bottom: 5px;\n"
"	font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-bottom: 5px solid rgb(57, 195, 221);\n"
"}")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.gain_annuel_exemple = QPushButton(self.frame_28)
        self.gain_annuel_exemple.setObjectName(u"gain_annuel_exemple")
        self.gain_annuel_exemple.setMaximumSize(QSize(16777215, 60))
        self.gain_annuel_exemple.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_56.addWidget(self.gain_annuel_exemple)

        self.repartition_dossier_par_pay_exemple = QPushButton(self.frame_28)
        self.repartition_dossier_par_pay_exemple.setObjectName(u"repartition_dossier_par_pay_exemple")
        self.repartition_dossier_par_pay_exemple.setMaximumSize(QSize(16777215, 60))
        self.repartition_dossier_par_pay_exemple.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_56.addWidget(self.repartition_dossier_par_pay_exemple)

        self.activite_mensuel_exemple = QPushButton(self.frame_28)
        self.activite_mensuel_exemple.setObjectName(u"activite_mensuel_exemple")
        self.activite_mensuel_exemple.setMaximumSize(QSize(16777215, 60))
        self.activite_mensuel_exemple.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_56.addWidget(self.activite_mensuel_exemple)


        self.verticalLayout_40.addWidget(self.frame_28)

        self.stackedWidget_8 = QStackedWidget(self.frame)
        self.stackedWidget_8.setObjectName(u"stackedWidget_8")
        self.gain_annuel = QWidget()
        self.gain_annuel.setObjectName(u"gain_annuel")
        self.horizontalLayout_86 = QHBoxLayout(self.gain_annuel)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.frame_29 = QFrame(self.gain_annuel)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_29)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_118 = QLabel(self.frame_29)
        self.label_118.setObjectName(u"label_118")

        self.verticalLayout_53.addWidget(self.label_118, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.set0 = QBarSet("Dossiers")
        self.set0.append(data1)
        self.series = QBarSeries()
        self.series.setBarWidth(1)
        self.series.append(self.set0)
        self.chart1 = QChart()
        self.chart1.addSeries(self.series)
        self.chart1.setTitle("Percent Example")
        self.chart1.setAnimationOptions(QChart.SeriesAnimations)

        categories = ["Jan", "Fev", "Mar", "Avr", "May", "Juin", "jul", "aut", "sept", "oct", "nov", "dec"]
        axis = QBarCategoryAxis()
        axis.append(categories)
        self.chart1.createDefaultAxes()
        self.chart1.setAxisX(axis, self.series)
        self.chart1.axisY(self.series).setRange(0, max(data1))

        self.chart1.legend().setVisible(True)
        self.chart1.legend().setAlignment(Qt.AlignBottom)
        self.graphicsView_GA = QChartView(self.chart1)
        self.graphicsView_GA.setRenderHint(QPainter.Antialiasing)

        self.verticalLayout_53.addWidget(self.graphicsView_GA)


        self.horizontalLayout_86.addWidget(self.frame_29)

        self.stackedWidget_8.addWidget(self.gain_annuel)
        self.repartition_dossier_par_pay = QWidget()
        self.repartition_dossier_par_pay.setObjectName(u"repartition_dossier_par_pay")
        self.horizontalLayout_90 = QHBoxLayout(self.repartition_dossier_par_pay)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.frame_30 = QFrame(self.repartition_dossier_par_pay)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_30)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.label_119 = QLabel(self.frame_30)
        self.label_119.setObjectName(u"label_119")

        self.verticalLayout_59.addWidget(self.label_119, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.series2 = QPieSeries()
        chart2 = QChart()
        chart2.legend().hide()
        chart2.addSeries(self.series2)
        chart2.createDefaultAxes()
        chart2.setAnimationOptions(QChart.SeriesAnimations)
        chart2.setTitle("Pie Chart Example")

        chart2.legend().setVisible(True)
        chart2.legend().setAlignment(Qt.AlignBottom)
        self.graphicsView_RDP = QChartView(chart2)
        self.graphicsView_RDP.setObjectName(u"graphicsView_RDP")
        self.graphicsView_RDP.setStyleSheet(u"border: 1px solid rgb(240, 240, 240);\n"
                                            "margin: 0px 20px;")

        self.verticalLayout_59.addWidget(self.graphicsView_RDP)


        self.horizontalLayout_90.addWidget(self.frame_30)

        self.stackedWidget_8.addWidget(self.repartition_dossier_par_pay)
        self.activite_mensuel = QWidget()
        self.activite_mensuel.setObjectName(u"activite_mensuel")
        self.horizontalLayout_91 = QHBoxLayout(self.activite_mensuel)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.frame_31 = QFrame(self.activite_mensuel)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_31)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_120 = QLabel(self.frame_31)
        self.label_120.setObjectName(u"label_120")

        self.verticalLayout_60.addWidget(self.label_120, 0, Qt.AlignHCenter)

        self.series3 = QLineSeries()

        # self.series << QPointF(11, 1) << QPointF(13, 3) << QPointF(17, 6) << QPointF(18, 3) << QPointF(20, 2)

        self.chart3 = QChart()

        self.chart3.addSeries(self.series3)
        # self.chart3.createDefaultAxes()
        categories = ["Jan", "Fev", "Mar", "Avr", "May", "Juin", "jul", "aut", "sept", "oct", "nov", "dec"]
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        axisY = QValueAxis()
        self.series3.attachAxis(axisY)
        self.chart3.setAxisX(axisX, self.series3)
        self.chart3.setAxisY(axisY, self.series3)
        self.chart3.setAnimationOptions(QChart.GridAxisAnimations)
        self.chart3.setTitle("Line Chart Example")

        self.chart3.legend().setVisible(True)
        self.chart3.legend().setAlignment(Qt.AlignBottom)
        self.graphicsView_AM = QChartView(self.chart3)
        self.graphicsView_AM.setRenderHint(QPainter.Antialiasing)

        self.verticalLayout_60.addWidget(self.graphicsView_AM)


        self.horizontalLayout_91.addWidget(self.frame_31)

        self.stackedWidget_8.addWidget(self.activite_mensuel)

        self.verticalLayout_40.addWidget(self.stackedWidget_8)


        self.horizontalLayout_92.addWidget(self.frame)

        self.stackedWidget.addWidget(self.statistics)

        self.verticalLayout_57.addWidget(self.stackedWidget)

        self.scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_56.addWidget(self.scroll_area)


        self.horizontalLayout_2.addWidget(self.content_frame)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(0)
        self.stackedWidget_6.setCurrentIndex(0)
        self.stackedWidget_7.setCurrentIndex(0)
        self.stackedWidget_8.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Port-Gest", None))
        self.menu_button.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.welcome_user.setText(QCoreApplication.translate("MainWindow", u"Bienvenu, Adimi !", None))
        self.settings.setText("")
        self.deconnexion.setText("")
        self.statistiques.setText(QCoreApplication.translate("MainWindow", u"STATISTIQUES", None))
        self.client_menu.setText(QCoreApplication.translate("MainWindow", u"CLIENT", None))
        self.personnels_interne.setText(QCoreApplication.translate("MainWindow", u"PERSONNEL INTERNE", None))
        self.Externe.setText(QCoreApplication.translate("MainWindow", u"PERSONNEL EXTERNE", None))
        self.documents.setText(QCoreApplication.translate("MainWindow", u"DOCUMENTS", None))
        self.marchandise_emballages.setText(QCoreApplication.translate("MainWindow", u"MARCHANDISES ET EMBALLAGES", None))
        self.transport_livraison.setText(QCoreApplication.translate("MainWindow", u"TRANSPORT ET LIVRAISON", None))
        self.pays_unite_monetaire.setText(QCoreApplication.translate("MainWindow", u"PAYS ET UNIT\u00c9 MON\u00c9TAIRE", None))
        self.facturation.setText(QCoreApplication.translate("MainWindow", u"FACTURATION", None))
        self.ajouter_3.setText(QCoreApplication.translate("MainWindow", u"Ajouter une facture", None))
        self.close_3.setText("")
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Montant total :", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Total pr\u00e9station :", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Total d\u00e9bours :", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"type", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"d\u00e9signiation", None));
        ___qtablewidgetitem2 = self.designationMontantTable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nom d\u00e9signation", None));
        ___qtablewidgetitem3 = self.designationMontantTable.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Montant debours", None));
        ___qtablewidgetitem4 = self.designationMontantTable.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Montant pr\u00e9station", None));
        self.etat_paiement_3.setItemText(0, QCoreApplication.translate("MainWindow", u"pay\u00e9", None))
        self.etat_paiement_3.setItemText(1, QCoreApplication.translate("MainWindow", u"non pay\u00e9", None))

        self.label_date_ouver_3.setText(QCoreApplication.translate("MainWindow", u"Etat paiement :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 dossier :", None))
        self.label_date_ferm_3.setText(QCoreApplication.translate("MainWindow", u"Mode paiement :", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Droits de timbre :", None))
        self.label_date_arr_3.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TVA :", None))
        self.calculerFacture.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.ImprimerFacture.setText(QCoreApplication.translate("MainWindow", u"Imprimer", None))
        self.enregistrer_facture.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.buttonAjouterFormFact.setText("")
        self.pushButton_4.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher une d\u00e9signation", None))
        self.ajouter.setText(QCoreApplication.translate("MainWindow", u"Ajouter un fichier", None))
        self.close.setText("")
        self.parcourir.setText(QCoreApplication.translate("MainWindow", u"Parcourir", None))
        self.enregistrerfichier.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Chemin :", None))
        self.ajouter_4.setText(QCoreApplication.translate("MainWindow", u"Ajouter un bon de sortie", None))
        self.close_4.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Chauffeur :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 bon :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 dossier :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"pc :", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Matricule :", None))
        self.enregistrer_bon_de_sortie.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.ajouter_6.setText(QCoreApplication.translate("MainWindow", u"Ajouter un bon de visite", None))
        self.close_6.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Bureau de douane :", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 bon :", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 dossier :", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"pc :", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Douanier :", None))
        self.enregistrer_bon_visite.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.ajouter_8.setText(QCoreApplication.translate("MainWindow", u"Ajouter un camion", None))
        self.close_8.setText("")
        self.eregistrer_camion.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Matricule : ", None))
        self.ajouter_10.setText(QCoreApplication.translate("MainWindow", u"Ajouter un chauffeur", None))
        self.pushButton.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom :", None))
        self.enregistrer_chauffeur.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Date de naissance :", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 t\u00e9l\u00e9phone :", None))
        self.ajouter_12.setText(QCoreApplication.translate("MainWindow", u"Ajouter un client", None))
        self.close_10.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 RC :", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Statut juridique :", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 succursale :", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 NIF :", None))
        self.enregistrer_client.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 NIC :", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Mandat :", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 t\u00e9l\u00e9phone :", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 article d'imposition :", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"E-mail :", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Nom du client :", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Addresse :", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Code postal :", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Expiration mandat :", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Expiration RC :", None))
        self.ajouter_13.setText(QCoreApplication.translate("MainWindow", u"Ajouter un d\u00e9clarant", None))
        self.close_11.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom :", None))
        self.enregistrer_declarent.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Date de naissance :", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 t\u00e9l\u00e9phone :", None))
        self.ajouter_14.setText(QCoreApplication.translate("MainWindow", u"Ajouter une d\u00e9signation", None))
        self.pushButton_6.setText("")
        self.enregistrer_designation.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Type :", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 marchandise :", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.ajouter_15.setText(QCoreApplication.translate("MainWindow", u"Ajouter un dossier", None))
        self.pushButton_8.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Gros :", None))
        self.label_code_monnaie.setText(QCoreApplication.translate("MainWindow", u"Code monnaie :", None))
        self.enregistrer_dossier.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"S/G :", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Lieu d'entreposage :", None))
        self.label_titre_transport.setText(QCoreApplication.translate("MainWindow", u"Titre transport :", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 d\u00e9clarant :", None))
        self.label_id_trans.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 transport :", None))
        self.label_n_fournisseur.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 fournisseur :", None))
        self.label_date_arr_4.setText(QCoreApplication.translate("MainWindow", u"Date arriv\u00e9 :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nom d\u00e9clarant:", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 fichier :", None))
        self.nature_dossier.setItemText(0, QCoreApplication.translate("MainWindow", u"Import", None))
        self.nature_dossier.setItemText(1, QCoreApplication.translate("MainWindow", u"Export", None))

        self.label_id_pays.setText(QCoreApplication.translate("MainWindow", u"ID pays :", None))
        self.label_nom_pays.setText(QCoreApplication.translate("MainWindow", u"Nom pays :", None))
        self.label_date_ouver_4.setText(QCoreApplication.translate("MainWindow", u"Date ouverture :", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Nom port :", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Observation :", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Statut dossier :", None))
        self.label_nom_client.setText(QCoreApplication.translate("MainWindow", u"Nom client :", None))
        self.statut_dossier.setItemText(0, QCoreApplication.translate("MainWindow", u"En cours", None))
        self.statut_dossier.setItemText(1, QCoreApplication.translate("MainWindow", u"Archiv\u00e9", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom d\u00e9clarant:", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Nature dossier :", None))
        self.lable_nb_conteneur.setText(QCoreApplication.translate("MainWindow", u"Nb conteneurs :", None))
        self.label_article_4.setText(QCoreApplication.translate("MainWindow", u"Article :", None))
        self.label_navire.setText(QCoreApplication.translate("MainWindow", u"Navire :", None))
        self.checkbox_creationDossierArchivage.setText(QCoreApplication.translate("MainWindow", u" Voulez-vous cr\u00e9er un dossier d'archivage pour ce dossier ?", None))
        self.ajouter_16.setText(QCoreApplication.translate("MainWindow", u"Ajouter un douanier", None))
        self.close_12.setText("")
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom :", None))
        self.enregistrer_douanier.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Date de naissance :", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 t\u00e9l\u00e9phone :", None))
        self.ajouter_17.setText(QCoreApplication.translate("MainWindow", u"Ajouter un emballage", None))
        self.close_13.setText("")
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Genre :", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 dossier :", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Type :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ID Embalage", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Pieds :", None))
        self.enregistrer_emballage.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.ajouter_18.setText(QCoreApplication.translate("MainWindow", u"Ajouter un expert", None))
        self.close_14.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 t\u00e9l\u00e9phone :", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom :", None))
        self.enregistrer_expert.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Date de naissance :", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Domaine :", None))
        self.ajouter_19.setText(QCoreApplication.translate("MainWindow", u"Ajouter un fournisseur", None))
        self.close_15.setText("")
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Adresse :", None))
        self.enregistrer_fournisseur.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.ajouter_20.setText(QCoreApplication.translate("MainWindow", u"Ajouter un interm\u00e9diare", None))
        self.close_16.setText("")
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Type :", None))
        self.enregistrer_intermediaire.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Nom interm\u00e9diare :", None))
        self.ajouter_21.setText(QCoreApplication.translate("MainWindow", u"Ajouter une marchandise", None))
        self.close_17.setText("")
        self.enregistrer_marchandice.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Description :", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 emballage :", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Montant :", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Nature :", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Poids :", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 facture :", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 dossier :", None))
        self.ajouter_22.setText(QCoreApplication.translate("MainWindow", u"Ajouter une unit\u00e9 mon\u00e9taire", None))
        self.close_18.setText("")
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Nom pays :", None))
        self.enregistrer_monnaie.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Code monnaie :", None))
        self.ajouter_23.setText(QCoreApplication.translate("MainWindow", u"Ajouter nature marchandise", None))
        self.close_19.setText("")
        self.enregistrer_nature_marchandice.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Nature :", None))
        self.ajouter_24.setText(QCoreApplication.translate("MainWindow", u"Ajouter un pays", None))
        self.close_20.setText("")
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Code :", None))
        self.enregistrer_pays.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.ajouter_25.setText(QCoreApplication.translate("MainWindow", u"Ajouter un repr\u00e9sentant", None))
        self.pushButton_10.setText("")
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 t\u00e9l\u00e9phone :", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom :", None))
        self.enregistrer_representant.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Date de naissance :", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Nom client :", None))
        self.ajouter_26.setText(QCoreApplication.translate("MainWindow", u"Ajouter un utilisateur", None))
        self.close_21.setText("")
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 t\u00e9l\u00e9phone :", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom :", None))
        self.enregistrer_user.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Date de naissance :", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
        self.gestion.setText(QCoreApplication.translate("MainWindow", u"Gestion des transports et de livraison", None))
        self.rechercher_transport_livraison.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher un dossier", None))
        self.ajouter_transport_livraison.setText(QCoreApplication.translate("MainWindow", u"ajouter", None))
        self.modifier_transport_livraison.setText(QCoreApplication.translate("MainWindow", u"modifier", None))
        self.supprimer_transpor_livraison.setText(QCoreApplication.translate("MainWindow", u"supprimer", None))
        self.label_2.setText("")
        ___qtablewidgetitem5 = self.tableCamion.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Matricule", None));
        ___qtablewidgetitem6 = self.tableIntermediaire.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem7 = self.tableIntermediaire.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem8 = self.tableFournisseur.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nom fournisseur", None));
        ___qtablewidgetitem9 = self.tableFournisseur.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem10 = self.tableChauffeur_2.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID chauffeur", None));
        ___qtablewidgetitem11 = self.tableChauffeur_2.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem12 = self.tableChauffeur_2.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None));
        ___qtablewidgetitem13 = self.tableChauffeur_2.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Date de naissance", None));
        ___qtablewidgetitem14 = self.tableChauffeur_2.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Telephone", None));
        self.Camions_button.setText(QCoreApplication.translate("MainWindow", u"Camions", None))
        self.chauffeur_button.setText(QCoreApplication.translate("MainWindow", u"Chauffeurs", None))
        self.four_button.setText(QCoreApplication.translate("MainWindow", u"Fournisseurs", None))
        self.inter_button.setText(QCoreApplication.translate("MainWindow", u"Intermediaires", None))
        self.gestion_2.setText(QCoreApplication.translate("MainWindow", u"Gestion des Documents", None))
        self.rechercher_gestion_document.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherche d'un document", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Tout", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Archiv\u00e9s", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"En cours", None))

        self.ajouter_gestion_document.setText(QCoreApplication.translate("MainWindow", u"ajouter", None))
        self.modifier_gestion_document.setText(QCoreApplication.translate("MainWindow", u"modifier", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"fermer", None))
        self.supprimer_gestion_document.setText(QCoreApplication.translate("MainWindow", u"supprimer", None))
        self.exporter_gestion_document.setText(QCoreApplication.translate("MainWindow", u"Imprimer", None))
        self.dossiers_2.setText(QCoreApplication.translate("MainWindow", u"Dossiers", None))
        self.fichiers_2.setText(QCoreApplication.translate("MainWindow", u"Fichiers", None))
        self.bon_de_visite.setText(QCoreApplication.translate("MainWindow", u"Bons de visite", None))
        self.bon_de_sortie.setText(QCoreApplication.translate("MainWindow", u"Bons de sortie", None))
        ___qtablewidgetitem15 = self.tableDossier.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ID Dossier", None));
        ___qtablewidgetitem16 = self.tableDossier.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"ID Client", None));
        ___qtablewidgetitem17 = self.tableDossier.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"ID D\u00e9clarant", None));
        ___qtablewidgetitem18 = self.tableDossier.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Date Ouverture", None));
        ___qtablewidgetitem19 = self.tableDossier.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Date arriv\u00e9e", None));
        ___qtablewidgetitem20 = self.tableDossier.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Date fermeture", None));
        ___qtablewidgetitem21 = self.tableDossier.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Navire", None));
        ___qtablewidgetitem22 = self.tableDossier.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Nb conteneurs", None));
        ___qtablewidgetitem23 = self.tableDossier.horizontalHeaderItem(8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Status dossier", None));
        ___qtablewidgetitem24 = self.tableDossier.horizontalHeaderItem(9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Id Fournisseur", None));
        ___qtablewidgetitem25 = self.tableDossier.horizontalHeaderItem(10)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Id Pays", None));
        ___qtablewidgetitem26 = self.tableDossier.horizontalHeaderItem(11)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Id_comp_trans", None));
        ___qtablewidgetitem27 = self.tableDossier.horizontalHeaderItem(12)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Titre Trsans", None));
        ___qtablewidgetitem28 = self.tableDossier.horizontalHeaderItem(13)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Nom Port", None));
        ___qtablewidgetitem29 = self.tableDossier.horizontalHeaderItem(14)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"S/G", None));
        ___qtablewidgetitem30 = self.tableDossier.horizontalHeaderItem(15)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Lieu Enterpot", None));
        ___qtablewidgetitem31 = self.tableDossier.horizontalHeaderItem(16)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Observation", None));
        ___qtablewidgetitem32 = self.tableDossier.horizontalHeaderItem(17)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Nature dossier", None));
        ___qtablewidgetitem33 = self.tableDossier.horizontalHeaderItem(18)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Gros", None));
        ___qtablewidgetitem34 = self.tableDossier.horizontalHeaderItem(19)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Article", None));
        ___qtablewidgetitem35 = self.tableDossier.horizontalHeaderItem(20)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Code monnaie", None));
        ___qtablewidgetitem36 = self.tableDossier.horizontalHeaderItem(21)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"ID FICHIER", None));
        ___qtablewidgetitem37 = self.tableFichier.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"ID FICHIER", None));
        ___qtablewidgetitem38 = self.tableFichier.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Chemin", None));
        ___qtablewidgetitem39 = self.tableBonSortie.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"ID Dossier", None));
        ___qtablewidgetitem40 = self.tableBonSortie.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Numero bon", None));
        ___qtablewidgetitem41 = self.tableBonSortie.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Date bon", None));
        ___qtablewidgetitem42 = self.tableBonSortie.horizontalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"PC", None));
        ___qtablewidgetitem43 = self.tableBonSortie.horizontalHeaderItem(4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"ID Chauffeur", None));
        ___qtablewidgetitem44 = self.tableBonSortie.horizontalHeaderItem(5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Matricule", None));
        ___qtablewidgetitem45 = self.tableBonVisite.horizontalHeaderItem(0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"ID dossier", None));
        ___qtablewidgetitem46 = self.tableBonVisite.horizontalHeaderItem(1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro bon", None));
        ___qtablewidgetitem47 = self.tableBonVisite.horizontalHeaderItem(2)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Date bon", None));
        ___qtablewidgetitem48 = self.tableBonVisite.horizontalHeaderItem(3)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"pc", None));
        ___qtablewidgetitem49 = self.tableBonVisite.horizontalHeaderItem(4)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"ID douanier", None));
        ___qtablewidgetitem50 = self.tableBonVisite.horizontalHeaderItem(5)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Bureau de douane", None));
        self.gestionpersonnelintermediaire.setText(QCoreApplication.translate("MainWindow", u"Gestion du Personnel Interne", None))
        self.rechercher_personnel_interne.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherche d'une personne interne", None))
        self.ajouter_personnel_interne.setText(QCoreApplication.translate("MainWindow", u"ajouter", None))
        self.modifier_personnel_interne.setText(QCoreApplication.translate("MainWindow", u"modifier", None))
        self.supprimer_personnel_interne.setText(QCoreApplication.translate("MainWindow", u"supprimer", None))
        self.utilisateur_button_personnel_interne.setText(QCoreApplication.translate("MainWindow", u"Utilisateurs", None))
        self.declarant_button_personnel_interne.setText(QCoreApplication.translate("MainWindow", u"D\u00e9clarants", None))
        self.label_3.setText("")
        ___qtablewidgetitem51 = self.tableUtilisateur.horizontalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"ID utilisateur", None));
        ___qtablewidgetitem52 = self.tableUtilisateur.horizontalHeaderItem(1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem53 = self.tableUtilisateur.horizontalHeaderItem(2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None));
        ___qtablewidgetitem54 = self.tableUtilisateur.horizontalHeaderItem(3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Date de Naissance", None));
        ___qtablewidgetitem55 = self.tableUtilisateur.horizontalHeaderItem(4)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Telephone", None));
        ___qtablewidgetitem56 = self.tableUtilisateur.horizontalHeaderItem(5)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem57 = self.tableDeclarent.horizontalHeaderItem(0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"ID D\u00e9clarant", None));
        ___qtablewidgetitem58 = self.tableDeclarent.horizontalHeaderItem(1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem59 = self.tableDeclarent.horizontalHeaderItem(2)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None));
        ___qtablewidgetitem60 = self.tableDeclarent.horizontalHeaderItem(3)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Date de Naissance", None));
        ___qtablewidgetitem61 = self.tableDeclarent.horizontalHeaderItem(4)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Telephone", None));
        self.gestion_3.setText(QCoreApplication.translate("MainWindow", u"Gestion des Marchandises et des Emballages", None))
        self.rechercher_marchandise_embalage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherche d'une marchandise ou d'un emballage", None))
        self.ajouter_marchandise_embalage.setText(QCoreApplication.translate("MainWindow", u"ajouter", None))
        self.modifier_marchandise_embalage.setText(QCoreApplication.translate("MainWindow", u"modifier", None))
        self.supprimer_marchandise_embalage.setText(QCoreApplication.translate("MainWindow", u"supprimer", None))
        self.marchandise_button.setText(QCoreApplication.translate("MainWindow", u"Marchandises", None))
        self.nature_button.setText(QCoreApplication.translate("MainWindow", u"Nature Marchandise", None))
        self.emballage_button.setText(QCoreApplication.translate("MainWindow", u"Emballages", None))
        self.designation_button.setText(QCoreApplication.translate("MainWindow", u"D\u00e9signations", None))
        self.label_6.setText("")
        ___qtablewidgetitem62 = self.tableEmbalage.horizontalHeaderItem(0)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"ID Emballage", None));
        ___qtablewidgetitem63 = self.tableEmbalage.horizontalHeaderItem(1)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Genre", None));
        ___qtablewidgetitem64 = self.tableEmbalage.horizontalHeaderItem(2)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem65 = self.tableEmbalage.horizontalHeaderItem(3)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Pieds", None));
        ___qtablewidgetitem66 = self.tableEmbalage.horizontalHeaderItem(4)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"ID Dossier", None));
        ___qtablewidgetitem67 = self.tableMarchandice.horizontalHeaderItem(0)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"ID Marchandise", None));
        ___qtablewidgetitem68 = self.tableMarchandice.horizontalHeaderItem(1)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Poids", None));
        ___qtablewidgetitem69 = self.tableMarchandice.horizontalHeaderItem(2)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Num facture", None));
        ___qtablewidgetitem70 = self.tableMarchandice.horizontalHeaderItem(3)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Nature", None));
        ___qtablewidgetitem71 = self.tableMarchandice.horizontalHeaderItem(4)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        ___qtablewidgetitem72 = self.tableMarchandice.horizontalHeaderItem(5)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"ID Dossier", None));
        ___qtablewidgetitem73 = self.tableMarchandice.horizontalHeaderItem(6)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"ID Emballage", None));
        ___qtablewidgetitem74 = self.tableMarchandice.horizontalHeaderItem(7)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem75 = self.tableNatureMarch.horizontalHeaderItem(0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Nature", None));
        ___qtablewidgetitem76 = self.tableDesigniation.horizontalHeaderItem(0)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Nom Designation", None));
        ___qtablewidgetitem77 = self.tableDesigniation.horizontalHeaderItem(1)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem78 = self.tableDesigniation.horizontalHeaderItem(2)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"ID Marchandise", None));
        self.gestion_5.setText(QCoreApplication.translate("MainWindow", u"Gestion des Pays et des Unit\u00e9s Mon\u00e9taires", None))
        self.rechercher_pays_monnaie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherche d'un pay ou d'une unit\u00e9 mon\u00e9taire", None))
        self.ajouter_pays_monnaie.setText(QCoreApplication.translate("MainWindow", u"ajouter", None))
        self.modifier_pays_monnaie.setText(QCoreApplication.translate("MainWindow", u"modifier", None))
        self.supprimer_pays_monnaie.setText(QCoreApplication.translate("MainWindow", u"supprimer", None))
        self.pays_button_pays_monnaie.setText(QCoreApplication.translate("MainWindow", u"Pays", None))
        self.monnaie_button_pays_monnaie.setText(QCoreApplication.translate("MainWindow", u"Monnaie", None))
        self.label_8.setText("")
        ___qtablewidgetitem79 = self.tablePays.horizontalHeaderItem(0)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Code pays", None));
        ___qtablewidgetitem80 = self.tablePays.horizontalHeaderItem(1)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Nom pays", None));
        ___qtablewidgetitem81 = self.tableMonnaie.horizontalHeaderItem(0)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Code monnaie", None));
        ___qtablewidgetitem82 = self.tableMonnaie.horizontalHeaderItem(1)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Nom pays", None));
        self.gestion_6.setText(QCoreApplication.translate("MainWindow", u"Gestion du Personnel Externe", None))
        self.rechercher_externe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherche d'une personne externe", None))
        self.ajouter_externe.setText(QCoreApplication.translate("MainWindow", u"ajouter", None))
        self.modifier_externe.setText(QCoreApplication.translate("MainWindow", u"modifier", None))
        self.supprimer_externe.setText(QCoreApplication.translate("MainWindow", u"supprimer", None))
        self.dounier_button_externe.setText(QCoreApplication.translate("MainWindow", u"Douaniers", None))
        self.expert_button_externe.setText(QCoreApplication.translate("MainWindow", u"Experts", None))
        self.representant_button_externe.setText(QCoreApplication.translate("MainWindow", u"Repr\u00e9sentants", None))
        self.label_9.setText("")
        ___qtablewidgetitem83 = self.table_douanier.horizontalHeaderItem(0)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"ID Douanier", None));
        ___qtablewidgetitem84 = self.table_douanier.horizontalHeaderItem(1)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem85 = self.table_douanier.horizontalHeaderItem(2)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None));
        ___qtablewidgetitem86 = self.table_douanier.horizontalHeaderItem(3)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Num tel", None));
        ___qtablewidgetitem87 = self.table_douanier.horizontalHeaderItem(4)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Date de naissance", None));
        ___qtablewidgetitem88 = self.table_expert.horizontalHeaderItem(0)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"ID Expert", None));
        ___qtablewidgetitem89 = self.table_expert.horizontalHeaderItem(1)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem90 = self.table_expert.horizontalHeaderItem(2)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None));
        ___qtablewidgetitem91 = self.table_expert.horizontalHeaderItem(3)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Num tel", None));
        ___qtablewidgetitem92 = self.table_expert.horizontalHeaderItem(4)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Date de naissance", None));
        ___qtablewidgetitem93 = self.table_expert.horizontalHeaderItem(5)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Domaine", None));
        ___qtablewidgetitem94 = self.table_representant.horizontalHeaderItem(0)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"ID Repr\u00e9sentant", None));
        ___qtablewidgetitem95 = self.table_representant.horizontalHeaderItem(1)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem96 = self.table_representant.horizontalHeaderItem(2)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None));
        ___qtablewidgetitem97 = self.table_representant.horizontalHeaderItem(3)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Num tel", None));
        ___qtablewidgetitem98 = self.table_representant.horizontalHeaderItem(4)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Date de naissance", None));
        ___qtablewidgetitem99 = self.table_representant.horizontalHeaderItem(5)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Nom client", None));
        self.gestion_4.setText(QCoreApplication.translate("MainWindow", u"Gestion des Clients", None))
        self.rechercherClientMenu.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherche d'un client", None))
        self.ajouterClientMenu.setText(QCoreApplication.translate("MainWindow", u"ajouter", None))
        self.modifierClientMenu.setText(QCoreApplication.translate("MainWindow", u"modifier", None))
        self.supprimer.setText(QCoreApplication.translate("MainWindow", u"supprimer", None))
        self.afficheClient_2.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        ___qtablewidgetitem100 = self.tableClienMenu.horizontalHeaderItem(0)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"ID Client", None));
        ___qtablewidgetitem101 = self.tableClienMenu.horizontalHeaderItem(1)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Code postale", None));
        ___qtablewidgetitem102 = self.tableClienMenu.horizontalHeaderItem(2)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem103 = self.tableClienMenu.horizontalHeaderItem(3)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"Statut juridique", None));
        ___qtablewidgetitem104 = self.tableClienMenu.horizontalHeaderItem(4)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem105 = self.tableClienMenu.horizontalHeaderItem(5)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"Observation", None));
        ___qtablewidgetitem106 = self.tableClienMenu.horizontalHeaderItem(6)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"Tel", None));
        ___qtablewidgetitem107 = self.tableClienMenu.horizontalHeaderItem(7)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"N\u00ba RC", None));
        ___qtablewidgetitem108 = self.tableClienMenu.horizontalHeaderItem(8)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"N\u00ba NIF", None));
        ___qtablewidgetitem109 = self.tableClienMenu.horizontalHeaderItem(9)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"N\u00ba SUCCURSALE", None));
        ___qtablewidgetitem110 = self.tableClienMenu.horizontalHeaderItem(10)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"N\u00ba NIS", None));
        ___qtablewidgetitem111 = self.tableClienMenu.horizontalHeaderItem(11)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"N\u00ba article d'imposition", None));
        ___qtablewidgetitem112 = self.tableClienMenu.horizontalHeaderItem(12)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"Date expiration mandat", None));
        ___qtablewidgetitem113 = self.tableClienMenu.horizontalHeaderItem(13)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"Date expiration RC", None));
        ___qtablewidgetitem114 = self.tableClienMenu.horizontalHeaderItem(14)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"N\u00ba MANDAT", None));
        self.gestion_8.setText(QCoreApplication.translate("MainWindow", u"Gestion des Factures", None))
        self.rechercherfacturesMenu.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherche d'une facture", None))
        self.ajouterFacturesMenu.setText(QCoreApplication.translate("MainWindow", u"ajouter", None))
        self.modifierFacturesMenu.setText(QCoreApplication.translate("MainWindow", u"modifier", None))
        self.supprimerFactures.setText(QCoreApplication.translate("MainWindow", u"supprimer", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Imprimer", None))
        self.afficheFactures_2.setText(QCoreApplication.translate("MainWindow", u"Factures", None))
        ___qtablewidgetitem115 = self.tableClienMenu_3.horizontalHeaderItem(0)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"N\u00ba  Facture", None));
        ___qtablewidgetitem116 = self.tableClienMenu_3.horizontalHeaderItem(1)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"ID Dossier", None));
        ___qtablewidgetitem117 = self.tableClienMenu_3.horizontalHeaderItem(2)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem118 = self.tableClienMenu_3.horizontalHeaderItem(3)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"TVA", None));
        ___qtablewidgetitem119 = self.tableClienMenu_3.horizontalHeaderItem(4)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"Total pr\u00e9station", None));
        ___qtablewidgetitem120 = self.tableClienMenu_3.horizontalHeaderItem(5)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"Total debours", None));
        ___qtablewidgetitem121 = self.tableClienMenu_3.horizontalHeaderItem(6)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"Droit de timbre", None));
        ___qtablewidgetitem122 = self.tableClienMenu_3.horizontalHeaderItem(7)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"Etat de paiement", None));
        ___qtablewidgetitem123 = self.tableClienMenu_3.horizontalHeaderItem(8)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"Mode de paiement", None));
        self.gain_annuel_exemple.setText(QCoreApplication.translate("MainWindow", u"Gain Annuel", None))
        self.repartition_dossier_par_pay_exemple.setText(QCoreApplication.translate("MainWindow", u"Repartition des Dossiers par Pays", None))
        self.activite_mensuel_exemple.setText(QCoreApplication.translate("MainWindow", u"Activit\u00e9 Mensuel", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Gain Annuel", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Repartition Dossier par Pay", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Activit\u00e9 mensuel", None))
    # retranslateUi

