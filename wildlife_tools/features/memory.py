import torch
import os
import numpy as np
from tqdm import tqdm 
from wildlife_tools.features.base import FeatureExtractor
from wildlife_tools.data import WildlifeDataset


class DataToMemory(FeatureExtractor):
    ''' Loads dataset to memory for faster access. '''

    def __call__(self, dataset: WildlifeDataset):
        features = []
        for x, y in tqdm(dataset, mininterval=1, ncols=100):
            features.append(x)
        return features
