@256
D=A
@SP
M=D
@RET0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@SP
D=M-D
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(RET0)
(Main.fibonacci)
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=D-M
M=-1
@TMP0
D;JGT
@SP
A=M
M=0
(TMP0)
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@IF_TRUE
D;JNE
@IF_FALSE
0;JMP
(IF_TRUE)
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D
@SP
M=M+1
@5
D=A
@LCL
A=M
A=A-D
D=M
@SP
A=M
M=D
@SP
M=M+1
@4
D=A
@LCL
A=M
A=A-D
D=M
@SP
A=M
M=D
@SP
M=M+1
@3
D=A
@LCL
A=M
A=A-D
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@LCL
A=M
A=A-D
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@LCL
A=M
A=A-D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@THAT
M=D
@SP
M=M-1
@SP
A=M
D=M
@THIS
M=D
@SP
M=M-1
@SP
A=M
D=M
@ARG
M=D
@SP
M=M-1
@SP
A=M
D=M
@LCL
M=D
@SP
M=M-1
@SP
A=M
A=M
0;JMP
(IF_FALSE)
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
@SP
M=M+1
@RET1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@SP
D=M-D
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(RET1)
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
@SP
M=M+1
@RET2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@SP
D=M-D
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(RET2)
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D+M
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D
@SP
M=M+1
@5
D=A
@LCL
A=M
A=A-D
D=M
@SP
A=M
M=D
@SP
M=M+1
@4
D=A
@LCL
A=M
A=A-D
D=M
@SP
A=M
M=D
@SP
M=M+1
@3
D=A
@LCL
A=M
A=A-D
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@LCL
A=M
A=A-D
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@LCL
A=M
A=A-D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@THAT
M=D
@SP
M=M-1
@SP
A=M
D=M
@THIS
M=D
@SP
M=M-1
@SP
A=M
D=M
@ARG
M=D
@SP
M=M-1
@SP
A=M
D=M
@LCL
M=D
@SP
M=M-1
@SP
A=M
A=M
0;JMP
(Sys.init)
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
@RET3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@SP
D=M-D
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(RET3)
(WHILE)
@WHILE
0;JMP
