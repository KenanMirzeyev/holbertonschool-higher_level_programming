#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    r = "https://jsonplaceholder.typicode.com/posts"
    respond = requests.get(r)
    print("Status Code: ", respond.status_code)
    
    if respond.status_code == 200:
        post = respond.json()
        for pos in post:
            print(pos['title'])

def fetch_and_save_posts():
    r = "https://jsonplaceholder.typicode.com/posts"
    respond = requests.get(r)
    
    if respond.status_code == 200:
        post = respond.json()

        structured = [
            {'id': pos['id'], 'title': pos['title'], 'body': pos['body']}
            for pos in post
        ]

        with open('post.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(structured)
