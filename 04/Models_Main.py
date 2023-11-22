import torch 
from Models import ExerciseModel


if __name__=="__main__":

    in_tensor = torch.ones((32,3,128,128))
    model = ExerciseModel()

    out = model(in_tensor)
    print(repr(out.size()))