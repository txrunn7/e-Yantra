from position_hold import swift #To get the current Drone Position

current_drone_position = swift().drone_position
nth_term = 0 #Index Variable for Coordinates Array
error = swift().error
#Given Coordinates
given_coordinates = [
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

#Setpoint which is to be changed is declared here as next_coordinate
next_coordinate = given_coordinates[nth_term]

#plus or minus 0.2 accuracy is checked here, then drone moves to next coordinate
if [1 if -0.2 < i < 0.2 else 0 for i in error] == [1, 1, 1]:
    next_coordinate = given_coordinates[nth_term]
    nth_term += 1