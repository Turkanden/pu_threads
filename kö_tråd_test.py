import threading
import queue


class Server(threading.Thread):
    def __init__(self, name, ce, cq, running):
        threading.Thread.__init__(self)
        self.name = name
        self.e = ce
        self.q = cq
        self.running = running
        self.allt = []
        
    def run(self):
        while self.running:
            self.e.wait()
            cmd = self.q.get()
            self.allt.append(cmd)
            print('Tog emot: ', cmd)
            if cmd != 'stop':
                self.e.clear()
            else:
                self.running = False

        for t_i in self.allt:
            print(t_i)
           
               
class Client(threading.Thread):
    def __init__(self, name, ce, cq, running):
        threading.Thread.__init__(self)
        self.name = name
        self.e = ce
        self.q = cq
        self.running = running
        
    def run(self):
        while self.running:
            while not self.e.is_set():
                cmd = input('Skriv in något: ')
                if cmd != 'stop':
                    self.q.put(cmd)
                    self.e.set()
                else:
                    self.q.put(cmd)
                    self.e.set()
                    self.running = False


if __name__ == '__main__':

    e = threading.Event()
    q = queue.Queue()

    threads = []

    t_server = Server(Server, e, q, True)
    t_client = Client(Client, e, q, True)
    t_server.start()
    t_client.start()

    threads.append(t_server)
    threads.append(t_client)

    for i in threads:
        i.join()



