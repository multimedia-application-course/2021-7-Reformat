import tkinter as tk
from tkinter import messagebox
import sys
from tkinter.filedialog import askopenfilename
import tkinter.ttk as ttk
from jpg_png import jpg2png, png2jpg
from jpg_pdf import pdf2jpg, pic2pdf
from mp3_wav import wav_to_mp3, mp3_to_wav


def click():
    global var, label, error_log, file_path
    if var.get() == '':
        error_log = tk.Label(win, text='请先选择要转化的格式！', fg='red', font=('Arial', 12))
        error_log.place(x=50, y=80)
        # print(var.get())
    else:
        if error_log != '':
            error_log.destroy()
            error_log = ''

        if var.get() == 'jpg转png' or var.get() == 'jpg转pdf':
            file_path = askopenfilename(filetypes=[('Image File', '*.jpg')])
        elif var.get() == 'png转jpg':
            file_path = askopenfilename(filetypes=[('Image File', '*.png')])
        elif var.get() == 'pdf转jpg':
            file_path = askopenfilename(filetypes=[('PDF', '*.pdf')])
        elif var.get() == 'mp3转wav':
            file_path = askopenfilename(filetypes=[('MP3', '*.mp3')])
        else:
            file_path = askopenfilename(filetypes=[('WAV', '*.wav')])
        if label != '':
            label.destroy()
        label = tk.Label(win, text=file_path)
        label.place(x=20, y=150)


def click2():
    global var, file_path, error_log
    if file_path == '':
        error_log = tk.Label(win, text='请先选择要转化的文件！', fg='red', font=('Arial', 12))
        error_log.place(x=50, y=150)
    else:
        if error_log != '':
            error_log.destroy()
            error_log = ''

        if var.get() == 'jpg转png':
            filename = tk.filedialog.asksaveasfilename(filetypes=[('Image File', '*.png')])
            if filename != '':
                if filename[-4:] != '.png':
                    filename += '.png'
                # 转换
                jpg2png(file_path, filename)
                tk.messagebox.showinfo('成功', '转换成功！')

        elif var.get() == 'jpg转pdf':
            filename = tk.filedialog.asksaveasfilename(filetypes=[('PDF', '*.pdf')])
            if filename != '':
                if filename[-4:] != '.pdf':
                    filename += '.pdf'
                # 转换
                pic2pdf(file_path, filename)
                tk.messagebox.showinfo('成功', '转换成功！')

        elif var.get() == 'png转jpg':
            filename = tk.filedialog.asksaveasfilename(filetypes=[('Image File', '*.jpg')])
            if filename != '':
                if filename[-4:] != '.jpg':
                    filename += '.jpg'
                # 转换
                png2jpg(file_path, filename)
                tk.messagebox.showinfo('成功', '转换成功！')

        elif var.get() == 'pdf转jpg':
            filename = tk.filedialog.asksaveasfilename(filetypes=[('Image File', '*.jpg')])
            if filename != '':
                if filename[-4:] != '.jpg':
                    filename += '.jpg'
                # 转换
                pdf2jpg(file_path, filename)
                tk.messagebox.showinfo('成功', '转换成功！')

        elif var.get() == 'mp3转wav':
            filename = tk.filedialog.asksaveasfilename(filetypes=[('WAV', '*.wav')])
            if filename != '':
                if filename[-4:] != '.wav':
                    filename += '.wav'
                # 转换
                mp3_to_wav(file_path, filename)
                tk.messagebox.showinfo('成功', '转换成功！')

        else:  # wav转mp3
            filename = tk.filedialog.asksaveasfilename(filetypes=[('MP3', '*.mp3')])
            if filename != '':
                if filename[-4:] != '.mp3':
                    filename += '.mp3'
                # 转换
                wav_to_mp3(file_path, filename)
                tk.messagebox.showinfo('成功', '转换成功！')


def on_closing():
    if messagebox.askokcancel("退出", "是否关闭本软件？"):
        win.destroy()
        sys.exit(0)


win = tk.Tk()
win.title('格式转换')
win.geometry('400x300')

# 选择按钮
tk.Button(win, text='选择文件', width=10, command=click).place(x=160, y=100)

label = ''
error_log = ''
file_path = ''

# 选择
tk.Label(text='选项：').place(x=50, y=50)
var = tk.StringVar()
combobox = ttk.Combobox(win, textvariable=var)
combobox['value'] = ('jpg转png', 'png转jpg', 'jpg转pdf', 'pdf转jpg', 'mp3转wav', 'wav转mp3')
combobox.place(x=130, y=50)

# 开始按钮
tk.Button(win, text='开始转换', width=10, command=click2).place(x=160, y=220)

# 拦截关闭事件
win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()
