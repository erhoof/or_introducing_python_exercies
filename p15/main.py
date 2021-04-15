import multiprocessing as mp
import random
import time

#     . Используйте модуль multiprocessing, чтобы создать 
#     три отдельных процесса. Заставьте каждый из них подождать 
#     случайное количество секунд между
# нулем и единицей, вывести текущее время, а затем завершить работу

def func():
    time.sleep(random.random())
    print(time.ctime())
    pass

def main():
    for num in range(3):
        p = mp.Process(target = func)
        p.start()

if __name__ == '__main__':
    main()
