from position_hold import swift 
class waypoint_coordinate_updater(swift):
    def __init__(self):
        super().__init__()
        self.nthterm = 0
        self.given_coordinates = [
            [0, 0, 23],
            [2, 0, 23],
            [2, 2, 23],
            [2, 2, 25],
            [-5, 2, 25],
            [-5, -3, 25],
            [-5, -3, 21],
            [7, -3, 21],
            [7, 0, 21],
            [0, 0, 19]

        ]
        self.run()

    def run(self):
        self.setpoint = self.given_coordinates[0]
        if [1 if -0.2 < i < 0.2 else 0 for i in self.error] == [1, 1, 1]:
            self.nth_term += 1
            self.setpoint = self.given_coordinates[self.nth_term]

w = waypoint_coordinate_updater()
w.run()
