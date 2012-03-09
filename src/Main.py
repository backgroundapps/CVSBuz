# -*- coding:utf-8 -*-

import os, CVS, FolderBuilder as builder


	
def move_files(rep, full_path, dir, obj):
	cmd = ''
	if obj[-3:] == 'dll':
		cmd = 'copy '+rep+dir+obj+' '+full_path+os.sep+'NAO_ENVIAR'
	else:	
		cmd = 'copy '+rep+dir+obj+' '+full_path
	os.system(cmd)

def make(): 
	ca = raw_input('Insira o CA: ')
	nome = raw_input('Insira o Nome: ')
	canome = ca+'-'+nome
	pacote = canome.upper()
	
	

	builder.build(pacote)	
	full_path = builder.get_full_path(pacote)
	rep = CVS.get_dir()
	
	f = open(os.path.abspath(os.curdir)+os.sep+'CA.txt')
	
	for i in f:
		lista = i.split(' - Versão ')
		ver = lista[-1].replace(' ', '')
		if len(lista) > 1:
			dirs_o = str(lista[0]).split(os.sep)
			dirs = str(lista[0]).split(dirs_o[-1])
		
			b = CVS.update(dirs[0], dirs_o[-1], ver, full_path, True)
			if b:
				print 'OK'
				move_files(rep, full_path, dirs[0], dirs_o[-1])
				b = CVS.update(dirs[0], dirs_o[-1], ver, full_path, False)
			else:
				print 'Repositório atualizado!'
	
make()	

