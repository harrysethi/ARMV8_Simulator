'''
@author: harinder
'''
import utilFunc
import mem
import const


def op_i(binary, N, instr, sub_op, setFlags):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27],'1')
    if(N == 32):
        rnVal = rnVal[32:64]
        r = 'w'
    elif(N == 64):
        r = 'x'
    imm12 = binary[10:22]
    shiftType = binary[8:10]
    instr += " " + r + str(rdKey) + ", " + r + str(rnKey) + ", #" + utilFunc.binaryToHexStr(imm12) + ", LSL"
    if shiftType == "00":
        imm12 = imm12.zfill(N)
        instr = instr + " #0"
    elif shiftType == "01":
        imm12 = (imm12 + '0' * 12).zfill(N)
        instr = instr + " #12"
        
    to_store, isSp = utilFunc.addSub(rdKey, rnVal, imm12, sub_op, N, setFlags)    
    utilFunc.finalize(rdKey, to_store.zfill(const.REG_SIZE), instr, isSp)

def execAdd_i32(binary):
    op_i(binary, 32, "ADD", '0', '0')

def execAdds_i32(binary):
    op_i(binary, 32, "ADDS", '0', '1')
    
def execSub_i32(binary):
    op_i(binary, 32, "SUB", '1', '0')
    
def execSubs_i32(binary):
    op_i(binary, 32, "SUBS", '1', '1')
    
def execAdd_i64(binary):
    op_i(binary, 64, "ADD", '0', '0')
    
def execAdds_i64(binary):
    op_i(binary, 64, "ADDS", '0', '1') 
    
def execSub_i64(binary):
    op_i(binary, 64, "SUB", '1', '0')
    
def execSubs_i64(binary): 
    op_i(binary, 64, "SUBS", '1', '1')
    
# fetches the operand2 for shift register operations
def fetchOp2_sr(rmVal, shiftType, amt, instr):
    if shiftType == "00":   
        op2 = utilFunc.lsl(rmVal, amt)
        instr += 'LSL'
    elif shiftType == "01":
        op2 = utilFunc.lsr(rmVal, amt)
        instr += 'LSR'
    elif shiftType == "10":
        op2 = utilFunc.asr(rmVal, amt)
        instr += 'ASR'
    return op2, instr


    
def op_sr(binary, N, instr, sub_op, setFlags):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmkey = utilFunc.getRegKeyByStringKey(binary[11:16])
    imm6 = binary[16:22]
    imm6Val = int(imm6, 2)
    
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    if(N == 32):
        rnVal = rnVal[32:64]
        rmVal = rmVal[32:64]
        r = 'w'
    elif(N == 64):
        r = 'x'  
    shiftType = binary[8:10]
    instr += " " + r + str(rdKey) + ", " + r + str(rnKey) + ", " + r + str(rmkey) + ", "
    op2, instr = fetchOp2_sr(rmVal, shiftType, imm6Val, instr)
    instr += " #" + str(imm6Val)
    to_store,isSp = utilFunc.addSub(rdKey, rnVal, op2, sub_op, N, setFlags) #isSp ignored
    utilFunc.finalize(rdKey, to_store.zfill(const.REG_SIZE), instr, '0')

def execAdd_sr32(binary):
    op_sr(binary, 32, "ADD", '0', '0')
    
def execAdds_sr32(binary):
    op_sr(binary, 32, "ADDS", '0', '1')
    
def execSub_sr32(binary):
    op_sr(binary, 32, "SUB", '1', '0')
    
def execSubs_sr32(binary):
    op_sr(binary, 32, "SUBS", '1', '1')
    
def execAdd_sr64(binary):
    op_sr(binary, 64, "ADD", '0', '0')
    
def execAdds_sr64(binary):
    op_sr(binary, 64, "ADDS", '0', '1')
    
def execSub_sr64(binary):
    op_sr(binary, 64, "SUB", '1', '0')
    
def execSubs_sr64(binary): 
    op_sr(binary, 64, "SUBS", '1', '1')
    
    
def op_er(binary, N, instr, sub_op, setFlags):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmkey = utilFunc.getRegKeyByStringKey(binary[11:16])
    option = binary[16:19]
    imm3 = binary[19:22]
    shift = int(imm3, 2)
    
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '1')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    if(N == 32):
        rnVal = rnVal[32:64]
        rmVal = rmVal[32:64]
        r = 'w'
    elif(N == 64):
        r = 'x'
        if(option[1:3] == '11'):
            rmToPrint = 'x'
        else:
            rmToPrint = 'w'
    instr += " " + r + str(rdKey) + ", " + r + str(rnKey) + ", " + rmToPrint + str(rmkey) + ", "
    op2, instr = utilFunc.extendReg(rmVal, shift, option, instr, N)
    instr += " #" + str(shift)
    to_store, isSp = utilFunc.addSub(rdKey, rnVal, op2, sub_op, N, setFlags)
    utilFunc.finalize(rdKey, to_store.zfill(const.REG_SIZE), instr, isSp)
       


# Add Subtract - Extended register
def execAdd_er32(binary):
   op_er(binary, 32, "ADD", '0', '0')
    
def execAdds_er32(binary):
   op_er(binary, 32, "ADDS", '0', '1')
    
def execSub_er32(binary):
   op_er(binary, 32, "SUB", '1', '0')
    
def execSubs_er32(binary):
    op_er(binary, 32, "SUBS", '1', '1')
    
def execAdd_er64(binary):
    op_er(binary, 64, "ADD", '0', '0')
    
def execAdds_er64(binary):
    op_er(binary, 64, "ADDS", '0', '1')
    
def execSub_er64(binary):
    op_er(binary, 64, "SUB", '1', '0')
    
def execSubs_er64(binary): 
    op_er(binary, 64, "SUBS", '1', '1')
    
