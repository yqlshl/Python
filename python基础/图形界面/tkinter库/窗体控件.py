
# 窗体显示操作
import tkinter
import os
LOGO_PATH='resource'+os.sep+'孙海龙.ico'

class Mainform:
	def __init__(self):
		root=tkinter.Tk()	# 创建一个窗体
		root.title('www.shl.com')	# 设置标题
		root.iconphoto(False,tkinter.PhotoImage(file=LOGO_PATH))
		root.maxsize(1000,400)		# 设置窗体j最大尺寸
		root.geometry('500x100+100+100')	# 设置窗体初始化尺寸,小写字母x，+号表示在显示器的位置
		root['background']='LightSlateGray'	# 设置背景颜色，可以从颜色展示py文件中查看选择
		# ======================文本标签定义==================
		label_text=tkinter.Label(root,text='统计科',		# 设置文本标签，在窗体内
		width=200,height=200,bg='#F23011',				# 设置标签宽度、高度、背景色
		fg='#ffffff',									# 设置字体颜色
		font=('微软雅黑',20))								# 设置字体样式大小															
		# ======================图片标签定义==================
		photo=tkinter.PhotoImage(image_path)			# 定义图片组件
		label_photo=tkinter.Label(root,image=photo)		# 图片标签，在窗体内
		# ==================文本标签定义=====================
		text=tkinter.Text(root,width=50,height=15,font=('微软雅黑,10'))	# 设置文本标签
		# 设置文本内容默认值
			 # 在当前光标所处的位置上进行内容的配置
		text.insert('current','孙海龙：')	# thinter.CURRENT='current'
		text.insert('end','www.shl.com')	# thinter.END='end'
		text.pack()                     # 显示文本标签	
		
		photo=tkinter.PhotoImage(image_path)    # 图片组件的定义
		text.image_create('end',image=photo)	# 在文本组件中进行图像显示
		
		
		label_photo.pack()		# 图片组件显示
		label_text.pack()		# 组件进行显示
		
		root.mainloop()		# 显示窗体
# 窗体定义logo，文件'*.ico'文件

Mainform()






