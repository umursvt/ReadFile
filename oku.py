import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog

class ExcelReaderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Excel Dosyası Adını Oku")
        self.setGeometry(100, 100, 400, 200)

        self.initUI()

    def initUI(self):
        self.select_button = QPushButton("Excel Dosyası Seç", self)
        self.select_button.setGeometry(50, 50, 150, 30)
        self.select_button.clicked.connect(self.select_excel_file)

        self.file_name_label = QLabel("", self)
        self.file_name_label.setGeometry(50, 100, 300, 30)

    def select_excel_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_path, _ = QFileDialog.getOpenFileName(self, "Excel Dosyası Seç", "", "Excel Dosyaları (*.xlsx);;Tüm Dosyalar (*)", options=options)
        
        if file_path:
            file_name = os.path.basename(file_path)
            self.file_name_label.setText(f"Seçilen Excel Dosyası: {file_name}")
        else:
            self.file_name_label.setText("Excel dosyası seçilmedi.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    excel_app = ExcelReaderApp()
    excel_app.show()
    sys.exit(app.exec_())
