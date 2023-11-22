import torch 
from torch import nn


if __name__=="__main__":
    _in = torch.ones((32,1024))
    print(repr(_in.size()))
    fc = nn.Linear(in_features=1024,out_features=256)
    out1 = fc(_in)
    print(repr(out1.size()))
    fc = nn.Linear(in_features=1024,out_features=2048)
    out2 = fc(_in)
    print(repr(out2.size()))
    out3 = out1.reshape(-1,16,16)
    print(repr(out3.size()))