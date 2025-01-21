from time import sleep
import threading

# join method is used to wait for the thread to complete its execution.
# In the example above, the main thread will wait for the t thread to complete its execution before continuing.
# This ensures that the t thread has finished before the main thread proceeds.
# The join() method can also take an optional timeout argument, which specifies the maximum time to wait for the thread to complete.
# If the timeout is reached before the thread completes, the join() method will return and the main thread will continue.
# The join() method is useful for coordinating the execution of multiple threads and ensuring that they complete in the correct order.

# Example:


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

# Approach 2:
thread_one.start()
thread_two.start()
