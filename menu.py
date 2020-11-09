import os
import getpass

os.system("tput setaf 3")
print("\t\t\tWelcome to my menu\n")

os.system("tput setaf 7")
print("\t\t\t-----------------")

pssd=getpass.getpass("Enter your password : ")

if pssd!="qwer123":
	os.system("tput setaf 2")
	print("PASSWORD INCORRECT")
	os.system("tput setaf 7")
	exit()
op=1
while op!=0:
	print("""
	\t\t 1 For AWS Operation
	\t\t 2 For Hadoop Operation
	\t\t 3 For Docker Operation
	\t\t 4 For Linux Operations
	\t\t 0 To exit
	""")
	op=input()
	if int(op)==1:
		while(1):

			print("""
			\t 1 To create a key pair
			\t 2 To create security group
			\t 3 To create ingress rules for the created security group
			\t 4 To launch the instance
			\t 5 To create EBS Volume
			\t 6 To attach EBS Volume to the given instance
			\t 7 To stop ec2 instance
			\t 8 To start ec2 instance
			\t 9 To terminate ec2 instance
			""")

			ch=input("Enter your choice : ")
			print(ch)


			if int(ch)==1:
				print("Enter the key name to be created:\t")
				key_name=input()
				os.system("aws ec2 create-key-pair --key name {}".format(key_name))
			elif int(ch)==2:
				print("Enter the security name:\t")
				s_name=input()
				print("Enter the VPC Id:\t")
				vpc_id=input()
				os.system("aws ec2 create-security-group --group-name {} --vpc-id {}".format(s_name,vpc_id))
			elif int(ch)==3:
				print("Enter the security group id:\t")
				s_id=input()
				print("Enter the IP Protocol:\t")
				protocol=input()
				print("Enter the Port No:\t")
				port_no=input()
				print("Input IP Ranges:\t")
				ip_range=input()
				os.system("aws ec2 authorize-security-group-ingress --group-id {} --ip-permissions IpProtocol ={},FromPort={}, ToPort={}, IpRanges=[{}]".format(s_id,protocol,port_no,port_no,ip_range))
			elif int(ch)==4:
				print ("Enter the AMI Id to launch the instance:\t")
				ami_id=input()
				print("Enter the instance type:\t")
				i_type=input()
				print("Enter the number of instance to be launched:\t")
				count=input()
				print("Enter the subnet id for the instance:\t")
				sub_id=input()
				print("Enter the security group id for the instance:\t")
				sg_id=input()
				print("Enter the security  key for the instance:\t")
				key=input()
				os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --kep-name {}".format(ami_id, i_type, count, sub_id, sg_id, key))
			elif int(ch)==5:
				print ("Enter the availability zone to create the volume:\t")
				a_zone=input()
				print("Enter the size of the volume:\t")
				size=input()
				os.system("aws ec2 create-volume --availability-zone {} --size {}".format(a_zone,size))
			elif int(ch)==6:
				print ("Enter volume id to attach to ec2 instance:\t")
				a_zone=input()
				print("Enter the instance id to attach EBS volume:\t")
				i_id=input()
				os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(a_zone,i_id))
			elif int(ch)==7:
				print("Enter the instance id to stop the ec2 instance:\t")
				i_id=input()
				os.system("aws ec2 stop-instances --instance-ids {}".format(i_id))
			elif int(ch)==8:
				print("Enter the instance id to start the ec2 instance:\t")
				i_id=input()
				os.system("aws ec2 start-instances --instance-ids {}".format(i_id))
			elif int(ch)==9:
				print("Enter the instance id to terminate the ec2 instance:\t")
				i_id=input()
				os.system("aws ec2 terminate-instances --instance-ids {}".format(i_id))
			else:
				print("INVALID INPUT")
	elif int(op)==2:
		print("Hadoop Operation")
	elif int(op)==3:
		 while(1):             
            			print("""
			\t1 to run a container
			\t2 to start a container
			\t3 to stop a container
			\t4 to remove a container
			\t5 to view logs for a container
			\t6 to list all containers
			\t7 to list all images
			""")
		            	choice=int(input())
           			 os.system("clear")
           			 if choice==1:
                				print("Enter container name")
               				 name=input()
               				 print("Enter image name")
              				 img_name=input()
               				 os.system("docker run -it --name {0} {1}".format(name,img_name))
           			elif choice==2:
               				 print("Enter container name/id")
               				 name=input()
               				 print("Starting container...") 
               				 os.system("docker start {}".format(name))
            			elif choice==3:
               				 print("Enter container name/id")
               				 name=input()
               				 print("Stopping container")
               				 os.system("docker stop {}".format(name))
            			elif choice==4:
                				print("Ënter container name/id")
              				name=input()
                				print("Removing container...")
               				os.system("docker stop {}".format(name))
                				os.system("docker rm -f {}".format(name))
           			elif choice==5:
                				print("Enter container name")
                				name=input()
                				print("Logs for {} are:".format(name))
                				os.system("docker logs {}".format(name))
            			elif choice==6:
                				print("Available containers are:")
                				os.system("docker ps")
           			elif choice==7:
                				print("Available images are:")
                				os.system("docket images")
              			else:
				print("Invalid Choice\n")
	elif int(op)==4:            
       		 while (1):
            			print("""
			Enter:			
			\t1 to view date and time
			\t2 to view calendar
			\t3 to start a service
			\t4 to stop a service
			\t5 to enable a service
			\t6 to disable a service
			\t7 to install a software using yum (yum repository must be configured)
			\t8 to uninstall a software using yum
			\t9 to view the details of a directory
			\t10 to open a file using gedit
			""")
            			choice=int(input())
           			os.system("clear")
			elif choice==1:
                				os.system("date")
            			elif choice==2:
                				os.system("cal")
            			if choice==3:
                				print("Enter service name")
                				name=input()
                				os.system("systemctl start {}".format(name))
           		 	elif choice==4:
                				print("Enter service name")
                				name=input()
                				os.system("systemctl stop {}".format(name))
            			elif choice==5:
                				print("Enter service name")
                				name=input()
                				os.system("systemctl enable {}".format(name))
            			elif choice==6:
                				print("Enter service name")
                				name=input()
                				os.system("systemctl disable {}".format(name))
            			elif choice==7:
                				print("Enter software name")
               				name=input()
                				os.system("yum install {}".format(name))
           			elif choice==8:
                				print("Enter software name")
                				name=input()
                				os.system("yum uninstall {}".format(name))
            			elif choice==9:
                				print("Enter directory name/address")
                				name=input()
                				os.system("ls {}".format(name))
            			elif choice==10:
                				print("Enter file name/address")
                				name=input()
               				os.system("gedit {}".format(name))
            			else:
				print("Invalid Choice\n")
	
	elif int(op)==0:
		print("Invalid Choice\n")
