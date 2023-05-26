import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

# Create the application
app = QGuiApplication(sys.argv)

# Create the QML engine
engine = QQmlApplicationEngine()

# Load the QML file
engine.load('path/to/your/qml/file.qml')

# Check if loading was successful
if not engine.rootObjects():
    sys.exit(-1)

# Run the application
sys.exit(app.exec())
