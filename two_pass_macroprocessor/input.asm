.model
.stack
.data
MSG1 DB 10,13,"Welcome$"
MSG2 DB 10,13,"TCET$"

.code
DISP MACRO XX
MOV AH,09
LEA DX,XX
INT 21H
ENDM

.startup
DISP MSG1
DISP MSG2

.exit
end
