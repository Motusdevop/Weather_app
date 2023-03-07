import sys
import desktops
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('source/app.ico'))
    app.setApplicationDisplayName("Your Weather")
    start_win = desktops.Start()
    sys.exit(app.exec_())