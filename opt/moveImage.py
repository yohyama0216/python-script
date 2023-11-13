import os
from PIL import Image
import shutil

dirs = ['aida','Adachi','aiko','aoki','Asuka','awa',
    'chika',
    'hagiwa','hara','hisa','hiyama',
    'isobe',
    'kaji','kageyama','kanna','komagata','kondo','kouno','kr',
    'machico','motegi','mp4',
    'no-metadata','no-png',
    'takara','test',
    'oikawa','other-png',
    'rie','rinon',
    'sayaka','safetensors','sumire','Sumire','Shiroma',
    'yamamoto','yamane','yt',
    'watanabe',
    'zip']

# 画像のメタデータをチェックして移動する関数
def move_image_based_on_metadata(src_directory):
    # 対象のディレクトリ内のファイルをすべてチェック
    for filename in os.listdir(src_directory):
        file_path = os.path.join(src_directory, filename)
        if filename.lower().endswith('.png'):  # PNGファイルだけを対象とする
            with Image.open(file_path) as img:
                metadata = img.info
                if 'parameters' not in metadata:
                    print('No metadata ' + filename)
                    shutil.move(file_path, os.path.join('./no-metadata/no-metadata-'+ filename))
                    continue
                
                # print(metadata['parameters'])
                # メタデータの中に特定のキーが存在するかをチェック
                for dir in dirs:
                    if dir in ['other-png']:
                        continue 

                    if dir in metadata['parameters']:
                        # 'A'が含まれている場合はAのフォルダへ移動
                        # print(os.path.join('./', dir + '/' + filename))
                        try:
                            shutil.move(file_path, os.path.join('./', dir + '/' + dir + '-' + filename))
                            continue
                        except Exception as e:
                            print(f"エラーが発生しました: {e}")
                            continue 

                #print('other png ' +filename)
                #shutil.move(file_path, os.path.join('./other-png/other-png-'+ filename))
                #if 'A' in metadata.get('Description', ''):
                #    # 'A'が含まれている場合はAのフォルダへ移動
                #    shutil.move(file_path, os.path.join(dest_directory_a, filename))
                #elif 'B' in metadata.get('Description', ''):
                #    # 'B'が含まれている場合はBのフォルダへ移動
                #    shutil.move(file_path, os.path.join(dest_directory_b, filename))
        elif filename.lower().endswith('.mp4'):  # mp4ファイルだけを対象とする
            print('Movie file ' + filename)
            shutil.move(file_path, os.path.join('./mp4/mp4-'+ filename))
        elif filename.lower().endswith('.safetensors'):
            print('LoRA or Checkpoint file ' + filename)
            shutil.move(file_path, os.path.join('./safetensors/safetensors-'+ filename))
        elif filename.lower().endswith('.zip'):
            print('zip file ' + filename)
            shutil.move(file_path, os.path.join('./zip/zip-'+ filename))
        else:
            print('No png ' + filename)
            shutil.move(file_path, os.path.join('./no-png/no-png-'+ filename))
        
# スクリプトのメイン部分
if __name__ == '__main__':
    src_dir = './images'  # PNGファイルがあるディレクトリのパス

    # 必要なフォルダが存在しない場合は作成
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)
    
    # メタデータに基づいて画像を移動
    move_image_based_on_metadata(src_dir)
