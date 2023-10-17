#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QFileDialog, QMessageBox
import os
from PIL import Image, ImageFilter


class ImageProcessor():

    def __init__(self):
        self.image = None
        self.filename = None
        self.changed = 'changed/'

    def LoadImage(self, filename):
        self.filename = filename
        path = os.path.join(workdir, self.filename)
        self.image =  Image.open(path)

    def showImage(self, path):
        image.hide()
        pixmapimage = QPixmap(path)
        w, h = image.width(), image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        image.setPixmap(pixmapimage)
        image.show()

    def do_bw(self):
        print('Объект image', self.image)
        self.image = self.image.convert("L")
        self.saveImage()
        path = os.path.join(workdir, self.changed, self.filename)
        self.showImage(path)

    def mirrow(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        path = os.path.join(workdir, self.changed, self.filename)
        self.showImage(path)

    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        path = os.path.join(workdir, self.changed, self.filename)
        self.showImage(path)

    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        path = os.path.join(workdir, self.changed, self.filename)
        self.showImage(path)

    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        path = os.path.join(workdir, self.changed, self.filename)
        self.showImage(path)

    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        path = os.path.join(workdir, self.changed, self.filename)
        self.showImage(path)

    def emboss(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        self.saveImage()
        path = os.path.join(workdir, self.changed, self.filename)
        self.showImage(path)

    def smooth(self):
        self.image = self.image.filter(ImageFilter.SMOOTH)
        self.saveImage()
        path = os.path.join(workdir, self.changed, self.filename)
        self.showImage(path)

    def edge_enhance(self):
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.saveImage()
        path = os.path.join(workdir, self.changed, self.filename)
        self.showImage(path)

    def contour(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.saveImage()
        path = os.path.join(workdir, self.changed, self.filename)
        self.showImage(path)

    def saveImage(self):
        path = os.path.join(workdir, self.changed)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

app = QApplication([])
main_win = QWidget()
main_win.resize(900, 600)
# workdir = QFileDialog.getExistingDirectory()

# print(os.listdir(workdir))
main_win.setWindowTitle('Easy Editor')
left_btn = QPushButton('Лево')
right_btn = QPushButton('Право')
mirrow_btn = QPushButton('Зеркало')
sharpen_btn = QPushButton('Резкость')
blur_btn = QPushButton('Размытие')
emboss_btn = QPushButton('Рельеф')
smooth_btn = QPushButton('Гладкость')
edge_enhance_btn = QPushButton('Улучшение краёв')
contour_btn = QPushButton('Контур')
b_w = QPushButton('Ч/Б')
file_button = QPushButton('Папка')
list_images = QListWidget()
image = QLabel('')
layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()
layout_4 = QHBoxLayout()
layout_5 = QHBoxLayout()
layout_5.addWidget(blur_btn)
layout_5.addWidget(emboss_btn)
layout_5.addWidget(smooth_btn)
layout_5.addWidget(edge_enhance_btn)
layout_5.addWidget(contour_btn)
layout_3.addLayout(layout_5)
layout_3.addWidget(image)
layout_4.addWidget(left_btn)
layout_4.addWidget(right_btn)
layout_4.addWidget(mirrow_btn)
layout_4.addWidget(sharpen_btn)
layout_4.addWidget(b_w)
layout_3.addLayout(layout_4)
layout_2.addWidget(file_button)
layout_2.addWidget(list_images)
layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)
main_win.setLayout(layout_1)
workdir = ''
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    try:
        list_files = os.listdir(workdir)
        return list_files
    except FileNotFoundError:
        QMessageBox.critical(main_win, 'Предупреждение', 'Выберете папку с изображениями')

def filter(files, extensions):
    result = []
    for file_ in files:
        for ext in extensions:
            if file_.endswith(ext):
                result.append(file_)
    return result

def showFilenameList():
    list_files = chooseWorkdir()
    if not(list_files is None):
        extensions = ['jpg', 'png', 'bmp', 'svg', 'eps', 'jpeg']
        result = filter(list_files, extensions)
        list_images.clear()
        for result_ in result:
            list_images.addItem(result_)

def showChooseImage():
    if list_images.currentRow() >= 0:
        filename = list_images.currentItem().text()
        workimage.LoadImage(filename)
        path = os.path.join(workdir, filename)
        workimage.showImage(path)

workimage = ImageProcessor()
blur_btn.clicked.connect(workimage.blur)
emboss_btn.clicked.connect(workimage.emboss)
edge_enhance_btn.clicked.connect(workimage.edge_enhance)
sharpen_btn.clicked.connect(workimage.sharpen)
contour_btn.clicked.connect(workimage.contour)
sharpen_btn.clicked.connect(workimage.sharpen)
right_btn.clicked.connect(workimage.right)
left_btn.clicked.connect(workimage.left)
mirrow_btn.clicked.connect(workimage.mirrow)
b_w.clicked.connect(workimage.do_bw)
list_images.currentRowChanged.connect(showChooseImage)
file_button.clicked.connect(showFilenameList)
main_win.show()
app.exec_()