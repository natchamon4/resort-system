import tkinter as tk 

# สร้างหน้าต่างหลัก App 
root = tk.Tk()
root.title("Resort Management System")
root.geometry("1000x800")

# ชื่อโปรแกรม
label = tk.Label(
    root,
    text="ระบบจัดการเข้าพักรีสอร์ท",
    font=("Tahoma", 16))


label.pack(pady=30)

root.mainloop() 