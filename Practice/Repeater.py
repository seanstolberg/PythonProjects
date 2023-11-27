import collections
import time

class Repeater:
    def __init__(self):
        self.buffer = collections.deque(maxlen=100000)

    def inputInt(self, i):
        self.buffer.append(i)

    def poke(self):
        return sorted(self.buffer)

class Request:
    def __init__(self, request_time, amount):
        self.request_time = request_time
        self.amount = amount

class VisaTransactionProcessor:
    def __init__(self):
        self.window_size = 2  # Rolling window size in seconds
        self.max_requests = 10000
        self.requests = collections.deque()
    
    def process_request(self, request: Request):
        current_time = time.time()
        while self.requests and current_time - self.requests[0].self.request_time >= self.window_size:
            self.requests.popleft()  # Remove requests outside the window
        if len(self.requests) < self.max_requests:
            self.requests.append(request)
            return True
        return False  # Reject the request if too many within the window
    

