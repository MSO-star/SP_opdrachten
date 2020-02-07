def function():

 with open('bestand.txt', 'r') as i:
    lines = i.readlines()

 lines = [line.replace('/n', '') for line in lines]

 with open('bestand.txt', 'w') as i:
    i.writelines(lines)
    i.close()


function()

