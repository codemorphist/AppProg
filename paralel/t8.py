import threading
import queue
import random
import time
import logging


logging.basicConfig(
    format="[%(levelname)s] %(message)s",
    level=logging.INFO,
)


class Hotel:
    def __init__(self, num_rooms, num_clients):
        self.num_rooms = num_rooms
        self.rooms = [None] * num_rooms  
        self.lock = threading.Lock()  
        self.wait_queue = queue.Queue()  
        self.total_queue_len = 0
        self.queue_len_nums = 0
        self.total_wait_time = 0  
        self.completed_clients = 0  
        self.num_clients = num_clients  

    def check_in(self, client):
        with self.lock:
            client_id = client.client_id
            for i in range(self.num_rooms):
                if self.rooms[i] is None:  
                    self.rooms[i] = client_id
                    check_in_time = time.time()
                    logging.info(f"Client {client_id} check in room {i}.")
                    return i
            logging.info(f"Client {client_id} added to queue.")
            self.wait_queue.put(client)
            self.size_queue()
            return None

    def check_out(self, room_id):
        if room_id is None:
            return 

        with self.lock:
            client_id = self.rooms[room_id]
            self.rooms[room_id] = None  

            self.completed_clients += 1  
            
            if not self.wait_queue.empty():
                self.size_queue()
                next_client = self.wait_queue.get()
                next_client_id = next_client.client_id
                self.rooms[room_id] = next_client
                next_client.room_id = room_id
                logging.info(f"Client {next_client_id} checked in to room {room_id} from queue.")

        if self.completed_clients == self.num_clients:
            logging.info("All clients have moved out of the rooms.")

    def size_queue(self):
        queue_len = self.wait_queue.qsize()
        self.total_queue_len += queue_len
        self.queue_len_nums += 1

    def send_wait_time(self, wait_time):
        with self.lock:
            self.total_wait_time += wait_time

    def calculate_statistics(self):
        avg_queue_length = int(self.total_queue_len / max(1, self.queue_len_nums))
        avg_wait_time = self.total_wait_time / max(1, self.num_clients)
        return avg_queue_length, avg_wait_time


class Client(threading.Thread):
    __CLIENTS__ = {}

    def __init__(self, hotel, client_id, t1, t2):
        if client_id in Client.__CLIENTS__:
            return Client.__CLIENTS__[client_id]

        super().__init__()

        Client.__CLIENTS__[client_id] = self

        self.hotel = hotel
        self.client_id = client_id
        self.room_id = None
        self.t1 = t1
        self.t2 = t2

    def run(self):
        arrival_time = random.uniform(0, self.t1)
        time.sleep(arrival_time)  
        logging.info(f"Client {self.client_id} come in hotel.")

        self.room_id = self.hotel.check_in(self)

        if self.room_id is None:
            self.wait_start = time.time()
            logging.info(f"Client {self.client_id} waiting in queue.")

            while self.room_id is None:
                time.sleep(0.01)  
                
            self.wait_time = time.time() - self.wait_start
            self.hotel.send_wait_time(self.wait_time)

        stay_time = random.uniform(1, self.t2)
        time.sleep(stay_time)  
        logging.info(f"Client {self.client_id} was in the room {self.room_id} {stay_time:.2f} sec.")
        self.hotel.check_out(self.room_id)


def simulate_hotel(num_rooms, num_clients, t1, t2):
    hotel = Hotel(num_rooms, num_clients)
    clients = [Client(hotel, i, t1, t2) for i in range(num_clients)]

    logging.info("Starging simulation of hotel")

    for client in clients:
        client.start()

    for client in clients:
        client.join()

    avg_queue_length, avg_wait_time = hotel.calculate_statistics()

    logging.info(f"Average queue length: {avg_queue_length}")
    logging.info(f"Average waiting time: {avg_wait_time:.2f} sec.")
    logging.info("Simulation ended.")


if __name__ == "__main__":
    simulate_hotel(num_rooms=25, num_clients=100, t1=2, t2=5)

