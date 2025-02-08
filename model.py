import json
from datetime import datetime

class FoodDatabase:
    def __init__(self, file_path):
        self.file_path = file_path
        self.food_data = self.load_data()

    def load_data(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def find_food_by_id(self, food_id):
        return next((food for food in self.food_data if food["id"] == food_id), None)

    def check_expiry(self, food_id):
        food = self.find_food_by_id(food_id)
        if food:
            today = datetime.now()
            try:
                # การตรวจสอบวันหมดอายุของอาหารสด
                if food["type"] == "สด":
                    expiry_date = datetime.strptime(food["expiry_date"], "%d/%m/%Y")
                    return "หมดอายุ" if expiry_date < today else "ยังไม่หมดอายุ"
                
                # การตรวจสอบวันหมดอายุของอาหารดอง
                elif food["type"] == "ดอง":
                    expiry_month_year = datetime.strptime(f"01/{food['expiry_date'][3:]}", "%d/%m/%Y")
                    return "หมดอายุ" if expiry_month_year < today else "ยังไม่หมดอายุ"
                
                # การตรวจสอบวันหมดอายุของอาหารกระป๋อง
                elif food["type"] == "กระป๋อง":
                    expiry_year = datetime.strptime(f"31/12/{food['expiry_date'][3:]}", "%d/%m/%Y")
                    expiry_date_plus_9 = expiry_year.replace(month=9)
                    return "หมดอายุ" if expiry_date_plus_9 < today else "ยังไม่หมดอายุ"
            except ValueError:
                return "วันที่ไม่ถูกต้อง"
        return None

    def validate_food_id(self, food_id):
        return len(str(food_id)) == 6 and str(food_id)[0] != '0'
