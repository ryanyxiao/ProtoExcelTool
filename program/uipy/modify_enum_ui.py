# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../designer/ui/modify_enum.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyEnumForm(object):
    def setupUi(self, ModifyEnumForm):
        ModifyEnumForm.setObjectName("ModifyEnumForm")
        ModifyEnumForm.resize(529, 642)
        self.lEtEnumDesc = QtWidgets.QLineEdit(ModifyEnumForm)
        self.lEtEnumDesc.setGeometry(QtCore.QRect(80, 50, 431, 20))
        self.lEtEnumDesc.setObjectName("lEtEnumDesc")
        self.cBxEnum = QtWidgets.QCheckBox(ModifyEnumForm)
        self.cBxEnum.setGeometry(QtCore.QRect(80, 610, 121, 16))
        self.cBxEnum.setObjectName("cBxEnum")
        self.label_7 = QtWidgets.QLabel(ModifyEnumForm)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label_7.setObjectName("label_7")
        self.lEtEnumName = QtWidgets.QLineEdit(ModifyEnumForm)
        self.lEtEnumName.setGeometry(QtCore.QRect(80, 10, 431, 20))
        self.lEtEnumName.setObjectName("lEtEnumName")
        self.label_8 = QtWidgets.QLabel(ModifyEnumForm)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(ModifyEnumForm)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 71, 21))
        self.label_10.setObjectName("label_10")
        self.bTnEnumModify = QtWidgets.QPushButton(ModifyEnumForm)
        self.bTnEnumModify.setGeometry(QtCore.QRect(280, 610, 75, 23))
        self.bTnEnumModify.setObjectName("bTnEnumModify")
        self.tBvEnum = QtWidgets.QTableWidget(ModifyEnumForm)
        self.tBvEnum.setGeometry(QtCore.QRect(80, 90, 431, 491))
        self.tBvEnum.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tBvEnum.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tBvEnum.setColumnCount(3)
        self.tBvEnum.setObjectName("tBvEnum")
        self.tBvEnum.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tBvEnum.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tBvEnum.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tBvEnum.setHorizontalHeaderItem(2, item)
        self.tBvEnum.verticalHeader().setDefaultSectionSize(35)
        self.tBvEnum.verticalHeader().setMinimumSectionSize(30)
        self.tBvEnum.verticalHeader().setSortIndicatorShown(False)
        self.tBvEnum.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(ModifyEnumForm)
        QtCore.QMetaObject.connectSlotsByName(ModifyEnumForm)

    def retranslateUi(self, ModifyEnumForm):
        _translate = QtCore.QCoreApplication.translate
        ModifyEnumForm.setWindowTitle(_translate("ModifyEnumForm", "修改枚举"))
        self.cBxEnum.setText(_translate("ModifyEnumForm", "仅导出服务器"))
        self.label_7.setText(_translate("ModifyEnumForm", "枚举名称："))
        self.label_8.setText(_translate("ModifyEnumForm", "枚举说明："))
        self.label_10.setText(_translate("ModifyEnumForm", "枚举字段："))
        self.bTnEnumModify.setText(_translate("ModifyEnumForm", "修改"))
        item = self.tBvEnum.horizontalHeaderItem(0)
        item.setText(_translate("ModifyEnumForm", "索引"))
        item = self.tBvEnum.horizontalHeaderItem(1)
        item.setText(_translate("ModifyEnumForm", "名称"))
        item = self.tBvEnum.horizontalHeaderItem(2)
        item.setText(_translate("ModifyEnumForm", "说明"))

