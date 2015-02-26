let g:action=""
let g:query=""
let dbname=input('Enter Database name: ')
map <Return> :call Select() <CR>
map q :call Quit() <CR>
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
    let comp_list = ['select']
    return comp_list
endfunc

function! Quit()
    let quit=input('Quit?(y/n)')
    if quit =~ 'y'
        let g:action="quit"
    endif
endfunction

function! Select()
    :norm ^yf;
    :let g:query=getreg('"')
    let g:action="select"
endfunction
