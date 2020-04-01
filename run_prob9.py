from vm import Intcode



#vm=Intcode([1102,34915192,34915192,7,4,7,99,0],[]) # should output a 16-digit number.
#print(vm.run_full())
#vm=Intcode([104,1125899906842624,99],[]) # should output the large number in the midd
#print(vm.run_full())

#vm=Intcode([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99],[])

#outputs=vm.run_full()
#print("[109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]")
#print(outputs)

vm=Intcode([int(i) for i in open('day9-input.txt').read().strip().split(',')],[1])
print(vm.run_full())

vm=Intcode([int(i) for i in open('day9-input.txt').read().strip().split(',')],[2])
try:
  print(vm.run_full())
except:
  print(vm.pos,vm.state[vm.pos])
  raise
