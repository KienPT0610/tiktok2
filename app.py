import tkinter as tk
import pyautogui as pag
import time
import webbrowser

# Biến toàn cục để lưu vị trí con trỏ chuột khi nhấn nút "CheckpointLike"
like_position = None

def follow_tiktok():
    # Lấy vị trí (x, y) từ các ô nhập
    try:
        x_follow = int(x_follow_entry.get())
        y_follow = int(y_follow_entry.get())
    except ValueError:
        output_text.insert(tk.END, f"Vui lòng bấm checkpointFollow cấp vị trí nút follow.\n")
        output_text.see(tk.END)
        return
    
    # Di chuyển con trỏ chuột đến vị trí (x_follow, y_follow)
    # pag.moveTo(x_follow, y_follow, duration=0.5)
    
    # Thực hiện click chuột vào vị trí này
    pag.click(x_follow, y_follow)

def like_tiktok():
    global like_position
    if like_position:
        pag.doubleClick(like_position)
        output_text.insert(tk.END, "Đã like video.\n")
        output_text.see(tk.END)
    else:
        output_text.insert(tk.END, "Vui lòng nhấn nút 'CheckpointLike' trước khi like video.\n")
        output_text.see(tk.END)

def watchTiktok(num_videos, watch_time):
    for i in range(1, num_videos + 1):
        output_text.insert(tk.END, f"Watching video {i}\n")
        output_text.see(tk.END)
        pag.keyDown('down')
        time.sleep(1)
        print('Watching video', i)
        follow_tiktok()
        like_tiktok()
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
    time.sleep(1.5)
    # Lấy vị trí hiện tại của con trỏ chuột
    current_position = pag.position()
    x_follow_entry.delete(0, tk.END)  # Xóa nội dung hiện tại của ô nhập x_follow
    y_follow_entry.delete(0, tk.END)  # Xóa nội dung hiện tại của ô nhập y_follow
    x_follow_entry.insert(0, current_position.x)  # Nhập vị trí x vào ô nhập x_follow
    y_follow_entry.insert(0, current_position.y)  # Nhập vị trí y vào ô nhập y_follow
    output_text.insert(tk.END, f"Vị trí Follow đã được cập nhật: ({current_position.x}, {current_position.y})\n")
    output_text.see(tk.END)

def get_mouse_position_like():
    global like_position
    time.sleep(1.5)
    # Lấy vị trí hiện tại của con trỏ chuột
    like_position = pag.position()
    output_text.insert(tk.END, f"Vị trí Like đã được cập nhật: {like_position}\n")
    output_text.see(tk.END)
    # Tự động nhập vị trí checkpoint like vào ô nhập x_like và y_like
    x_like_entry.delete(0, tk.END)  # Xóa nội dung hiện tại của ô nhập x_like
    y_like_entry.delete(0, tk.END)  # Xóa nội dung hiện tại của ô nhập y_like
    x_like_entry.insert(0, like_position.x)  # Nhập vị trí x vào ô nhập x_like
    y_like_entry.insert(0, like_position.y)  # Nhập vị trí y vào ô nhập y_like

def open_tiktok():
     # Tạo URL đăng nhập với username và password
    login_url = f"https://www.tiktok.com/"
    # Mở trang web trong trình duyệt mặc định
    webbrowser.open(login_url)

# Tạo cửa sổ
root = tk.Tk()
root.title("auto tiktok by KienPT")
# root.geometry("400x700")
# Thay đổi icon
root.iconbitmap("/icon.ico") 

# Tạo khung chứa các ô nhập vị trí Follow
follow_frame = tk.Frame(root)
follow_frame.pack(pady=5)

# Tạo nhãn và ô nhập cho vị trí x_follow
x_follow_label = tk.Label(follow_frame, text="x_follow:")
x_follow_label.pack(side=tk.LEFT, padx=5)
x_follow_entry = tk.Entry(follow_frame)
x_follow_entry.pack(side=tk.LEFT, padx=5)

# Tạo nhãn và ô nhập cho vị trí y_follow
y_follow_label = tk.Label(follow_frame, text="y_follow:")
y_follow_label.pack(side=tk.LEFT, padx=5)
y_follow_entry = tk.Entry(follow_frame)
y_follow_entry.pack(side=tk.LEFT, padx=5)

# Tạo khung chứa các ô nhập vị trí Like
like_frame = tk.Frame(root)
like_frame.pack(pady=5)

# Tạo nhãn và ô nhập cho vị trí x_like
x_like_label = tk.Label(like_frame, text="x_like:")
x_like_label.pack(side=tk.LEFT, padx=5)
x_like_entry = tk.Entry(like_frame)
x_like_entry.pack(side=tk.LEFT, padx=5)

# Tạo nhãn và ô nhập cho vị trí y_like
y_like_label = tk.Label(like_frame, text="y_like:")
y_like_label.pack(side=tk.LEFT, padx=5)
y_like_entry = tk.Entry(like_frame)
y_like_entry.pack(side=tk.LEFT, padx=5)

# Tạo nhãn và ô nhập vị trí tìm kiếm TikTok
search_frame = tk.Frame(root)
search_frame.pack(pady=5)

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
output_text = tk.Text(root, height=10, width=70)
output_text.pack(pady=10)

# Tạo khung chứa các nút bấm
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

#Tạo ô mở web tiktok
open_Tiktok = tk.Button(button_frame, text="Open Tiktok", command=open_tiktok)
open_Tiktok.pack(side=tk.LEFT, padx=5)

# Tạo nút "Start"
start_button = tk.Button(button_frame, text="Start", command=start_action)
start_button.pack(side=tk.LEFT, padx=5)

# Tạo nút "End"
end_button = tk.Button(button_frame, text="End", command=end_action)
end_button.pack(side=tk.LEFT, padx=5)

# Tạo nút "CheckpointFollow"
checkpoint_follow_button = tk.Button(button_frame, text="CheckpointFollow", command=get_mouse_position)
checkpoint_follow_button.pack(side=tk.LEFT, padx=5)

# Tạo nút "CheckpointLike"
checkpoint_like_button = tk.Button(button_frame, text="CheckpointLike", command=get_mouse_position_like)
checkpoint_like_button.pack(side=tk.LEFT, padx=5)

# Khởi chạy vòng lặp sự kiện của cửa sổ
root.mainloop()
