from tkinter import *
from tkinter import messagebox  
import tkinter as tk
import matplotlib.pyplot as plt

window = tk.Tk()


frame = Frame(window,relief=RAISED)
frame.pack()

window.geometry("700x500")

window.title("Shortest Job First (Preemptive)")

window.config(background='#EEF7FF')
frame.config(background='#EEF7FF')


def on_spinbox_change():
    value = spinbox.get()

    
def submit():
  global labeld,taskb,taskp
  task_number = spinbox.get()
  task_number_int = int(task_number)
  details = Tk()
  frameD = Frame(details,relief=RAISED)
  frameD.pack()
  details.geometry("700x500")
  details.title("Shortest Job First (Preemptive)")
  details.config(background='#EEF7FF')
  frameD.config(background='#EEF7FF')
  window.destroy()
  
  def validate_int(value):
    if value.isdigit():
        return True
    elif value == "":
        return True
    else:
        return False
      
  def done():
    global burst_time,process_arrival_time,task,complete,finish,minm,t,short,wt,bt,at,n,total_wt,total_tat,rest,total_rest,t,st,ft
    
    task = [i + 1 for i in range(task_number_int)]
    bt = [int(entry.get()) for entry in taskbb]
    at = [int(entry.get()) for entry in taskpp]
    last = Tk()
    framel = Frame(last,relief=RAISED)
    framel.pack()
    last.geometry("1280x480")
    last.title("Shortest Job First (Preemptive)")
    last.config(background='#EEF7FF')
    framel.config(background='#EEF7FF')
    details.destroy()
    
    #waiting time = finish Time − Burst Time − Arrival Time
    def waiting_time(processes, n, wt,rest): 
      rt = [0] * n

      for i in range(n): 
          rt[i] = processes[i][1]
      complete = 0
      t = 0
      minm = 999999999
      short = 0
      check = False
      gantt_data = []
      y_ticks = set()

      while (complete != n):
          
          # Find process with minimum remaining 
          # time among the processes that 
          # arrives till the current time`
          for j in range(n):
              if ((processes[j][2] <= t) and 
                  (rt[j] < minm) and rt[j] > 0):
                  minm = rt[j]
                  short = j
                  check = True
                  y_ticks.add(j+1)
                  
          #Process ready to be excuted
          if (check == False):
              t += 1
              continue
          
          gantt_data.append((t, t + 1, processes[short][0]))
          
          
          #Response time
          #Response time = Current time - Arrival time
          if rest[short] == -1:
            rest[short] = t - proc[short][2]
          
          # Reduce remaining time by one 
          rt[short] -= 1
          

          minm = rt[short] 
          if (minm == 0): 
              minm = 999999999

          if (rt[short] == 0): 

              complete += 1
              check = False
              
              finish = t + 1
              
              wt[short] = (finish - proc[short][1] - proc[short][2])

              if (wt[short] < 0):
                  wt[short] = 0
          
          t += 1
      # Plot Gantt chart
      fig, gnt = plt.subplots()
      gnt.set_xlabel('Time')
      gnt.set_ylabel('Processes')
      gnt.set_yticks(range(1,n+1))
      gnt.set_yticklabels([f'Task {tsk}' for tsk in y_ticks])

      for start, end, task in gantt_data:
          gnt.broken_barh([(start, end - start)], (task - 0.4, 0.8), facecolors=('tab:blue'))

      plt.title('Gantt Chart')
      plt.grid(True)
      plt.show()
            
    #turn around time = Burst Time + Waiting Time
    def turnaround_time(processes, n, wt, tat):
      for i in range(n):
        tat[i] = processes[i][1] + wt[i]
        
    def avg_time(processes, n , rest):
      
      waiting_time(processes, n, wt,rest) 
      turnaround_time(processes, n, wt, tat) 
      
      for i in range(n):
        labell1 = Label(framel, text=wt[i], font=('Arial', 10, 'bold'), fg='black', bg='#CDE8E5')
        labell1.grid(row = i + 1,column=1,pady = 12, padx = 12) 
        labell2 = Label(framel, text=tat[i], font=('Arial', 10, 'bold'), fg='black', bg='#CDE8E5')
        labell2.grid(row = i + 1,column=2,pady = 12, padx = 12)
        labell3 = Label(framel, text=rest[i], font=('Arial', 10, 'bold'), fg='black', bg='#CDE8E5')
        labell3.grid(row = i + 1,column=3,pady = 12, padx = 12)
      
  
    if __name__ =="__main__":
      
      proc = []

      for i in range(len(task)):
        proc.append([task[i], int(bt[i]), int(at[i])])
      n = task_number_int
      wt = [0] * n
      tat = [0] * n 
      total_wt = 0
      total_tat = 0
      total_rest = 0
      rest = [-1] * n
      #waiting_time(proc, n, wt,rest)
      turnaround_time(proc, n, wt, tat)
      avg_time(proc, n , rest)
      
        
      for i in range(n):
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
        total_rest = total_rest + rest[i] 
        labell4 = Label(framel, text=float(total_wt /n), font=('Arial', 10, 'bold'), fg='black', bg='#CDE8E5')
        labell4.grid(row = 1,column=4,pady = 12, padx = 12) 
        labell5 = Label(framel, text=float(total_tat / n), font=('Arial', 10, 'bold'), fg='black', bg='#CDE8E5')
        labell5.grid(row = 1,column=5,pady = 12, padx = 12) 
        labell5 = Label(framel, text=float(total_rest / n), font=('Arial', 10, 'bold'), fg='black', bg='#CDE8E5')
        labell5.grid(row = 1,column=6,pady = 12, padx = 12) 
        
    for i in range(1, task_number_int + 1):
      labell = Label(framel,text='Task' + str(i),font=('Arial',10,'bold'),fg='black',bg='#CDE8E5',relief=FLAT,bd=10)
      labell.grid(row = i,column=0,pady = 12, padx = 12)
      labell1 = Label(framel,text='Waiting Time',font=('Arial',10,'bold'),fg='black',bg='#CDE8E5',relief=FLAT,bd=10)
      labell1.grid(row = 0,column=1,pady = 12, padx = 12)
      labell2 = Label(framel,text=' Turnaround Time',font=('Arial',10,'bold'),fg='black',bg='#CDE8E5',relief=FLAT,bd=10)
      labell2.grid(row = 0,column=2,pady = 12, padx = 12)
      labell3 = Label(framel,text='Response Time',font=('Arial',10,'bold'),fg='black',bg='#CDE8E5',relief=FLAT,bd=10)
      labell3.grid(row = 0,column=3,pady = 12, padx = 12)
    labell4 = Label(framel,text='Average Waiting Time',font=('Arial',10,'bold'),fg='black',bg='#CDE8E5',relief=FLAT,bd=10)
    labell4.grid(row = 0,column=4,pady = 12, padx = 12)
    labell5 = Label(framel,text='Average Turnaround Time',font=('Arial',10,'bold'),fg='black',bg='#CDE8E5',relief=FLAT,bd=10)
    labell5.grid(row = 0,column=5,pady = 12, padx = 12)
    labell6 = Label(framel,text='Average Response Time',font=('Arial',10,'bold'),fg='black',bg='#CDE8E5',relief=FLAT,bd=10)
    labell6.grid(row = 0,column=6,pady = 12, padx = 12)
    

  validation = frameD.register(validate_int)

  taskpp=[]
  taskbb=[]
  
  for i in range(1, task_number_int + 1):
    labelt = Label(frameD,text='Task' + str(i),font=('Arial',10,'bold'),fg='black',bg='#CDE8E5',relief=FLAT,bd=10)
    labelt.grid(row = i,column=0,pady = 12, padx = 12)
    labeld = Label(frameD,text=' process arrival time',font=('Arial',10,'bold'),fg='black',bg='#CDE8E5',relief=FLAT,bd=10)
    labeld.grid(row = 0,column=1,pady = 12, padx = 12)
    labeld = Label(frameD,text='burst time',font=('Arial',10,'bold'),fg='black',bg='#CDE8E5',relief=FLAT,bd=10)
    labeld.grid(row = 0,column=2,pady = 12, padx = 12)
    taskp = Entry(frameD,font=('Arial'),fg='black',bg='#CDE8E5',validate="key", validatecommand=(validation, '%P'))
    taskp.grid(row = i,column=1,pady = 12, padx = 12)
    taskb = Entry(frameD,font=('Arial'),fg='black',bg='#CDE8E5',validate="key", validatecommand=(validation, '%P'))
    taskb.grid(row = i,column=2,pady = 12, padx = 12)
    taskbb.append(taskb)
    taskpp.append(taskp)
    
  Done_button = Button(details,text='Send',font=('Arial',10,'bold'),command=done,cursor='hand2',fg='black',bg='#4D869C',activebackground='#4D869C',activeforeground='#4D869C',relief=RAISED,bd=5)
  Done_button.pack(pady=30)
  

label = Label(frame,text='Enter number of process: ',font=('Arial',20,'bold'),fg='black',bg='#CDE8E5',relief=RIDGE,bd=10,padx=20,pady=20)
label.pack(pady=20)


spinbox = tk.Spinbox(window, from_=1, to=100, width=10,relief="sunken", repeatdelay=500, repeatinterval=100,font=("Arial", 12), bg='#CDE8E5' ,fg="black", command=on_spinbox_change)
spinbox.config(state="readonly", cursor="hand2", bd=5, justify="center", wrap=True,)
spinbox.pack(padx=20, pady=20)


submit_button = Button(window,text='Submit',font=('Arial',10,'bold'),command=submit,cursor='hand2',fg='black',bg='#4D869C',activebackground='#4D869C',activeforeground='#4D869C',relief=RAISED,bd=5)
submit_button.pack(pady=50)


window.mainloop()  # place window
