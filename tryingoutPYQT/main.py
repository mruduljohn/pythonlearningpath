import sys
from PyQt5.QtCore import QObject,QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView


if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = QQuickView()
    view.setSource(QUrl.fromLocalFile('Screen01.ui.qml'))
    view.show()

    sys.exit(app.exec())
