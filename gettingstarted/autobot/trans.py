from googletrans import Translator

class tra:

    def trans(self,txt):
        trans = Translator()
        det = trans.detect(txt) 
        #out = trans.translate("hallo, ich habe ein Problem mit der Hardware und pls helfen mir bro", dest='en')
    
        if det.lang is not 'en':
            out = trans.translate(txt, dest='en')
            reply = out.text
            #print(det.lang)
        ckl = det.lang
        print(ckl)
        # return the translated text to main .........    
        return reply,ckl
        #print(out)
    
    def re_trans(re_txt,ck):
        re_trans = Translator()
        re_det = re_trans.detect(re_txt)
        print(ck)
        if ck is not 'en':
            #print(ck)
            re_txt = re_trans.translate(re_txt , dest=ck)
            #print(re_out) 
        re_reply = re_txt.text
        print(re_reply)
        return re_reply


if __name__ == "__main__":
    obj = tra()
    obj.trans("hallo, ich habe ein Problem mit der Hardware und pls helfen mir bro")
    obj.re_trans("mock it up",'de')



