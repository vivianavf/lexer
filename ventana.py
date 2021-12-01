from ventana_ui import *
from lexer import *
from parser import *

### Interfaz gráfica
## Aporte de: Viviana Vera

### Incluye archivos: untitled.ui, ventana_ui.py, ventana.py
# Ejecutable: ventana.py

# fix bug importar una imagen como fondo de la ventana

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
        self.ui.actionAnalizar.triggered.connect(self.analizarLexico)
        self.ui.actionAnalizarSyntax.triggered.connect(self.analizarSyntax)
        self.ui.actionLimpiar.triggered.connect(self.limpiar)


    # Metodo para importar archivos
    # Solo permite importar .txt
    def importar(self):
        archivo = QFileDialog.getOpenFileName(self, 'importar',  '?\lexer', 'index.txt')
        if archivo[0]:
            with open(archivo[0], 'rt') as f:
                datos = f.read()
                self.ui.codigo_fuente.setText(datos)

    # Otro metodo para importar archivos
    # Permite importar cualquier archivo
    def importar2(self):
        dlg = QFileDialog()
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read().strip()
                if data:
                    self.ui.codigo_fuente.setText(data+'\n')

    # Analiza de manera lexica el texto en consola
    def analizarLexico(self):
        self.ui.consola.setText("")
        self.ui.errores.setText("")
        #Obtener datos que esten en el codigo fuente
        datos = self.ui.codigo_fuente.toPlainText().strip()
        # analisis completo
        resultado_lexico = prueba(datos)
        cadena = ""
        for lex in resultado_lexico:
            cadena += lex+"\n"

        #errores
        resultado_errores = analisiserrores(datos)
        cadena_errores = ""
        for error in resultado_errores:
            cadena_errores+= error+"\n"

        self.ui.consola.setText(cadena)
        self.ui.errores.setText(cadena_errores)


    ## Analiza de manera sintáctica y semántica el texto en consola
    def analizarSyntax(self):
        self.ui.consola.setText("")
        self.ui.errores.setText("")
        # Obtener datos que esten en el codigo fuente
        datos = self.ui.codigo_fuente.toPlainText().strip()
        # analisis completo
        resultado_syntax,resultado_errores = pruebasyntax(datos)
        print("resultado",resultado_syntax,resultado_errores)
        cadena = resultado_syntax
        # errores
        cadena_errores = resultado_errores

        self.ui.consola.setText(cadena)
        self.ui.errores.setText(cadena_errores)

    #Elimina todos los textos en pantalla
    def limpiar(self):
        self.ui.consola.setText("")
        self.ui.codigo_fuente.setText("")
        self.ui.errores.setText("")

if __name__ == "__main__":
    #Instanciar la app
    app = QApplication(sys.argv)
    #Instanciar la ventana principal
    window = MainWindow()
    #Mostrar la ventana
    window.show()
    #Controlar el cierre de la app
    sys.exit(app.exec_())

