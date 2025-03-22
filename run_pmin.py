import os
import shutil
for i in range(1,10):
	os.system('py tao_list_pmin.py')
	os.system('py main.py ver{} t t s'.format(str(i)))
	folder_name='PMINMOD/PACK VER{} PMINMOD'.format(str(i))
	os.system('py tachfilepmin.py VER{} VER{}'.format(str(i),str(i)))
	shutil.make_archive(folder_name, 'zip', folder_name)
	if os.path.exists(folder_name):
		shutil.rmtree(folder_name)