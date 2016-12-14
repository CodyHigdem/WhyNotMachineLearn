# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:37:50 2016

@author: cody
"""

import tensorflow as tf
import data_utils
import seq2seq_model

def train():
    #prepare said dataset
    encoder_train, decoder_train = data_utils.prepare_custom_data(
        gConfig['working_directory'])
        #attempt to tokenize the sentences
    train_set = read_data(encorder_train, decoder_train)