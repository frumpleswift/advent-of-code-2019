class Intcode:

  def __init__(self,state:list,inputs:list):

    self.state=state.copy()
    self.state.extend([0 for i in range(0,999999)])
    self.inputs=inputs
    self.base=0
    self.pos=0
    self.debug=False
    self.opcodes = {
      1:self._add,
      2:self._multiply,
      3:self._input,
      4:self._output,
      5:self._true,
      6:self._false,
      7:self._less_than,
      8:self._equals,
      9:self._rel_base,
      }

  def _get_arg(self,arg:int):
    mode=self.modes[arg]
    if mode == 0:
      return self.state[ self.state[self.pos + arg] ]
    if mode == 1:
      return self.state[self.pos + arg]
    if mode == 2:
      return self.state[ self.state[self.pos + arg] + self.base ]
    raise Exception("Invalid mode {} found at {}".format(mode,self.pos))

  def _get_pos(self,arg:int):
    if self.modes[arg] == 2:
      return self.state[self.pos+arg]+self.base
    return self.state[self.pos + arg]

  def _true(self):
    b=self._get_arg(1)
    j=self._get_arg(2)

    p=self.pos+3
    if b != 0:
      p=j

    self.pos=p

  def _false(self):
    b=self._get_arg(1)
    j=self._get_arg(2)

    p=self.pos+3
    if b == 0:
      p=j

    self.pos=p

  def _add(self):
    x=self._get_arg(1)
    y=self._get_arg(2)
    p=self._get_pos(3)
    self.state[ p ] = x+y
    self.pos+=4

  def _multiply(self):
    x=self._get_arg(1)
    y=self._get_arg(2)
    p=self._get_pos(3)
    self.state[ p ] = x*y
    self.pos+=4

  def _input(self):
    x = self.inputs.pop(0)
    p = self._get_pos(1)
    self.state[p]=x
    self.pos+=2

  def _less_than(self):
    x=self._get_arg(1)
    y=self._get_arg(2)
    p=self._get_pos(3)

    self.state[p]=0
    if x<y:
      self.state[p]=1

    self.pos+=4

  def _equals(self):
    x=self._get_arg(1)
    y=self._get_arg(2)
    p=self._get_pos(3)
    self.state[p]=0
    if x==y:
      self.state[p]=1

    self.pos+=4

  def _output(self):

    x=self._get_arg(1)
    self.pos+=2
    return x

  def _rel_base(self):

    self.base += self._get_arg(1)
    self.pos+=2

  def run(self):

    args=(str(self.state[self.pos]))
    code=int(args[-2:])
    self.modes=[9]
    self.modes.extend([int(i) for i in reversed(args[0:-2])])
    self.modes.extend([0 for i in range(0,10-len(self.modes))])

    if self.debug:
      print(code,self.pos,self.base,self.inputs,self.state[self.pos:self.pos+5])

    out = self.opcodes[ code ]()

    return out

  def run_full(self):
    outputs=[]
    while self.state [ self.pos ] != 99:
      out = self.run()
      if out:
        outputs.append(out)
    return outputs
