from subprocess import call
from exifread import process_file
from re import search
folder = raw_input('Scan folder: ')
call('ls ' + folder + ' > list.txt', shell=True)
with open('list.txt', 'r') as f:
    files = f.read().split()
    for file in files:
        renamed = False
        print 'rename ' + file
        with open(folder + '/' + file, 'r') as f:
            try:
                tags = process_file(f)
                time = str(tags['EXIF DateTimeOriginal']).replace(' ', '-').replace(':', '')
            except:
                time = 'NO-EXIF'

        call('zbarimg -q ' + folder + '/' + file + ' > code.txt', shell=True)
        with open('code.txt', 'r') as f:
            for line in f:
                match = search(':([0-9]{12})', line)
                if match:
                    print '\t\t\t\tto ' + match.group(1) + '_' + time + '.jpg'
                    call('mv ' + folder + '/' + file + ' ' + folder + '/' + match.group(1) + '_' + time + '.jpg', shell=True)
                    renamed = True
                    break

        if not renamed:
            print '\t\t\t\tto ' + file[:-4] + '_' + time + '.jpg'
            call('mv ' + folder + '/' + file + ' ' + folder + '/' + file[:-4] + '_' + time + '.jpg', shell=True)
call('rm -f list.txt code.txt', shell=True)
