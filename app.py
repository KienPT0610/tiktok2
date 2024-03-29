import tkinter as tk
import pyautogui as pag
import time

def follow_tiktok():
    # Lấy vị trí (x, y) từ các ô nhập
    try:
        x_follow = int(x_follow_entry.get())
        y_follow = int(y_follow_entry.get())
    except ValueError:
        output_text.insert(tk.END, f"Vui lòng nhập số nguyên cho vị trí x và y.\n")
        output_text.see(tk.END)
        return
    
    # Di chuyển con trỏ chuột đến vị trí (x_follow, y_follow)
    pag.moveTo(x_follow, y_follow, duration=0.5)
    
    # Thực hiện click chuột vào vị trí này
    pag.click()

def watchTiktok(num_videos, watch_time):
    for i in range(1, num_videos + 1):
        output_text.insert(tk.END, f"Watching video {i}\n")
        output_text.see(tk.END)
        pag.keyDown('down')
        print('Watching video', i)
        follow_tiktok()
        time.sleep(watch_time)


def start_action():
    name = name_entry.get()
    print("Xin chào,", name)
    
    try:
        num_videos = int(num_videos_entry.get())
        watch_time = float(watch_time_entry.get())  # Thời gian xem mỗi video
    except ValueError:
        output_text.insert(tk.END, f"Vui lòng nhập một số nguyên cho số lượng video muốn xem và một số cho thời gian xem mỗi video.\n")
        output_text.see(tk.END)
        print("Vui lòng nhập một số nguyên cho số lượng video muốn xem và một số cho thời gian xem mỗi video.")
        return
    
    output_text.delete('1.0', tk.END)
    
    op = True
    if op == True:
        watchTiktok(num_videos, watch_time)

def end_action():
    print("End button clicked")
    root.destroy()

def get_mouse_position():
    time.sleep(3)
    # Lấy vị trí hiện tại của con trỏ chuột
    current_position = pag.position()
    output_text.insert(tk.END, f"Current mouse position: {current_position}\n")
    output_text.see(tk.END)

# Tạo cửa sổ
root = tk.Tk()
root.title("auto tiktok")
root.geometry("400x600")

# Tạo nhãn và ô nhập cho vị trí x_follow
x_follow_label = tk.Label(root, text="Nhập vị trí x_follow:")
x_follow_label.pack(pady=5)
x_follow_entry = tk.Entry(root)
x_follow_entry.pack(pady=5)

# Tạo nhãn và ô nhập cho vị trí y_follow
y_follow_label = tk.Label(root, text="Nhập vị trí y_follow:")
y_follow_label.pack(pady=5)
y_follow_entry = tk.Entry(root)
y_follow_entry.pack(pady=5)

# Tạo nhãn và ô nhập tên
name_label = tk.Label(root, text="Nhập tên video muốn xem:")
name_label.pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Tạo nhãn và ô nhập số lượng video muốn xem
num_videos_label = tk.Label(root, text="Nhập số lượng video muốn xem:")
num_videos_label.pack(pady=5)
num_videos_entry = tk.Entry(root)
num_videos_entry.pack(pady=5)

# Tạo nhãn và ô nhập thời gian xem mỗi video
watch_time_label = tk.Label(root, text="Nhập thời gian xem mỗi video (giây):")
watch_time_label.pack(pady=5)
watch_time_entry = tk.Entry(root)
watch_time_entry.pack(pady=5)

# Tạo ô view hiển thị lệnh print
output_text = tk.Text(root, height=10, width=100)
output_text.pack(pady=10)

# Tạo nút "Start"
start_button = tk.Button(root, text="Start", command=start_action)
start_button.pack(pady=5)

# Tạo nút "End"
end_button = tk.Button(root, text="End", command=end_action)
end_button.pack(pady=5)

# Tạo nút "Checkpoint"
checkpoint_button = tk.Button(root, text="CheckpointFollow", command=get_mouse_position)
checkpoint_button.pack(pady=5)

# Khởi chạy vòng lặp sự kiện của cửa sổ
root.mainloop()
