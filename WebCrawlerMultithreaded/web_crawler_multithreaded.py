import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import threading
import queue

class WebCrawler:
    def __init__(self, start_url, max_threads=5, max_pages=50, max_depth=3, allowed_domains=None):
        self.start_url = start_url
        self.max_threads = max_threads
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.url_queue = queue.Queue()
        self.visited_urls = set()
        self.lock = threading.Lock()
        self.results = []
        self.crawled_count = 0

        if allowed_domains is None:
            parsed_start_url = urlparse(start_url)
            self.allowed_domains = {parsed_start_url.netloc}
        else:
            self.allowed_domains = set(allowed_domains)

        self.url_queue.put((start_url, 0))

    def _is_valid(self, url):
        parsed = urlparse(url)
        return bool(parsed.scheme) and bool(parsed.netloc) and parsed.netloc in self.allowed_domains

    def _get_links(self, html_content, base_url):
        soup = BeautifulSoup(html_content, 'html.parser')
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(base_url, href)
            full_url = full_url.split('#')[0]
            if self._is_valid(full_url):
                links.add(full_url)
        return links

    def _worker(self):
        while True:
            try:
                url, depth = self.url_queue.get(timeout=1)
            except queue.Empty:
                break

            with self.lock:
                if url in self.visited_urls or self.crawled_count >= self.max_pages:
                    self.url_queue.task_done()
                    continue
                self.visited_urls.add(url)
                self.crawled_count += 1

            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                
                if 'text/html' not in response.headers.get('Content-Type', ''):
                    self.url_queue.task_done()
                    continue

                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.string if soup.title else "No Title"
                with self.lock:
                    self.results.append({"url": url, "title": title})

                if depth < self.max_depth:
                    new_links = self._get_links(response.text, url)
                    for link in new_links:
                        with self.lock:
                            if link not in self.visited_urls and self.crawled_count < self.max_pages:
                                self.url_queue.put((link, depth + 1))
            except requests.exceptions.RequestException:
                pass
            finally:
                self.url_queue.task_done()

    def start_crawl(self):
        threads = []
        for _ in range(self.max_threads):
            thread = threading.Thread(target=self._worker)
            thread.daemon = True
            threads.append(thread)
            thread.start()

        self.url_queue.join()
        return self.results