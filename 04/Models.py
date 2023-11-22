import torch 
from torch import nn

class ExerciseModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.conv = nn.Conv2d(in_channels=3,out_channels=256,kernel_size=5,stride=8)
        self.batchNorm = nn.BatchNorm2d(num_features=256)
        self.relu = nn.ReLU()
        self.lin = nn.Linear(in_features=256*16*16,out_features=64)


    def forward(self,_in):
        _in = self.conv(_in)
        _in = self.batchNorm(_in)
        _in = self.relu(_in)
        _in =_in.view(-1,256*16*16)
        _in = self.lin(_in)
        return _in