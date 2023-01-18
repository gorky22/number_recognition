import os
import re
import shutil

dataset_positive = 'Dataset_v1.2/Positive'
dataset_negative = 'Dataset_v1.2/Negative'

dataset_seven = 'seven_plastics'

num_of_datas = {'1': 0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}

# this function creates directories needed for easier loading 
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


## move -> separate dataset to appropriate dirrectories bolognese university
def move_v12():
    # splitting data for getting just 1-7 labelled and added them to final folder dataset
    # !! note number 8 is included in folder negative 
    for data in os.listdir(dataset_positive):
        tmp = data.split('_', -1)
        num = remove_str(tmp[2])
        if num is not None and num < 8 and num > 0:
            shutil.copy(os.path.join(dataset_positive, data), os.path.join(f'datasets/{num}', data))

            num_of_datas[str(num)] +=1

    for data in os.listdir(dataset_negative):
        shutil.copy(os.path.join(dataset_negative, data), os.path.join(f'datasets/{8}', data))
        num_of_datas[str(8)] +=1


## move -> separate dataset to appropriate dirrectories kaggle
def move_seven():
    for nums in  os.listdir(dataset_seven):
        actual_num  = nums.split('_')[0]
        actual_dir = os.path.join(dataset_seven, nums)
        for img in os.listdir(actual_dir):
            shutil.copy(os.path.join(actual_dir, img), os.path.join(f'datasets/{actual_num}', img))
            num_of_datas[actual_num] +=1
            

create_dir_for_dataset()
move_v12()
move_seven()



print(f'moved : ')

for key in num_of_datas:
    print(f'number {key}: {num_of_datas[key]}')
        