import math
# def typeConfirmation():
#     if(type == 1 ):
#         print('RMSD selected!')
#         data()
#     elif(type == 2):
#         print('MC-MC H-Bond selected!')
#         data()
#     elif(type == 3):
#         print('P-W H-Bond selected!')
#         data()
#     elif(type == 4):
#         print('SASA selected!')
#         data()
#     else:
#         print('Invalid selection. Please try again.')
#         structureSelection()
def structureSelection():
    structure = input('Select the type using the corresponding number: \nRMSD (1) \nMC-MC H-Bond (2) \nP-W H-Bond (3) \nSASA (4)\n')
    if(structure == '1'):
        structureSelection.structure = 'RMSD'
        print(structureSelection.structure + ' selected!')
        return structureSelection.structure
    elif(structure == '2'):
        structure = 'MC-MC H-Bond'
        print(structureSelection.structure + ' selected!')
        return structureSelection.structure      
    elif(structure == '3'):
        structure = 'P-W H-Bond'
        print(structureSelection.structure + ' selected!')
        return structureSelection.structure
    elif(structure == '4'):
        structure = 'SASA'
        print(structureSelection.structure + 'elected!')
        return structureSelection.structure
    else:
        print('Invalid selection. Please try again.')
        structureSelection()
def datapH():
    yesnopH = input('Do you have a pH value? (Y/N)\n')
    if(yesnopH.casefold() == 'y'):
        datapH.pH = input('Please enter your pH value.\n')
        if(not datapH.pH.isdigit()):
            print('Invalid pH!')
            datapH()
        elif(int(datapH.pH) < 1 or int(datapH.pH) > 14):
            print('Invalid pH!')
            datapH()
    elif(yesnopH.casefold() == 'n'):
        pass
    else:
        print('Invalid response!')
        datapH()
def dataTemperature():
    yesnotemperature = input('Do you have a temperature value (\u00B0C)? (Y/N)\n')
    if(yesnotemperature.casefold() == 'y'):
        dataTemperature.temperature = input('Please enter your temperature value (\u00B0C)\n')
        if(not dataTemperature.temperature.isdigit()):
            print('Invalid temperature!')
            dataTemperature()
    elif(yesnotemperature.casefold() == 'n'):
        pass
    else:
        print('Invalid response!')
        dataTemperature()
def dataStructure():
    yesnostructure = input('Do you have a value corresponding to the ' + structureSelection.structure + '? (Y/N)\n')
    if(yesnostructure.casefold() == 'y'):
        dataStructure.structureValue = input('Please enter the corresponding value in nm or nm^2.\n')
        if(not dataStructure.structureValue.isdigit()):
            print('Invalid structure value!')
            dataStructure()
        elif(int(dataStructure.structureValue) <= 0):
            print('Invalid structure value!')
            dataStructure()
    elif(yesnostructure.casefold() == 'n'):
        pass
    else:
        print('Invalid response!')
        dataStructure()
def data():
    datapH()
    dataTemperature()
    dataStructure()

structureSelection()
data()