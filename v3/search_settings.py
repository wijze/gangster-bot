class Search_settings:
    def __init__(self, depth=2, time_limit=0.01) -> None:
        self.iterative_deepening = False
        self.fixed_depth = True  # if iterative deepening, max depth = depth
        self.depth = depth  # moves to took in future, keep low for performance, (2,3)
        self.capture_search_depth = 2
        self.time_limit = time_limit  # s

        self.matings_score = 1000000
        self.draw_score = -200  # we don't like draws

        self.random_order = False  # slower if true

        # evauluation type does not work with capture search
        # options: material, both (position+material) (default), legalmoves
        self.evaluation_type = "both"
        self.capture_search = True
