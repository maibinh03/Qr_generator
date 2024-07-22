from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image, ImageTk

#WINDOW
root = Tk()
root.title("Tạo mã QR - Mai Thanh Bình Boong")
root.geometry('500x250')

def generate_qr():
    #save file
    save_path = filedialog.asksaveasfilename(title="Lưu mã", filetypes=(("PNG File", ".png"), ("All Files", "*.*")))

    if save_path:
        if not save_path.endswith(".png"):
            save_path = f'{save_path}.png'
        
        #Tạo qr và lưu thành png
        qr = pyqrcode.create(entry_field.get())
        qr.png(save_path, scale="5")

        #Hiển thị qr luôn
        global get_image #Biến Global rất tệ nhưng cần thiết vì Tkinter quá dở và biến sẽ cook nếu ở trong hàm và không phải Global
        get_image = ImageTk.PhotoImage(Image.open(save_path))
        qr_picture.config(image=get_image)

def clear():
    entry_field.delete(0, END)
    qr_picture.config(image="")

#GUI
welcome_label = Label(root, text="Xin mời sử dụng phần mềm tạo mã QR!")
welcome_label.pack(pady=20)

entry_field = Entry(root, font=("Poppins", 18))
entry_field.pack(pady=20)

submit_button = Button(root, text="Tạo mã QR", command = generate_qr)
submit_button.pack(pady="20")
clear_button = Button(root, text="Xoá", command=clear)
clear_button.pack(pady="20")


qr_picture = Label(root, text="")
qr_picture.pack(pady=20)


root.mainloop()