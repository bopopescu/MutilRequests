'''
Created on 2013-3-15

@author: poorevil
'''

class CategoaryModel(object):
    
    '''
    Ŀ¼model
    '''
    
    def __init__(self,cId,title,parentCId=0):
        self.cId = cId                              #Ŀ¼id
        self.title = title                          #����
        self.parentCId = parentCId                  #����Ŀid