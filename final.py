import csv
import os

class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"[{self.priority}] {self.title}: {self.description}"

class ToDoList:
    def __init__(self, file_name='tasks.csv'):
        self.tasks = []
        self.file_name = file_name
        self.load_from_csv()

    def add_task(self, title, description, priority):
        new_task = Task(title, description, priority)
        self.tasks.append(new_task)
        self.save_to_csv()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_to_csv()
            return removed
        return None

    def show_tasks(self):
        if not self.tasks:
            print("\nلیست کارها خالی است.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}")

    def save_to_csv(self):
        with open(self.file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Description', 'Priority'])
            for task in self.tasks:
                writer.writerow([task.title, task.description, task.priority])

    def load_from_csv(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.tasks.append(Task(row['Title'], row['Description'], row['Priority']))
                    


def main():
    todo = ToDoList()
    
    while True:
        print("\n--- مدیریت لیست کارها ---")
        print("1. اضافه کردن کار")
        print("2. مشاهده کارها")
        print("3. حذف کار")
        print("4. خروج")
        
        choice = input("انتخاب شما: ")
        
        if choice == '1':
            title = input("عنوان کار: ")
            desc = input("توضیحات: ")
            priority = input("اولویت (بالا/متوسط/پایین): ")
            todo.add_task(title, desc, priority)
            print("کار با موفقیت اضافه شد.")
            
        elif choice == '2':
            print("\nلیست کارهای شما:")
            todo.show_tasks()
            
        elif choice == '3':
            todo.show_tasks()
            if todo.tasks:
                try:
                    idx = int(input("شماره کار مورد نظر برای حذف: "))
                    removed = todo.remove_task(idx)
                    if removed:
                        print(f"کار '{removed.title}' حذف شد.")
                    else:
                        print("شماره نامعتبر!")
                except ValueError:
                    print("لطفاً یک عدد وارد کنید.")
                    
        elif choice == '4':
            print("خداحافظ!")
            break
        else:
            print("انتخاب نامعتبر!")

if __name__ == "__main__":
    main()