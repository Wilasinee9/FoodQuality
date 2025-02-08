import tkinter as tk
from tkinter import messagebox

class FoodQualityGUI:
    def __init__(self, root, food_controller):
        self.root = root
        self.food_controller = food_controller
        self.root.title("Food Quality Checker")
        self.root.geometry("400x300")
        self.root.configure(bg="#2E2E2E")
        self.create_widgets()

    def create_widgets(self):
        self.food_id_label = tk.Label(self.root, text="กรอกรหัสอาหาร :", font=("Helvetica", 14), fg="#FFFFFF", bg="#2E2E2E")
        self.food_id_label.pack(pady=10)

        self.food_id_entry = tk.Entry(self.root, font=("Helvetica", 14), width=20, justify="center", bd=2, bg="#444444", fg="white")
        self.food_id_entry.pack(pady=5)

        self.check_button = tk.Button(self.root, text="ตรวจสอบ", command=self.check_food, font=("Helvetica", 12), bg="#4CAF50", fg="#2E2E2E", relief="raised", width=20)
        self.check_button.pack(pady=10)

        self.report_button = tk.Button(self.root, text="รายงานสถานะอาหารทั้งหมด", command=self.show_report, font=("Helvetica", 12), bg="#2196F3", fg="#2E2E2E", relief="raised", width=20)
        self.report_button.pack(pady=10)

    def check_food(self):
        food_id = self.food_id_entry.get()
        try:
            food_id = int(food_id)
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกเป็นตัวเลข")
            return

        result = self.food_controller.validate_food(food_id)
        messagebox.showinfo("ผลการตรวจสอบ", result)

    def show_report(self):
        report = self.food_controller.generate_report()

        
        report_window = tk.Toplevel(self.root)
        report_window.title("รายงานสถานะอาหาร")
        report_window.geometry("500x400")
        report_window.configure(bg="#2E2E2E")

   
        for i in range(8):
            report_window.grid_rowconfigure(i, weight=1)
        for i in range(3):
            report_window.grid_columnconfigure(i, weight=1)

 
        header_label = tk.Label(report_window, text="ประเภทอาหาร", font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E", width=20, relief="solid")
        header_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        valid_label = tk.Label(report_window, text="ใช้ได้", font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E", width=10, relief="solid")
        valid_label.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        expired_label = tk.Label(report_window, text="หมดอายุ", font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E", width=10, relief="solid")
        expired_label.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

       
        food_types = ["อาหารสด", "อาหารดอง", "อาหารกระป๋อง"]
        food_data = [
            [report['fresh_food']['valid'], report['fresh_food']['expired']],
            [report['pickled_food']['valid'], report['pickled_food']['expired']],
            [report['canned_food']['valid'], report['canned_food']['expired']]
        ]

        
        for i, food_type in enumerate(food_types):
            tk.Label(report_window, text=food_type, font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E", width=20, relief="solid").grid(row=i+1, column=0, padx=5, pady=5, sticky="ew")
            tk.Label(report_window, text=food_data[i][0], font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E", width=10, relief="solid").grid(row=i+1, column=1, padx=5, pady=5, sticky="ew")
            tk.Label(report_window, text=food_data[i][1], font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E", width=10, relief="solid").grid(row=i+1, column=2, padx=5, pady=5, sticky="ew")

       
        summary_label = tk.Label(report_window, text="สรุปสถานะอาหาร", font=("Helvetica", 14), fg="#FFFFFF", bg="#2E2E2E", pady=10)
        summary_label.grid(row=4, columnspan=3)

        tk.Label(report_window, text=f"จำนวนอาหารที่ใช้ได้: {report['valid_food']}", font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E").grid(row=5, columnspan=3, padx=5, pady=5, sticky="ew")
        tk.Label(report_window, text=f"จำนวนอาหารที่หมดอายุ: {report['expired_food']}", font=("Helvetica", 12), fg="#FFFFFF", bg="#2E2E2E").grid(row=6, columnspan=3, padx=5, pady=5, sticky="ew")

        
        close_button = tk.Button(report_window, text="ปิด", command=report_window.destroy, font=("Helvetica", 12), bg="#f44336", fg="#2E2E2E", relief="raised")
        close_button.grid(row=7, columnspan=3, pady=10)

if __name__ == "__main__":
    root = tk.Tk()

    class FoodController:
        def validate_food(self, food_id):
            return "อาหารใช้ได้"
        
        def generate_report(self):
            return {
                'total_food': 50,
                'fresh_food': {'valid': 30, 'expired': 5},
                'pickled_food': {'valid': 10, 'expired': 3},
                'canned_food': {'valid': 5, 'expired': 2},
                'valid_food': 45,
                'expired_food': 5
            }

    food_controller = FoodController()
    gui = FoodQualityGUI(root, food_controller)
    root.mainloop()
