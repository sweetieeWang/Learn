from torchvision import transforms
from PIL import Image
img_path = 'datasets/hymenoptera_data/train/ants/0013035.jpg'
img = Image.open(img_path)
print(img)
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)
print(tensor_img)
