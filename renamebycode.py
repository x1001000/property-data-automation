from subprocess import call
from re import search
from exifread import process_file
folder = raw_input('Scan folder: ')
call('ls ' + folder + ' > list', shell=True)
with open('list', 'r') as f:
    files = f.read().split()
    for file in files:
        print 'Scanning ' + file
        call('zbarimg -q ' + folder + '/' + file + ' > code', shell=True)
        with open('code', 'r') as f:
            for line in f:
                match = search(':([0-9]{12})', line)
                if match:
                    with open(folder + '/' + file, 'r') as f:
                        tags = process_file(f)
                        time = str(tags['EXIF DateTimeOriginal']).replace(' ', '-').replace(':', '')
                        print '\trenamed ' + match.group(1) + '_' + time + '.jpg'
                        call('mv ' + folder + '/' + file + ' ' + folder + '/' + match.group(1) + '_' + time + '.jpg', shell=True)