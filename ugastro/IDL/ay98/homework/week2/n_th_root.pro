;; This buffer is for notes you don't want to save, and for Lisp evaluation.
;; If you want to create a file, visit that file with C-x C-f,
;; then enter the text in that file's own buffer.

function n_th_root, a, b
 ; find the nth root of a number
 If (a LT 0) Then Begin
 return, 0
endif else begin
 y = a^(1./b)
 return, y
endelse
end

