import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4 import QtNetwork
import Tkinter, tkFileDialog


class FlaskThread(QThread):

    def __init__(self,app):
        QThread.__init__(self)
        self.app = app
        self.manager = QtNetwork.QNetworkAccessManager()
        self.manager.finished.connect(self.finished)

    def __del__(self):
        self.wait()


    def run(self):
        self.app.run()

    def download(self, reply):
        self.request = QtNetwork.QNetworkRequest(reply.url())
        self.reply = self.manager.get(self.request)

    def finished(self):

        filename = str(self.reply.url().path()).split('/')[-1]+".png"
        print("filename "+filename)
        root = Tkinter.Tk()
        root.withdraw()

        dirname = tkFileDialog.askdirectory(parent=root, initialdir="/Desktop",
                                            title='You are downloading a file, please select a directory to place the file. Close the window to cancel')
        if dirname.strip() != '':
            dirname = dirname.replace('/', '\\')
            print("dirname "+dirname)
            f = open(dirname + '\\' + filename, 'wb')
            f.write(str(self.reply.readAll()))
            f.close()
        else:
            pass

def main(app):
    th = FlaskThread(app)
    th.start()
    #qt init
    qtapp = QApplication(sys.argv)
    qtapp.aboutToQuit.connect(lambda : th.terminate())
    webview = QWebView()
    webview.setWindowTitle("Dynamic Topic Modelling")
    webview.setWindowIcon(QIcon("icon.png"))
    webview.load(QUrl('http://localhost:5000'))
    webview.resize(1280,768)
    webview.show()
    webview.page().setForwardUnsupportedContent(True)
    webview.page().unsupportedContent.connect(th.download)
    sys.exit(qtapp.exec_())

