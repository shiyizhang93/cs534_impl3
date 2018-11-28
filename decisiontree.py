# !/usr/bin/env python

import numpy as np
import csv
import sys, os, pdb
from process_data import *

class DecisionTree():
	def __init__(self, fn_train, fn_valid, fn_test=None):
		self.csv_train = CSV(fn_train)
		self.csv_train.extract_XY()
		self.csv_train.categorize_Y()
		self.x_train, self.y_train = self.csv_train.convert_all_to_numbers()		

		self.csv_valid = CSV(fn_valid)
		self.csv_valid.extract_XY()
		self.csv_valid.categorize_Y()
		self.x_valid, self.y_valid = self.csv_valid.convert_all_to_numbers()		

		if fn_test != None:
			self.csv_test = CSV(fn_test)
			self.csv_test.extract_XY_test()
			self.csv_test.categorize_Y()
			self.x_test, self.y_test = self.csv_test.convert_all_to_numbers()
      
  #Calculate gini index and the benefit of splite feature    
  def gini_benefit(cp,cm,clp,clm,crp,crm):
    if clp+clm==0 or crp+crm==0:
      return 0
    pUl = (2*clp*clm/((clp+clm)*(cp+cm)))
    pUr = (2*crp*crm/((crp+crm)*(cp+cm)))
    Ua =  (2*cp*cm/(cp+cm)**2)
    return (Ua-pUl-pUr)
  
  #split to different leaf
  def split_leaf(self, threshold, para, leaf_clp, leaf_clm, leaf_crp, leaf_crm):
    left_leaf = np.array([])
    right_leaf = np.array([])
    for i in rang(0,len(self.x_train[:][0])-1):
      y_value = self.y_train[i]
      if self.x_train[i][para] <= T:
        left_leaf = np.append(self.x_train[i][para])
        if self.x_train[i][para] == 1:
          leaf_clp += 1
        else:
          leaf_clm += 1
      else:
        right_leaf = np.append(self.x_train[i][para])
        if self.x_train[i][para] == 1:
          leaf_crp += 1
        else:
          leaf_crm += 1
  return left_leaf, right_leaf, leaf_clp, leaf_clm, leaf_crp, leaf_crm
  
  #Make a decision tree
  def make_node(self, previous_feature=None):
    #initialize the parameters
    
    gini = 0
    gini_f = 0
    gini_temp
        
    T = 0
    T_f = 0
    T_temp
    
    feature = 0
    tree_clp, tree_clm, tree_crp, tree_crm = 0, 0, 0, 0
    
    left_node = np.array([])
    right_node = np.array([])
    left_node_f = np.array([])
    right_node_f = np.array([])
    left_node_temp = np.array([])
    right_node_temp = np.array([])
    
    #Calculate the number of result 3 and 5
    temp = 0
    for i in range(0, len(self.y_train[:])-1):
      if self.y_train[i] == 1:
        temp += 1
    cp = temp
    cm = len(self.y_train[:])-temp
    #Calculate gini-index and benefit
    for j in range(0, len(self.x_train[0][:])-1):
      for k in range(0, len(self.x_train[:][0])-1):
        T_temp = self.x_train[k][j]
        left_node_temp, right_node_temp, tree_clp, tree_clm, tree_crp, tree_crm = split_leaf(self, T, j, tree_clp, tree_clm, tree_crp, tree_crm)
        gini_temp = gini_benefit(cp, cm, tree_clp, tree_clm, tree_crp, tree_crm)
        if gini_temp > gini_f:
          gini_f= gini_temp
          left_node_f = left_node_temp
          right_node_f = left_node_temp
          T_f = T_temp
      if gini_f > gini:
        gini = gini_f
        left_node = left_node_f
        right_node = right_node_f
        T = T_f
  return gini, left_node, right_node, T
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
          
        