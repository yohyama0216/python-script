import os
from PIL import Image
import shutil

png_dirs = ['aida','Adachi','aiko','aoki','Asuka','awa',
    'chika',
    'hagiwa','hara','hisa','hiyama',
    'isobe',
    'kaji','kageyama','kanna','komagata','kondo','kouno','kr',
    'machico','motegi',
    'no-metadata','no-png',
    'takara','test',
    'oikawa',
    'rie','rinon',
    'sayaka','sumire','Sumire','Shiroma',
    'yamamoto','yamane','yt',
    'watanabe',
]

other_dirs = [
    'mp4','mov',
    'safetensors',
    'zip',
    'pdf',
    'xml','xlsx'
]

def create_directories():
    for other_dir in other_dirs:
        os.makedirs('./after/other/' + other_dir, exist_ok=True)

    for png_dir in png_dirs:
        os.makedirs('./after/images/png/' + png_dir, exist_ok=True)

def move_file(file_path, dir_name, prefix, filename):
    try:
        shutil.move(file_path, os.path.join('./', dir_name + '/' + prefix + '-' + filename))
    except Exception as e:
        print(f"ファイル {filename} の移動中にエラーが発生しました: {e}")

def move_image_based_on_metadata(src_directory):
    for filename in os.listdir(src_directory):
        file_path = os.path.join(src_directory, filename)
        file_ext = filename.lower().split('.')[-1]

        if file_ext == 'png':
            try:
                with Image.open(file_path) as img:
                    metadata = img.info

                if 'parameters' not in metadata:
                    print('No metadata ' + filename)
                    move_file(file_path, './after/images/no-metadata', 'no-metadata', filename)
                    continue

                for dir in png_dirs:
                    if dir == 'other-png':
                        continue

                    if dir in metadata['parameters']:
                        move_file(file_path, './after/images/png' + dir, dir, filename)
                        break

            except IOError:
                print(f"ファイル {filename} の読み込み中にエラーが発生しました。")
        
        elif file_ext in ['jpg','jpeg']:
            move_file(file_path, 'after/images/jpg', file_ext, filename)

        elif file_ext in other_dirs:
            move_file(file_path, './after/other/'+ file_ext, file_ext, filename)
        
        else:
            print('Other file ' + filename)
            move_file(file_path, './after/other', 'other', filename)
        
if __name__ == '__main__':
    src_dir = './before'
    create_directories()
    move_image_based_on_metadata(src_dir)