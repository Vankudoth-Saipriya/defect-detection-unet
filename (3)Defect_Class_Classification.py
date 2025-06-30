import os
from torch.utils.data import Dataset
from PIL import Image
import numpy as np
import torch
import torchvision.transforms as transforms

class DefectDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform if transform else transforms.ToTensor()

        # ✅ Define class mapping
        self.class_mapping = {
            0: 0,  # Background
            1: 1,  # Defect_Class5
            2: 2,  # Defect_Class8
            3: 3,  # Defect_Class9
            4: 4,  # Defect_Class10
            5: 5,  # Defect_Class11
        }
        
        self.num_classes = len(self.class_mapping)  # ✅ Ensure correct num_classes

        # Define image and mask directories
        self.image_dir = os.path.join(root_dir, "Img.After.Melting")
        self.mask_dirs = {
            0: os.path.join(root_dir, "Defect_Class0"),
            1: os.path.join(root_dir, "Defect_Class5"),
            2: os.path.join(root_dir, "Defect_Class8"),
            3: os.path.join(root_dir, "Defect_Class9"),
            4: os.path.join(root_dir, "Defect_Class10"),
            5: os.path.join(root_dir, "Defect_Class11"),
        }

        # Load image filenames
        self.image_filenames = sorted(os.listdir(self.image_dir))

    def __len__(self):
        return len(self.image_filenames)

    def __getitem__(self, idx):
        img_name = self.image_filenames[idx]
        img_path = os.path.join(self.image_dir, img_name)

        # Load and transform image
        image = Image.open(img_path).convert("RGB")
        image = self.transform(image)

        # Initialize mask as background (0)
        mask = np.zeros((image.shape[1], image.shape[2]), dtype=np.uint8)

        # Load and combine defect masks
        for class_idx, mask_dir in self.mask_dirs.items():
            mask_path = os.path.join(mask_dir, img_name)
            if os.path.exists(mask_path):
                defect_mask = Image.open(mask_path).convert("L")
                defect_mask = np.array(defect_mask, dtype=np.uint8)

                if class_idx in self.class_mapping:  # ✅ Ensure valid mapping
                    mask[defect_mask > 0] = self.class_mapping[class_idx]
                else:
                    print(f"⚠️ WARNING: Class {class_idx} not found in class_mapping!")

        # Convert mask to tensor
        mask = torch.tensor(mask, dtype=torch.long)

        return image, mask
