import threading
import queue

class ExceptionThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._exception_queue = queue.Queue()
        self._result_queue = queue.Queue()

    def run(self):
        try:
            if self._target:
                res = self._target(*self._args, **self._kwargs)
                self._result_queue.put(res)
        except Exception as e:
            self._exception_queue.put(e)

    def get_exception(self):
        try:
            return self._exception_queue.get(block=False)
        except queue.Empty:
            return None

    def get_result(self):
        try:
            return self._result_queue.get(block=False)
        except queue.Empty:
            return None


def f(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError(f"Invalid value of n, it must be positive integer")
    if n <= 1:
        return 1
    return f(n-1) + f(n-2)


if __name__ == "__main__":
    thread = ExceptionThread(target=f, args=(1,))
    thread.start()
    thread.join()

    exception = thread.get_exception()
    if exception:
        print(f"Exception in thread: {exception}")
    else:
        print("Thread ended without exceptions")
        print(f"Result: {thread.get_result()}")

