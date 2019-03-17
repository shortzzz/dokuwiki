import os

rootdir = '/home/andy/projects/dokuwiki/linuxWiki/dokuwiki/data/pages'

i = 0
for root, dirs, files in os.walk(rootdir, topdown=True):
	parent_folder = os.path.basename(os.path.normpath(root))
	print('PAR: '+parent_folder)
	
	directory_names = ''
	for name in dirs:
		#   * [[./linux:start|Linux]]
		directory_names = directory_names + '  * [[./'+name+':start|'+(name.title()).replace('_',' ').replace('-',' ')+']]' + '\n'
		print('DIR: '+name)
	
	file_names = ''
	for name in files:
		if name.endswith('.txt') and name != 'start.txt':
			#   * [[./linux_count_files_in_directory|Linux_Count_Files_In_Directory]]
			name=name.replace('.txt','')
			file_names = file_names + '  * [[./'+name+'|'+(name.title()).replace('_',' ').replace('-',' ')+']]' +'\n'
			print('FIL: '+name)
	print(file_names)
	
	with open(os.path.join(root,'start.txt'),'w') as f:
		print(i)
		if i == 0:
			f.write('====== Inhalt des Wikis ======\n')
		else:
			f.write('====== '+parent_folder.title()+' ======'+'\n')
			pass
		print (directory_names)
		f.write(directory_names)
		print (file_names)
		f.write(file_names)
		#exit()


	i = i+1