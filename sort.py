from pathlib import Path
import shutil
from threading import Thread, Event
import logging
import time
from sys import argv
import os

logging.basicConfig(level=logging.ERROR, format="%(threadName) s%(message)s")

folders = {'images': ['png', 'jpg', 'jpeg', 'svg','ico'],
           'video': ['mp4', 'mov', 'mkv', 'avi','3gp'],
           'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx', 'rtf','torrent'],
           'audio': ['mp3', 'ogg', 'wav', 'amr','m4a'],
           'archives': ['zip', 'gz', 'tar', 'dmg','7z','bz2','iso','app'],
           'prog': ['js', 'py', 'vsix', 'sh', 'html','css','xml', 'pyc','sqlite3','json','scss'],
           'other':['',' ']
           }

def rename(file):
    new = Path(os.path.join(file.parent,'|c_'+file.name))
    os.rename(file, new)
    return new



def move_file(file):
    
    if file.name.startswith('.DS'):
        os.remove(file)
        return True
    
    for ext in folders:
        if file.suffix[1:] in folders[ext]:
            try:
                os.mkdir(SORT_DIR/ext)
            except:
                pass
            path_to_dir = SORT_DIR / ext
            logging.error(f'move {file.name} -> {path_to_dir.name} ')
            while True:
                if file.name in [s.name for s in path_to_dir.iterdir()]:
                    new = rename(file)
                    move_file(new) 
                else:
                    shutil.move(file, path_to_dir)
                return True
                    
    path_to_dir = SORT_DIR / 'other'
    logging.error(f'move {file.name} -> {path_to_dir.name} ')
    if path_to_dir.exists():
        try:
            shutil.move(file, path_to_dir)
            return True
        except:
            new = rename(file)
            move_file(new) 
            return True
    else:
        os.mkdir(path_to_dir)


    

# ----------------------
# sorting the files    
def sort(file):
    # удление .DS файлов
    if file.name.startswith('.DS'):
        os.remove(file)
        return True
    
    print(f'| Sorting file {file.name}')

    # Если это не директория, отправка в перекинуть файл
    if not file.is_dir():
        move_file(file)

    # если файл в ключах (фолдерс) и родитель SORT_DIR (пропускаем)
    elif file.name in folders.keys() and file.parent == SORT_DIR:
        print(f'Папка {file.name} нам не нужн так как она в {file.parent}')
        time.sleep(0.3)
        return None
    
    # файл директория 
    elif file.is_dir():  
        if len(os.listdir(file)) == 0:
            os.rmdir(file)
            return True
        for fl in file.iterdir():
            if fl.is_dir():
                if len(os.listdir(fl)) == 0 :
                    os.rmdir(fl)
                    continue
                elif len(os.listdir(fl.parent)) == 0 :
                    os.rmdir(fl.parent)
                else:
                    sort(fl)

            else:
                move_file(fl)

                if len(os.listdir(file)) == 0:
                    os.rmdir(file)
                elif len(os.listdir(fl.parent)) == 0 :
                    os.rmdir(fl.parent)
        
# ----------------------
# timer for testing condition and time
def timer(th):
    a = 0.0
    while True:
        time.sleep(0.1)
        a+=0.1
        a = round(a,2)
        print(' '*100, a, end='\r')
        logging.error(f'Nu da')
        if th.is_set():
            logging.error(f'Ne set')
            break

# ----------------------
def create_thread(dir):   
    event = Event()
    threads = []
    tr_timer = Thread(target=timer, args=(event,))
    tr_timer.start()
    for file in dir.iterdir():
        logging.error(f'| Work with - {file.name}')
        tr = Thread(target=sort, args=(file,))
        tr.start()
        threads.append(tr)
    [x.join() for x in threads]
    print(threads)
    event.set()
    logging.error('| Done')


if __name__ == '__main__':
    global SORT_DIR
    dir = argv[1]
    SORT_DIR = Path(dir)
    for i in range(10):
        create_thread(SORT_DIR)
    
