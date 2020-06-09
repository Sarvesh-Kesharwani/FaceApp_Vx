from kivy.app import App
from kivy.core.clipboard.clipboard_android import PythonActivity
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationLayout
from kivymd.toolbar import Toolbar
from kivy.uix.screenmanager import ScreenManager
from jnius import autoclass
from kivy.utils import platform
import socket
from kivy.uix.button import Button
from kivy.uix.widget import Widget

PythonActivity = autoclass('org.kivy.android.PythonActivity')
activity = PythonActivity.mActivity

Context = autoclass('android.content.Context')
vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)

class Connect(NavigationLayout):
    def __init__(self, **kwargs):
        super(Connect, self).__init__(**kwargs)

    if platform == 'android':
        vibrator.vibrate(100)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.0.10', 1234))
        msg = s.recv(1024)
        print(msg.decode("utf-8"))

    def do_action(self):
        self.lbl.text = 'Button Clicked'  #!(''-'')!


class MainApp(App):
    def build(self):
        return Connect()

if __name__=='__main__':
    MainApp().run()

