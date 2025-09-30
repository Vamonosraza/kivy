from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
import requests
import json
from config import UNSPLASH_ACCESS_KEY, LOCATION_QUERIES

class PhotoLocationApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        
        # UI Elements
        self.location_label = Label(text='Location: Not detected', size_hint_y=0.1)
        self.add_widget(self.location_label)
        
        self.image_widget = AsyncImage(size_hint_y=0.7)
        self.add_widget(self.image_widget)
        
        self.get_photo_btn = Button(text='Get Random Photo', size_hint_y=0.1)
        self.get_photo_btn.bind(on_press=self.get_location_photo)
        self.add_widget(self.get_photo_btn)
        
        self.status_label = Label(text='Ready', size_hint_y=0.1)
        self.add_widget(self.status_label)
    
    def get_location_photo(self, instance):
        self.status_label.text = 'Getting location...'
        # For now, we'll use a default location (GPS implementation next)
        self.get_photo_from_unsplash("nature")
    
    def get_photo_from_unsplash(self, query="landscape"):
        try:
            url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
            
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                photo_url = data['urls']['regular']
                self.image_widget.source = photo_url
                self.status_label.text = f'Photo loaded: {query}'
            else:
                self.status_label.text = 'Failed to load photo'
        except Exception as e:
            self.status_label.text = f'Error: {str(e)}'

class PhotoLocationAppMain(App):
    def build(self):
        return PhotoLocationApp()

if __name__ == '__main__':
    PhotoLocationAppMain().run()