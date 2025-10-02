from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
import requests
import json
import random
import time
from config import UNSPLASH_ACCESS_KEY, LOCATION_QUERIES

class PhotoLocationApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        self.used_photo_ids = set()  # Track used photos
        self.retry_count = 0  # Track retries for debugging
        
        # UI Elements
        self.location_label = Label(text='Location: Not detected', size_hint_y=0.1)
        self.add_widget(self.location_label)
        
        self.image_widget = AsyncImage(size_hint_y=0.7, allow_stretch=True, keep_ratio=True)
        self.add_widget(self.image_widget)
        
        self.get_photo_btn = Button(text='Get Random Photo', size_hint_y=0.1)
        self.get_photo_btn.bind(on_press=self.get_location_photo)
        self.add_widget(self.get_photo_btn)
        
        self.status_label = Label(text='Ready', size_hint_y=0.1)
        self.add_widget(self.status_label)
    
    def get_location_photo(self, instance):
        self.status_label.text = 'Getting photo...'
        self.get_photo_btn.disabled = True
        self.retry_count = 0  # Reset retry count
        
        # Get random category and query
        category = random.choice(list(LOCATION_QUERIES.keys()))
        queries = LOCATION_QUERIES.get(category, ["landscape"])
        random_query = random.choice(queries)
        
        print(f"Selected category: {category}, query: {random_query}")
        self.get_photo_from_unsplash(random_query)
    
    def get_photo_from_unsplash(self, query="landscape"):
        try:
            # Add more randomization parameters
            timestamp = int(time.time() * 1000)  # Use milliseconds for more randomness
            random_page = random.randint(1, 100)  # Random page number
            
            url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}&t={timestamp}&page={random_page}"
            
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                photo_id = data.get('id')
                
                print(f"Got photo ID: {photo_id}, Used IDs: {len(self.used_photo_ids)}")
                
                # Check if we've seen this photo before
                if photo_id in self.used_photo_ids and self.retry_count < 3:
                    print(f"Duplicate photo detected, retrying... (attempt {self.retry_count + 1})")
                    self.retry_count += 1
                    
                    # Try a completely different category and query
                    all_queries = []
                    for category_queries in LOCATION_QUERIES.values():
                        all_queries.extend(category_queries)
                    new_query = random.choice(all_queries)
                    
                    # Add small delay to avoid rate limiting
                    Clock.schedule_once(lambda dt: self.get_photo_from_unsplash(new_query), 0.5)
                    return
                
                # Add to used photos
                self.used_photo_ids.add(photo_id)
                
                photo_url = data['urls']['regular']
                
                # Clear previous image and load new one
                self.image_widget.source = ''
                Clock.schedule_once(lambda dt: self.load_new_image(photo_url), 0.1)
                
                # Update status with photo info
                photographer = data.get('user', {}).get('name', 'Unknown')
                self.status_label.text = f'Photo by {photographer} ({query})'
                print(f"Loaded photo by {photographer}")
            else:
                self.status_label.text = f'API Error: {response.status_code}'
        except Exception as e:
            self.status_label.text = f'Error: {str(e)}'
            print(f"Error: {e}")
        finally:
            # Re-enable button
            self.get_photo_btn.disabled = False
    
    def load_new_image(self, photo_url):
        """Load new image with proper refresh"""
        self.image_widget.source = photo_url
        self.image_widget.reload()

class PhotoLocationAppMain(App):
    def build(self):
        return PhotoLocationApp()

if __name__ == '__main__':
    PhotoLocationAppMain().run()