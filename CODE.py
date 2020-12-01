import subprocess
print("----------------WELCOME TO LVM AUTOMATION SCRIPT----------------------------")
print()
print()
a=1
while a==1:
	print('''------Enter the Code what you want to do:

		 1) Create PV
		 2) Create VG
		 3) Create LV
		 4) PV Display
		 5) VG Display
		 6) LV Display
		 7) Format LV
		 8) Mount LV
		 9) Increase LVM Size
		 10) Increase VG Size
		 11) Exit
		  ''')

	print("-----------------------------------------------------------------------------")
	choice= int(input())
	if choice==1:
		print("Enter Volume Name( Ex:sdb,sda)")
		volname=input()
		slash="/"
		status=subprocess.getoutput("pvcreate {}dev{}{}".format(slash,slash,volname))
		print("pvcreate {}dev{}{}".format(slash,slash,volname))
		if status[0] == 1:
		  print("PV CREATED!")
		  print()
		  print(status[1])
		  continue
		else:
		  
		  print(status[1])
		  continue
	elif choice==2:
		vgname=input("Enter VG name(EX:abc)")
		volname1=input("Enter PV1 Name(EX:/dev/sda)")
		volname2=input("Enter PV2 Name(EX:/dev/sdv)")
		status=subprocess.getoutput("vgcreate {} {} {}".format(vgname,volname1,volname2))
		if status[0]==1:
		  print("VG CREATED!")
		  print()
		  print(status[1])
		  continue
		else:
		  
		  print(status[1])
		  continue
	elif choice==3:
		print("Enter LV Name")
		volname=input()
		print("Enter VG Name(EX: ABC)")
		vgname=input()
		size=int(input("Enter Size"))
		status=subprocess.getoutput("lvcreate --size +{}G --name {} {}".format(size,volname,vgname))
		print(status)
		if status[0]==1:
		  print("LV CREATED!")
		  print()
		  print(status[1])
		  continue
		else:
		   
		  print(status[1])
		  continue
	elif choice==4:
		print("Enter PV name(EX: /dev/sda)")
		pvname=input()
		status=subprocess.getoutput("pvdisplay {}".format(pvname))
		print(status)
		if status[0]==1:
		  print(status[1])
		  continue
		else:
		  
		  print(status[1])
		  continue
	elif choice==5:
		print("Enter VG name(Ex: iiex)")
		vgname=input()
		status=subprocess.getoutput("vgdisplay {}".format(vgname))
		print(status)
		if status[0]==1:
		  print(status[1])
		  continue
		else:
		  
		  print(status[1])
		  continue
	elif choice==6:
		print("Enter LV name(EX: abc)")
		lvname=input()
		vgname=input("Enter VG Name")
		slash="/"
		status=subprocess.getoutput("lvdisplay {}{}{}".format(vgname,slash,lvname))
		print(status)
		if status[0]==1:
		  print(status[1])
		  continue
		else:
		  
		  print(status[1])
		  continue
	elif choice==7:
		print("Enter VGNAME")
		slash="/"
		vgname=input()
		lvname=input("Enter LV name(Ex: abc)")
		status=subprocess.getoutput("mkfs.ext4 /dev{}{}{}{}".format(slash,vgname,slash,lvname))
		print(status)
		if status[0] ==1:
		  print(status[1])
		  continue
		else:
		  
		  print(status[1])
		  continue
	elif choice==8:
		print("Enter VGNAME(Ex: ABC)")
		slash="/"
		vgname=input()
		lvname=input("Enter LV name")
		mountpoint=input("Enter path of mountpoint")
		status=subprocess.getoutput("mount /dev{}{}{}{} {}".format(slash,vgname,slash,lvname,mountpoint))
		print(status)
		if status[0]==1:
		  print(status[1])
		  continue
		else:
		  
		  print(status[1])
		  continue
	elif choice==9:
		print("Enter VGNAME(Ex: abc)")
		slash="/"
		vgname=input()
		lvname=input("Enter LV name(Ex: abc)")
		newsize=int(input("Enter new size"))
		status=subprocess.getoutput("lvextend --size +{}G /dev{}{}{}{}".format(newsize,slash,vgname,slash,lvname))
		print(status)
		subprocess.getoutput("resize2fs /dev{}{}{} {}".format(slash,vgname,slash,lvname))
		if status[0]==1:
		  print(status[1])
		  continue
		else:
		  
		  print(status[1])
		  continue
	elif choice==10:
		print("Enter VGNAME")
		vgname=input()
		pvname=input("Enter PV name(Ex: /dev/sdb)")
		status=subprocess.getoutput("vgextend {} {}".format(vgname,pvname))
		if status[0]==1:
		  print(status[1])
		  continue
		else:
		  
		  print(status[1])
		  continue

	else:   
		print("GOODBYE")
		exit()
