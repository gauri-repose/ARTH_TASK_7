def RH():    #this function used for 'Run RHEL8 Commands'
    os.system("espeak-ng 'In   which  Command  do  you  want  to Run?  Press  Valid  Number '")
    while True:
        os.system("tput setaf 4")
        print('\t\t\t Choose the Options for your Requirements')
        os.system("tput setaf 7")
        print("""Press 1. for date
Press 2. for calendar
Press 3. for check IP address
Press 4. for Check Internet Connectivity
Press 5. for create a file
Press 6. for create New user
Press 7. to exit this and back to main menu""")
        os.system("tput setaf 3")
        ip = input("Press the number which is you want to run:")
        os.system("tput setaf 7")
        if int(ip)==1:
            os.system("date")
        elif int(ip)==2:
            os.system("cal")
        elif int(ip)==3:
            os.system("ifconfig enp0s3")
        elif int(ip)==4:
            os.system("ping goo.gl -c 4")
        elif int(ip)==5:
            i = input("write file name: ")
            os.system("gedit {}".format(i))
        elif int(ip)==6:
            i = input("type username: ")
            os.system("useradd {}".format(i))
            os.system("passwd {}".format(i))             
        elif int(ip)==7:
            break
        else:
            print("Only press options number")
            
        input('Enter to continue......')
        os.system("clear")
      
    

def PR():  #this function used 'Create a Partition'
        os.system("clear")
        os.system("tput setaf 3")
        print("\t\tFor Partition\n")
        os.system("tput setaf 7")
        os.system("espeak-ng 'In   Which  type  of   Partition   are   you   want   to   do?'")
        print('''Press 1. for LVM (Logical volume Partition) Partition
Press 2. for Increase or Decrease the size of Static Partiton''')

        ip = input("Press Option for particular Partition: ")

        if int(ip)==1:
            a = input("Confirm Your System have Attached New Hard Disk [Y/N]? ")
            b = "Y"
            if a != b:
                print("First you ADD new Hard Disk")
                exit()

            os.system("clear")
            while True:
                os.system("tput setaf 3")
                print("\t\tLVM Partition\n")
                os.system("tput setaf 7")
                print("""Press 1: to see device name
Press 2: to see description of  Physical volume
Press 3: Create Physical Volume
Press 4: to see description of Volume Group
Press 5: Create Volume Group
Press 6: to see description of Logical Volume
Press 7: Create Logical Volume
Press 8: Format the partition with (ext4) type
Press 9: Attach/Linked the partition with folder
Press 10: Check my device is linked with folder
Press 11: to exit this partition and back to main menu""")

                ch = input("Enter Option: ")

                if int(ch)==1:
                    os.system("fdisk -l")

                elif int(ch)==2:
                    os.system("pvdisplay")

                elif int(ch)==3:
                    d = input("Write your device name: ")
                    os.system("pvcreate {}".format(d))

                elif int(ch)==4:
                    os.system("vgdisplay")

                elif int(ch)==5:
                    g = input("Write Group name: ")
                    d = input("Write your 1st device name: ")
                    d2 = input("Write your 2nd device name: ")
                    os.system("vgcreate {0} {1} {2}".format(g,d,d2))

                elif int(ch)==6:
                    os.system("lvdisplay")
                elif int(ch)==7:
                    s = input("Give the Size of Logic Volume with (K,M,G,T): ")
                    n = input("Write Name of your Logic Volme: ")
                    os.system("lvcreate --size {0} --name {1}".format(s,n))

                elif int(ch)==8:
                    f = input("Write Device name which is you want to format: ")
                    os.system("mkfs.ext4 {}")
                    print("this device is formatted with (ext4) type...Done")

                elif int(ch)==9:
                    m = input("Write device name which is You want to attached/linked: ")
                    f = input("Write folder name (where you want to linked): ")
                    os.system("mount {0} {1}".format(m,f))

                elif int(ch)==10:
                    os.system("df -h")

                elif int(ch)==11:
                    break

                else:
                    print("Please 'Press' valid number's....")

                    
        if int(ip)==2:
            os.system("clear")
            while True:
                os.system("tput setaf 3")
                print("\t\tElasticity of Static Partition \n")
                os.system("tput setaf 7")
                print('''Press 1. to see report of File System and Disk
Press 2. for Increase/Decrease the size
Press 3. for Formatting the Increasing part
Press 4. for Linking the Partition
Press 5. For Back ''')

                i = input("Enter Options: ")
                if int(i)==1:
                    os.system("lsblk")
                    os.system("df -h")
                    os.system("tput setaf 6")
                    print("\tNote in which Partition you want to Increase or Decrease the size, also note the mountpoint/folder name")
                    os.system("tput setaf 7")
                
                elif int(i)==2:
                    d = input("Type Disk name: ")
                    os.system("umount {}".format(d))
                    os.system("fdisk {}".format(d))
                
                elif int(i)==3:
                    p = input("Type Partition disk name for format : ")
                    os.system("e2fsck -f {}".format(p))
                    os.system("resize2fs {}".format(p))
                
                elif int(i)==4:
                    p = input("Type partition disk name for linking: ")
                    m = input("Type the folder name for linking: ")
                    os.system("mount {0} {1}".format(p,m))
                
                elif int(i)==5:
                    break
                else:
                    os.system("tput setaf 1")
                    print("Only Press valid Option")
                    os.system("tput setaf 7")



def EX(): #this function used to 'Terminate this Program'
        os.system("tput setaf 6")
        os.system('espeak-ng "Ok.. Bye.."')
        print("Ok.. Bye..")
        os.system("tput setaf 7")
        exit()

def WB():#this function used for Web Browser
    while True:

        import webbrowser
        os.system("tput setaf 3")
        print("\t\t Web Browser\n")
        os.system("tput setaf 7")
        print('''1. Open Google Search on Browser
2. Open Facebook page for Login
3. Open Gmail page for Login
4. Open Docker-Hub page
5. Open AWS on browser
6. Back to main menu''')

        i = input("Type Option : ")
        if int(i)==1:
            webbrowser.open("https://www.google.com/")
        elif int(i)==2:
            webbrowser.open("https://www.facebook.com/")
        elif int(i)==3:
            webbrowser.open("google.com%2Fmail%2F&osid=1&service=mail&ss=1&ltmpl=default&rm=false")
        elif int(i)==4:
            webbrowser.open("https://hub.docker.com/")
        elif int(i)==5:
            webbrowser.open("https://aws.amazon.com/")
        elif int(i)==6:
            break
        else:
            os.system("tput setaf 1")
            print("Press Only valid options...")
            os.system("tput setaf 7")

def WS(): #this function is used to Configure web server
    os.system("clear")
    while True:

        os.system("tput setaf 3")
        print("\t\tConfiguring Web Server\n")
        os.system('tput setaf 7')
        print('''1. Check the Web Server Software Install or Not
2. If not, Then Install Web Server Software
3. Check status, Web Service Start or Not
4. If not. Then Start the Web Service
5. Create File which is you want to show the Client
6. Check list of how many files we have :
7. Check this file on Web Browser
8. Back to main menu''')

        i = input("Enter Options: ")
        if int(i)==1:
            os.system("yum list httpd")
        elif int(i)==2:
            os.system("yum install httpd")
        elif int(i)==3:
            os.system("systemctl status httpd")
        elif int(i)==4:
            os.system("systemctl start httpd")
        elif int(i)==5:
            f = input("Type File name: ")
            os.system("gedit {}".format(f))
        elif int(i)==6:
            os.system("ls /var/www/html")
        elif int(i)==7:
            f = input("Type which file you want to Show: ")
            print(" wait ....browser is open..")
            import webbrowser
            webbrowser.open("http://192.168.43.223/{}".format(f))
        elif int(i)==8:
            break
        else:
            os.system("tput setaf 1")
            print("Press only Valid Options..")
            os.system("tput setaf 7")

def DO(): #this function is used to Docker set-up
    os.system("clear")
    while True:

        os.system("tput setaf 3")
        print("\t\tDOCKER Set-Up\n")
        os.system("tput setaf 7")
        print('''1. Check Docker install or not
2. If not, Then Install Docker
3. Start the docker service 
4. Check Information about Docker
5. Show How many Docker Image have
6. Download Docker Image
7. Check How many Container (O.S.) are running or stopped
8. Launch New Container (O.S.)
9. Go Inside the Container (O.S.)
10. Shut down Container (O.S.)
11. Start the Container (0.S.)
12. Back to main menu''')
        
        i = input("Enter Options : ")
        if int(i)==1:
            os.system("docker version")
        elif int(i)==2:
            os.system("yum install docker-ce --nobest")
        elif int(i)==3:
            os.system("systemctl start docker")
        elif int(i)==4:
            os.system("docker info")
        elif int(i)==5:
            os.system("docker images")
        elif int(i)==6:
            print("First, Search the OS Image ....")
            s = input("Write Image name for searching: ")
            os.system("docker search {}".format(s))
            print("Now, Go for Download the Image....")
            d = input("Write the Image name: ")
            v = input("Type Image Version name: ")
            os.system("docker pull {0}:{1}".format(d,v))
        elif int(i)==7:
            os.system("docker ps -a")
        elif int(i)==8:
            n = input("Type Container name: ")
            m = input("Type Image name: ")
            v = input("Type Image Version name: ")
            os.system("docker run -dit --name {0} {1}:{2}".format(n,m,v))
        elif int(i)==9:
            n = input("Type Container name: ")
            os.system("docker attach {}".format(n))
        elif int(i)==10:
            n = input("Type Container name: ")
            os.system("docker stop {}".format(n))
        elif int(i)==11:
            n = input("Type Container name: ")
            os.system("docker start {}".format(n))
        elif int(i)==12:
            break
        else:
            os.system("tput setaf 1")
            print("Enter Only valid Options....")
            os.system("tput setaf 7")

def RM():  #this function is used to Remote Login
    os.system("clear")
    while True:
        print('''Press 1. for Go to Login in Remote System
Press 2. for Only Execute Some Command in Remote System
Pres 3. Back main menu''')
        i = input("Enter Valid Option: ")
        if int(i)==1:
            ip = input("type IP Address of the Remote system: ")
            os.system("ssh {} -y".format(ip))
        elif int(i)==2:
            ip = input("type IP Address of the Remote system: ")
            c = input("Type the Command name: ")
            os.system("ssh {0} -y {1}".format(ip,c))
        elif int(i)==3:
            break
        else:
            os.system("tput setaf 1")
            print("Enter Only valid Options....")
            os.system("tput setaf 7")

def HP():  #this function is used to make a Hadoop Cluster
    os.system("clear")
    while True:
        os.system("tput setaf 3")
        print("\t\tMaking a Hadoop Cluster\n")
        os.system("tput setaf 7")
        print('''1. Check Hadoop Software Install or Version of Hadoop
2. Make a System as a Node (Name/Data/Client)
3. Start this Node (Name/Data)
4. Check the Service is Start
5. Check the Report of HDFS
6. Upload File in HDFS
7. Check the folder in HDFS
8. Read the File from HDFS
9. Back in main menu''')
        i = input("Enter Options: ")
        if int(i)==1:
            os.system("hadoop -version")

        elif int(i)==2:
            while True:
                print("""Press 1. for make system as a Name-node
Press 2. format the Name-node
Press 3. for make system as a Data-node
Press 4. for make system as a Client-node
Press 5. back to HDFS Cluster menu..""")
                n = input("Press Valid Number to make system as Node: ")
                if int(n)==1:
                    f = input("Type folder name: ")
                    os.system("mkdir /{}".format(f))
                    print(" Your /{} is Created...".format(f))
                    os.system("vim /etc/hadoop/hdfs-site.xml")
                    os.system("vim /etc/hadoop/core-site.xml")
                elif int(n)==2:
                    os.system("hadoop namenode -format")
                elif int(n)==3:
                    f = input("Type folder name: ")
                    os.system("mkdir /{}".format(f))
                    print(" Your /{} is Created...".format(f))
                    print("...Open hdfs-site.xml file...")
                    os.system("vim /etc/hadoop/hdfs-site.xml")
                    os.system("vim /etc/hadoop/core-site.xml")
                elif int(n)==4:
                    os.system("vim /etc/hadoop/core-site.xml")
                elif int(n)==5:
                    break
                else:
                    os.system("tput setaf 1")
                    print("Press Only valid Options for making Node....")
                    os.system("tput setaf 7")

        elif int(i)==3:
            while True:
                print("""Press 1. for Start the Name-node
Press 2. for Start the Data-node
Press 3. back to HDFS Cluster menu...""")
                s = input("Press No. for Start the Node: ")
                if int(s)==1:
                    os.system("hadoop-daemon.sh start namenode")
                elif int(s)==2:
                    os.system("hadoop-daemon.sh start datanode")
                elif int(s)==3:
                    break
                else:
                    os.system("tput setaf 1")
                    print("Press Only valid Options for Starting the Node....")
                    os.system("tput setaf 7")

        elif int(i)==4:
            os.system("jps")

        elif int(i)==5:
            os.system("hadoop dfsadmin -report")

        elif int(i)==6:
            f = input("Type the Location/name of file: ")
            os.system("hadoop fs -put {}".format(f))

        elif int(i)==7:
            os.system("hadoop fs -ls /")

        elif int(i)==8:
            f = input("Type which file you want to read: ")
            os.system("hadoop fs -cat /{}".format(f))

        elif int(i)==9:
            break

        else:
            os.system("tput setaf 1")
            print("Press Only valid Options for....")
            os.system("tput setaf 7")

def AWS():  #this function is used to AWS-CLI
    os.system("clear")
    while True:
        os.system("tput setaf 3")
        print("\t\tAWS-CLI\n")
        os.system("tput setaf 7")
        print('''1. Check AWS-CLI Install
2. AWS Help
3. AWS Configure/Authentication process:
4. Check Descriptions of Instances
5. Launch Amazon-Linux Instance on AWS Cloud
6. Stop Instances
7. Start Instances
8. Back to main menu..''')
        i = input("Enter Options: ")
        if int(i)==1:
            os.system("aws --version")
        elif int(i)==2:
            os.system("aws help")
        elif int(i)==3:
            os.system("aws configure")
        elif int(i)==4:
            os.system("aws ec2 describe-instances")
        elif int(i)==5:
            a = input("How many instances you want to launch: ")
            os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count {0} --key-name alinux".format(a))
        elif int(i)==6:
            a = input("Type Instance Id: ")
            os.system("aws ec2 stop-instances --instance-ids {}".format(a))
        elif int(i)==7:
            a = input("Type Instance Id: ")
            os.system("aws ec2 start-instances --instance-ids {}".format(a))
        elif int(i)==8:
            break
        else:
            os.system("tput setaf 1")
            print("Press Only valid Options for....")
            os.system("tput setaf 7")

import os
os.system('tput setaf 3')
print("\t\t\t Welcome to Mig Home")
os.system("tput setaf 7")
print('\t\t\t --------------------------\n')

os.system("espeak-ng 'Hello..  My name is Mig, This is My-Area I gonna  Helping  You to Set-Up Your  Environments..' ")

while True :
    os.system("tput setaf 2")
    print("\tPress what you want to do....\n")
    os.system("tput setaf 7")
    print('''1. Run RHEL8 Commands
2. Online Python Interpreter
3. Setup Hadoop Cluster 
4. Create a Partition
5. AWS-CLI used
6. Docker Technology Set-up
7. Configure Web Server
8. Open Browser 
9. Go for SSH Login
10. Terminate this "Mig Home"..''')
    os.system('espeak-ng "Read   this   menu  and          Enter  you  valid   Options   which is  you  want  to do"')
    os.system("tput setaf 3")
    i = input("Enter your choice which is you want to do: ")
    os.system("tput setaf 7")

    if int(i)==1:
        RH()
    elif int(i)==2:
        os.system("python3")
    elif int(i)==3:
        HP()
    elif int(i)==4:
        PR()
    elif int(i)==5:
        AWS()
    elif int(i)==6:
        DO()
    elif int(i)==7:
        WS()
    elif int(i)==8:
        WB()
    elif int(i)==9:
        RM()
    elif int(i)==10:
        EX()
    else:
        os.system("tput setaf 1")
        print("please only Press valid Options..")
        os.system("tput setaf 7")

    input("ENTER to continue ...." )
    os.system("clear")

