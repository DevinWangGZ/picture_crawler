# -*- coding: utf-8 -*-

import logging
import sys
from six.moves.urllib.parse import urlsplit

from icrawler.builtin import (BaiduImageCrawler, BingImageCrawler,
                              FlickrImageCrawler, GoogleImageCrawler,
                              GreedyImageCrawler, UrlListCrawler)

max_num = 2000

def test_google(keywordList):
    for keyword in keywordList:
        google_crawler = GoogleImageCrawler(
            downloader_threads=4,
            storage={'root_dir': 'images/google/'+keyword},
            log_level=logging.INFO)
        google_crawler.crawl(keyword, max_num=max_num)


def test_bing(keywordList):
    for keyword in keywordList:
        bing_crawler = BingImageCrawler(
            storage={'root_dir': 'images/bing/'+keyword}, log_level=logging.INFO)
        bing_crawler.crawl(keyword, max_num=max_num)

def test_baidu(keywordList):
    for keyword in keywordList:
        baidu_crawler = BaiduImageCrawler(
            downloader_threads=4, storage={'root_dir': 'images/baidu/'+keyword})
        baidu_crawler.crawl(keyword, max_num=max_num)

def test_flickr(keywordList):
    for keyword in keywordList:
        flickr_crawler = FlickrImageCrawler(
            apikey='adc52c6f6bf8166d95f4c459f851e2c6',
            downloader_threads=4,
            storage={'root_dir': 'images/flickr/'+keyword}, log_level=logging.INFO)
        flickr_crawler.crawl(apikey='adc52c6f6bf8166d95f4c459f851e2c6', tags=keyword, max_num=max_num, tag_mode='all', group_id='68012010@N00')

def test_greedy(domainList, keywordList):
    greedy_crawler = GreedyImageCrawler(
        parser_threads=4, storage={'root_dir': 'images/greedy'})
    greedy_crawler.crawl(
        domains=domainList, min_size=(10, 10), keywords=keywordList)

def main():
    keywordList = [line.rstrip('\n') for line in open('keyword.txt')]
    for key in keywordList:
        print (key)


    domainList = [line.rstrip('\n') for line in open('domain.txt')]
    for domain in domainList:
        domain = '{0.scheme}://{0.netloc}'.format(urlsplit(domain))
        print (domain)

    if len(sys.argv) == 1:
        dst = 'all'
    else:
        dst = sys.argv[1:]
    if 'all' in dst:
        dst = ['google', 'bing','baidu']  #, 'flickr', 'greedy'
        #dst = ['greedy']
    if 'google' in dst:
        test_google(keywordList)
    if 'bing' in dst:
        test_bing(keywordList)
    if 'baidu' in dst:
        test_baidu(keywordList)
    if 'flickr' in dst:
        test_flickr(keywordList)
    if 'greedy' in dst:
        test_greedy(domainList, keywordList)


if __name__ == '__main__':
    main()
