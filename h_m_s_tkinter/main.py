from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import mysql.connector
from tkinter import messagebox

class login():
    def __init__(self,root):
        self.root= root
        self.root.title("Hospital management system")
        self.root.geometry("1540x800+0+0")


        # declare variables for getting data
        self.Nameoftablets= StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.Nooftablets = StringVar()
        self.issuedate = StringVar()
        self.expdate = StringVar()
        self.dailydose = StringVar()
        self.lot = StringVar()
        self.sideeffect = StringVar()
        self.furtherinfo = StringVar()
        self.storage = StringVar()
        self.drivingusingmachine = StringVar()
        self.howtousemedicine = StringVar()
        self.patientid = StringVar()
        self.nhsnumner = StringVar()
        self.patientname = StringVar()
        self.dateodbirth = StringVar()
        self.pateientaddress = StringVar()


        Labeltitle = Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="grey",bg="white",font=("times new romen",50,"bold"))
        Labeltitle.pack(side=TOP,fill=X)

        # ========================making Data frame ========================
        dataframe = Frame(self.root,bd=20,relief=RIDGE)
        dataframe.place(x=0,y=120,width=1540,height=400)

        dataframeleft = LabelFrame(dataframe,bd=10,padx=20,relief=RIDGE,
                                   font=("times new romen",12,"bold"),text="Pateient Information")
        dataframeleft.place(x=0,y=5,width=980,height=350)


        dataframeRight = LabelFrame(dataframe,bd=10,padx=20,relief=RIDGE,
                                   font=("times new romen",12,"bold"),text="precription")
        dataframeRight.place(x=990,y=5,width=460,height=350)


        # ========================making button frame ========================
        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1540,height=70)



        # ========================making details frame ========================
        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1540,height=190)


        # ================= Label fields ===========================
        # 1.
        lebletablet = Label(dataframeleft,text="Name of Tablets",font=("times new romen",12,"bold"),padx=2,pady=6)
        lebletablet.grid(row=0,column=0)
        comNameTable = ttk.Combobox(dataframeleft,textvariable=self.Nameoftablets,font=("times new romen",12,"bold"),width=33,justify="center")
        comNameTable["values"] = ("Diclocin Fort","Ponstan","Disprin","PainKiller")
        comNameTable.grid(row=0,column=1)


        # 2.
        lebletablet = Label(dataframeleft,text="Reference #",font=("times new romen",12,"bold"),padx=2,pady=6)
        lebletablet.grid(row=1,column=0,sticky=W)
        txtref = Entry(dataframeleft,textvariable=self.ref,font=("aerial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)


        # 3.
        lebletablet = Label(dataframeleft,text="Dose",font=("times new romen",12,"bold"),padx=2,pady=6)
        lebletablet.grid(row=2,column=0,sticky=W)
        txtdose = Entry(dataframeleft,textvariable=self.Dose,font=("aerial",13,"bold"),width=35)
        txtdose.grid(row=2,column=1)


        # 4.
        lebletablet = Label(dataframeleft,text="No of Tablets",font=("times new romen",12,"bold"),padx=2,pady=6)
        lebletablet.grid(row=3,column=0,sticky=W)
        txttablets = Entry(dataframeleft,textvariable=self.Nooftablets,font=("aerial",13,"bold"),width=35,justify="center")
        txttablets.grid(row=3,column=1)


        # 5.
        lebletablet = Label(dataframeleft,text="Lot",font=("times new romen",12,"bold"),padx=2,pady=6)
        lebletablet.grid(row=4,column=0,sticky=W)
        txtlot = Entry(dataframeleft,textvariable=self.lot,font=("aerial",13,"bold"),justify="center",width=35)
        txtlot.grid(row=4,column=1)


        # 6.
        lebletablet = Label(dataframeleft,text="issue date",font=("times new romen",12,"bold"),padx=2,pady=6)
        lebletablet.grid(row=5,column=0,sticky=W)
        txtissuedate = Entry(dataframeleft,textvariable=self.issuedate,font=("aerial",13,"bold"),width=35,justify="center")
        txtissuedate.grid(row=5,column=1)


        # 7.
        lebletablet = Label(dataframeleft,text="Exp Date",font=("times new romen",12,"bold"),padx=2,pady=6)
        lebletablet.grid(row=6,column=0,sticky=W)
        txtexpdate = Entry(dataframeleft,textvariable=self.expdate,font=("aerial",13,"bold"),width=35,justify="center")
        txtexpdate.grid(row=6,column=1)


        # 8.
        lebletablet = Label(dataframeleft,text="Daily Dose",font=("times new romen",12,"bold"),padx=2,pady=6)
        lebletablet.grid(row=7,column=0,sticky=W)
        txtdailydose = Entry(dataframeleft,textvariable=self.dailydose,font=("aerial",13,"bold"),width=35,justify=CENTER)
        txtdailydose.grid(row=7,column=1)

        # 9.
        lebletablet = Label(dataframeleft,text="Side Effect",font=("times new romen",12,"bold"),padx=2,pady=6)
        lebletablet.grid(row=8,column=0,sticky=W)
        txtsideeffect = Entry(dataframeleft,textvariable=self.sideeffect,font=("aerial",13,"bold"),width=35,justify=CENTER)
        txtsideeffect.grid(row=8,column=1)


        # 10.
        labelfurtherinfo = Label(dataframeleft,text="Further Info",font=("aerial",12,"bold"),padx=4,pady=6)
        labelfurtherinfo.grid(row=0,column=2,sticky=W)
        txtfurtherinfo = Entry(dataframeleft,textvariable=self.furtherinfo,font=("aerial",13,"bold"),width=35,justify=CENTER)
        txtfurtherinfo.grid(row=0,column=3)


        # 11.
        labelbloodpressure = Label(dataframeleft,text="Blood Pressure",font=("aerial",12,"bold"),padx=4,pady=6)
        labelbloodpressure.grid(row=1,column=2,sticky=W)
        txtbloodpressure = Entry(dataframeleft,textvariable=self.drivingusingmachine,font=("aerial",13,"bold"),width=35,justify=CENTER)
        txtbloodpressure.grid(row=1,column=3)


        # 12.
        labelstorage = Label(dataframeleft,text="Storage Advise",font=("aerial",12,"bold"),padx=4,pady=6)
        labelstorage.grid(row=2,column=2,sticky=W)
        txtstorage = Entry(dataframeleft,textvariable=self.storage,font=("aerial",13,"bold"),width=35,justify=CENTER)
        txtstorage.grid(row=2,column=3)


        # 13.
        labelMedication = Label(dataframeleft,text="Medication",font=("aerial",12,"bold"),padx=4,pady=6)
        labelMedication.grid(row=3,column=2,sticky=W)
        txtmedication = Entry(dataframeleft,textvariable=self.howtousemedicine,font=("aerial",13,"bold"),width=35,justify=CENTER)
        txtmedication.grid(row=3,column=3)


        # 14.
        labelpatientid = Label(dataframeleft,text="Patient Id",font=("aerial",12,"bold"),padx=4,pady=6)
        labelpatientid.grid(row=4,column=2,sticky=W)
        txtpatientid = Entry(dataframeleft,textvariable=self.patientid,font=("aerial",13,"bold"),width=35,justify=CENTER)
        txtpatientid.grid(row=4,column=3)


        # 15.
        labelnhsnumber = Label(dataframeleft,text="NHS Number",font=("aerial",12,"bold"),padx=4,pady=6)
        labelnhsnumber.grid(row=5,column=2,sticky=W)
        txtnhsnumber = Entry(dataframeleft,textvariable=self.nhsnumner,font=("aerial",13,"bold"),width=35,justify=CENTER)
        txtnhsnumber.grid(row=5,column=3)


        # 16.
        labelpatientname = Label(dataframeleft,text="Patient Name",font=("aerial",12,"bold"),padx=4,pady=6)
        labelpatientname.grid(row=6,column=2,sticky=W)
        txtpatientname = Entry(dataframeleft,textvariable=self.patientname,font=("aerial",13,"bold"),width=35,justify=CENTER)
        txtpatientname.grid(row=6,column=3)


        # 17.
        labeldob = Label(dataframeleft,text="D.O.B",font=("aerial",12,"bold"),padx=4,pady=6)
        labeldob.grid(row=7,column=2,sticky=W)
        txtdob = Entry(dataframeleft,textvariable=self.dateodbirth,font=("aerial",13,"bold"),width=35,justify=CENTER)
        txtdob.grid(row=7,column=3)


        # 18.
        labeladdress = Label(dataframeleft,text="Address",font=("aerial",12,"bold"),padx=4,pady=6)
        labeladdress.grid(row=8,column=2,sticky=W)
        txtaddress = Entry(dataframeleft,textvariable=self.pateientaddress,font=("aerial",13,"bold"),width=35,justify=CENTER)
        txtaddress.grid(row=8,column=3)



        # ==================================== dataframeRight=======================================

        self.txtperception = Text(dataframeRight,font=("times new romen",12,"italic"),width=45,height=16,padx=2,pady=4)
        self.txtperception.grid(row=0,column=0)



        # ======================================= buttons =============================================

        btnperception = Button(Buttonframe,command=self.iperception,width=20,font=("aerial",11,"bold"),bg="green",fg="white",padx=2,pady=4,text="Perception")
        btnperception.grid(row=0,column=1)

        btnperceptiondata = Button(Buttonframe,command=self.iperceptiondata,width=20,font=("aerial",11,"bold"),bg="green",fg="white",padx=2,pady=4,text="Perception Data")
        btnperceptiondata.grid(row=0,column=2)

        btnupdate = Button(Buttonframe,command=self.Update_data,width=20,font=("aerial",11,"bold"),bg="blue",fg="white",padx=2,pady=4,text="Update")
        btnupdate.grid(row=0,column=3)

        btndelete = Button(Buttonframe,command=self.deletedata,width=20,font=("aerial",11,"bold"),bg="red",fg="white",padx=2,pady=4,text="Delete")
        btndelete.grid(row=0,column=4)

        btnclear = Button(Buttonframe,command=self.cleardata,width=20,font=("aerial",11,"bold"),bg="brown",fg="white",padx=2,pady=4,text="Clear")
        btnclear.grid(row=0,column=5)

        btnexit = Button(Buttonframe,command=self.iexit,width=20,font=("aerial",11,"bold"),bg="black",fg="white",padx=2,pady=4,text="Exit")
        btnexit.grid(row=0,column=6)



        # =====================================Scrollbar=======================================

        scrol_x = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scrol_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_tablet = ttk.Treeview(Detailsframe,columns=("name_of_table","ref","dose","no_of_tablets","iot","issue date",
                                                                  "exp_date","daily_dose","storage","nhsnumber","dob","address"),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)
        
        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)

        scrol_x=ttk.Scrollbar(command=self.hospital_tablet.xview)
        scrol_y=ttk.Scrollbar(command=self.hospital_tablet.yview)

        self.hospital_tablet.heading("name_of_table",text="Name of Table")
        self.hospital_tablet.heading("ref",text="Ref")
        self.hospital_tablet.heading("dose",text="Dose")
        self.hospital_tablet.heading("no_of_tablets",text="No_of_tablets")
        self.hospital_tablet.heading("iot",text="Iot")
        self.hospital_tablet.heading("issue date",text="Issue date")
        self.hospital_tablet.heading("exp_date",text="Exp Date")
        self.hospital_tablet.heading("daily_dose",text="Daily Dose")
        self.hospital_tablet.heading("storage",text="Storage")
        self.hospital_tablet.heading("nhsnumber",text="NHS number")
        self.hospital_tablet.heading("dob",text="DOB")
        self.hospital_tablet.heading("address",text="Adress")

        self.hospital_tablet["show"]='headings'

        self.hospital_tablet.column("name_of_table",width=100)
        self.hospital_tablet.column("ref",width=100)
        self.hospital_tablet.column("dose",width=100)
        self.hospital_tablet.column("no_of_tablets",width=100)
        self.hospital_tablet.column("iot",width=100)
        self.hospital_tablet.column("issue date",width=100)
        self.hospital_tablet.column("exp_date",width=100)
        self.hospital_tablet.column("daily_dose",width=100)
        self.hospital_tablet.column("storage",width=100)
        self.hospital_tablet.column("storage",width=100)
        self.hospital_tablet.column("nhsnumber",width=100)
        self.hospital_tablet.column("dob",width=100)
        self.hospital_tablet.column("address",width=100)
        
        self.hospital_tablet.pack(fill=BOTH,expand=1)
        # use buttonrelease function you can use more buttonrelease
        self.hospital_tablet.bind("<ButtonRelease-1>",self.get_cursor)
        # when application is running data automatically fetched and shows on the table
        self.fetch_data()
        
        
            

        # ================================== functionality ================================


    def iperceptiondata(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error","please fill all fields")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Chodrykhan@880",database="crud_operation")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO hospital_managemnt_system VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",(
                                                                                                                        self.Nameoftablets.get(),
                                                                                                                        self.ref.get(),
                                                                                                                        self.Dose.get(),
                                                                                                                        self.Nooftablets.get(),
                                                                                                                        self.issuedate.get(),
                                                                                                                        self.expdate.get(),
                                                                                                                        self.lot.get(),
                                                                                                                        self.storage.get(),
                                                                                                                        self.dailydose.get(),
                                                                                                                        self.nhsnumner.get(),
                                                                                                                        self.patientname.get(),
                                                                                                                        self.dateodbirth.get(),
                                                                                                                        self.pateientaddress.get(), 
                                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("record Insert","data has been saved successfully")
    

    def Update_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Chodrykhan@880",database="crud_operation")
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE hospital_managemnt_system SET name_of_tablet=%s,dose=%s,no_of_tablets=%s,iot=%s,issue_date=%s,exp_date=%s,daily_dose=%s,storage=%s,nhsnumber=%s,patientname=%s,dob=%s,patientaddress=%s WHERE ref_no=%s",(
                                                                                                                                                                                                                                            self.Nameoftablets.get(),
                                                                                                                                                                                                                                            self.Dose.get(),
                                                                                                                                                                                                                                            self.Nooftablets.get(),
                                                                                                                                                                                                                                            self.lot.get(),
                                                                                                                                                                                                                                            self.issuedate.get(),
                                                                                                                                                                                                                                            self.expdate.get(),
                                                                                                                                                                                                                                            self.dailydose.get(),
                                                                                                                                                                                                                                            self.storage.get(),
                                                                                                                                                                                                                                            self.nhsnumner.get(),
                                                                                                                                                                                                                                            self.patientname.get(),
                                                                                                                                                                                                                                            self.dateodbirth.get(),
                                                                                                                                                                                                                                            self.pateientaddress.get(),
                                                                                                                                                                                                                                            self.ref.get(), 
                                                                                                                                                                                                                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("UPDATE RECORD","Record has been Updated Successfully")


    def iperception(self):
        self.txtperception.insert(END,"NAME OF TABLETS:\t\t\t"+ self.Nameoftablets.get()+ "\n")
        self.txtperception.insert(END,"REF:\t\t\t"+ self.ref.get()+"\n")
        self.txtperception.insert(END,"DOB:\t\t\t"+ self.dateodbirth.get()+"\n")
        self.txtperception.insert(END,"EXP-DATE:\t\t\t"+ self.expdate.get()+"\n")
        self.txtperception.insert(END,"ISSUE-DATE:\t\t\t"+ self.issuedate.get()+"\n")
        self.txtperception.insert(END,"STORAGE:\t\t\t"+ self.storage.get()+"\n")
        self.txtperception.insert(END,"DOSE:\t\t\t"+ self.Dose.get()+"\n")
        self.txtperception.insert(END,"NO-OF-TABLETS:\t\t\t"+ self.Nooftablets.get()+"\n")
        self.txtperception.insert(END,"NHS-NUMBER:\t\t\t"+ self.nhsnumner.get()+"\n")
        self.txtperception.insert(END,"PATIENT-NAME:\t\t\t"+ self.patientname.get()+"\n")
        self.txtperception.insert(END,"I-O-T:\t\t\t"+ self.lot.get()+"\n")
        self.txtperception.insert(END,"PATIENT_ADDRESS:\t\t\t"+ self.pateientaddress.get()+"\n")
        
        


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Chodrykhan@880",database="crud_operation")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM hospital_managemnt_system")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_tablet.delete(*self.hospital_tablet.get_children())
            for i in rows:
                self.hospital_tablet.insert("",END,values=i)
            conn.commit()
        conn.close()

    def deletedata(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Chodrykhan@880",database="crud_operation")
        mycursor = conn.cursor()
        query = ("DELETE FROM hospital_managemnt_system where ref_no=%s")
        value = (self.ref.get(),)
        mycursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("DELETE","Record has been successfully deleted")

    def cleardata(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.Nooftablets.set("")
        self.lot.set("")
        self.issuedate.set("")
        self.expdate.set("")
        self.dailydose.set("")
        self.storage.set("")
        self.nhsnumner.set("")
        self.patientname.set("")
        self.dateodbirth.set("")
        self.pateientaddress.set("")

    def iexit(self):
        iexit = messagebox.askyesno("Hospital Management System","are you want to Exit press Yes")
        if iexit > 0:
            root.destroy()
            return
        


    

    def get_cursor(self,event=""):
        cursor_row = self.hospital_tablet.focus()
        content = self.hospital_tablet.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.Nooftablets.set(row[3])
        self.lot.set(row[4])
        self.issuedate.set(row[5])
        self.expdate.set(row[6])
        self.dailydose.set(row[7])
        self.storage.set(row[8])
        self.nhsnumner.set(row[9])
        self.patientname.set(row[10])
        self.dateodbirth.set(row[11])
        self.pateientaddress.set(row[12])
    
        


        





root = Tk()
obj = login(root)
root.mainloop()
