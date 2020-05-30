filename1 = input('输入要复制的文件名：')
filename2 = input('输入新文件名:')

with open(filename1) as f1,open(filename2,'w') as f2:
	f2.write(f1.read())

print('复制成功！')

