# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Proyecto1(object):
    def setupUi(self, Proyecto1):
        Proyecto1.setObjectName("Proyecto1")
        Proyecto1.resize(702, 410)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        Proyecto1.setFont(font)
        Proyecto1.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Proyecto1)
        self.centralwidget.setObjectName("centralwidget")
        self.lblSaludo = QtWidgets.QLabel(self.centralwidget)
        self.lblSaludo.setGeometry(QtCore.QRect(480, 130, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.lblSaludo.setFont(font)
        self.lblSaludo.setText("")
        self.lblSaludo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblSaludo.setObjectName("lblSaludo")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(540, 300, 131, 51))
        self.btnAceptar.setObjectName("btnAceptar")
        self.lblTitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitulo.setGeometry(QtCore.QRect(250, 60, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setObjectName("lblTitulo")
        self.lblDNI = QtWidgets.QLabel(self.centralwidget)
        self.lblDNI.setGeometry(QtCore.QRect(70, 140, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblDNI.setFont(font)
        self.lblDNI.setObjectName("lblDNI")
        self.lblApellidos = QtWidgets.QLabel(self.centralwidget)
        self.lblApellidos.setGeometry(QtCore.QRect(70, 170, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblApellidos.setFont(font)
        self.lblApellidos.setObjectName("lblApellidos")
        self.lblNombre = QtWidgets.QLabel(self.centralwidget)
        self.lblNombre.setGeometry(QtCore.QRect(410, 170, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.btnAceptar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar_2.setGeometry(QtCore.QRect(230, 260, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.btnAceptar_2.setFont(font)
        self.btnAceptar_2.setObjectName("btnAceptar_2")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(350, 260, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.btnSalir.setFont(font)
        self.btnSalir.setObjectName("btnSalir")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 100, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(70, 230, 611, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.ltApellidos = QtWidgets.QLineEdit(self.centralwidget)
        self.ltApellidos.setGeometry(QtCore.QRect(190, 170, 191, 20))
        self.ltApellidos.setObjectName("ltApellidos")
        self.ltDNI = QtWidgets.QLineEdit(self.centralwidget)
        self.ltDNI.setGeometry(QtCore.QRect(190, 130, 191, 20))
        self.ltDNI.setTabletTracking(False)
        self.ltDNI.setObjectName("ltDNI")
        self.ltNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.ltNombre.setGeometry(QtCore.QRect(490, 170, 191, 20))
        self.ltNombre.setObjectName("ltNombre")
        Proyecto1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Proyecto1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 27))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(14)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.menuArchivo.setFont(font)
        self.menuArchivo.setObjectName("menuArchivo")
        Proyecto1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Proyecto1)
        self.statusbar.setObjectName("statusbar")
        Proyecto1.setStatusBar(self.statusbar)
        self.actionSalir_2 = QtWidgets.QAction(Proyecto1)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.actionSalir_2.setFont(font)
        self.actionSalir_2.setObjectName("actionSalir_2")
        self.menuArchivo.addAction(self.actionSalir_2)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(Proyecto1)
        QtCore.QMetaObject.connectSlotsByName(Proyecto1)

    def retranslateUi(self, Proyecto1):
        _translate = QtCore.QCoreApplication.translate
        Proyecto1.setWindowTitle(_translate("Proyecto1", "Pinche ventana"))
        self.btnAceptar.setText(_translate("Proyecto1", "Boton"))
        self.lblTitulo.setText(_translate("Proyecto1", "XESTIÓN CLIENTES"))
        self.lblDNI.setText(_translate("Proyecto1", "DNI"))
        self.lblApellidos.setText(_translate("Proyecto1", "Apellidos"))
        self.lblNombre.setText(_translate("Proyecto1", "Nombre"))
        self.btnAceptar_2.setText(_translate("Proyecto1", "Aceptar"))
        self.btnSalir.setText(_translate("Proyecto1", "Salir"))
        self.menuArchivo.setTitle(_translate("Proyecto1", "Archivo"))
        self.actionSalir_2.setText(_translate("Proyecto1", "Salir"))
        self.actionSalir_2.setShortcut(_translate("Proyecto1", "Ctrl+S"))