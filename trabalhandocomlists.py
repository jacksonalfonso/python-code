"""
    TRABALHANDO COM LISTAS
"""

pessoas = [['Jackson',['Filho','Pai','Avô'],'H'], ['Leila',['Filha','Mãe','Amiga'],'F']]
#print(type(pessoas))                     

for pessoa, parentescos, genero in pessoas:
   for parentesco in parentescos:
      if genero == 'H':
         print(f'{pessoa} além de ser um super Homem ainda é : {parentesco}')
      else:
         print(f'{pessoa} além de ser uma super mulher ainda é : {parentesco}')

