import pickle
import os
#import settings
def cat_nlp(st):
        
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        picky = os.path.join(BASE_DIR , 'category.model')
        with open(picky, 'rb') as model:
                tes = pickle.load(model)
        #st = ["""purchase po dear purchased received items lite updated include device under user name link please add allocation device thanks please log retrieve old device after receive item please take consideration mandatory receipts section order receive item ordered how video link please make return old device back accessories left receive receive old device take off user name kind regards administrator """]
        
        # use category dict to identify the category based on ID
        #st=[st]
        category_id = {1:"instance related issues",2:"oracle error",3:"pc needs",4:"user accounts",5:"hardware issues",6:"Network issues",7:"access issues",8:"remote connection issues",9:"Switch management",10:"other issues",11:"leave",12:"other issues"}
        out =int(tes.predict(st))
        ret = out
        for i in category_id:
                if out in category_id.keys():
                        out = category_id[out]
        #print(out)

        # return the ID to main .... 
        return ret

def tic_nlp(st):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        picky = os.path.join(BASE_DIR , 'ticket_type.model')
        with open(picky, 'rb') as model:
                tes = pickle.load(model)
        #st = ["""purchase po dear purchased received items lite updated include device under user name link please add allocation device thanks please log retrieve old device after receive item please take consideration mandatory receipts section order receive item ordered how video link please make return old device back accessories left receive receive old device take off user name kind regards administrator """]

        # use category dict to identify the category based on ID
        st=[st]
        out =int(tes.predict(st))

        # 1 - incident 
        # 0 - request
        #print(out)
        # return the ID to main .... 
        return out



#if __name__ == "__main__":
    #tic_nlp("i request u to mock my code")
    #exatificator("hi , iam not getting proper access  rights so please give me permission to authenticate my credentials")