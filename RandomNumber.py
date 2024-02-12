import random
import tkinter as tk


def label_config(text):
    label.config(label, text=text)


root = tk.Tk(className="猜数字游戏")
root.title("随机数生成器")
root.geometry("250x160+300+300")
root.maxsize(250, 160)
root.minsize(250, 160)

label = tk.Label(root, font=("方正兰亭超细黑简体", "15", "bold"))
label.place(x=45, y=1)
label_config("请设置上界和下界")

tk.Label(root, text="下界：", font=("方正兰亭超细黑简体", "10", "bold")).place(x=15, y=40)
entry1 = tk.Entry(root)
entry1.place(x=75, y=40)


tk.Label(root, text="上界：", font=("方正兰亭超细黑简体", "10", "bold")).place(x=15, y=80)
entry2 = tk.Entry(root)
entry2.place(x=75, y=80)


def funcRandomStart(event):
    minn, maxn = int(entry1.get()), int(entry2.get())
    label_config(f"随机数：{random.randint(minn,maxn)}")


button = tk.Button(root, text="生成随机数", width=10, height=2)
button.bind("<Button-1>", funcRandomStart)
button.place(x=90, y=110)

root.mainloop()
