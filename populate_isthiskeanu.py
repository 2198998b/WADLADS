import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isthiskeanureeves_project.settings')

import django
django.setup()
from isthiskeanureeves.models import Category, Page, UserProfile, User

def populate():
    keanothim = [{"title": "Not Keanu","user": 1,"rating": -50,"image": "notkeanu.jpg" }]
    keanew = [{"title": "New Keanu","user": 1,"rating": 0,"image": "newkeanu.jpg" }]
    topkeanu = [{"title": "top Keanu","user": 1,"rating": 75,"image": "goodkeanu.jpg" }]
    
    categories = {"topkeanu":{"pages":topkeanu,"title": "Top Keanu"},
    "keanew":{"pages":keanew,"title": "Kea New"},
    "keanothim":{"pages":keanothim,"title": "Kea Not Him"}}

    for category, category_data in  categories.items():
        c = add_category(category_data["title"])
#        for p in category_data["pages"]:
#            add_page(c, p["title"], p["user"],p["rating"],p["image"])

#add this populate in^ (needs a user instance)

#        for c in Category.objects.all():
#            for p in Page.objects.filter(category=c):
#                print("- {0} - {1}".format(str(c), str(p)))
                
      
#def add_category(name, image):
def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]#, img=image)[0]
    #c = Category.objects.get_or_create(name=name, img=image)[0]
    #c.rating = rating //OUT
    c.save()
    return c

def add_page(category, title, user, rating=0,image = "null",):
    p = Page.objects.get_or_create(category = category, title=title, user = user, rating = rating, image = image)[0]
    p.user = user
    p.rating = rating
    p.image = image
    p.save()
    return p

# Starts execution here
if __name__ == '__main__':
    print("Starting isthiskeanureeves population script...")
    populate()
