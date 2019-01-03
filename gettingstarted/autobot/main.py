from .tester import *
from .cap import pi 
from .trans import tra


def main():    
    # capture text using freshservice api ........
    p = pi()
    txt , ticket_id = p.cap()
    t = tra()
    ck = ""
    # txt = obj.cap()    
    print(txt)
    print(ticket_id)
    # translate to english using google translate .........
    en_txt, ck = t.trans(txt)
    # en_txt = str(en_txt)
    en_txt = [en_txt]
    #print(en_txt)
    # generate issue ID using nlp .........
    
    tic=tester.tic_nlp(en_txt)
    #tic = 1
    if tic is 1:
        issue_id = cat_nlp(en_txt)
    
   
        print(issue_id)
        soln =  p.soln_check(issue_id , en_txt)
        print(soln)
        
        
        if soln is None or soln is 0:
            print("Assigning to agent.....")
            p.ticket_update(ticket_id)
        else:
            # exatification process ....
            #ex_id = tester.exatificator(en_txt, issue_id)
            soln = tra.re_trans(soln,ck)
            p.rep_soln(soln , ticket_id)
            print("ticket resolved")
    # check for solution using issue ID ..........
    else:
       print("Assign to agent")
if __name__ == "__main__":
    main()

    
