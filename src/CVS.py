# -*- coding:utf-8 -*-

import os, PARAM as p



def get_dir():
	return p.disk +os.sep+ p.serv +os.sep+ p.repo +os.sep

def update(dir, obj, ver, full_path, action):
	b = True
	
	mypath = get_dir() + dir
		
	
	os.chdir(mypath)
	
	#cmd = 'cvs -r -d '+p.CVSROOT+' update -P -r '+ver+' -- '
	cmd = 'cvs -r update -P -r '+ver+' -- '
	
	add = 'cvs add -- '
	commit = 'cvs -r '+p.CVSROOT+' commit -m "Incluido via GetCVS ... " '
	if not os.path.exists(mypath+os.sep+obj):
		print "adicionando ... "
		os.system('cvs -r update -P -A')
		
	print 'atualizando ... '+obj
	f = open('exec.bat','w')
	
	if(action):			
		f.write(str(cmd+obj).replace('\n',' ') )
	else:
		f.write(str('cvs -r update -P -A -- '+obj).replace('\n',' ') )
	f.close()
	os.system('exec.bat')
	os.system('del exec.bat')
		
	#else:
	#	print "adicionando ... "
	#	os.system('cvs -r update -P -A')
	return b	

	
	

	
