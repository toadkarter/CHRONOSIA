# This is a small tool that will allow me to convert
# text I've written for the VN portion of the game
# directly into Python code

# Opening input and output files
vntextfile = open("vntext.txt","r",encoding="utf8")
vnresultsfile=open("vnformatted.txt","w",encoding="utf8")

# Setting variable name counters
lncounter=1
sncounter=0
j=1

totalScreenList="totalScreenList=["

# Looping through lines in file
for line in vntextfile:

    # Print screen variable if there is a blank line in the file 
    if line=="\n":
        vnresultsfile.write(f'screen{sncounter}=[')
        while j<lncounter-1:
            vnresultsfile.write(f'line{j},')
            j+=1
        vnresultsfile.write(f'line{lncounter-1}]\n')
        vnresultsfile.write('\n')
        print(f"screen{sncounter}...OK")
        totalScreenList+=(f"screen{sncounter},")
        sncounter+=1
        j+=1
    
    # Convert to line variable
    else:
        dialogue=line.replace('\n', '')
        vnresultsfile.write(f'line{lncounter}="{dialogue}"\n')
        print(f"line{lncounter}...OK")
        lncounter+=1

totalScreenList=totalScreenList[:-1]
totalScreenList+="]"

vnresultsfile.write(totalScreenList)