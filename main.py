from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.behaviors import CircularRippleBehavior,RectangularRippleBehavior,CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty
#from kivymd.uix.label import MDIcon

class CategoryCard(RectangularRippleBehavior,MDFloatLayout,CommonElevationBehavior,ButtonBehavior):
	pass
	
class ProfileButton(CircularRippleBehavior,ButtonBehavior,MDFloatLayout):
	profile_img = StringProperty("/storage/emulated/0/Download/iPortfolio/assets/img/my-profile-img.jpg")


class BadgeIconButton(CircularRippleBehavior,ButtonBehavior,MDFloatLayout):
	badge_icon = StringProperty("numeric-5")
	icon = StringProperty("bell-outline")
	

class BottomBar(MDFloatLayout,FakeRectangularElevationBehavior):
	pass

class SearchBar(MDFloatLayout,FakeRectangularElevationBehavior):
	pass
	
class Mwayi(MDApp):
	def build(self):
		screen_manager = ScreenManager()
		screen_manager.add_widget(Builder.load_file('homepage.kv'))
		return screen_manager

if __name__ == '__main__':
	Mwayi().run()