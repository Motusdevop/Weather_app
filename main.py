import sys
import desktops
from PyQt5.QtWidgets import QApplication
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_win = desktops.Start()
    start_win.show()
    correct = desktops.Correct()
    sys.exit(app.exec_())