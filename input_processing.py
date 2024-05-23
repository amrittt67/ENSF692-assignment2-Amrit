# input_processing.py
# AMRIT KAUR, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.

# No global variables are permitted

# You do not need to provide additional commenting above this class, just the user-defined functions within the class

# sys is needed to exit() the program when menu entry 0 is provided
import sys

class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"
        

    # Replace these comments with your function commenting
    # update_status method needs a reference to calling object, and other values to be passed to object.
    def update_status(self, light, pedestrian, vehicle):
        self.light = light              # object's light property is now new light value coming from main function
        self.pedestrian = pedestrian    # similarly for pedestrian and vehicle
        self.vehicle = vehicle


# The sensor object should be passed to this function to print the action message and current status
def print_message(sensor):
    # print_sensor function takes sensor object, then by using if/elif construct, a single message is printed for STOP, Proceed and Caution
    if sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("\nSTOP\n")
    elif sensor.light == "green" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        print("\nProceed\n")
    elif sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        print("\nCaution\n")
    
    # finally, a general message depicting current sensor properties is also printed
    print(f"Light = {sensor.light} , Pedestrian = {sensor.pedestrian} , Vehicle = {sensor.vehicle} .")


# Complete the main function below
def main():
    sensor = Sensor()       # create sensor object
    print("\n***ENSF 692 Car Vision Detector Processing Program***")
    while True:     # while is used to keep program running unless manually stopped using menu entry 0
        print("\nAre changes are detected in the vision input?")
        print("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program ", end="")
        try:
            x = input()     # menu entry is assigned to variable x
            if x == "0":    # menu entry 0 means exit the program
                sys.exit()
            elif x == "1" or x == "2" or x == "3":                  # validate x, it should be either 1, or 2 or 3
                print("What change has been identified? ", end="")
                y = input()     # status input is assigned to variable y
                
                if x == "1":    # menu entry is for Light change
                    if y == "green" or y == "yellow" or y == "red":     # color status input is passed to update_status method, while other values remains same
                        sensor.update_status(y, sensor.pedestrian, sensor.vehicle)
                    else:
                        print("Invalid vision change.")     # when status input is other than green, yellow or red
                elif x == "2":  # menu entry is for Pedestrian change
                    if y == "yes" or y == "no":     # pedestrian status input is passed to update_status, while other values remains same
                        sensor.update_status(sensor.light, y, sensor.vehicle)
                    else:
                        print("Invalid vision change.") # if status input is other than yes or no
                else:
                    if y == "yes" or y == "no":     # vehicle status input is passed to update_status, while other values remains same
                        sensor.update_status(sensor.light, sensor.pedestrian, y)
                    else:
                        print("Invalid vision change.") # if status input is other than yes or no
                
                # finally, print the status message
                print_message(sensor)
            else:   # when menu entry item is other than 0, 1, 2, or 3, ValueError exception is raised
                raise ValueError('You must select either 1, 2, 3 or 0.')
        except ValueError as error: # ValueError exception raised above is caught here
            print(error)    # Exception message is printed here
            continue        # finally, restart the loop again to allow selecting menu entries for 0, 1, 2, or 3.
        

# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

