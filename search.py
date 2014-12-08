#coding=utf8
from subprocess import call
from re import search

call('ls -1R 財物位置 > ls.txt', shell=True)
call('cp property.csv match.csv', shell=True)
call('rm -f location.txt', shell=True)
call('touch location.txt', shell=True)

keywords = []
codes = []

def search_and():
    for i in range(len(keywords)):
        call('mv match.csv search.csv', shell=True)
        call('touch match.csv', shell=True)
        with open('search.csv') as f:
            for line in f:
                match = search(keywords[i], line)
                if match:
                    with open('match.csv', 'a') as f:
                        f.write(line)

def location_txt():
    with open('match.csv') as f:
        for line in f:
            match = search('[0-9]{12}', line)
            codes.append(match.group(0))
    with open('ls.txt') as f:
        for line in f:
            match = search(':', line)
            if match:
                with open('location.txt', 'a') as f:
                    f.write(line)
            for i in range(len(codes)):
                match = search(codes[i], line)
                if match:
                    with open('location.txt', 'a') as f:
                        f.write(line)

while True:
    keyword = raw_input('Search keyword: ')
    if keyword == '':
        break
    keywords.append(keyword)
while True:
    andor = raw_input('Use (A)nd / (O)r: ')
    if andor == 'A':
        search_and()
        location_txt()
        break
    if andor == 'O':
        print 'Or is not yet ready...'
    continue

call('rm search.csv match.csv ls.txt', shell=True)
