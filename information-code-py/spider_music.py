import requests
from bs4 import BeautifulSoup
import json
import re

def get_html(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows'
    }