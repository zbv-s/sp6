import threading, time
from threading import Thread, Barrier

def bigrams(word, barrier):
    from collections import Counter
    print(f"Thread {word}: multiplying")
    res=Counter(word[idx : idx + 2] for idx in range(len(word)-1))
    print(f"{word}: {res}")
    th_name = threading.current_thread().name
    print(f"{th_name} wait barrier with {barrier.n_waiting}")
    worker_id=barrier.wait()
    print(f"{th_name} passing barrier {worker_id}")
    return res

def division_text(test_str):
     threads = []
     words = test_str.split()
     n=len(words)
     barrier = threading.Barrier(n)
     for word in words:
         thread = Thread(target=bigrams, args=(word,barrier, ))
         threads.append(thread)
         print(f"{thread.getName()}: starting")
         thread.start()
         time.sleep(0.3)
     for thread in threads:
         print(f"{thread.getName()}: joining")
         thread.join()
         print(f"{thread.getName()}: done")

if __name__ == '__main__':
      test_str = input("Enter the string: ")
      res = division_text(test_str)  

