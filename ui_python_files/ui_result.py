from PyQt5.QtWidgets import QApplication, QDialog, QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QVBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PyQt5.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform


class Ui_Dialog(QDialog):

    def __init__(self):

        super().__init__()

        self.resize(490, 225)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(
            """
            *{
                background: #381e0d;
                border: none;
            }
            """
        )

        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.frame)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMaximumSize(QSize(16777215, 35))
        self.titleBar.setFrameShape(QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleBar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.titleBar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.labelTitle = QLabel(self.frame_4)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(
            """
            *{
                color: white;
                font-size: 18px;
            }
            """
        )

        self.horizontalLayout_4.addWidget(self.labelTitle)
        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.titleBar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(35, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.exitButton = QPushButton(self.frame_5)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setMaximumSize(QSize(15, 15))
        self.exitButton.setStyleSheet(
            """
            *{
                background: rgb(255, 55, 55);
                border: none;
                border-radius: 7px;
            }
            """
        )

        self.horizontalLayout_3.addWidget(self.exitButton)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.titleBar)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelHash = QLabel(self.frame_3)
        self.labelHash.setObjectName(u"labelHash")
        self.labelHash.setStyleSheet(
            """
            *{
                color: white;
                font-size: 22px;
            }
            """
        )

        self.labelHash.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.labelHash)

        self.labelResult = QLabel(self.frame_3)
        self.labelResult.setObjectName(u"labelResult")
        self.labelResult.setStyleSheet(
            """
            *{
                color: white;
                font-size: 22px;
            }
            """
        )

        self.labelResult.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.labelResult)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(200, 35))
        self.pushButton.setStyleSheet(
            """
            *{
                background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 51, 51, 255), stop:1 rgba(255, 131, 51, 255));
                color: white;
                border-radius: 17px;
            }
            """
        )

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(35)
        self.shadow.setColor(Qt.red)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.pushButton.setGraphicsEffect(self.shadow)

        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        self.exitButton.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.close)
