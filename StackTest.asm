//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@eq0
D;JNE
@SP
A=M-1
M=-1
(eq0)

//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

//eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@eq1
D;JNE
@SP
A=M-1
M=-1
(eq1)

//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@eq2
D;JNE
@SP
A=M-1
M=-1
(eq2)

//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@lt0
D;JGE
@SP
A=M-1
M=-1
(lt0)

//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

//lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@lt1
D;JGE
@SP
A=M-1
M=-1
(lt1)

//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@lt2
D;JGE
@SP
A=M-1
M=-1
(lt2)

//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@gt0
D;JLE
@SP
A=M-1
M=-1
(gt0)

//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

//gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@gt1
D;JLE
@SP
A=M-1
M=-1
(gt1)

//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=0
@gt2
D;JLE
@SP
A=M-1
M=-1
(gt2)

//push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1

//add
@SP
AM=M-1
D=M
A=A-1
M=D+M

//push constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1

//sub
@SP
AM=M-1
D=M
A=A-1
M=M-D

//neg
@SP
A=M-1
M=-M

//and
@SP
AM=M-1
D=M
A=A-1
M=D&M

//push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

//or
@SP
AM=M-1
D=M
A=A-1
M=D|M

//not
@SP
A=M-1
M=!M

