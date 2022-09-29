from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


Window.size = (324, 580)


class MyContent(BoxLayout):
    pass


class HomeScreen(Screen):
    pass

class LoginScreen(Screen):
    pass


class RegistrationScreen(Screen):
    pass


class RegistrationScreen2(Screen):
    pass


class ProfileScreen(Screen):
    pass



class Matchify(MDApp):
    def build(self):
        GUI = Builder.load_file("main.kv")
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Orange"
        return GUI



    def change_screen(self, screen_name):
        # Get ScreenManager
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name


# GIT ADD . TO ADDMDExpansionPanelTwoLine
# GIT STATUS TO CHECK
# GIT COMMIT -M "SECOND SAMPLE"
# GIT REMOTE ADD ORIGIN URL
# GIT PUSH -U ORIGIN MASTER

Matchify().run()
