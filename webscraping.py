import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def extract_article_titles(soup):
    titles = []
    for title in soup.find_all('h2', class_='article-title'):
        titles.append(title.get_text())
    return titles

def main():
    url = 'https://example.com/news'
    html_content = fetch_webpage(url)
    if html_content:
        soup = parse_html(html_content)
        titles = extract_article_titles(soup)
        print("Article Titles:")
        for title in titles:
            print(title)

if __name__ == "__main__":
    main()
