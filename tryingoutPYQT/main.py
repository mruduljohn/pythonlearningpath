import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSlot

# Create the application
app = QGuiApplication(sys.argv)

# Create the QML engine
engine = QQmlApplicationEngine()

# Load the QML file
engine.load('C:/Users/mrudu/Documents/GitHub/pythonlearningpath/tryingoutPYQT/Course_Success_.ui.qml')

# Check if loading was successful
if not engine.rootObjects():
    sys.exit(-1)
class BackendObject(QObject):
    @pyqtSlot(str)
    def greet(self, name):
        print('Hello,', name)

# Create an instance of the backend object
backend = BackendObject()

# Expose the backend object to QML
engine.rootContext().setContextProperty('backend', backend)

# Run the application
sys.exit(app.exec())
