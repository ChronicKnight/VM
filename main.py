def clean(line):
  
  line = line.strip() # strip leading and trailing blanks
  newline = ""  # initialize a line to write assembler code instructions to
  if len(line) > 0 and line[0:2] != "//":  # check for a comment line
    for c in line:  # need to look at each character to make sure there isn't an inline commenet after the code
      if c != "/":  # a "/" would indicate the  beginning of a comment, we can disregard the rest of the line
        newline = newline + c;  # add character to line of assembly code
      else:
        break # disregard the rest of the line
    newline = newline.strip()   
    newline = newline + "\n"    # write the clean line
  return newline

def pass1(vmFileName):

  vmFile = open(vmFileName + ".vm", "r")
  vmCleanfile = open("c" + vmFileName + ".vm", "w")
  print ("Cleaning " + vmFileName + ".vm of any comments or white space....")

  for line in vmFile:
    newline = clean (line)
    vmCleanfile.write(newline)

# Important to remember to close the files
  vmFile.close()
  vmCleanfile.close()



def pass2(vmFileName):
  segments = {"local":"LCL", "argument":"ARG", "this":"THIS", "that":"THAT"}

  readFile = open("c" + vmFileName + ".vm", "r")
  writeFile = open(vmFileName + ".asm", "w")
  writeString = ""
  gtCount = 0
  ltCount = 0
  eqCount = 0

  for line in readFile:
    splitLine = line.split()

    if splitLine[0] == "push":
      if splitLine[1] in segments:
        writeString = ("//push " + splitLine[1] + " " + splitLine[2] + "\n@" + segments[splitLine[1]] + "\nD=M\n@" + splitLine[2] + "\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n\n")
        
      elif splitLine[1] == "constant":
        writeString = ("//push constant " + splitLine[2] + "\n@" + splitLine[2] + "\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n\n")
      
      else:  
        if splitLine[1] == "static":
          atPlace = "Foo." + splitLine[2]
        elif splitLine[1] == "temp":
          atPlace = str(5 + int(splitLine[2]))
        elif splitLine[1] == "pointer":
            atPlace = str(3 + int(splitLine[2]))
        writeString = ("//push " + splitLine[1] + " " + splitLine[2] + "\n@" + atPlace + "\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n\n")
      
      writeFile.write(writeString)
   

    elif splitLine[0] == "pop":
      if splitLine[1] in segments:
        writeString = ("//pop " + splitLine[1] + " " + splitLine[2] + "\n@" + segments[splitLine[1]] + "\nD=M\n@" + splitLine[2] +"\nD=D+A\n@13\nM=D\n@SP\nAM=M-1\nD=M\n@13\nA=M\nM=D\n\n")
      else:        
        if splitLine[1] == "static":
          atPlace = "Foo." + splitLine[2]
        elif splitLine[1] == "temp":
          atPlace = str(5 + int(splitLine[2]))
        elif splitLine[1] == "pointer":
          atPlace = str(3 + int(splitLine[2]))
        writeString = ("//pop " + splitLine[1] + " " + splitLine[2] + "\n@SP\nAM=M-1\nD=M\n@" + atPlace + "\nM=D\n\n")
      
      writeFile.write(writeString)

    elif splitLine[0] == "add":
      writeFile.write("//add\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D+M\n\n")

    elif splitLine[0] == "sub":
      writeFile.write("//sub\n@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D\n\n")
      
    elif splitLine[0] == "neg":
      writeFile.write("//neg\n@SP\nA=M-1\nM=-M\n\n")
      
    elif splitLine[0] == "eq":
      writeFile.write("//eq\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=0\n@eq" + str(eqCount) +"\nD;JNE\n@SP\nA=M-1\nM=-1\n(eq" + str(eqCount) +")\n\n")
      eqCount += 1
   
    elif splitLine[0] == "gt":
      writeFile.write("//gt\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=0\n@gt" + str(gtCount) +"\nD;JLE\n@SP\nA=M-1\nM=-1\n(gt" + str(gtCount) +")\n\n")
      gtCount += 1
      
    elif splitLine[0] == "lt":
      writeFile.write("//lt\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=0\n@lt" + str(ltCount) +"\nD;JGE\n@SP\nA=M-1\nM=-1\n(lt" + str(ltCount) + ")\n\n")
      ltCount += 1

    elif splitLine[0] == "and":
      writeFile.write("//and\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D&M\n\n")
    
    elif splitLine[0] == "or":
      writeFile.write("//or\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D|M\n\n")
      #writeFile.write("//or\n@SP\nAM=M-1\nD=!M\nA=A-1\nM=!M\nM=D&M\n\n")
    
    elif splitLine[0] == "not":   
      writeFile.write("//not\n@SP\nA=M-1\nM=!M\n\n")
      #writeFile.write("//not\n@SP\nA=M-1\nD=M\n@notLabel" + str(notCount) +"\nD;JEQ\n@SP\nA=M-1\nMD=!M\n@notEnd" + str(notCount) + "\nD;JEQ\n@SP\nA=M-1\nM=!M\n@notEnd" + str(notCount) + "\n0;JMP\n(notLabel" + str(notCount) +")\n@SP\nA=M-1\nM=-1\n(notEnd" + str(notCount) + ")\n\n")
      #notCount += 1

  readFile.close()
  writeFile.close()
      
#push, pop
#add, sub, neg, eq, get, lt, and, or, not


  


vmFileName = input("Enter the .vm file to translate: ")
pass1(vmFileName)
pass2(vmFileName)


  

# //add
# @SP
# AM=M-1
# D=M
# A=A-1
# M=D+M

# //push constant int
# @int
# D=A
# @SP
# A=M
# M=D
# @SP
# M=M+1

# #pop x
# @SP
# AM=M-1
# D=M
# @x
# M=D

# #sub
# @SP
# AM=M-1
# D=M
# A=A-1
# M=M-D
# #sub = ("//sub\n@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D")

# #neg
# @SP
# A=M-1
# M=-M
# #neg = ("//neg\n@SP\nA=M-1\nM=-M\n")

# //eq
# @SP
# AM=M-1
# D=M
# A=A-1
# D=M-D
# M=0
# @END
# D;JNE
# @SP
# A=M-1
# M=-1
# (END)

# #and
# @SP
# AM=M-1
# D=M
# A=A-1
# M=D&M
# #and = ("//and\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D&M\n")

# #gt
# @SP
# AM=M-1
# D=M
# A=A-1
# D=M-D
# M=0
# @END
# D;JLE
# @SP
# A=M-1
# M=-1
# (END)

# #lt
# @SP
# AM=M-1
# D=M
# A=A-1
# D=M-D
# M=0
# @END
# D;JGE
# @SP
# A=M-1
# M=-1
# (END)
# #lt = ("//lt\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\nM=0\n@END\nD;JGE\n@SP\nA=M-1\nM=-1\n(END)")

# #not   need to add more to make it only carry through when either -1 or 0
# @SP
# A=M-1
# M=!M
# #not = ("//not\n@SP\nA=M-1\nM=!M\n")

# or
# @SP
# AM=M-1
# D=M
# A=A-1
# M=D|M
# ("//or\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D|M\n\n")