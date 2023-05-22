import torchxrayvision as xrv
import torch
import torchvision
import skimage
import numpy as np

img = skimage.io.imread("view1_frontal.jpg") # this is lung opacity
img = xrv.datasets.normalize(img, 255) # convert 8-bit image to [-1024, 1024] range
img = np.mean(img, axis=1)[None,...]  # Convert to single color channel
img = np.expand_dims(img, axis=0) 
# reize image to 224 x 224 pixels
transform = torchvision.transforms.Compose([torchvision.transforms.Resize(224)])
img = transform(torch.from_numpy(img))


# # Load model and process image
model = xrv.models.DenseNet(weights="densenet121-res224-all")
outputs = model(img[None,...]) # or model.features(img[None,...])

# Print results
e = dict(zip(model.pathologies, outputs[0].detach().numpy()))
print(e)

## Results: It's max was 84% for lung opacity

# {'Atelectasis': 0.56839526, 
# 'Consolidation': 0.56888735, 
# 'Infiltration': 0.2754276, 
# 'Pneumothorax': 0.52556527, 
# 'Edema': 0.47924855, 
# 'Emphysema': 0.5275707, 
# 'Fibrosis': 0.13631964, 
# 'Effusion': 0.5207366, 
# 'Pneumonia': 0.7087451,
#  'Pleural_Thickening': 0.19831477, 
# 'Cardiomegaly': 0.21343403, 
# 'Nodule': 0.5159247,
#  'Mass': 0.5853982, 
# 'Hernia': 0.0063520977, 
# 'Lung Lesion': 0.08911495, 
# 'Fracture': 0.4101464, 
# Lung Opacity': 0.8488826, '
# Enlarged Cardiomediastinum': 0.62651}