import tkinter as tk 
from tkinter import  ttk

def open_add_stay_window():
    add_window = tk.Toplevel(root)
    add_window.title("เพิ่มข้อมูลเข้าพัก")
    add_window.geometry("600x400")
    
    tk.Label(
        add_window,
        text="หน้าฟอร์มเพิ่มข้อมูลเข้าพัก",
        font=("Tahoma", 20)
        ).pack(pady=10)
    
    frame = tk.Frame(add_window)
    frame.pack(pady=10)
    
    # ชื่อลูกค้า 
    tk.Label(frame, text= "ชื่อลูกค้า :").grid(row=0, column=0, sticky="w", pady=5)
    entry_name = tk.Entry(frame, width=40)
    entry_name.grid(row=0, column=1, padx=10)

    # เลือกห้อง
    tk.Label(frame, text="เลือกห้อง : ").grid(row=1, column=0, sticky="w", pady=5)
    room_var = tk.StringVar()
    combo_room = ttk.Combobox(
        frame,
        textvariable =room_var,
        values = [str(i) for i in range(1,13)],
        width = 37,
        state = "readonly"
    )
    combo_room.grid(row=1,column=1,padx=10)
    
    # เพิ่มจำนวนผู้เข้าพัก 
    tk.Label(frame, text="จำนวนผู้เข้าพัก :").grid(row=2, column=0, sticky="w",pady=5)
    cus_var = tk.StringVar()
    cus_count = ttk.Combobox(
        frame, 
        textvariable= cus_var,
        values= [str(i) for i in range(1,5)],
        width= 37,
        state = "readonly", 
    )
    cus_count.grid(row=2,column=1,padx=10)
    
    
# สร้างหน้าต่างหลัก App 
root = tk.Tk()
root.title("Resort Management System")
root.geometry("600x400")

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