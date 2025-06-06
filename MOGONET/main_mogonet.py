""" Example for MOGONET classification
"""
from train_test import train_test
import torch

if __name__ == "__main__":    
    data_folder = 'ROSMAP'
    view_list = [1,2,3]
    num_epoch_pretrain = 500
    num_epoch = 2500
    lr_e_pretrain = 1e-3  
    lr_e = 5e-4
    lr_c = 1e-3
    
    if data_folder == 'ROSMAP':
        num_class = 2
        # adj_parameter = 5  # Try different values
        # dim_he_list = [200,200,100]
    if data_folder == 'BRCA':
        num_class = 5
    
    adj_metric = "cosine"
    
    train_test(data_folder, view_list, num_class,
               lr_e_pretrain, lr_e, lr_c, 
               num_epoch_pretrain, num_epoch)             