import torch
from torch.nn import Module


class TrainingModule(Module):
    def __init__(self,mytensor,elem_add,elem_multiply):
        super().__init__()
        self.mytensor = mytensor
        self.elem_add = elem_add
        self.elem_multiply = elem_multiply

    def forward (self,x):
        p2out = x + self.mytensor
        p3out = p2out + self.elem_add
        p4out = p3out * self.elem_multiply
        return (p2out,p3out,p4out)
if __name__=="__main__":
    mymodel = TrainingModule(torch.ones((3,3)),4,6)

    p2out,p3out,p4out = mymodel(torch.full((3,3),2))
    
    print("===== problem 2 =====")
    print(repr(p2out))
    print("===== problem 3 =====")
    print(repr(p3out))
    print("===== problem 4 =====")
    print(repr(p4out))