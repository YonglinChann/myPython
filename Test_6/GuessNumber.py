import random
import tkinter
from tkinter.messagebox import showerror, showinfo
from tkinter.simpledialog import askinteger

root = tkinter.Tk()
root.title('猜数游戏')
root .geometry('280x80+400+300')
root.resizable(False,False)

varNumber = tkinter.StringVar(root, value = '0')
totalTimes = tkinter.IntVar(root, value = 0)
already = tkinter.IntVar(root, value = 0)
currentNumber = tkinter.IntVar(root, value = 0)
times = tkinter.IntVar(root, value = 0)
right = tkinter.IntVar(root, value = 0)
lb = tkinter.Label(root, text = '请输入一个整数：')
lb.place(x = 10, y = 10, width = 100, height = 20)
entryNumber = tkinter.Entry(root, width=140, textvariable=varNumber)
entryNumber.place(x=110, y=10, width=140, height=20)
entryNumber['state'] = 'disabled'

def closeWindow():
    message = '本次共玩游戏 {0} 次，猜对 {1} 次！\n欢迎下次再玩！'.format(times.get(), right.get())
    tkinter.messagebox.showinfo('战绩', message)
    root.destroy()
root.protocol('WM_DELETE_WINDOW', closeWindow)
def buttonClick():
    if button['text']=='Start Game':
        while True:
            try:
                start = tkinter.simpledialog.askinteger('允许的最小整数', '最小数', initialvalue=1)
                break
            except:
                pass
        while True:
            try:
                end = tkinter.simpledialog.askinteger('允许的最大整数', '最大数', initialvalue=10)
                break
            except:
                pass
        currentNumber.set(random.randint(start, end))
        while True:
            try:
                t = tkinter.simpledialog.askinteger('最多允许猜几次？', '总次数', initialvalue=3)
                totalTimes.set(t)
                break
            except:
                pass
        #已猜次数初始化为0
        already.set(0)
        button['text'] = '剩余次数：' + str(t)
        #把文本框初始化为0
        varNumber.set('0')
        #允许用户开始输入整数
        entryNumber['state'] = 'normal'
        #玩游戏的次数加1
        times.set(times.get() + 1)
    else:
        #一共允许猜几次
        total = totalTimes.get()
        #本次游戏的正确答案
        current = currentNumber.get()
        #玩家本次猜的数
        try:
            x = int(varNumber.get())
        except:
            tkinter.messagebox.showerror('抱歉', '必须输入整数')
            return
        if x == current:
            tkinter.messagebox.showinfo('恭喜', '猜对啦')
            button['text'] = 'Start Game'
            #禁用文本框
            entryNumber['state'] = 'disabled'
            right.set(right.get() + 1)
        else:
            #已猜次数加1
            already.set(already.get()+1)
            if x > current:
                tkinter.messagebox.showerror('抱歉', '猜的数太大了')
            else:
                tkinter.messagebox.showerror('抱歉', '猜的数太小了')
            #可猜次数用完了
            if already.get()==total:
                tkinter.messagebox.showerror('抱歉', '游戏结束了，正确的数是：'+str(currentNumber.get()))
                button['text'] = 'Start Game'
                #禁用文本框
                entryNumber['state'] = 'disabled'
            else:
                button['text'] = '剩余次数：' + str(total-already.get())

button = tkinter.Button(root, text='Start Game', command=buttonClick)
button.place(x=10, y=40, width=250, height=20)
root.mainloop()

