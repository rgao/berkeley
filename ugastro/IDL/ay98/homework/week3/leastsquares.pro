function F1, L
                                ; function that outputs a 2xn matrix
                                ; with the 1st column as L and the 2nd
                                ; column as 1's
 n = n_elements(L)
 x = fltarr(n) + 1
 S = [[L],[x]]
 A = transpose(S)
 return, A
end 

function F2, A, y
 ; multiply the 2xn matrix by a 1xn matrix y
 B = invert(transpose(A)##A)##transpose(A)##transpose(y)
 return, B
end































