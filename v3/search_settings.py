class Search_settings:
    def __init__(self) -> None:
        self.iterative_deepening = False
        self.fixed_depth = True # if iterative deepening, max depth = depth
        self.depth = 2 # moves to took in future, keep low for performance, (2,3)
        self.time_limit = 0.01 #s

        self.matings_score = 1000000
        

