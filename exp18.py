import random
def monty_hall():
	runs=10000
	stay=0
	switch=0
	print(f"running{runs}simulations...")
	for i in range(runs):
	  doors=[0,0,1]
	  random.shuffle(doors)
	  
	  car=doors.index(1)
	  pick=random.randint(0,2)
	  
	  host=-1
	  for i in range(3):
	    if i !=pick and i !=car:
	      host=i
	      break
	  
	  new_pick=-1
	  for i in range(3):
	    if i !=pick and i !=host:
	      new_pick=i
	      break
	      
	    if pick==car:
	      stay +=1
	    if new_pick==car:
	      switch +=1
	  
	  print("\nResults")
	  stay_percent=(stay/runs)*100
	  switch_present=(switch/runs)*100
	  print(f"'stay' strategy wins:{stay}/{runs} ({stay_percent:.2f}%)")
	  print(f"'switch' strategy wins:{switch}/{runs} ({switch_present:.2f}%)")
	  
monty_hall()
	   
