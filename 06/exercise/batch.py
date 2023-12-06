import matplotlib.pyplot as plt
from torchvision import transforms 
from PIL import Image
from pathlib import Path
from torch.utils.data import Dataset,DataLoader,random_split
import torch

class ImageTransform():
    def __init__(self,resize,mean,std):
        self.data_transform = {
            'train': transforms.Compose([
                transforms.RandomHorizontalFlip(),
                transforms.RandomResizedCrop(resize,scale=(0.8,1.0)),
                transforms.ToTensor(),
                transforms.Normalize(mean,std)
            ]),

            'val': transforms.Compose([
                transforms.Resize((resize)),
                transforms.ToTensor(),
                transforms.Normalize(mean,std)
            ])
        }

    def __call__(self,img,phase='train'):
        return self.data_transform[phase](img)
    
class MyDataset(Dataset):
    def __init__(self,img_list,transform=None,phase='train'):
        self.transform = transform
        self.phase = phase
        self.img_list = img_list

    def __len__(self):
        return len(self.img_list)
    
    def __getitem__(self,idx):
        img_path = self.img_list[idx]
        img = Image.open(img_path)
        img_tensor = self.transform(img,self.phase)
        img_path = Path(img_path)
        parts = img_path.parts
        label = int(parts[-2])

        return img_tensor,label
    
if __name__ == "__main__":  
    data_directory = "../../05/exercise/data"
    data_directory_path = Path(data_directory).resolve()
    dir_list = sorted(list(data_directory_path.glob("*")))
    file_list = []
    for dir in dir_list:
        file_path_list = list(dir.glob("*"))
        file_list += file_path_list

    dataset_size = len(file_list)
    train_ratio = 0.8
    train_size =  int(train_ratio*dataset_size)
    val_size = dataset_size - train_size
    # dataloader = DataLoader(dataset=MyDataset("."),batch_size=8)
    train_dataset,val_dataset = random_split(file_list,[train_size,val_size])
    size = 24
    mean = (0.5,0.5,0.5) 
    std = (0.5,0.5,0.5) 
    train_dataset = MyDataset(train_dataset,transform=ImageTransform(size,mean,std),phase='train')
    val_dataset = MyDataset(val_dataset,transform=ImageTransform(size,mean,std),phase='val')
    print("===== problem2 =====")
    print(f"Train dataset size: {len(train_dataset)}")
    print(f"Val dataset size: {len(val_dataset)}")
    train_dataloader = torch.utils.data.DataLoader(
    train_dataset, batch_size=8)

    val_dataloader = torch.utils.data.DataLoader(
        val_dataset, batch_size=8)
    print("===== problem3 =====")
    for batch in train_dataloader:
        data,labels = batch
        print("Data shape:",data.shape)
        print("Labels:",labels)    