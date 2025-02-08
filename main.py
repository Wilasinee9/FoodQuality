from tkinter import Tk
from controller import FoodController
from model import FoodDatabase
from view import FoodQualityGUI

if __name__ == "__main__":
    root = Tk()
    food_database = FoodDatabase("food_data.json")
    food_controller = FoodController(food_database)
    
    view = FoodQualityGUI(root, food_controller)  
    root.mainloop()

