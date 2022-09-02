import math
def structureSelection():
    structure = input('Select the type using the corresponding number: \nRMSD (1) \nMC-MC H-Bond (2) \nP-W H-Bond (3) \nSASA (4)\n')
    if(structure == '1'):
        structureSelection.structure = 'RMSD'
        print(structureSelection.structure + ' selected!')
    elif(structure == '2'):
        structureSelection.structure = 'MC-MC H-Bond'
        print(structureSelection.structure + ' selected!')
    elif(structure == '3'):
        structureSelection.structure = 'P-W H-Bond'
        print(structureSelection.structure + ' selected!')
    elif(structure == '4'):
        structureSelection.structure = 'SASA'
        print(structureSelection.structure + ' selected!')
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
        if(structureSelection.structure == 'RMSD'):
            dataStructure.structureValue = input('Please enter the corresponding value in nm.\n')
        else:
            dataStructure.structureValue = input('Please enter the corresponding value in nm^2.\n')
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
    if((datapH.pH == 'None' and dataTemperature.temperature == 'None') or (datapH.pH == 'None' and dataStructure.structureValue == 'None') or (dataTemperature.temperature == 'None' and dataStructure.structureValue == 'None')):
        print("\n\nERROR: At least 2 attributes are required for prediction.")
        exit
    else:
        print('\n\nSummary of Data:')
        print('pH: ' + datapH.pH)
        print('Temperature: ' + dataTemperature.temperature + '\u00B0C')
        if(structureSelection.structure == 'RMSD'):
            print(structureSelection.structure + ': ' + dataStructure.structureValue + ' nm')
        else:
            print(structureSelection.structure + ': ' + dataStructure.structureValue + ' nm^2')
def prediction():
    print('\n\nPrediction function: Work in progress. This function will take the listed attributes and predict whether the spike protein denatures or not and the values of missing attributes, if there are any.')
structureSelection()
data()
prediction()