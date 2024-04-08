from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder 
import kivy
import sys 
from kivy.uix.image import Image
from kivy.core.image import ImageLoader
ImageLoader.loaders.append(ImageLoader.loaders.pop(ImageLoader.loaders.index(kivy.core.image.img_pil.ImageLoaderPIL )))
from kivy.core.window import Window
# kivyoptionlist=list(kivy.kivy_options['image'])
# kivyoptionlist.append(kivyoptionlist.pop(kivyoptionlist.index('pil')))
# kivy.kivy_options['image']=tuple(kivyoptionlist)
from kivymd.uix.button import MDIconButton
from kivy.clock import Clock
Window.size=(300,580)
from PIL import Image


class LoginPage(MDApp):

    def build(self):
        global screen_manager
        screen_manager=ScreenManager()
        self.root=Builder.load_file("info.kv")
        self.root=Builder.load_file("busisetup.kv")
        screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("otp.kv"))
        screen_manager.add_widget(Builder.load_file("info.kv"))
        screen_manager.add_widget(Builder.load_file("busisetup.kv"))
        screen_manager.add_widget(Builder.load_file("select.kv"))
        screen_manager.add_widget(Builder.load_file("contact.kv"))
        screen_manager.add_widget(Builder.load_file("confirm.kv"))
        
        return screen_manager
    
    def set_text(self):
        screen=screen_manager.get_screen('info')
        name_input=screen.ids.name.text
        screen1=screen_manager.get_screen('busisetup')
        if(name_input!=""):
            screen1.ids.dis.text=name_input

    def on_start(self):
        Clock.schedule_once(self.login,5)

    def login(self,*args):  
        screen_manager.current="login"
    
if __name__=="__main__":
    LoginPage().run()