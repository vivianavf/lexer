from ventana_ui import *
from lexer import *
from parser import *

import sys
from PyQt5.QtWidgets import QAction, QApplication, QFileDialog, QMainWindow

class MainWindow(QMainWindow):

    ## Clase principal de la app
    def __init__(self, *args, **kwargs):

        #Inicializamos
        super().__init__()
        #QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        #Instanciar ventanas
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Conectar las acciones con las funciones definidas
        self.ui.actionImportar.triggered.connect(self.importar2)
        self.ui.actionAnalizar.triggered.connect(self.analizar)

    # Metodo para importar archivos
    def importar(self):
        archivo = QFileDialog.getOpenFileName(self, 'importar',  '?\lexer', 'index.txt')
        if archivo[0]:
            with open(archivo[0], 'rt') as f:
                datos = f.read()
                self.ui.texto.setText(datos)

    # Otro metodo para importar archivos
    def importar2(self):
        dlg = QFileDialog()
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read().strip()
                if data:
                    self.ui.texto.setText(data+'\n')


    def analizar(self):
        self.ui.consola.setText('a')

if __name__ == "__main__":
    #Instanciar la app
    app = QApplication(sys.argv)
    #Instanciar la ventana principal
    window = MainWindow()
    #Mostrar la ventana
    window.show()
    #Controlar el cierre de la app
    sys.exit(app.exec_())

