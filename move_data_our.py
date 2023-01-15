import os
import re
import shutil

dataset_positive = 'Our_dataset/Dataset_v1.2/Positive'
dataset_negative = 'Our_dataset/Dataset_v1.2/Negative'

def create_dir_for_dataset():
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'datasets')
    
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    
    for i in range(1,9):
        if not os.path.exists(os.path.join(final_directory, f'{i}') ):
            child_directory = os.path.join(final_directory, f'{i}') 
            os.makedirs(child_directory)
            
def remove_str(str):
    nums = re.findall(r'\d+', str)
    if len(nums) == 0:
        return None
    return int(nums[0])

count = 0

create_dir_for_dataset()
import shutil

# splitting data for getting just 1-7 labelled and added them to final folder dataset
# !! note number 8 is included in folder negative 
for data in os.listdir(dataset_positive):
    tmp = data.split('_', -1)
    num = remove_str(tmp[2])
    if num is not None and num < 8 and num > 0:
        shutil.copy(os.path.join(dataset_positive, data), os.path.join(f'datasets/{num}', data))
        count+=1

for data in os.listdir(dataset_negative):
    shutil.copy(os.path.join(dataset_negative, data), os.path.join(f'datasets/{8}', data))
    count+=1

print(count)
        