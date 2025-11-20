import os
import sys
import matplotlib.pyplot as plt
def day_structure():
    days = {}
    while True:
        subject = input("Enter name of the subject (if done leave subject blank): ")
        if subject == "":
            break
        mark = input("1 for present , 0 for absent: ")
        days[subject] = mark
    return days

def data_collection():
    sem = input("Semester: ")
    folder_name = "Sem" + sem
    os.makedirs(folder_name, exist_ok=True)
    weeks = int(input("Duration of semester (in weeks): "))
    for n in range(weeks):
        print(f"Week{n+1}")
        working_days = int(input("Number of working days: "))
        for i in range (working_days):
            print(f"Day{i+1}")
            day_s = day_structure()
            for day in day_s:
                with open(f"{folder_name}/Week{n+1}","a") as file:
                    file.write(f"{day},{day_s[day]}\n")

def data_retrieval(sem_no,week_no):
    data = []
    tem = []
    with open(f"Sem{sem_no}/Week{week_no}") as file:
        for line in file:
            data.append(line.replace('\n','').strip())
    for dat in data:
        sub,mar= dat.split(',')
        tem.append({'subject':sub,'mark':mar})
    return tem

def attendance(tem):
    total_classes = len(tem)
    subject_total={}
    for t in tem:
        r=t['subject']
        if r in subject_total.keys():
            subject_total[r] +=1
        else:
            subject_total[r] =1

    subject_attended={}
    for t in tem:
        a=t['subject']
        b = t['mark']
        if a in subject_attended.keys():
            if b == '1':
                subject_attended[a] +=1
        else:
            subject_attended[a] = 0
            if b == '1':
                subject_attended[a] +=1
    weekly_attended = 0
    for s in subject_attended:
        weekly_attended += subject_attended[s]
    subject_summary=[]
    for s in  subject_total:
        subject_summary.append({'name':s,'total':subject_total[s],'attended':subject_attended[s]})

    return subject_summary , total_classes , weekly_attended

def percentage(summary,total,week):
    perc_per_subject = {}
    for s in summary:
        sub_name = s['name']
        sub_total = s['total']
        att = s['attended']
        perc_per_subject[sub_name] = round((att/sub_total),3)
    week_att = round((week/total)*100,2)

    return week_att,perc_per_subject


def plot_weekly_attendance_pie(weekly_percentages,sem):
    print("Plot started")
    labels = [f"Week {i+1}" for i in range(len(weekly_percentages))]
    sizes = weekly_percentages
    filename = "Weekly Pie for Semester" + sem

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Weekly Attendance Distribution")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Pie saved at {filename}")

def main():
    if len(sys.argv)==1:
        print("Collecting data")
        data_collection()
        print("Data recorded successfully")
        print("To access weekly data give 'stats (semesternumber) (weeknumber)' as command prompts")
        print("To access semester wise data give 'Semester (semesternumber)' as command prompts")
    elif sys.argv[1] == "stats":
        try:
            te_m = data_retrieval(sys.argv[2],sys.argv[3])
            summary,total,week = attendance(te_m)
            a,b = percentage(summary,total,week)
            for p in b:
                print(f"{p.capitalize()} - {b[p] *100}%")
            print(f"Weekly attendance  : {a}%")
            print(f"You have attended {week} classes out of {total} classes this week.")
        except FileNotFoundError:
            sys.exit("No data")
    elif sys.argv[1] == "Semester":
        try:
            week_count = len(os.listdir(f"Sem{sys.argv[2]}"))
            weekly_perc = []
            for i in range(week_count):
                te_m = data_retrieval(sys.argv[2],i+1)
                summary,total,week = attendance(te_m)
                c,_= percentage(summary,total,week)
                weekly_perc.append(c)
            plot_weekly_attendance_pie(weekly_perc,sys.argv[2])
        except FileNotFoundError:
            sys.exit("Sem data not found")

if __name__ == "__main__":
    main()

