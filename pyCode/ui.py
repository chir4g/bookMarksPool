from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QTextEdit,QVBoxLayout,QGridLayout,QPushButton,QLineEdit,QSizePolicy,QScrollArea,QMessageBox,QHBoxLayout
from PyQt5.QtGui import QIcon,QImage,QPixmap
from PyQt5.QtCore import Qt
import sys

from base import insert,fetch

class markCreationBox(QWidget):
 
    def __init__(self):
        super(markCreationBox,self).__init__()
        self.title = 'Book Mark Pool'
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.Layout = markCreationWidgetLayout()
        self.setLayout(self.Layout.markLayout)
        self.setGeometry(150,150,800,200)
        self.show()


class markCreationWidgetLayout(QWidget):
    def __init__(self,parent=None):
        super(markCreationWidgetLayout,self).__init__()
        
        #Elements Present on Note Creation GUI
        self.name = QLabel('Name')
        self.nameEdit = QLineEdit()
        self.link = QLabel('Link')
        self.linkEdit = QLineEdit()
        self.saveButton = QPushButton("Save")
        self.saveButton.clicked.connect(self.createNewMark)
        self.marksList = QPushButton("List")
        self.marksList.clicked.connect(self.createMarksList)

        #Main Layout
        self.markLayout = QGridLayout()

        #<<<--------------TAG LAYOUT----------------------->>>
        self.tagLayout = QHBoxLayout()
        self.tag1 = QLineEdit()
        self.tag1.setPlaceholderText("Tag 1")
        self.tag2 = QLineEdit()
        self.tag2.setPlaceholderText("Tag 2")
        self.tag3 = QLineEdit()
        self.tag3.setPlaceholderText("Tag 3")
        
        self.tagLayout.addWidget(self.tag1)
        self.tagLayout.addWidget(self.tag2)
        self.tagLayout.addWidget(self.tag3)
        #<<<----------------------------------------------->>>

        #Position of Widgets/Elements on Main Layout
        self.markLayout.addWidget(self.name, 1, 0)
        self.markLayout.addWidget(self.nameEdit, 1, 1)

        self.markLayout.addWidget(self.link, 2, 0)
        self.markLayout.addWidget(self.linkEdit, 2, 1)
        
        self.markLayout.setRowStretch(2,2)
        self.markLayout.addWidget(self.saveButton,3,0)
        self.markLayout.addWidget(self.marksList,4,0)

        self.markLayout.addLayout(self.tagLayout,3,1)


    def createNewMark(self):

        result = insert(self.nameEdit.text(),self.linkEdit.text(),self.tag1.text(), self.tag2.text(),self.tag3.text())

        if result == 'Successful':
            QMessageBox.about(self, "Successful","BookMark Created")
        else:
            QMessageBox.about(self,"Warning",result)

    
    def createMarksList(self):
        self.content = fetch()
        print(self.content)
        self.noteWindow = markShowBox(self.content)
        self.noteWindow.show()


class markShowBox(QWidget):
    """Class to display already created notes in a window"""

    def __init__(self,content):
        super(markShowBox,self).__init__()
        self.title = 'Created Notes'
        self.markContents = content
        self.initUI()
        
    def initUI(self):
        self.mainLayout = QVBoxLayout()
        self.setWindowTitle(self.title)
        self.setGeometry(150,150,800,400)

        self.marks = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setSpacing(5.0)

        #List Generation of all the marks
        for key,value in self.markContents.items():
            self.marktile = markTile(key,value)
            self.scroll_layout.addLayout(self.marktile.markTileLayout)


        self.marks.setWidget(self.scroll_widget)
        self.mainLayout.addWidget(self.marks)
        self.setLayout(self.mainLayout)
        self.show()
    


class markTile(QWidget):
    def __init__(self,creator,values):
        super(markTile,self).__init__()
        self.creator = QLabel('<b>%s</b>'%creator)
        self.tag1 = QLabel('<b>%s</b>'%values['tag1'])
        self.tag2 = QLabel('<b>%s</b>'%values['tag2'])
        self.tag3 = QLabel('<b>%s</b>'%values['tag3'])
        self.link = QLabel(values['link'])

        self.firstLine = QHBoxLayout()
        self.noteTileLayout = QVBoxLayout()

        self.firstLine.addWidget(self.creator)
        self.firstLine.addWidget(self.tag1)
        self.firstLine.addWidget(self.tag2)
        self.firstLine.addWidget(self.tag3)
        self.noteTileLayout.addLayout(self.firstLine)

        self.noteTileLayout.addWidget(self.link)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = markCreationBox()
    sys.exit(app.exec_())