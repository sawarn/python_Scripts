#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 02:04:16 2020

@author: rashi
"""
import torch
import torch.nn
from torch.autograd import Variable
import torch.nn.functional as F

class SimpleCNN(torch.nn.Module):
   def __init__(self):
      super(SimpleCNN, self).__init__()
      
      #First Conv Block
      #Input channels = 1, output channels = 16
      #self.conv1 = torch.nn.Conv2d(1, 16, kernel_size = 3, stride = 1, padding = 1)
      #self.relu1 = torch.nn.ReLU()
      #self.pool = torch.nn.MaxPool2d(kernel_size = 2, stride = 2, padding = 0)
      #self.conv1_drop = torch.nn.Dropout2d()
      self.layer1 = torch.nn.Sequential(
            torch.nn.Conv2d_1(1, 16, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2, padding = 0),
            torch.nn.Dropout())
      
      #Second Conv block
      #self.conv2 = torch.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=3, stride=1, padding=1)
      #self.relu2 = torch.nn.ReLU()
      #self.conv3 = torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
      #self.relu3 = torch.ReLU()
      #self.pool = torch.nn.MaxPool2d(kernel_size=2)
      self.layer1 = torch.nn.Sequential(
            torch.nn.Conv2d(16, 16, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2, padding = 0),
            torch.nn.Dropout())
      
   def forward(self, x):
       x = F.relu(self.conv1(x))
       x = self.pool(x)
       return (x)

