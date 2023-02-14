from datetime import datetime, date, timedelta
from tqdm import tqdm
import time
import sys

# print(sys.stdin)
# for line in sys.stdin:
#     print(line)

for i in tqdm(range(20), desc='Compressing', unit='file'):
    time.sleep(i+1)
    # if (i+1) % 5 == 0:
    #     print(i+1)


# d = datetime.today() - timedelta(days=int(365.25*15))
# d2 = date(2007, 1, 1)
#
#
# d3 = d+timedelta(hours=1)
# d4 = d+timedelta(hours=2)
# print(60 - datetime.today().minute + 1)
