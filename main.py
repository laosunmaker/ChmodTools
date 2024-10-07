import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from tools import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Suid.setEnabled(False)
        self.ui.Sgid.setEnabled(False)
        self.ui.Sticky.setEnabled(False)
        self.ui.calcbutton.clicked.connect(self.calculate)
        self.ui.EnableSGT.checkStateChanged.connect(self.enablesgt)
        self.ui.calcbackbutton.clicked.connect(self.calculateback)
    def formatauths(self,r,w,x):
        #格式化权限
        r= int(r)
        w= int(w)
        x= int(x)
        res=str(r*100+w*10+x)#二进制拼接
        return str(int(res, 2))
    def formataback(self,Auth):
        tmp=list('{:03b}'.format(Auth))#格式化权限
        for i in range(0, len(tmp)):
            if tmp[i]=='0':tmp[i]=False
            else:tmp[i]=True
        return tmp
    def calculate(self):
        UserAuth=self.formatauths(self.ui.Ur.isChecked(), self.ui.Uw.isChecked(), self.ui.Ux.isChecked())
        GroupAuth=self.formatauths(self.ui.Gr.isChecked(), self.ui.Gw.isChecked(), self.ui.Gx.isChecked())
        OtherAuth=self.formatauths(self.ui.Or.isChecked(), self.ui.Ow.isChecked(), self.ui.Ox.isChecked())
        if self.ui.EnableSGT.isChecked():
            SgtAuth=self.formatauths(self.ui.Suid.isChecked(), self.ui.Sgid.isChecked(), self.ui.Sticky.isChecked())
            Auth=SgtAuth+UserAuth+GroupAuth+OtherAuth
        else:
            Auth=UserAuth+GroupAuth+OtherAuth#拼接权限
        self.ui.ans.setText(Auth)
    def calculateback(self):
        Auth=self.ui.ans.text()
        Auth=int(Auth)
        
        if self.ui.EnableSGT.isChecked():
            SgtAuth=Auth//1000
            UserAuth=Auth//100%10
            GroupAuth=Auth//10%10
            OtherAuth=Auth%10
        else:
            UserAuth=Auth//100
            GroupAuth=Auth//10%10
            OtherAuth=Auth%10
        UserAuth=self.formataback(UserAuth)
        self.ui.Ur.setChecked(UserAuth[0])
        self.ui.Uw.setChecked(UserAuth[1])
        self.ui.Ux.setChecked(UserAuth[2])
        GroupAuth=self.formataback(GroupAuth)
        self.ui.Gr.setChecked(GroupAuth[0])
        self.ui.Gw.setChecked(GroupAuth[1])
        self.ui.Gx.setChecked(GroupAuth[2])
        OtherAuth=self.formataback(OtherAuth)
        self.ui.Or.setChecked(OtherAuth[0])
        self.ui.Ow.setChecked(OtherAuth[1])
        self.ui.Ox.setChecked(OtherAuth[2])
        if self.ui.EnableSGT.isChecked():
            SgtAuth=self.formataback(SgtAuth)
            self.ui.Suid.setChecked(SgtAuth[0])
            self.ui.Sgid.setChecked(SgtAuth[1])
            self.ui.Sticky.setChecked(SgtAuth[2])
    def enablesgt(self):
        if self.ui.EnableSGT.isChecked():
            self.ui.Suid.setEnabled(True)
            self.ui.Sgid.setEnabled(True)
            self.ui.Sticky.setEnabled(True)
        else:
            self.ui.Suid.setEnabled(False)
            self.ui.Sgid.setEnabled(False)
            self.ui.Sticky.setEnabled(False)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())