import tkinter as tk
import tkinter.messagebox

# 登录按钮事件处理函数
def login():
	# 获取用户名和密码
	name = entryName.get()    # 获取文本框中输入的账号名
	pwd = entryPwd.get()         # 获取密码框中输入的密码
	password = {}

	with open("pw.txt", "r") as f:
		for line in f:
			line = line.strip().split(' ')
			password[line[0]] = line[1]
	if password.get(name) == pwd:
		tkinter.messagebox.showinfo(title = ' ',message = '登录成功')
	else:
		tkinter.messagebox.showerror(' ',message = '该用户不存在或密码错误！')
	fp.close()


	# if name == 'helloworld' and pwd == '123456':
	# 	tk.messagebox.showinfo(title='提示',
	# 		message='登录成功')
	# else:
	# 	tk.messagebox.showerror('提示', message='该用户不存在或密码错误！')
	# 	varName.set('')                # 清空文本框
	# 	varPwd.set('')                   # 清空密码框

# 第一步：创建应用程序窗口
window = tk.Tk()
window.title('模拟 QQ')
window.geometry('340x240')     # 根据样图宽高比例，设定合适的窗口大小

# 第三步：创建账号密码的标签
labelName = tk.Label(window,
	text='账号  ',
	font=('微软雅黑', 12),
	fg='grey',
	justify=tk.RIGHT
	)
labelName.place(x=50,y=57)

labelPwd = tk.Label(window,
	text='密码  ',
	font=('微软雅黑', 12),
	fg='grey',
	justify=tk.RIGHT
	)
labelPwd.place(x=50,y=96)

# 第四步：创建字符串变量和文本框组件，同时设置关联的变量
varName = tk.StringVar(window, value='')
entryName = tk.Entry(window,
	textvariable=varName)
entryName.place(x=100,y=54)

varPwd = tk.StringVar(window, value='')
entryPwd = tk.Entry(window,
	show='*',
	textvariable=varPwd)
entryPwd.place(x=100,y=94)

# 第五步：创建按钮组件，同时设置按钮事件处理函数
buttonOk = tk.Button(window,
	text='登  录',
	relief='flat',
	command=login)
buttonOk.place(x=85,y=160, width=170, height=38)

# 启动消息循环
window.mainloop()
