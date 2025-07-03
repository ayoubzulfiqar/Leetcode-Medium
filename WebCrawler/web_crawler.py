import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import time

class WebCrawler:
    def __init__(self, start_urls, max_depth=2, allowed_domains=None, user_agent=None, delay=0.5):
        if not start_urls:
            raise ValueError("start_urls cannot be empty.")

        self.start_urls = list(set(start_urls))
        self.max_depth = max_depth
        self.visited_urls = set()
        self.to_visit_queue = deque()
        self.crawled_data = {}
        self.session = requests.Session()
        self.delay = delay

        if user_agent:
            self.session.headers.update({'User-Agent': user_agent})
        else:
            self.session.headers.update({'User-Agent': 'Mozilla/5.0 (compatible; MyWebCrawler/1.0; +http://example.com/bot)'})

        if allowed_domains:
            self.allowed_domains = set(allowed_domains)
        else:
            self.allowed_domains = set(urlparse(url).netloc for url in self.start_urls)

        for url in self.start_urls:
            if self._is_valid_url(url):
                self.to_visit_queue.append((url, 0))
            else:
                print(f"Warning: Start URL '{url}' is not valid or not in allowed domains. Skipping.")

    def _is_valid_url(self, url):
        parsed_url = urlparse(url)
        return parsed_url.scheme in ['http', 'https'] and parsed_url.netloc in self.allowed_domains

    def _get_page_content(self, url):
        try:
            print(f"Fetching: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            content_type = response.headers.get('Content-Type', '').lower()
            if 'text/html' not in content_type and 'text/plain' not in content_type:
                print(f"Skipping non-HTML content for {url} (Content-Type: {content_type})")
                return None

            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def _extract_links(self, base_url, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            
            absolute_url = urljoin(base_url, href).split('#')[0] 
            
            parsed_absolute = urlparse(absolute_url)
            
            normalized_path_segments = [s for s in parsed_absolute.path.split('/') if s not in ('', '.')]
            normalized_path = '/' + '/'.join(normalized_path_segments) if normalized_path_segments else '/'
            
            normalized_url = parsed_absolute._replace(path=normalized_path).geturl()

            if self._is_valid_url(normalized_url):
                links.append(normalized_url)
        return list(set(links))

    def crawl(self):
        while self.to_visit_queue:
            current_url, current_depth = self.to_visit_queue.popleft()

            if current_url in self.visited_urls:
                continue

            if current_depth > self.max_depth:
                print(f"Skipping {current_url} - Max depth ({self.max_depth}) reached.")
                continue

            self.visited_urls.add(current_url)
            print(f"Crawling ({current_depth}/{self.max_depth}): {current_url}")

            html_content = self._get_page_content(current_url)
            if html_content:
                extracted_links = self._extract_links(current_url, html_content)
                self.crawled_data[current_url] = extracted_links

                for link in extracted_links:
                    if link not in self.visited_urls:
                        self.to_visit_queue.append((link, current_depth + 1))
            else:
                self.crawled_data[current_url] = []

            time.sleep(self.delay)

        print("\nCrawling finished.")
        return self.crawled_data

if __name__ == "__main__":
    print("--- Starting Crawler for example.com ---")
    start_urls_1 = ["http://www.example.com"]
    crawler1 = WebCrawler(start_urls=start_urls_1, max_depth=1, delay=0.1)
    results1 = crawler1.crawl()
    print("\n--- Results for example.com ---")
    for url, links in results1.items():
        print(f"URL: {url}")
    print(f"Total URLs crawled: {len(results1)}")

    print("\n\n--- Starting Crawler for a Wikipedia page (shallow) ---")
    start_urls_2 = ["https://en.wikipedia.org/wiki/Web_crawler"]
    allowed_domains_2 = ["en.wikipedia.org"]
    crawler2 = WebCrawler(start_urls=start_urls_2, max_depth=1, allowed_domains=allowed_domains_2, delay=0.5)
    results2 = crawler2.crawl()
    print("\n--- Results for Wikipedia page ---")
    for url, links in results2.items():
        print(f"URL: {url}")
    print(f"Total URLs crawled: {len(results2)}")

    print("\n\n--- Starting Crawler with multiple start URLs and deeper crawl ---")
    start_urls_3 = [
        "http://quotes.toscrape.com/",
        "http://quotes.toscrape.com/page/2/"
    ]
    allowed_domains_3 = ["quotes.toscrape.com"]
    custom_user_agent = "MyCustomCrawler/1.0 (Python; +http://yourwebsite.com/bot)"

    crawler3 = WebCrawler(
        start_urls=start_urls_3,
        max_depth=2,
        allowed_domains=allowed_domains_3,
        user_agent=custom_user_agent,
        delay=0.2
    )
    results3 = crawler3.crawl()
    print("\n--- Results for quotes.toscrape.com ---")
    for url, links in results3.items():
        print(f"URL: {url}")
    print(f"Total URLs crawled: {len(results3)}")

    print("\n--- Visited URLs ---")
    print(crawler3.visited_urls)
