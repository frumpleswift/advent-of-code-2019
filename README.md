# advent-of-code-2019
These are my solutions to four problems from the 2019 [Advent of Code](https://adventofcode.com/2019) challenges.  Three of the challenges use a "virtual machine" that executes "compiled code," referred to as intcode in the problems.  The virtual machine is implemented in the vm.py file.

All Advent of Code challenges come in two parts.  The code provided hear solves both parts, save for Day 17, where only the first part is solved.


**[Day 8: Space Image Format](https://adventofcode.com/2019/day/8)**
The solution for the day 8 challenges is implemented in images.py, with the intcode input saved to image_input.

bash-4.2$ python3.6 images.py
[[1 0 0 0 0 1 0 0 1 0 0 1 1 0 0 1 1 1 0 0 1 0 0 1 0]
 [1 0 0 0 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0]
 [1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 1 0 0 1 0 1 1 1 1 0]
 [1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 1 1 1 0 0 1 0 0 1 0]
 [1 0 0 0 0 1 0 0 1 0 1 0 0 1 0 1 0 0 0 0 1 0 0 1 0]
 [1 1 1 1 0 1 0 0 1 0 0 1 1 0 0 1 0 0 0 0 1 0 0 1 0]]
bash-4.2$

**[Day 9: Sensor Boost](https://adventofcode.com/2019/day/9)**
The solution is implemented in run_prob9.py, using the intcode in day9-input.txt, and leverages the Intcode class in vm.py

bash-4.2$ python3.6 run_prob9.py
[4288078517]
[69256]
bash-4.2$

**[Day 13: Care Package](https://adventofcode.com/2019/day/13)**
The solution is implemented in arcade.py, using the intcode in arcade-input.txt, and leverages the Intcode class in vm.py.

The output will display the arcade game as it is "played" to solve the second part of the challenge.

**[Day 17: Set and Forget](https://adventofcode.com/2019/day/17)**

The solution is implemented in rescue.py, using the intcode in scaffold.txt, and leverages the Intcode class in vm.py.

The output will display the scaffold alignment and the solution to the first part of the problem.# advent-of-code-2019
