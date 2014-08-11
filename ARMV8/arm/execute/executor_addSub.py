'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.utils.utilFunc import setInstrFlag

#Add Subtract - Immediate
def execAdd_i32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    imm6 = int(binary[16:22],2)
    setInstrFlag()
    
    
def execAdds_i32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execSub_i32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execSubs_i32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execAdd_i64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execAdds_i64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execSub_i64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execSubs_i64(binary): 
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
#Add Subtract - Shift register
def execAdd_sr32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execAdds_sr32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execSub_sr32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execSubs_sr32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execAdd_sr64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execAdds_sr64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execSub_sr64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execSubs_sr64(binary): 
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
#Add Subtract - Extended register
def execAdd_er32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execAdds_er32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execSub_er32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execSubs_er32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execAdd_er64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execAdds_er64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execSub_er64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execSubs_er64(binary): 
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    