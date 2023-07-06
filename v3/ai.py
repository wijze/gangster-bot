import time

class Agent:
    def __init__(self) -> None:
        self.time_limit = 0.00001 #s
    
    def search(self, board, depth):
        start_time = time.time()
        if (time.time() - start_time) < self.time_limit:
            print(depth)
            self.search(board, depth+1)
        else: return


# a = Agent()
# a.search("a", 0)