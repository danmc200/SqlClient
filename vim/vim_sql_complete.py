#!/usr/bin/python
def read_keywords(filename):
    keywords = []
    keywords_fle = open(filename, 'r')
    for keyword in keywords_fle.readlines():
        keywords.append(keyword.replace('\n',''))
    return keywords

def filter_list(part, keywords):
    dictionary = []
    for word in keywords:
        if((len(word) >= len(part)) and (part.upper() == word[:len(part)])):
            dictionary.append(word)
    return dictionary

class Complete():

    def __init__(self, vim, driver):
        self.vim = vim
        self.driver = driver
        self.keywords = []
        self.keywords = read_keywords('sqlite_keywords.txt')


    def set_complete(self, part):
        dictionary = filter_list(part, self.keywords)
        self.vim.command('let g:comp_list=' + str(dictionary))
