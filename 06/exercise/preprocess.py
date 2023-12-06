import matplotlib.pyplot as plt
from torchvision import transforms 
from PIL import Image


preprocess_1 = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5,0.5,0.5],std=[0.5,0.5,0.5])
     
])
preprocess_2 = transforms.Compose([
    transforms.ToTensor(),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness=0.3,contrast=0.2,saturation=0.2,hue=0.2)
])

preprocess_3 = transforms.Compose([
    transforms.ToTensor(),
    transforms.RandomRotation(degrees=45),
    transforms.RandomResizedCrop(size=(224,224),scale=(0.1,1.0))
])

image_path = "./exercise_data/dog_img.png"
image = Image.open(image_path)
processed_image1 = preprocess_1(image)
processed_image2 = preprocess_2(image)
processed_image3 = preprocess_3(image)
plt.imshow(processed_image1.permute(1,2,0))
plt.show()
plt.imshow(processed_image2.permute(1,2,0))
plt.show()
plt.imshow(processed_image3.permute(1,2,0))
plt.show()