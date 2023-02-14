import json
import os
from tqdm import tqdm
#import Path

STORAGE_DIR = 'C:/Users/nikit/PycharmProjects/github_scrapping/data_2015'
OUTPUT_DIR = 'C:/Users/nikit/PycharmProjects/github_scrapping/data_2015_compressed_2'

if __name__ == '__main__':
    files = os.listdir(STORAGE_DIR)
    files.sort(key=lambda x: int(x.split('.')[0]))
    print('Sorted!')
    counter = 0
    json_new_list = list()

    with open(STORAGE_DIR + '/' + files[0], 'r') as init:
        last_date = json.load(init)['created_at'].split('T')[0]

    for file in tqdm(files, desc='Compressing', unit='file'):
        counter = counter + 1
        with open(STORAGE_DIR + '/' + file, 'r') as _input:
            json_file = json.load(_input)
            tmp_date = json_file['created_at'].split('T')[0]
            tmp_id = json_file['id']
            if last_date != tmp_date:
                with open(OUTPUT_DIR + '/' + last_date + '.json', 'w', encoding='utf-8') as _output:
                    json.dump(json_new_list, _output)
                    json_new_list = list()
                last_date = tmp_date
            json_new_list.append(json_file)
#        if counter % 1000 == 0:
#            print(f'Processed {counter} files')

    with open(OUTPUT_DIR + '/' + last_date + '.json', 'w', encoding='utf-8') as _output:
        json.dump(json_new_list, _output)
