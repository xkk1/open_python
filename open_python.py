#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Python便携版启动脚本
author: 小喾苦
date: 2022/8/27 19:51:06
QQ: 3434623263
bilibili: https://space.bilibili.com/513689605
personal website: https://xkk1.github.io/
"""
import tkinter as tk
import tkinter.filedialog
import tkinter.scrolledtext
import webbrowser
import sys
import os
import os.path
# import threading
# import subprocess


pyvi = sys.version_info
python_version = f'{pyvi.major}.{pyvi.minor}.{pyvi.micro}'
python_path = os.path.dirname(os.path.abspath(sys.argv[0])) + os.sep
python_exe = python_path + "python.exe"
pythonw_exe = python_path + "pythonw.exe"


def open_idle():
    os.system(f'cd /d {python_path} & start pythonw Lib\idlelib\idle.pyw')
    # def idle():
    #     os.system('pythonw Lib\idlelib\idle.pyw')
    # threading.Thread(target=idle).start() # , args=(old_verson, ))

def open_python():
    os.system(f'cd /d {python_path} & start python')
    # def python():
    #     subprocess.call(
    #         'python', 
    #         creationflags=subprocess.CREATE_NEW_CONSOLE)
    # threading.Thread(target=python).start() # , args=(old_verson, ))

def open_manuals():
    os.system(f'cd /d {python_path} & start Doc\python{pyvi.major}{pyvi.minor}{pyvi.micro}.chm')
    # def manuals():
    #     os.system(f'Doc\python{pyvi.major}{pyvi.minor}{pyvi.micro}.chm')
    # threading.Thread(target=manuals).start() # , args=(old_verson, ))

def open_module_docs():
    os.system(f'cd /d {python_path} & start python -m pydoc -b')
    # def module_docs():
    #     subprocess.call(
    #         'python -m pydoc -b', 
    #         creationflags=subprocess.CREATE_NEW_CONSOLE)
    # threading.Thread(target=module_docs).start() # , args=(old_verson, ))

def run_py():
    file_name = tkinter.filedialog.askopenfilename(
        title = '打开Python文件(Open Python File)',
        filetypes=[
            ('Python File', '*.py'), 
            ('Python File (no console)', '*.pyw'),
            ('All Files', '*')],
            #initialdir='C:\\Windows'),
            )#返回文件名--打开
    # print(file_name)
    if file_name != '':
        # file_path = ''
        # for i in file_name.split('/')[:-1]:
        #     file_path += i + '/'
        file_path = os.path.dirname(file_name)
        os.system(f'cd /d {file_path} & start "{file_name}" "{python_exe}" "{file_name}"')
        """
        def py(file_name):
            # os.system('pythonw "' + file_name + '"')
            # 打开新的命令提示符
            file_path = ''
            for i in file_name.split('/')[:-1]:
                file_path += i + '/'
            temp = open('temporary_file.bat', 'w')
            temp.write('cd /d %s\n' % file_path)
            temp.write('start python "' + file_name + '"')
            # temp.write(' & PAUSE')
            temp.close()
            subprocess.call(
                'temporary_file.bat', 
                creationflags=subprocess.CREATE_NEW_CONSOLE)
            os.remove('temporary_file.bat')
        threading.Thread(target=py, args=(file_name, )).start()  # , args=(old_verson, ))
        """

def run_pyw():
    file_name = tkinter.filedialog.askopenfilename(
        title = '打开Python文件(Open Python File)',
        filetypes=[
            ('Python File (no console)', '*.pyw'),
            ('Python File', '*.py'), 
            ('All Files', '*')],
            )
    if file_name != '':
        file_path = os.path.dirname(file_name)
        os.system(f'cd /d {file_path} & start "{file_name}" "{pythonw_exe}" "{file_name}"')

def open_scripts():
    os.system(f"cd /d {python_path}Scripts{os.sep} & start cmd")
    """
    def scripts():
        temp = open('temporary_file.bat', 'w')
        temp.write('cd Scripts & cls & cmd')
        temp.close()
        subprocess.call(
            'temporary_file.bat', 
            # shell = True,
            creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        os.remove('temporary_file.bat')
    threading.Thread(target=scripts).start()
    """

def open_path():
    os.system('start explorer %s' % python_path) # os.path.abspath('.'))

def show_information(information="", title="Python便携版信息", icon="Lib\idlelib\Icons\idle.ico"):
    """显示信息"""
    global information_window
    global information_scrolledtext
    
    def save_txt(information=information, title=title):
        filename = tkinter.filedialog.asksaveasfilename(
            title='请选择你要保存的地方', filetypes=[('TXT', '*.txt'), ('All Files', '*')],
            initialfile='%s' % title,
            defaultextension = 'txt',  # 默认文件的扩展名
            )
        if filename == '':
            return False
        else:
            with open(filename, 'w') as f:
                f.write(information)
            return True
    try:
        information_window.deiconify()
        information_window.title(title)
        information_scrolledtext.delete(0.0, tk.END)
        information_scrolledtext.insert(tk.END, information)

    except:
        information_window = tk.Tk()
        information_window.title(title)
        try:  # 尝试设置图标
            information_window.iconbitmap(icon)
        except:
            pass
        information_scrolledtext = tkinter.scrolledtext.ScrolledText(
            information_window,
            width=70,
            height=30,
            undo=True
            )
        information_scrolledtext.pack(expand=tk.YES, fill=tk.BOTH, padx=5, pady=5)
 
        information_scrolledtext.insert(tk.INSERT, information)

        '''创建一个弹出菜单'''
        menu = tk.Menu(information_window,
                    tearoff=False,
                    )

        menu.add_command(label="剪切", command=lambda:information_scrolledtext.event_generate('<<Cut>>'))
        menu.add_command(label="复制", command=lambda:information_scrolledtext.event_generate('<<Copy>>'))
        menu.add_command(label="粘贴", command=lambda:information_scrolledtext.event_generate('<<Paste>>'))
        menu.add_command(label="删除", command=lambda:information_scrolledtext.event_generate('<<Clear>>'))
        menu.add_command(label="撤销", command=lambda:information_scrolledtext.event_generate('<<Undo>>'))
        menu.add_command(label="重做", command=lambda:information_scrolledtext.event_generate('<<Redo>>'))
        menu.add_separator()
        menu.add_command(label="个人网站", command=lambda:webbrowser.open("https://xkk1.github.io/"))
        menu.add_command(label="哔哩哔哩", command=lambda:webbrowser.open("https://space.bilibili.com/513689605"))

        def popup(event):
            menu.post(event.x_root, event.y_root) # post在指定的位置显示弹出菜单

        information_scrolledtext.bind("<Button-3>", popup) # 绑定鼠标右键,执行popup函数
        
        bottom_frame = tk.Frame(information_window)
        bottom_frame.pack()
        
        save_button = tk.Button(
                bottom_frame,
                text="保存为文本文档(*.txt)",
                command=lambda:save_txt(information=information_scrolledtext.get('1.0', tk.END).rstrip()))
        save_button.pack(side=tk.RIGHT, padx=5,pady=5)

        close_button = tk.Button(
                bottom_frame,
                text="关闭",
                command=information_window.destroy)
        close_button.pack(side=tk.RIGHT, padx=5,pady=5)

        def copy_to_clipboard():
            """Copy current contents of text_entry to clipboard."""
            information_window.clipboard_clear()  # Optional.
            information_window.clipboard_append(information_scrolledtext.get('1.0', tk.END).rstrip())
        
        copy_button = tk.Button(
                bottom_frame,
                text="复制内容到剪贴板",
                command=copy_to_clipboard,
                )
        copy_button.pack(side=tk.LEFT, padx=5,pady=5)
        
        information_window.mainloop()

def show_help():
    """显示帮助信息"""
    show_information(information=f"""      Python{python_version}便携版帮助

运行Python脚本时将要运行的脚本托向open_python.bat即可

run_python.bat支持的命令行参数：
    所有python.exe支持的命令行参数
    (注意:命令行参数不要超过9个)

卸载时只需把安装目录下的所有文件删除即可
安装目录：{os.path.abspath('.')}


关于
Python {python_version} 便携版启动脚本
版本：V0.0.4
更新日志：
    1. 解决了不能运行脚本的重大BUG
    2. 重写了打开程序逻辑
    3. 优化了主窗口显示
    4. 更详细的帮助
    5. 帮助增加保存、复制、右键菜单
制作者：小喾苦
联系方式：
  邮箱：3434623263@qq.com
  QQ：3434623263
  哔哩哔哩(www.bilibili.com)：
    用户名：小喾苦
    UID：513689605
    空间：https://space.bilibili.com/513689605
  个人网站：
    Github Pages：https://xkk1.github.io/
    Gitee Pages：https://xkk2.gitee.io/
""",title=f"Python {python_version} 便携版帮助信息")
    

def main():
    """程序入口，显示主窗口"""
    root = tk.Tk()
    root.title(f'Python {python_version}')  # 标题
    root.resizable(0,0)  # 禁止调节窗口大小
    try:  # 尝试打开设置图标
        root.iconbitmap('Lib\idlelib\Icons\idle.ico')
    except:
        pass

    frame = tk.Frame(root)
    frame.pack(padx=4, pady=4)
    
    button_idle = tk.Button(frame, text='启动\nIDLE', command=open_idle)
    button_idle.grid(row=0, column=0, padx=4, pady=4, sticky=tk.E+tk.W)
    
    button_python = tk.Button(frame, text=f'Python\n{python_version}', command=open_python)
    button_python.grid(row=0, column=1, padx=4, pady=4, sticky=tk.N+tk.S+tk.E+tk.W)
    
    button_manuals = tk.Button(frame, text=f'Python {python_version}\nManuals手册', command=open_manuals)
    button_manuals.grid(row=0, column=2, padx=4, pady=4, sticky=tk.N+tk.S+tk.E+tk.W)
    
    button_module_docs = tk.Button(frame, text=f'Python {python_version}\nModule Docs', command=open_module_docs)
    button_module_docs.grid(row=1, column=0, padx=4, pady=4, sticky=tk.N+tk.S+tk.E+tk.W)
    
    button_py = tk.Button(frame, text='运行\n*.py文件', command=run_py)
    button_py.grid(row=1, column=1, padx=4, pady=4, sticky=tk.N+tk.S+tk.E+tk.W)
    
    button_pyw = tk.Button(frame, text='运行\n*.pyw文件', command=run_pyw)
    button_pyw.grid(row=1, column=2, padx=4, pady=4, sticky=tk.N+tk.S+tk.E+tk.W)
    
    button_scripts = tk.Button(frame, text='Scripts\n可用pip等命令', command=open_scripts)
    button_scripts.grid(row=2, column=0, padx=4, pady=4, sticky=tk.N+tk.S+tk.E+tk.W)
    
    button_path = tk.Button(frame, text='打开\n安装目录', command=open_path)
    button_path.grid(row=2, column=1, padx=4, pady=4, sticky=tk.N+tk.S+tk.E+tk.W)
    
    button_help = tk.Button(frame, text='show help\n帮助信息', command=show_help)
    button_help.grid(row=2, column=2, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)
    
    root.mainloop()  #循环消息，让窗口活起来


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    else:
        argv = ''
        for i in sys.argv[1:]:
            argv += ' "' + i +'"'
        file_name = sys.argv[1]
        # file_path = ''
        # for i in file_name.split('\\')[:-1]:
        #     file_path += i + '/'
        file_path = os.path.dirname(file_name)
        os.system(f'cd /d {file_path} & {python_exe} {argv}')
        """
        temp = open('temporary_file.bat', 'w')
        if file_path != '':
            temp.write('cd /d %s\n' % file_path)
        temp.write('"%~dp0python"' + argv + '')
        # temp.write(' & PAUSE')
        temp.close()
        os.system('temporary_file.bat')
        os.remove('temporary_file.bat')
        """
