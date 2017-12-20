#!/usr/bin/python
import  tkSimpleDialog
from Tkinter import *
import os
import tkMessageBox
import time
import subprocess


class Manager(object):
    def __init__(self):
        self.GUI = Tk()
        self.GUI.configure(background='black')
        self.GUI.title("welcome to the manager tool")
        self.GUI.geometry("1200x600")
        self.LEL1 = Label(self.GUI, text='admin control', font=35, fg='black', bg="orange").pack(
            side=TOP, anchor=N, expand=YES
        )

        self.LEL2 = Label(self.GUI, text='apache2 server', font=35, fg='black', bg='orange',).pack(
            side=TOP, anchor=NW, expand=YES
        )
        self.buttn1 = Button(self.GUI, text='start', command=self.ApacheStart)
        self.buttn1.place(x=0, y=150)
        self.buttn2 = Button(self.GUI, text='stop', command=self.ApacheStop)
        self.buttn2.place(x=60, y=150)
        self.buttn3 = Button(self.GUI, text='status', command=self.ApacheStatus)
        self.buttn3.place(x=120, y=150)
        self.LEL3 = Label(self.GUI, text='bind9 server', font=35, fg='black', bg='orange' ).pack(
            side=TOP, anchor=NW, expand=YES
        )
        self.buttn4 = Button(self.GUI, text='start', command=self.BindeStart)
        self.buttn4.place(x=0, y=270)
        self.buttn5 = Button(self.GUI, text='stop', command=self.BindStop)
        self.buttn5.place(x=60, y=270)
        self.buttn6 = Button(self.GUI, text='status',command=self.BindStatus)
        self.buttn6.place(x=120, y=270)



        self.LEL4 = Label(self.GUI, text='mysql server', font=35, fg='black', bg='orange' ).pack(
            side=TOP, anchor=NW, expand=YES
        )

        self.buttn7 = Button(self.GUI, text='start', command=self.MysqlStart)
        self.buttn7.place(x=0, y=410)
        self.buttn8 = Button(self.GUI, text='stop', command=self.MysqlStop)
        self.buttn8.place(x=60, y=410)
        self.buttn9 = Button(self.GUI, text='status', command=self.MysqlStatus)
        self.buttn9.place(x=120, y=410)

        self.LEL5 = Label(self.GUI, text='squid server', font=35, fg='black', bg='orange' ).pack(
            side=TOP, anchor=NW, expand=YES
        )

        self.buttn10 = Button(self.GUI, text='start', command=self.SquidStart)
        self.buttn10.place(x=0, y=520)
        self.buttn11 = Button(self.GUI, text='stop', command=self.SquidStop)
        self.buttn11.place(x=60, y=520)
        self.buttn12 = Button(self.GUI, text='status', command=self.SquidStatus)
        self.buttn12.place(x=120, y=520)

        self.SystemCtl = Label(self.GUI, text='journalctl', font=25, fg='black', bg='orange').place(x=950, y=120)
        self.buttnSystemctl = Button(self.GUI, text='check', command=self.Journalctl).place(x=950, y=160)


        self.LELCreateUser = Label(self.GUI, text='create users and\ncheck users and groups', fg='black', bg='orange', font=25).place(x=950,y=210)
        self.ButtnCreateUser =   Button(self.GUI, text='click here', command=self.PanelUsersAndGroups).place(x=950, y=259)
        self.wiresharkLeL= Label(self.GUI, text='to see the traffic use\nwireshark',fg='black', bg='orange', font=25).place(x=950,y=310)
        selfwiresharkButt = Button(self.GUI, text='wireshark', command=self.WiresharkCall).place(x=950, y=360)

        mainloop()

    def PanelUsersAndGroups(self):
        self.UsersAndGroups = Tk()
        self.UsersAndGroups.configure(background='black')
        self.UsersAndGroups.title('Users and groups')
        self.UsersAndGroups.geometry('660x660')
        self.UsersAndGroupsLebel1 = Label(self.UsersAndGroups, text='welcome to create and check status of users',
                                          font=25, fg='black', bg='orange').place(x=170, y=0)
        self.UsersAndGroupsLebel2 = Label(self.UsersAndGroups,
                                          text='here you can create a user with a password^__^',
                                          font=25, fg='black', bg='orange').place(x=170, y=100)
        self.UsersAndGroupsLebel3 = Label(self.UsersAndGroups, text='the first option is adduser').place(x=170, y=176)
        self.UsersAndGroupsEntry = Entry(self.UsersAndGroups, )
        self.UsersAndGroupsEntry.place(x=360, y=172)
        self.UsersAndGroupspasswod1 = Label(self.UsersAndGroups, text='insert the password').place(x=170, y=210)
        self.UsersAndGroupspasswodEny1  = Entry(self.UsersAndGroups, show='*')
        self.UsersAndGroupspasswodEny1.place(x=360,y=210)
        self.UsersAndGroupsButton1 = Button(self.UsersAndGroups, text='adduser', command=self.Print2).place(x=530, y=190)
        self.UsersAndGroupsLebel4 = Label(self.UsersAndGroups, text='here you can check a user hes groups', font=5, fg='black',bg='orange').place(x=170, y=250)
        self.UsersAndGroupsLebel5 = Label(self.UsersAndGroups, text='insert the name of the user \nin the system to check ').place(x=170, y=280)
        self.UsersAndGroupsEntryUserCheck = Entry(self.UsersAndGroups,)
        self.UsersAndGroupsEntryUserCheck.place(x=360,y=285)
        self.UsersAndGroupsEntryUserCheckButt = Button(self.UsersAndGroups, text="check", command=self.CheckUsersGroupsAndAll).place(x=530, y=285)
        self.UsersAndGroupsLebel7 = Label(self.UsersAndGroups, text='to see the all mounts').place(x=170,y=323)
        self.UsersAndGroupsButton3 = Button(self.UsersAndGroups, text='see the mounts',command=self.CheckMounts).place(x=360,y=320)
        self.UsersAndGroupsLebel6 = Label(self.UsersAndGroups, text='click to to see the all users').place(x=170, y=390)
        self.UsersAndGroupsButton2 = Button(self.UsersAndGroups, text='click to see users',command=self.CheckAllUsers).place(x=360, y=390)
        self.UsersAndGroupsLebel6 = Label(self.UsersAndGroups, text='click to to see the all groups').place(x=170, y=430)
        self.UsersAndGroupsButton2 = Button(self.UsersAndGroups, text='click to see groups', command=self.CheckAllGroups).place(x=360, y=430)
        self.UsersAndGroupsLebel8 = Label(self.UsersAndGroups, text='to create a new mount("new mount disk")').place(x=170,y=353)
        self.UsersAndGroupsButton4 = Button(self.UsersAndGroups, text='click to create', command=self.CreateNewMount).place(x=435,y=353)
        self.UsersAndGroupsLebel9 = Label(self.UsersAndGroups, text='insert the username\nyou want to change  the password').place(x=170, y=460)
        self.UsersAndGroupsEntry2 = Entry(self.UsersAndGroups)
        self.UsersAndGroupsEntry2.place(x=390,y=468)
        self.UsersAndGroupsButton5 = Button(self.UsersAndGroups,  text='for change password', command=self.ChangeAPasswordUser).place(x=390, y=490)
        self.UsersAndGroupsL10 = Label(self.UsersAndGroups, text='for create a new group\ninsert here the name group').place(x=170,y=530)
        self.UsersAndGroupsEntry3 = Entry(self.UsersAndGroups)
        self.UsersAndGroupsEntry3.place(x=350,y=530)
        self.UsersAndGroupsButton6 = Button(self.UsersAndGroups, text='for create a group', command=self.CreateAgroup).place(x=350, y=560)
        self.UsersAndGroupsL11 = Label(self.UsersAndGroups, text='for add users to another\ngroups').place(x=170,y=600)
        self.UsersAndGroupsButton7 = Button(self.UsersAndGroups,text='for add users to groups', command=self.ToAddUsersToAnotherGroups).place(x=350,y=600)

    def WiresharkCall(self):
        os.system('wireshark')

    def ToAddUsersToAnotherGroups(self):
        infoAbutUser = tkSimpleDialog.askstring('hello', 'insert the user you want to add to the group')
        infoAbutGroup = tkSimpleDialog.askstring('hello', 'now insert the name of the group')
        os.system("usermod -aG "+ infoAbutGroup + '\t' + infoAbutUser)
        tkMessageBox._show(title='finish the add', message='we finish the add user '+ infoAbutUser+" to the "+ infoAbutGroup+' group')


    def CreateAgroup(self):
        os.system('groupadd '+ self.UsersAndGroupsEntry3.get())
        tkMessageBox._show(title='create a new group', message='we create a new group\nGroupName: '+ self.UsersAndGroupsEntry3.get())


    def ChangeAPasswordUser(self):
        ChangePasswordUser = tkSimpleDialog.askstring('insert a password', 'insert the new password for the user', show='*')
        os.system('echo '+self.UsersAndGroupsEntry2.get()+ ":" + ChangePasswordUser+ "|" + "chpasswd")
        tkMessageBox._show(title='the password is cheaged', message='this user password is changed\n user: '+self.UsersAndGroupsEntry2.get())






    def CreateNewMount(self):
        mountDirctory = tkSimpleDialog.askstring('write and a new dirctory', 'write the dirctory you want to create a new folder of add a new mount')
        os.system('mkdir -p '+ mountDirctory +"")
        os.system("gnome-terminal -e 'watch fdisk -l'")
        mountinfoDisk = tkSimpleDialog.askstring('isert your new disk', 'plaese insert the dirctory of the new disk and\nlook on the another window  hopup')
        os.system("mount -t ext2 "+ mountinfoDisk + "\t" + mountDirctory+ "")

    def CheckMounts(self):
        self.command4 = ('mount')
        self.get4 = subprocess.Popen(self.command4, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.text4 = self.get4.stdout.read()
        self.CheckCheck = Tk()
        self.CheckCheck.configure(background='black')
        self.CheckCheck.title('see the mounets')
        self.CheckCheck.geometry('1100x600')
        self.CheckCheckLeb = Label(self.CheckCheck, text=self.text4).pack(anchor=CENTER)


    def CheckAllGroups(self):
        self.command3 = ('cat','/etc/group')
        self.get3 = subprocess.Popen(self.command3, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.text3 = self.get3.stdout.read()
        self.CheckCheck = Tk()
        self.CheckCheck.configure(background='black')
        self.CheckCheck.title('all the groups in the system')
        self.CheckCheck.geometry('600x900')
        self.CheckCheckLeb = Label(self.CheckCheck, text=self.text3).pack(anchor=CENTER)



    def CheckAllUsers(self):
        self.command2 = ('cat','/etc/passwd')
        self.get2 = subprocess.Popen(self.command2, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.text2 = self.get2.stdout.read()
        self.CheckCheck = Tk()
        self.CheckCheck.configure(background='black')
        self.CheckCheck.title('all the users in the system')
        self.CheckCheck.geometry('690x900')
        self.CheckCheckLeb = Label(self.CheckCheck, text=self.text2).pack(anchor=CENTER)
    def CheckUsersGroupsAndAll(self):
        self.command1 = (['id', self.UsersAndGroupsEntryUserCheck.get()])
        self.get = subprocess.Popen(self.command1, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.text = self.get.stdout.read()
        tkMessageBox._show(title='hello',message=self.text)
    def Print2(self):
        os.system("useradd" + "\t" + str(self.UsersAndGroupsEntry.get()) +"\t" +"-s"+"\t" "/bin/bash" "\t"+ "-m" +"\t"+ "-p "+ str(self.UsersAndGroupspasswodEny1.get()))
    def ApacheStart(self):
        os.system("service apache2 start")
        tkMessageBox._show(title='apache2', message='the apache2 start')
    def ApacheStop(self):
        os.system("service apache2 stop")
        tkMessageBox._show(title='apache2', message='the apache2 stoped')
    def ApacheStatus(self):
        os.system("gnome-terminal -e 'service apache2 status'")
    def BindeStart(self):
        os.system("service bind9 start")
        tkMessageBox._show(title='bind9', message='the bind9 start')
    def BindStop(self):
        os.system("service bind9 stop")
        tkMessageBox._show(title='mysql', message='the bind9 stoped')
    def BindStatus(self):
        os.system("gnome-terminal -e 'service bind9 status'")
    def MysqlStart(self):
        os.system("service mysql start")
        tkMessageBox._show(title='mysql', message='the mysql start')
    def MysqlStop(self):
        os.system("service mysql stop")
        tkMessageBox._show(title='mysql', message='the mysql stoped')
    def MysqlStatus(self):
        os.system("gnome-terminal -e 'watch service mysql status'")
    def SquidStart(self):
        os.system("service squid start")
        tkMessageBox._show(title='mysql', message='the squid start')
    def SquidStop(self):
        os.system("service squid stop")
        tkMessageBox._show(title='squid', message='the squid stoped')
    def SquidStatus(self):
        os.system("gnome-terminal -e 'service squid status'")
    def Journalctl(self):
        os.system("gnome-terminal -e 'journalctl -xe'")

    def OpenVpnStart(self):
        os.system("service openvpn start")
        tkMessageBox._show(title='openvpn', message='the openvpn start')
    def OpenVpnStop(self):
        os.system("service openvpn stop")
        tkMessageBox._show(title='openvpn', message='the openvpn stoped')
    def OpenVpnstatus(self):
        os.system("gnome-terminal -e 'service openvpn status'")



a = Manager()


def Starting():
    a.GUI

def main():
    Starting()
main()
