import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
data = []
req = requests.get(f"https://rategain.com/blog/", headers=headers)
soup = BeautifulSoup(req.content, "html.parser")
blog_posts = soup.find_all('article', class_='category-blog')
for post in blog_posts:
    title = post.find('div', class_='content').find('a').text.strip()
    date = post.find('div', class_='blog-detail').find('span').text.strip()
    image_url = post.find('div',class_="img").find('a')['data-bg']
    likes_count = post.find('a', class_='zilla-likes').find('span').text.strip()
    data.append({"Blog Title": title, "Blog Date": date, "Image URL": image_url, "Likes Count":likes_count})
df = pd.DataFrame(data)
df.to_excel('blog_data.xlsx', index=False)