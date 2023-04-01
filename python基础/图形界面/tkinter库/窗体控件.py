
# 窗体显示操作
import tkinter
import os
LOGO_PATH='resource'+os.sep+'shl.png'

class Mainform:
	def __init__(self):
		self.root=tkinter.Tk()	# 创建一个窗体
		self.root.title('www.shl.com')	# 设置标题
		self.root.iconphoto(False,tkinter.PhotoImage(file=LOGO_PATH))
		self.root.maxsize(1000,400)		# 设置窗体j最大尺寸
		self.root.geometry('500x100+100+100')	# 设置窗体初始化尺寸,小写字母x，+号表示在显示器的位置
		self.root['background']='LightSlateGray'	# 设置背景颜色，可以从颜色展示py文件中查看选择
		# ======================标签控件定义==================
		self.label_text=tkinter.Label(self.root,text='统计科',		# 设置文本标签，在窗体内
		width=200,height=200,bg='#F23011',				# 设置标签宽度、高度、背景色
		fg='#ffffff',									# 设置字体颜色
		font=('微软雅黑',20))								# 设置字体样式大小															
		# ======================图片标签控件定义==================
		photo=tkinter.PhotoImage(image_path)			# 定义图片组件
		self.label_photo=tkinter.Label(self.root,image=photo)		# 图片标签，在窗体内
		# ==================文本标签定义=====================
		self.text=tkinter.Text(self.root,width=50,height=15,font=('微软雅黑,10'))	# 设置文本标签
		# 设置文本内容默认值
			 # 在当前光标所处的位置上进行内容的配置
		self.text.insert('current','孙海龙：')	# thinter.CURRENT='current'
		self.text.insert('end','www.shl.com')	# thinter.END='end'
		self.text.pack()                     # 显示文本标签	
		
		photo=tkinter.PhotoImage(image_path)    # 图片组件的定义
		self.text.image_create('end',image=photo)	# 在文本组件中进行图像显示
	 #=============================按钮控件定义===========================
		photo=tkinter.PhotoImage(file=image_path)	# 创建图片组件
		self.button=tkinter.Button(self.root,text='性感美女',image=photo,
		compound='left',fg='black',# 图片和文件同时显示，定义compound属性，放在图片的对应地方
		font=('微软雅黑',20)
		)		# 创建按钮组件
		 # 按钮绑定事件
		self.button=tkinter.Button(self.root,text='点击输入信息',fg='black',font=('微软雅黑',20))
		self.button.bind('<Button-1>',lambda event:self.event_handle_button(event))
		self.button.pack()
		
		# 窗体绑定一个鼠标单击事件，对应一个鼠标的按键编码‘<Button-1>’（鼠标左键），参数的传递
		self.root.bind('<Button-1>',lambda event: self.event_handle(event,'www.shl.com')) # 绑定处理事件
		
		button.pack()	# 按钮组件显示
		
		label_photo.pack()		# 图片组件显示
		label_text.pack()		# 组件进行显示
		
		root.mainloop()		# 显示窗体
# 窗体定义logo，文件'*.ico'文件
	 # 窗体绑定事件后 处理绑定事件的函数
	def event_handle(self,event,info):
		label_text=tkinter.Label(self.root,text='中国平煤神马集团职业病防治院',width=200,height=200,
		bg='#223011',font=('微软雅黑',20),fg='#ffffff')
		label_text.pack()
		tkinter.messagebox.showinfo(title='shl信息提示',message=info)
	 # 按钮绑定时间后，处理绑定事件的函数
	def event_handle_button(self,event):
		# 执行以下信息会出现输入的对话框
		input_message=tkinter.simpledialog.askstring('提示信息','请输入要显示的信息：')
		label_text=tkinter.Label(self.root,text=input_message,width=200,height=200,
		bg='#223011',font=('微软雅黑',20),fg='#ffffff')
		label_text.pack()



Mainform()






