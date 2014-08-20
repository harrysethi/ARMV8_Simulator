fn1:
mov w3, #3
mov w4, #4
ret
_start:
mov x1, #2
BL fn1
mov x0, #2
