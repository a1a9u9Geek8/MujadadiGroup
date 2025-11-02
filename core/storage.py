from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.conf import settings
import os

class GitHubStorage(Storage):
    def __init__(self):
        self.base_url = 'https://raw.githubusercontent.com/a1a9u9Geek8/MujadadiGroup/main/media/'
    
    def _save(self, name, content):
        # For now, just return the name - files will be manually synced to GitHub
        return name
    
    def delete(self, name):
        pass
    
    def exists(self, name):
        return False
    
    def url(self, name):
        return self.base_url + name
    
    def size(self, name):
        return 0