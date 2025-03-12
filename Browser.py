import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QLineEdit, QAction, 
    QVBoxLayout, QListWidget, QWidget
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setWindowTitle("Browser dengan Bookmark")

        screen = QApplication.primaryScreen().availableGeometry()
        width, height = screen.width()-100, screen.height()-100
        # Set ukuran jendela yang lebih kecil (contoh: 1024x768)
        self.resize(width, height)

        # Dapatkan ukuran layar dan pusatkan jendela
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

        # Navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        add_bookmark_btn = QAction('➕ Bookmark', self)
        add_bookmark_btn.triggered.connect(self.add_bookmark)
        navbar.addAction(add_bookmark_btn)

        self.browser.urlChanged.connect(self.update_url)

        # Bookmark Area
        self.bookmark_list = QListWidget()
        self.bookmark_list.itemClicked.connect(self.navigate_to_bookmark)

        # Layout untuk Bookmark di bawah Browser
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.bookmark_list)

        # Atur proporsi: browser (besar) - bookmark (kecil)
        layout.setStretch(0, 9)  # Browser mengambil 8 bagian
        layout.setStretch(1, 1)  # Bookmark mengambil 2 bagian

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text().strip()
        if not url.startswith("http"):
            if "." in url:
                url = "http://" + url
            else:
                url = "https://www.google.com/search?q=" + url.replace(" ", "+")
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString().replace("http://", "").replace("https://", ""))

    def add_bookmark(self):
        current_url = self.browser.url().toString()
        self.bookmark_list.addItem(current_url)

    def navigate_to_bookmark(self, item):
        url = item.text()
        self.browser.setUrl(QUrl(url))

app = QApplication(sys.argv)
QApplication.setApplicationName("My Browser with Bookmark")
window = MainWindow()
window.show()  # Gunakan .show() untuk mengatur ukuran custom tanpa maximize
app.exec_()
