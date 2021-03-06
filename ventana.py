from ventana_ui import *
from parser import *
from lexer import *
import threading
import time
#from segunda import *
### Interfaz gráfica
## Aporte de: Viviana Vera

### Incluye archivos: untitled.ui, ventana_ui.py, ventana.py
# Ejecutable: ventana.py

# TODO: fix bug poner una imagen como fondo de la ventana

import sys
from PyQt5.QtWidgets import QAction, QApplication, QFileDialog, QMainWindow

#qtCreatorFile = "cargando.ui"
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MainWindow(QMainWindow):
    ## Clase principal de la app
    def __init__(self, *args, **kwargs):
        # Inicializamos
        super().__init__()
        # QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        # Instanciar ventanas
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Cambiar el nombre de la ventana
        self.setWindowTitle("Analizar Léxico-Sintáctico-Semántico")

        # Conectar las acciones con las funciones definidas
        self.ui.actionImportar.triggered.connect(self.importar2)

        #mostrar progress bar
        #self.ui.actionAnalizar.triggered.connect(self.abrir)
        #mostrar el resultado
        self.ui.actionAnalizar.triggered.connect(self.analizarLexico)

        #mostrar PB
        #self.ui.actionAnalizarSyntax.triggered.connect(self.showPB)
        #mostrar el resultado
        self.ui.actionAnalizarSyntax.triggered.connect(self.analizarSyntax)

        #limpiar
        self.ui.actionLimpiar.triggered.connect(self.limpiar)
        #sacar la barra de progreso
        #self.ui.actionLimpiar.triggered.connect(self.hidePB)

        self.ui.progressBar.setValue(0)
        self.ui.progressBar.hide()

        # Cuadros de textos no editables
        self.ui.errores.setReadOnly(True)
        self.ui.resultado.setReadOnly(True)

    def abrir(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ventana()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def showPB(self):
        self.ui.progressBar.show()
        x = 0
        while x<=100:
            x+=0.1
            self.ui.progressBar.setValue(x)


    def hidePB(self):
        self.ui.progressBar.hide()
        self.ui.progressBar.setValue(0)

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
                    self.ui.codigo_fuente.setText(data + '\n')

    # Elimina todos los textos en pantalla
    def limpiar(self):
        self.ui.resultado.setText("")
        self.ui.codigo_fuente.setText("")

    # Analiza de manera lexica el texto en consola
    def analizarLexico(self):
        self.ui.resultado.setText("")
        self.ui.errores.setText("")
        # Obtener datos que esten en el codigo fuente
        datos = self.ui.codigo_fuente.toPlainText().strip()

        # analisis completo
        resultado_lexico = prueba(datos)
        cadena = ""
        for lex in resultado_lexico:
            cadena += lex + "\n"

        # errores
        resultado_errores = analisiserrores()
        cadena_errores = ""
        for error in resultado_errores:
            cadena_errores += error + "\n"
        if cadena_errores == "":
            cadena_errores += "NO HAY ERRORES ☺"
        self.ui.resultado.setText(cadena)
        self.ui.errores.setText(cadena_errores)

    ## Analiza de manera sintáctica y semántica el texto en consola
    def analizarSyntax(self):
        self.ui.resultado.setText("")
        self.ui.errores.setText("")
        # Obtener datos que esten en el codigo fuente
        datos = self.ui.codigo_fuente.toPlainText().strip()
        # resultados
        # Aqui va el codigo de los resultados y errores
        # variable resultado = un string con los resultados del parser
        # variable cadena_errores = un string con los errores del parser
        # si se hace una lista se la recorre y concatena a una cadena

        resultado = "\n".join(pruebasyntax(datos))  # aqui va la funcion pruebasyntax(datos)
        cadena_errores = "\n".join(errorsyntax())  # aqui va la funcion errorsyntax()

        self.ui.resultado.setText(resultado)
        self.ui.errores.setText(cadena_errores)

# class Proceso(threading.Thread):
#     contador = 0
#
#     def __init__(self, dialogo):
#         threading.Thread.__init__(self)
#         self.dialogo = dialogo
#         self.contador = 0
#
#     def run(self):
#         while self.contador<= 100:
#             time.sleep(1)
#             #time.sleep(1)  #Que espere 1 segundo
#             self.dialogo.ui.progressBar.setValue(self.contador)
#             self.contador+=10


if __name__ == "__main__":
    # Instanciar la app
    app = QApplication(sys.argv)
    # Instanciar la ventana principal
    window = MainWindow()
    # Mostrar la ventana
    window.show()
    # Controlar el cierre de la app
    sys.exit(app.exec_())
