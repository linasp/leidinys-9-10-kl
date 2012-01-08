" to deal with hidden hyphenation chars pasted from Word
command! Fixshit ,%s/\%xad//g

" various rst shortcuts
vmap <C-i> di**<Esc>P
vmap <C-b> di****<Esc>hP
vmap <C-c> di````<Esc>hP

" todo: fix minus symbols ("–" to "-")

function! Mathify(string)
    " Perform LaTeX transformations on the given string
    let string = a:string

    " ... -> \ldots
    let string = substitute(string, '\.\.\.', '\\ldots', 'g')

    " blah -> \text{blah}
    let string = substitute(string, '([A-Za-z]\{3,})', '\\text{ \1 }', 'g')

    " replace bad - and * symbols
    let string = substitute(string, '·', '*', 'g')

    " £ -> \le
    let string = substitute(string, '£', '\\le', 'g')

    " a+ b*c =d -> a + b * c = d
    let string = substitute(string, '\s\?\([+|\-|/|*|=]\)\s\?', ' \1 ', 'g')

    " * -> \cdot
    let string = substitute(string, '*', '\\cdot', 'g')

    " a1 -> a_1
    let string = substitute(string, '\([A-Za-z]\)\([0-9|i|j|k|m|n]\)', '\1_\2', 'g')

    " { } -> \{ \}
    let string = substitute(string, '{', '\\{', 'g')
    let string = substitute(string, '}', '\\}', 'g')


    let string = ":math:`" . string . "`"
    return string
endfunction

vmap <C-m> "adi<C-R>=Mathify(@a)<CR><Esc>
