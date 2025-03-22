for i in range(110,210,10):
    i=str(i)
    import os
    os.system(f'python mod_cam_xa.py {i}')
    import shutil
    shutil.make_archive(f'File_mod/cam xa {i}','zip',f'File_mod/cam xa {i}')