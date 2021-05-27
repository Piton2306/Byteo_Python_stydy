"""метод Try..Finaly"""

import time

try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("Вы отменили чтение файла")
finally:
    f.close()
    print("Очисткак: закрытие файла")

"""метод with"""
import time

with open("poem.txt") as f:
    for line in f:
        time.sleep(1)
        print(line, end="")
