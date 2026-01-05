import tkinter as tk 

def open_add_stay_window():
    add_window = tk.Toplevel(root)
    add_window.title("เพิ่มข้อมูลเข้าพัก")
    add_window.geometry("600x400")
    
    label = tk.Label(
        add_window,
        text="หน้าฟอร์มเพิ่มข้อมูลเข้าพัก",
        font=("Tahoma", 14))
    
    label.pack(pady=20)

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

btn_add = tk.Button(
    root,
    text="เพิ่มข้อมูลเข้าพัก",
    font=("Tahoma", 14),
    width=20,
    height=2,
    command = open_add_stay_window)

btn_add.pack(pady=10)   

btn_exit = tk.Button(
    root,
    text="ออกจากระบบ",
    font=("Tahoma", 14),
    width=20,
    height=2,
    command=root.quit)  

btn_exit.pack(pady=10)

root.mainloop() 