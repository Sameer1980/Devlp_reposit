data='Luthra, Shivani <shivani.a.luthra@capgemini.com>; on behalf of; IN, Architects Desk <architectsdesk.in@capgemini.com>'
tags=data.split()
print (tags)
# stp1=tags[2].lstrip('<')
# print (stp1)
sm_col_rem=tags[2].rstrip(';')
#print (sm_col_rem)
pos1=data.find('<')
pos2=data.find('>',pos1)
email=data[pos1+1:pos2]
print (f"Email : {email}")
name=tags[1] + ' ' +tags[0].rstrip(',')
print (f"Name : {name}")
#tag_rem_dl_right=tags[9].rstrip('>')
tag_rem_dl_right=tags[9]
#print (sm_col_rem_dl_right)
tag_rem_dl_left=tags[9].lstrip('<')
#print (sm_col_rem_dl_left)
pos3=tag_rem_dl_right.find('<')
pos4=tag_rem_dl_right.find('>',pos3)
#sprint (pos4)
DL_email=tag_rem_dl_right[pos3+1:pos4]
print (f"DL Email ID: {DL_email}")
 