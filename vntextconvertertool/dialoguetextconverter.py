

dialoguetextfile = open("dialoguetext.txt","r",encoding="utf8")
dialogueresultsfile=open("dialoguetextformatted.txt","w",encoding="utf8")

totalDialogue=0
instanceDialogue=0
instanceLineNum=0

for line in dialoguetextfile:
    if "***" in line:
        instanceDialogue+=1
        looping=True
        while looping:
            instanceLineNum+=1
            if line=="\n":
                dialogueresultsfile.write(f"dialogue{totalDialogue}_{instanceDialogue}=[dialogue{totalDialogue}_{instanceDialogue}_option,")
                for i in range(2, instanceLineNum-1):
                    dialogueresultsfile.write(f"dialogue{totalDialogue}_{instanceDialogue}_{i},")
                dialogueresultsfile.write(f"dialogueresultsfile.write(dialogue{totalDialogue}_{instanceDialogue}_{instanceLineNum}]\n")
                dialogueresultsfile.write("\n")
                totalDialogue+=1
                looping=False
            else:
                if instanceLineNum==1:
                    dialogueresultsfile.write(f'dialogue{totalDialogue}_{instanceDialogue}_option="{line}"\n')
                else:
                    dialogueresultsfile.write(f'dialogue{totalDialogue}_{instanceDialogue}_{instanceLineNum}="{line}"\n')
                instanceLineNum+=1
print("Finished")








