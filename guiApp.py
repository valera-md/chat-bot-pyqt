#guiApp.py
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QComboBox
from PyQt6.QtGui import QImage, QPixmap
from PIL import ImageQt
# costumizing UI: XML (python, qt creator/designer, css ...)

from bot import *
#    .withModel("dall-e-2")\
#    .withUrl("/v1/images/generations")\
#    .withModel("gpt-3.5-turbo")\
#    .withUrl("/v1/chat/completions")\
#    .build()

#print(openBot.replyTo("How many parameters do you use as a midel ?"))
#print(openBot.replyTo("Draw a red dog"))

def save_image():
 save_image = ImageQt.fromqpixmap(imageLabel.pixmap())
 save_image.save('test.jpg')

def onButtonClick():
 botBuilder = BotBuilder("openai", "John")\
    .withKey("api-key")\
 #print("button clicked")
 #print(edit.text())
 
 match combo.currentText():
  case 'Image':
   openBot = botBuilder.withModel("dall-e-2")\
           .withUrl("/v1/images/generations")\
           .build()
   reply, replyType = openBot.replyTo(edit.text())
   imageData = requests.get(reply).content
   image = QImage()
   image.loadFromData(imageData)
   pixmap = QPixmap(image)
   pixmap = pixmap.scaledToWidth(400)
   pixmap = pixmap.scaledToHeight(400)
   imageLabel.setPixmap(QPixmap(pixmap))
   imageLabel.show()
   print("done")
   save_image_button = QPushButton("save image", parent = window)
   save_image_button.move(50, 670)
   save_image_button.clicked.connect(save_image)
   save_image_button.show ()
   #print(reply)
   # hm3* complete the TOM diagram
   # hm4* add a push button, make it so if the user clicks the button the app saves the image in the current folder
  case 'Chat':
  # hm1: display the text answer
#hm2: try to use css: color, backgroung, font-size, padding, margin, border, text-align, ...
   openBot = botBuilder.withModel("gpt-3.5-turbo")\
           .withUrl("/v1/chat/completions")\
           .build()
   reply, replyType = openBot.replyTo(edit.text())
   textData = requests.get(reply).content
   imageLabel.setText(textData)
 
# 1. create the application object
app = QApplication([]) # приложение ждёт аргументов от выполняемой среды
width = app.screens()[0].size().width()
height = app.screens()[0].size().height()
# 2. create the main window
window = QWidget()
window.setWindowTitle("Welcome to GUI Chat Bot App")
window.setGeometry(int(width/2) - 250, int(height/2) - 350, 500, 700)
#window.setGeometry(200, 200, 500, 700)
window.setStyleSheet(
 "background: lightblue;"
)
combo = QComboBox(parent = window)
combo.addItem('Chat')
combo.addItem('Image')
combo.move(50, 50)
# 3. create a text label
label = QLabel("Ask anything ...", parent = window)
label.move(50, 100)
#label2 = QLabel("Another label", parent = window)
edit = QLineEdit(parent = window)
edit.setGeometry(50, 150, 300, 50)
button = QPushButton("ASK", parent = window)
button.move(50, 200)
button.clicked.connect(onButtonClick)
imageLabel = QLabel("result", parent = window)
imageLabel.setGeometry(50, 250, 400, 400)
imageLabel.setStyleSheet(
 "border: 1px solid white;"
)
window.show()
sys.exit(app.exec())