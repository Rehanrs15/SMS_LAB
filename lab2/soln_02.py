from random import randint
 
Service_Time_Nurse = 7

#interarrival time of patient
#EACH ITEM [TIME, PROBABILITY, MAPPING]
Patient = [[5, 0.5, (0,49)], [10, 0.3, (50,79)], [15, 0.2, (80,99)]]

#interarrival time of doctor
#EACH ITEM [TIME, PROBABILITY, MAPPING]
Doctor = [[4, 0.3, (0,29)], [8, 0.5, (30,79)], [12, 0.2, (80,99)]]

serviceTimeDOctor = (4 * 0.3) + (8 * 0.5) + (12 * 0.2)

#number of trails
values = 10
Simulation_Table = []
for i in range(1,values+1):
	appending_list = []
	for j in range(14):	
		#pateint_no append
		appending_list.append(i)
		r = randint(0,99)
		appending_list.append(r)
		for m in range(len(Patient)):
			b = r in range(Patient[m][2][0],Patient[m][2][1])
			if b == True:
				appending_list.append(Patient[m][0])
			else:
				continue
		arrivalTime = 0
		if i == 1:
			arrivalTime = appending_list.append(Patient[i][0])
		else:
			get = Simulation_Table[(i-1)-1][3]
			arrivalTime = get + Patient[i-1][0]
			appending_list.append(arrivalTime)
		#end of patient calculation
		#--
		#start of nusrse calcualtion
		start,service = 0,0
		if i == 1:
			start = Patient[i-1][0]
			appending_list.append(start)
			service = 7
			appending_list.append(service)
		else:
			get1 = Simulation_Table[(i-1)-1][4]
			appending_list.append(get1+7)
			appending_list.append(7)
		finish_time = start+service
		appending_list.append(finish_time) #finish time
		
		#wait time
		if i == 1:
			#wait time = 0 for first patient
			appending_list.append(0)
		else:
			get_arrival_time = arrivalTime
			previous_finish_time = Simulation_Table[(i-1)-1][6]
			appending_list.append(previous_finish_time - get_arrival_time)
			
		#end of nurse
		#--
		#start of doctor
		#--
		#--
		#start time of doctor
		doctor_start_time = finish_time
		appending_list.append(doctor_start_time)
		#Random
		d = randint(0,99)
		appending_list.append(d)
		#service time
		service_time = 0
		for m in range(len(Doctor)):
			b = r in range(Doctor[m][2][0],Doctor[m][2][1])
			if b == True:
				service_time = Patient[m-1][0]
				appending_list.append(service_time)
			else:
				continue
		#finish time
		doctor_finish_time = doctor_start_time + service_time
		appending_list.append(doctor_finish_time)
		
		#wait time
		if i == 1:
			appending_list.append(0)
		else:
			previous_finish_time = Simulation_Table[(i-1)-1][11]
			if doctor_start_time >= previous_finish_time:	
				appending_list.append(0)
			else:
				appending_list.append(doctor_start_time - previous_finish_time)
		
		#TIme in system
		appending_list.append(doctor_finish_time - Patient[i-1][0])
	Simulation_Table.append(appending_list)


for k in range(len(Simulation_Table)):
	print("Patient ",i," time in system = ",Simulation_Table[i][13])

		
		
			
		
		
