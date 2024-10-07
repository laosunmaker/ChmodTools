# ChmodToos
A calculation tool for chmod permission codes on Linux systems
一个用于计算Linux chmod 权限代码的小工具
## 支持
- [x] 含义→代码（正向计算）
- [x] 代码→含义（逆向计算）
- [x] 附加权限(suid,sgid,sticky)
## 源码构建所需依赖
```bash
pip install pyside6
```
## 项目说明
main.py：项目主程序
tools.py：通过pyuic转换而得到的python界面程序
tools.ui：项目ui文件
