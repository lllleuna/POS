from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


Window.size = (850, 667)
Window.clearcolor = (1, 1, 1, 1)
Builder.load_file('ui.kv')


class MainWindow(Screen):
    pass
        
class SignupWindow(Screen):
    #Sign Up Page textinput getting the value
    usernew = ObjectProperty()
    namenew = ObjectProperty()
    emailnew = ObjectProperty()
    agenew = ObjectProperty()
    sexnew = ObjectProperty()
    passnew = ObjectProperty()
    conpassnew = ObjectProperty()


class SecondWindow(Screen):
    pass

class ProfileWindow(Screen):
    pass

class BillsWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ScrollViewWindow(Screen):
    pass

class MainWidget(Widget):
    pass

class BurgerKingApp(App):
    def build(self): #Output the content of MainWidget
        return WindowManager()
    
    def check_account(self, user, passw):
        if user.text == "leuna" and passw.text == "123":
            self.root.current = "second"
            user.text = ""
            passw.text = ""

BurgerKingApp().run()
