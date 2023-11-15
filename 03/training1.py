import numpy as np
import torch

if __name__ == "__main__":
 data = np.array([
[[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
[[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
[[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]])

 tensor = torch.tensor(data, dtype=float)
 print("===== problem 1 =====")
 print(tensor.size()) 
 
 changed_tensor = torch.permute(tensor, (2, 0, 1))
 print("===== problem 2 =====")
 print(changed_tensor)
 print(changed_tensor.size())

 sum_changed_tensor = changed_tensor.sum(dim=0)
 print("===== problem 3 =====")
 print(sum_changed_tensor)

 mean_changed_tensor = sum_changed_tensor.mean(dim=1)
 print("===== problem 4 =====")
 print(mean_changed_tensor)

 mean_changed_tensor_another = sum_changed_tensor.sum(dim=1)/sum_changed_tensor.size(dim=1)
 print("===== problem 5 =====")
 print(mean_changed_tensor_another)
 