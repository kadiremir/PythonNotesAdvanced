"""2025, Kadir Emir,

This file is to explain what is a thread in general.

A thread is a separate flow of execution within a process.

Consider that you have some independent tasks that can be executed concurrently. For instance:

- Download file A (takes 5 minutes)
- Play a FIFA game (takes 10 minutes)
- Download file B (takes 5 minutes)

If you consider all these tasks as a single process, then
it will take 20 minutes to complete all tasks.

However, if you consider each task as a separate thread, then
- You can start downloading file A,
- Start playing FIFA game,
- Start downloading file B.

In this case, you can complete all tasks in 10 minutes.
"""

import threading
from time import sleep


def my_threading_function(x: int):
    print("Threading function is started.")
    print(f"Sleeping for {x} seconds.")
    sleep(x)
    print("Threading function is ended.")


t = threading.Thread(target=my_threading_function, args=(5,))
print("Active threads:", threading.active_count())
t.start()
print("Note that this line is executed before the threading function is completed.")
print("Active threads:", threading.active_count())


def my_threading_function_new(x: int):
    print("New threading function is started.")
    sleep(x)


for i in range(10):
    k = threading.Thread(target=my_threading_function_new, args=(2,))
    k.start()
    print(f"Thread {i} is started.")
    print("Active threads:", threading.active_count())
