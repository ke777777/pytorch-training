import matplotlib.pyplot as plt
from torchvision import transforms 
from PIL import Image
from pathlib import Path
from torch.utils.data import Dataset

class MyDataset(Dataset):

    def __init__(self,dataset_dir):
        dir_path_resolved = Path(dataset_dir).resolve()
        self.img_list = list(dir_path_resolved.glob("*/*.png"))
        self.transform = transforms.Compose([
            transforms.ToTensor(),
        ]
        ) 
    
    def __len__(self):
        return len(self.img_list)   

    def __getitem__(self,idx):
        img_path = self.img_list[idx]
        img = Image.open(img_path)   
        img_tensor = self.transform(img)
        img_path = Path(img_path)
        parts = img_path.parts
        label = int(parts[9])

        return img_tensor,label

if __name__ == "__main__":
    my_dataset = MyDataset("./data")
    img,label = my_dataset[13]
    print("---問1---")
    print(img.size())
    print("---問2---")
    print(label)
   
    