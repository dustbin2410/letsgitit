
import os
import sys
import string
import subprocess

def exec_cmd(cmd):
    os.system(cmd)

def get_branch_list():
    logfile = "get_branch_list.tmp.txt"
    exec_cmd("git branch > " + logfile)
    
    lines = open(logfile, 'r').readlines()
    items = []
    currbr = ""
    for item in lines:
        item = item.strip()
        if len(item) <= 1: continue
        if item[0] == '*': 
            item = item[1:].strip()
            currbr = item
        items.append(item)
        
    exec_cmd("rm -rf " + logfile)
    return (items, currbr)

def get_curr_branch(outfile):
    items, currbr = get_branch_list();
    open(outfile, 'w').write(currbr)

def get_next_branch(outfile):
    items, currbr = get_branch_list();
    
    maxidx = 0
    for item in items:
        if item.find('br') == 0:
            curidx = int(item[2:])
            if curidx > maxidx: maxidx = curidx

    if maxidx > 0:
        open(outfile, 'w').write(str(maxidx))
    else:
        open(outfile, 'w').write('')

def clear_branch():
    items, currbr = get_branch_list()
    
    mainbr = "master"
    if "main" in items: mainbr = "main"
    exec_cmd("git checkout " + mainbr)
        
    for item in items:
        if item.find('br') != 0: continue
        cmd = "git branch -D " + item
        exec_cmd(cmd)

prog = sys.argv[0]
acnt = len(sys.argv)

if acnt == 1:
    print("{%s} command", (prog))
    exit(1)

cmd = sys.argv[1]
if __name__ == "__main__":
    if cmd == "--currbr":
        outfile = 'brlog'
        if acnt > 2: outfile = sys.argv[2]
        get_curr_branch(outfile)
    if cmd == "--nextbr":
        outfile = 'brlog'
        if acnt > 2: outfile = sys.argv[2]
        get_next_branch(outfile)
    if cmd == "--clearbr":
        clear_branch()
        

