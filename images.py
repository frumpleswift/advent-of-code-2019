import numpy as np
layer_items=25*6
inputs = open('image_input').read().strip()
start=0
end=layer_items
layers=[]
while end < len(inputs):
    layer=inputs[start:end]
    #print(start,end,layer)
    start=end
    end=end+layer_items
    layers.append(layer)
#print(layers)

zero=19999999999999999
mult=0
min_z=9999999999999999999
min_mult=0
the_layer=-999
for l in layers:
    z=0
    one=0
    two=0
    for p in str(l):
        if  p=="0":
           z+=1
        if  p=="1":
          one+=1
        if p=="2":
            two+=1
    if z < min_z:
      min_z=z
      min_mult=one*two
      the_layer=l
#print(min_z,min_mult)
#print(the_layer)

final = layers[0]
#for i,l in enumerate(layers):
#    print(i,l)
#    for p,s in enumerate(l):
#        print(p,s)

def test(a,b):
    if b==2:
        return a
    return b
vtest = np.vectorize(test)

a = np.array([int(i) for i in inputs])
#print(a)
#print(a.shape)
b=np.reshape(a,(100,6,25))
image = np.full((6,25),2,dtype=int)

for l in reversed(b):
    image=vtest(image,l)

print(image)
