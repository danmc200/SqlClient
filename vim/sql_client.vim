let g:action=""
let g:query=""
let g:comp_list=[]

let dbname=input('Enter Database name: ')
map <Return> :call Select() <CR>
"<C-J> = Ctrl-Enter for Ubuntu
map <C-J> :call SelectToBlankLine() <CR>
map Q :call Quit() <CR>
let &omnifunc='sql_client#Complete'

python << EOF
import vim
import drivers.sqlite3_complete as sqlite3_complete
import vim_ui, vim_listener

dbname = vim.eval('dbname')

ui = vim_ui.Ui(vim)
v_thread = vim_listener.VimListener(vim, ui, dbname)
v_thread.start()

EOF

function! sql_client#Complete(findstart, base)
    let g:action="complete"
    "block until listener loads
    while g:comp_list == []
    endwhile
    let comp_list=g:comp_list
    let g:comp_list=[]
    return comp_list
endfunction

function! Quit()
    let quit=input('Quit?(y/n)')
    if quit == 'y'
        let g:action="quit"
    endif
endfunction

function! SelectToBlankLine()
    y
    /^\s*\n
    :call Select()
endfunction

function! Select()
    :let g:query=getreg('"')
    let g:action="select"
endfunction
