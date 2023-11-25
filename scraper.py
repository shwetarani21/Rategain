import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

req = requests.get("https://rategain.com/blog/", headers=headers)

soup = BeautifulSoup(req.content, "html.parser")

# print(soup.prettify())

blog_posts = soup.find_all('article', class_='category-blog')  
for post in blog_posts:
    title = post.find('div', class_='content').find('a').text.strip()
    date = post.find('div', class_='blog-detail').find('span').text.strip()
    image_url = post.find('div',class_="img").find('a')['data-bg']
    likes_count = post.find('a', class_='zilla-likes').find('span').text.strip()
    print(title)
    print(date)
    print(image_url)
    print(likes_count)