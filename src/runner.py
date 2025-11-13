thonimport json
import os
from extractors.google_scraper import GoogleScraper
from extractors.amazon_scraper import AmazonScraper
from extractors.youtube_scraper import YouTubeScraper
from outputs.exporter import Exporter

class KeywordSuggestionsScraper:
    def __init__(self, config):
        self.config = config
        self.google_scraper = GoogleScraper()
        self.amazon_scraper = AmazonScraper()
        self.youtube_scraper = YouTubeScraper()
        self.exporter = Exporter()

    def run(self):
        # Load keywords from the input
        with open(self.config['input_file'], 'r') as file:
            keywords = file.readlines()

        results = []

        for keyword in keywords:
            keyword = keyword.strip()
            result = self.scrape_keyword(keyword)
            results.append(result)

        # Export results
        self.exporter.export(results, self.config['output_file'])

    def scrape_keyword(self, keyword):
        google_results = self.google_scraper.scrape(keyword)
        amazon_results = self.amazon_scraper.scrape(keyword)
        youtube_results = self.youtube_scraper.scrape(keyword)

        return {
            "keyword": keyword,
            "platforms": {
                "google": google_results,
                "amazon": amazon_results,
                "youtube": youtube_results
            },
            "timestamp": self.get_timestamp()
        }

    def get_timestamp(self):
        return "2025-01-08T01:16:10.368Z"

if __name__ == "__main__":
    config = {
        "input_file": "data/inputs.sample.txt",
        "output_file": "data/sample.json"
    }
    scraper = KeywordSuggestionsScraper(config)
    scraper.run()