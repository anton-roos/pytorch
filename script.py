from d2l import torch

x = torch.arange(12, dtype=torch.float32)
print(x)
print(x.numel())
print(x.shape)
X = x.reshape(3, 4)
print(X)

y = torch.zeros((2, 3, 4))
print(y)

z = torch.ones((6, 3, 4))
print(z)

randomTensor = torch.randn(3, 4)
print(randomTensor)

tensorConstructed = torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(tensorConstructed)

print(X[-1], X[1:3])
X[1, 2] = 17
print(X)

X[1:3] = 99
print(X)

x = torch.exp(x)
print(x)

x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
print(x + y, x - y, x * y, x / y, x ** y)

import os

os.makedirs(os.path.join('data'), exist_ok=True)
data_file = os.path.join('data', 'house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('''NumRooms,RoofType,Price
NA,NA,127500
2,NA,106000
4,Slate,178100
NA,NA,140000''')