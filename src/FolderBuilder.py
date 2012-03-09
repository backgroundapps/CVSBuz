# -*- coding:utf-8 -*-

import os, PARAM as p

folder_name = ''

def get_full_path(pacote):
	ca = pacote[:5]
	full_path = 'K:'+os.sep+'Pacotes'+os.sep+get_folder_up(ca)+os.sep+pacote
	return full_path

def get_folder_up(ca):
	folder_up = ''
	if int(ca[3:5])<51 and int(ca[3:5]) <> 0:
		folder_up = ca[:3]+'01-'+ca[:3]+'50'
	elif int(ca[3:5]) == 0:
		folder_up = ca[:2]+str((int(ca[2])-1 ))+'51-'+ ca
	else:
		folder_up = ca[:3]+'51-'+ ca[:2] + str( (int(ca[2])+1 ) ) +'00'
	return folder_up
	
	

	
def build(pacote):
	
	os.system('mkdir '+get_full_path(pacote))	
	os.system('mkdir '+get_full_path(pacote)+os.sep+'NAO_ENVIAR')	
	os.system('copy '+'K:\\Pacotes\\SUPORTE\\CHCKLST_NOME_OBJ.xls '+get_full_path(pacote)+os.sep+'NAO_ENVIAR')	
	os.system('copy '+'K:\\Pacotes\\SUPORTE\\CheckListDistribuicao.xls '+get_full_path(pacote)+os.sep+'NAO_ENVIAR')	
	os.system('copy '+'K:\\Pacotes\\SUPORTE\\New_AjudaPacote.exe '+get_full_path(pacote)+os.sep+'NAO_ENVIAR')	
	os.system('copy '+'K:\\Pacotes\\SUPORTE\\bd.sql '+get_full_path(pacote)+os.sep+'NAO_ENVIAR')	
	
	
"""     test methods    """
def test_build():
	build('19601')
#test_build()

def test_full_path():
	print get_full_path('19611')
#test_full_path()



def test_folder_up():
	print get_folder_up('19049')
	print get_folder_up('19050')
	print get_folder_up('19051')
	print get_folder_up('19052')
#test_folder_up()	

def test_dir():	
	print 'CA '+'19049'
	dir('19049','Marcio')

	print 'CA '+'19055'
	dir('19055','fernando')
#test_dir()