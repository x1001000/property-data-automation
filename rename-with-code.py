from subprocess import call
from exifread import process_file
from re import search
folder = raw_input('Scan folder: ')
call('ls ' + folder + ' > list.txt', shell=True)
with open('list.txt', 'r') as f:
    files = f.read().split()
    for file in files:
        print 'Scanning ' + file
        call('zbarimg -q ' + folder + '/' + file + ' > code.txt', shell=True)
        with open('code.txt', 'r') as f:
            for line in f:
                match = search(':([0-9]{12})', line)
                if match:
                    with open(folder + '/' + file, 'r') as f:
                        try:
                            tags = process_file(f)
                            time = str(tags['EXIF DateTimeOriginal']).replace(' ', '-').replace(':', '')
                            print '\trenamed ' + match.group(1) + '_' + time + '.jpg'
                            call('cp ' + folder + '/' + file + ' ' + folder + '/' + match.group(1) + '_' + time + '.jpg', shell=True)
                        except:
                            print '\trenamed ' + match.group(1) + '_no_exif' + '.jpg'
                            call('cp ' + folder + '/' + file + ' ' + folder + '/' + match.group(1) + '_no_exif' + '.jpg', shell=True)
