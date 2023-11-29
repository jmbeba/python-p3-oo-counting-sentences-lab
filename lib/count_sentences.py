#!/usr/bin/env python3

import re
class MyString:
  def __init__(self, value=""):
    if(type(value) == str):
      self._value = value
    else:
      print("The value must be a string.")
      
  def get_value(self):
      return self._value
  
  def set_value(self, value):
    if(type(value) == str):
      self._value = value
    else:
      print("The value must be a string.")  
        
  def is_sentence(self):
    return self._value.endswith('.')
  
  def is_question(self):
    return self._value.endswith('?')
  
  def is_exclamation(self):
    return self._value.endswith('!')
  
  def count_sentences(self):
    '''
      [.!?] is used to match occurrences of ?, ! or . in the string.
    '''
    return len([word for word in re.split(r'[.!?]', self._value) if word != ''])
      
  value = property(get_value, set_value)  

