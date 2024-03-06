import sys
from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from qtpy.QtCore import QTimer
from plyer import notification

class RemainderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.active_timers = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Remainder App')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.setStyleSheet(
            "QWidget {background-color: #87CEFA; border-radius: 10px;}"
            "QLabel {font-size: 14px;}"
            "QLineEdit {font-size: 14px; border: 1px solid black; border-radius: 5px;}"
            "QPushButton {font-size: 14px; padding: 10px; background-color: #1E90FF; color: white; border-radius: 10px;}"
            "QPushButton:hover {background-color: #4682B4;}"
        )

        self.drink_water_label = QLabel('Drink Water (mins):')
        self.drink_water_input = QLineEdit()
        self.drink_water_input.setMaximumWidth(50)
        self.layout.addWidget(self.drink_water_label)
        self.layout.addWidget(self.drink_water_input)

        self.walk_time_label = QLabel('Walk Time (mins):')
        self.walk_time_input = QLineEdit()
        self.walk_time_input.setMaximumWidth(50)
        self.layout.addWidget(self.walk_time_label)
        self.layout.addWidget(self.walk_time_input)

        self.eye_protection_label = QLabel('Eye Break (mins):')
        self.eye_protection_input = QLineEdit()
        self.eye_protection_input.setMaximumWidth(50)
        self.layout.addWidget(self.eye_protection_label)
        self.layout.addWidget(self.eye_protection_input)

        self.start_button = QPushButton('Start Reminders')
        self.start_button.clicked.connect(self.startReminders)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)

    def startReminders(self):
        drink_water_time = int(self.drink_water_input.text()) if self.drink_water_input.text() else 0
        walk_time = int(self.walk_time_input.text()) if self.walk_time_input.text() else 0
        eye_protection_time = int(self.eye_protection_input.text()) if self.eye_protection_input.text() else 0

        if drink_water_time > 0:
            self.setupReminderTimer(drink_water_time, 'Drink Water')
        if walk_time > 0:
            self.setupReminderTimer(walk_time, 'Take a Walk')
        if eye_protection_time > 0:
            self.setupReminderTimer(eye_protection_time, 'Take Eye Break')

    def setupReminderTimer(self, time_interval, reminder):
        timer = QTimer()
        timer.timeout.connect(lambda: self.showReminder(reminder))
        timer.start(time_interval * 1000 * 60)
        self.active_timers.append(timer)

    def showReminder(self, reminder):
        notification.notify(
            title="Reminder",
            message=f"It's time to {reminder}!",
            app_name="Remainder App",
            timeout=10
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RemainderApp()
    window.show()
    sys.exit(app.exec_())
