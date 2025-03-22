import os
import shutil
for i in range(1,10):
	os.system('py tao_list_tu_dong.py')
	os.system('py main.py VER{}MSP t t s'.format(str(i)))
	folder_name='File_Mod/VER{}MSP'.format(str(i))
	shutil.make_archive(folder_name, 'zip', folder_name)
	if os.path.exists(folder_name):
		shutil.rmtree(folder_name)