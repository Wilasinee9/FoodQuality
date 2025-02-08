class FoodController:
    def __init__(self, food_database):
        self.food_database = food_database

    def validate_food(self, food_id):
        if not self.food_database.validate_food_id(food_id):
            return "รหัสอาหารไม่ถูกต้อง. รหัสต้องเป็นตัวเลข 6 หลักและไม่ขึ้นต้นด้วย 0"
        
        food = self.food_database.find_food_by_id(food_id)
        if food is None:
            return "ไม่พบรหัสอาหารในฐานข้อมูล"
        
        expiry_status = self.food_database.check_expiry(food_id)
        return f"สถานะการหมดอายุ: {expiry_status}"
    
    def generate_report(self):
        foods = self.food_database.food_data
        total_food = len(foods)
        expired_food = 0
        valid_food = 0


        fresh_food = {'valid': 0, 'expired': 0}
        pickled_food = {'valid': 0, 'expired': 0}
        canned_food = {'valid': 0, 'expired': 0}

        for food in foods:
            expiry_status = self.food_database.check_expiry(food["id"])
            
            if expiry_status == "หมดอายุ" or expiry_status == "วันที่ไม่ถูกต้อง":
                expired_food += 1
                if food["type"] == "สด":
                    fresh_food['expired'] += 1
                elif food["type"] == "ดอง":
                    pickled_food['expired'] += 1
                elif food["type"] == "กระป๋อง":
                    canned_food['expired'] += 1
            else:
                valid_food += 1
                if food["type"] == "สด":
                    fresh_food['valid'] += 1
                elif food["type"] == "ดอง":
                    pickled_food['valid'] += 1
                elif food["type"] == "กระป๋อง":
                    canned_food['valid'] += 1

 
        return {
            "total_food": total_food,
            "expired_food": expired_food,
            "valid_food": valid_food,
            "fresh_food": fresh_food,
            "pickled_food": pickled_food,
            "canned_food": canned_food
        }
