import threading

def worker(num):
    """tråd worker function"""
    print ('Worker %s\n' % num)
    return

threads = []
for i in range(5):
    t = threading.Thread(target = worker, args = (i,)) ## Måste nog ha med , här
    threads.append(t)
    t.start()


## När man startar programmet så kommer trådarna inte i ordning, varför?

    

