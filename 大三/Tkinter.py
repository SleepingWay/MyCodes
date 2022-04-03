# import tkinter as tk
# import tkinter.messagebox
#
# window = tk.Tk()
# window.title('my window')
# window.geometry('600x400')
#
#
# def hit_me():
#     # tk.messagebox.showinfo(title='Hi',message='hahahahha')
#     # tk.messagebox.showerror(title='Hi',message='has error')
#     # tk.messagebox.showwarning(title='Hi', message='has warning')
#     # print(tk.messagebox.askokcancel(title='Hi',message='hahaha'))
#     # print(tk.messagebox.askquestion(title='Hi', message='hahaha'))
#     # print(tk.messagebox.askyesno(title='Hi', message='hahaha'))
#     # print(tk.messagebox.askretrycancel(title='Hi', message='hahaha'))
#     print(tk.messagebox.askyesnocancel(title='Hi', message='hahaha'))
#
#
# b = tk.Button(window, text='hit me', command=hit_me,padx=50,pady=0).pack()
# b.grid(row,minisize=10)
# window.mainloop()
import tkinter as tk


class Cyh:
    # 设定初始窗口界面展示效果
    def __init__(self):
        window = tk.Tk()
        window.geometry("800x500+760+350")
        #按钮
        self.choose = tk.Button(window,text='请选择PE文件',width=15)
        self.choose.grid(row=1,column=1)
        self.fields = tk.Button(window,text='文件头的各项字段',width=15)
        self.fields.grid(row=3,column=1)
        self.blocks = tk.Button(window,text='区块表和区块信息',width=15)
        self.blocks.grid(row=5,column=1)
        self.table = tk.Button(window,text='输入和输出表信息',width=15)
        self.table.grid(row=7,column=1)
        self.resource = tk.Button(window,text='资源表信息',width=15)
        self.resource.grid(row=9,column=1)
        col_count, row_count = window.grid_size()
        for col in range(col_count):
            window.grid_columnconfigure(col, minsize=10)
        for row in range(row_count):
            window.grid_rowconfigure(row, minsize=40)
        #文本框

        window.mainloop()

window = Cyh()