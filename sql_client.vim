let g:action=""
let g:query=""
let dbname=input('Enter Database name: ')
map <Return> :call Select() <CR>
map q :call Quit() <CR>

python << EOF
import vim
import sqlite3_complete, vim_ui, vim_listener

dbname = vim.eval('dbname')

ui = vim_ui.Ui(vim)
v_thread = vim_listener.VimListener(vim, ui, dbname)
v_thread.start()

EOF

function! Quit()
    let quit=input('Quit?(y/n)')
    if quit =~ 'y'
        let g:action="quit"
    endif
endfunction

function! Select()
    let g:action="select"
endfunction
