from django.shortcuts import render
from datetime import date
from django.http import Http404

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Sagal",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 
            1500s, when an unknown printer took a galley of type and scrambled it
             to make a type specimen book. It has survived not only five centuries, 
            but also the leap into electronic typesetting, remaining essentially 
            unchanged.

            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 
            1500s, when an unknown printer took a galley of type and scrambled it
             to make a type specimen book. It has survived not only five centuries, 
            but also the leap into electronic typesetting, remaining essentially 
            unchanged.
            unchanged.

            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 
            1500s, when an unknown printer took a galley of type and scrambled it
             to make a type specimen book. It has survived not only five centuries, 
            but also the leap into electronic typesetting, remaining essentially 
            unchanged.
            unchanged.
        """
    },
    {
        "slug": "nature",
        "image": "woods.jpg",
        "author": "Sagal",
        "date": date(2021, 7, 21),
        "title": "Nature at It's Best",
        "excerpt": "Nature is amazing! The amount of inspiration i get when walking in nature is incredible",
        "content": """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 
            1500s, when an unknown printer took a galley of type and scrambled it
             to make a type specimen book. It has survived not only five centuries, 
            but also the leap into electronic typesetting, remaining essentially 
            unchanged.

            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 
            1500s, when an unknown printer took a galley of type and scrambled it
             to make a type specimen book. It has survived not only five centuries, 
            but also the leap into electronic typesetting, remaining essentially 
            unchanged.
            unchanged.

            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 
            1500s, when an unknown printer took a galley of type and scrambled it
             to make a type specimen book. It has survived not only five centuries, 
            but also the leap into electronic typesetting, remaining essentially 
            unchanged.
            unchanged.
        """
    },
    {
        "slug": "Programming-is-fun",
        "image": "coding.jpg",
        "author": "Sagal",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great",
        "excerpt": "Did you ever spend hours searching that one error in your code",
        "content": """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 
            1500s, when an unknown printer took a galley of type and scrambled it
             to make a type specimen book. It has survived not only five centuries, 
            but also the leap into electronic typesetting, remaining essentially 
            unchanged.

            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 
            1500s, when an unknown printer took a galley of type and scrambled it
             to make a type specimen book. It has survived not only five centuries, 
            but also the leap into electronic typesetting, remaining essentially 
            unchanged.
            unchanged.

            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 
            1500s, when an unknown printer took a galley of type and scrambled it
             to make a type specimen book. It has survived not only five centuries, 
            but also the leap into electronic typesetting, remaining essentially 
            unchanged.
            unchanged.
        """
    }
]

def get_date (post):
    return post['date']

# Create your views here.

def home_view(request):
    sorted_posts = sorted(all_posts, key= get_date)
    latest_posts =sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "all_posts": latest_posts
    })

def post_view(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def all_view(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render (request, "blog/post-detail.html", {
        "post": identified_post
    })

