# coding=utf-8
import requests
from selenium import webdriver





class Douyu:
    def __init__(self):
        self.start_url='https://www.douyu.com/directory/all'
        self.driver=webdriver.Chrome()

    def run(self):
        pass
