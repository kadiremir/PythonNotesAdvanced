"""2025, Kadir Emir, https://github.com/kadiremir

### What is a Thread?

    - A **thread** is a separate flow of execution within a process.
    - It enables concurrent execution of tasks, allowing for more efficient use of resources and reduced overall time for task completion.

### Example Scenario
Imagine you have three independent tasks that can run concurrently:

- **Download File A** (takes 5 minutes)
- **Play a FIFA Game** (takes 10 minutes)
- **Download File B** (takes 5 minutes)

If you treat all these tasks as part of a **single process**, the total time required would be:

- **20 minutes** (tasks executed sequentially).

However, if each task is executed in a **separate thread**, the tasks can overlap, and execution might look like this:

1. Start downloading File A.
2. Start playing the FIFA game.
3. Start downloading File B.

With this approach, all tasks can be completed in **10 minutes**, as the downloads and gameplay occur concurrently.

Notes:
    Threads make multitasking possible, improving efficiency in scenarios where tasks are independent and can be executed simultaneously.
"""

import threading
from time import sleep


def my_threading_function(x: int):
    """This function is executed in a separate thread."""
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
    """This function is executed in a separate thread."""
    print("New threading function is started.")
    sleep(x)


for i in range(10):
    k = threading.Thread(target=my_threading_function_new, args=(2,))
    k.start()
    print(f"Thread {i} is started.")
    print("Active threads:", threading.active_count())


##################################################
# JOIN method

# The join method is used to wait for the thread to complete its execution.
# In the example below, the main thread will wait for the t thread to complete its execution before continuing.
# This ensures that the t thread has finished before the main thread proceeds.
# The join() method can also take an optional timeout argument, which specifies the maximum time to wait for the thread to complete.
# If the timeout is reached before the thread completes, the join() method will return and the main thread will continue.
# The join() method is useful for coordinating the execution of multiple threads and ensuring that they complete in the correct order.


def waiting_thread(x: int):
    print(f"Thread to wait for {x} seconds is started.")
    sleep(x)
    print(f"Thread to wait for {x} seconds is ended.")


thread_one = threading.Thread(target=waiting_thread, args=(5,))
thread_two = threading.Thread(target=waiting_thread, args=(10,))

# Approach 1:
# thread_one.start()
# thread_one.join()
# thread_two.start()
# thread_two.join()

# Expected output:
# Thread to wait for 5 seconds is started.
# Thread to wait for 5 seconds is ended.
# Thread to wait for 10 seconds is started.
# Thread to wait for 10 seconds is ended.

# Approach 2:
# thread_one.start()
# thread_two.start()

# Expected output:
# Thread to wait for 5 seconds is started.
# Thread to wait for 10 seconds is started.
# Thread to wait for 5 seconds is ended.
# Thread to wait for 10 seconds is ended.