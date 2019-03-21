# テンプレートファイルの文字列を置き換えてURLエンコードをかけて返す
import sys
import os
import shutil
import re
import urllib.parse

# 定数
COUNT = 5
TARGET_WORD = 'custom02_9'
TPL_FILE = 'tpl/sample.txt'
DIST_REPLACE_PATH = 'dist/replace'
DIST_ENCODE_PATH = 'dist/encode'

if not os.path.isfile(TPL_FILE):
    print('テンプレートとなるファイルが存在しません。')
    sys.exit(0)

for i in range(1, COUNT+1):
    # 書き込み用のファイルを作成し、置き換えつつ追記
    replace_file_name = DIST_REPLACE_PATH+'/sample_r_{}.txt'.format(i)
    replace_file = open(replace_file_name, mode='w')
    replace_word = 'custom_{}'.format(i)
    with open(TPL_FILE) as f:
        for line in f:
            replace_file.write(re.sub(TARGET_WORD, replace_word, line))
        replace_file.close()

    # エンコード用のファイルを作成し、エンコードした結果を追記
    encode_file_name = DIST_ENCODE_PATH+'/sample_e_{}.txt'.format(i)
    encodeFile = open(encode_file_name, mode='w')
    with open(replace_file_name) as f:
        encodeFile.write(urllib.parse.quote(f.read()))

sys.exit(0)
