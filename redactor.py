import json
import os
from tqdm import tqdm


def raw_process():
    STORAGE_DIR = 'E:/BigData/OBSOLETE/github_parser/data'
    OUTPUT_DIR = 'data'

    files = os.listdir(STORAGE_DIR)
    print('Sorting...')
    files.sort(key=lambda x: os.path.getmtime(STORAGE_DIR + '/' + x))
    print('Sorted!')
    counter = 0
    json_new = list()

    with open(STORAGE_DIR + '/' + files[0]) as init:
        last_date = json.load(init)['created_at'].split('T')[0]

    for file in tqdm(files:
        counter = counter + 1
        with open(STORAGE_DIR + '/' + file) as _input:
            try:
                json_file = json.load(_input)
            except UnicodeDecodeError:
                print(f'Bad unicode symbol at file {file}.json')
                continue

            tmp_date = json_file['created_at'].split('T')[0]
            if last_date != tmp_date:
                with open(OUTPUT_DIR + '/' + last_date + '.json', 'w') as _output:
                    json.dump(json_new, _output)
                    json_new = list()
                last_date = tmp_date
            json_new.append(json_file)

        if counter % 10000 == 0:
            print(f'Processed {counter} files')

    with open(OUTPUT_DIR + '/' + last_date + '.json', 'w') as _output:
        json.dump(json_new, _output)


def reformart():
    INPUT_PATH = 'E:/BigData/OBSOLETE/github_parser/input'
    OUTPUT_PATH = 'data_new'
    files = os.listdir(INPUT_PATH)
    count = 0
    for file in files:
        new_repos = list()
        with open(INPUT_PATH + '/' + file, 'r') as f:
            old_json = json.load(f)
            for repo in old_json:
                new_repos.append(old_json[repo])
        with open(OUTPUT_PATH + '/' + file, 'w') as out:
            json.dump(new_repos, out)
        count += 1
        if count % 100 == 0:
            print(count)


if __name__ == '__main__':
    reformart()
