import torch
from torch import nn


if __name__=="__main__":
    my_tensor = torch.ones((32,3,128,128))
    print(repr(my_tensor.size()))
    conv = nn.Conv2d(in_channels=3,kernel_size=3,out_channels=64)
    out1 = conv(my_tensor)
    print(repr(out1.size()))
    conv = nn.Conv2d(in_channels=3,kernel_size=3,out_channels=256,stride=2,padding=1)
    out2 = conv(my_tensor)
    print(repr(out2.size()))
    conv = nn.Conv2d(in_channels=3,kernel_size=5,out_channels=64,padding=1)
    out1_2 = conv(my_tensor)
    print(repr(out1_2.size()))
    conv = nn.Conv2d(in_channels=3,kernel_size=5,out_channels=256,padding=2,stride=2)
    out2_2 = conv(my_tensor)
    print(repr(out2_2.size()))
