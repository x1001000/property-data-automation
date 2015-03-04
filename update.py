#coding=utf8
from subprocess import call
from re import search

call('rm latest.a.csv latest.b.csv', shell=True)
call('ls -1R 財物位置 > ls.txt', shell=True)

def latest_dict():
    latest = dict()
    with open('ls.txt') as f:
        for line in f:
            match = search(':', line)
            if match:
                location = line[:-2]
            match = search('[0-9]{12}', line)
            if match:
                m = search('([0-9]{8})-([0-9]{6})', line)
                datetime = int(m.group(1) + m.group(2))
                if latest.get(match.group(0), [0,0])[0] < datetime:
                    latest[match.group(0)] = [datetime, location]
    return latest

latest = latest_dict()

with open('latest.a.csv', 'a') as F:
    with open('property.a.csv') as f:
        for line in f:
            F.write(line[:-2])
            for key, val in latest.items():
                match = search(key, line)
                if match:
                    F.write(',' + str(val[0]) + ',' + val[1])
                    break
            F.write('\n')
with open('latest.b.csv', 'a') as F:
    with open('property.b.csv') as f:
        for line in f:
            F.write(line[:-2])
            for key, val in latest.items():
                match = search(key, line)
                if match:
                    F.write(',' + str(val[0]) + ',' + val[1])
                    break
            F.write('\n')

call('rm ls.txt', shell=True)
