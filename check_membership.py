"""

This script can be used to check all nested groups/members of a given Google group.

"""
#	Written for Python 2.7 and GAM 4.31

#	Should have 2 arguements, Group name (everybody@), type (child/parent/all)
import sys
import shlex
import subprocess
import pdb

gam_alias="/Users/teresajiang/bin/gam/gam"
group_email = sys.argv[1]

#pdb.set_trace()
def getGroupChildren():
#	group_children = os.system("{} print group-members group {}".format(gam_alias, group_name))
	gam_cmd = '%s print group-members group %s' % (gam_alias, group_email)

	args = shlex.split(gam_cmd)
	process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = process.communicate()

	members = []	
	if process.returncode == 0:

		if out:
			out = out.split('\n')
			for i in range(1, len(out)):
				row = out[i].split(',')
				print(row)
				if len(row) >= 3:
					if row[4] == 'USER':
						members.append(row[2].lower())
					elif row[4] == 'GROUP'


	typemem=type(members)
	print(typemem)
	#return members

getGroupChildren()


#gam print group-members group group_name 
#	Specify fields by appending fields <email>

#gam print group-members member group_name
#	Specify fields by appending fields <email>

#	Python pretty print: https://docs.python.org/2/library/pprint.html