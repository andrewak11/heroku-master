import requests
import json
from bs4 import BeautifulSoup
from .arclassifier import *
import os
class pi:
    api_key = "MSVwNcSZEIs9QhZNtyd2"
    domain = "hyphencorp"
    password = "freshservice"
    #ticket_id = 0
    def cap(self):

        
        ######################################################################################################################################################################################
        ############################# TICKET GET REQUEST ##################################################################################################################################
        ######################################################################################################################################################################################
        # Return the tickets that are new or opend & assigned to you
        # If you want to fetch all tickets remove the filter query param

        # request for getting ticket
        r = requests.get("https://"+ self.domain +".freshservice.com/api/v2/tickets?filter=new_and_my_open", auth = (self.api_key, self.password))
        

        # request for replying to the user
        ####r = requests.post("https://"+ domain +".freshdesk.com/api/v2/tickets/"+ticket_id+"/reply", auth = (api_key, password), headers = headers, data = json.dumps(note))
        
        ###### r = requests.post("https://"+ domain +".freshdesk.com/api/v2/solution/categories.json ", auth = (api_key, password), headers = headers)

        
        if r.status_code == 200:
            print("Request processed successfully, the response is given below")
            #print(r.content)
            ht = r.json()
            #print(ht)
            #soup = BeautifulSoup(ht, 'html5lib')
            #txt = soup.get_text(strip=True)
            # if(ht['tickets'][0]['type']) == 'incident':
            s1 = (ht['tickets'][0]['description'])
            #to get id
            s2 = (ht['tickets'][0]['id'])
            #print(s2)
            #ticket_id = s2
           
                # sub = (ht['tickets'][0]['category'])
                # print(sub)
            soup = BeautifulSoup(s1, 'html.parser')
            txt = soup.get_text(strip = True)
            #print(txt)
            return txt , s2
            # else:
            #     print('request heyyy!!!!')
            #     # sub = (ht['tickets'][0]['sub_category'])
            #     # print(sub)
        else:
            print("Failed to read tickets, errors are displayed below,")
            response = json.loads(r.content)
            print(response["errors"])

            print("x-request-id : " + r.headers['x-request-id'])
            print("Status Code : " + str(r.status_code))


    def soln_check(self,id,txt):

        ####ID for solutions ......!!!!!
        #11000036514 - Instance Related Issues (1)
        #####11000054746 - Email Issues
        #11000036515 - Oracle Errors (2)
        #11000036516 - PC Needs (3)
        #11000036517 - User Account Issues (4)
        #11000036518 - Hardware Issues (5)
        #11000036519 - Access Issues (7)
        #11000036520 - Remote Connection Issues (8)
        #11000036521 - Switch Management Issues (9)
        #11000036522 - Other Issues (10)

        dic = { 1: '11000036514' , 2: '11000054746' , 3: '11000036515' ,4: '11000036517' , 5: '11000036516'  , 6: '11000036518' , 7: '11000036519' , 8: '11000036520' , 9: '11000036521' , 10: '11000036522'}   
        #id = 5
        # ID checking......!!!

        for i in dic:
            if id in dic.keys():
                temp = id
                id = dic[id]
                break
        #print(id)

    ################## ARTICLE FINDER #####################################
       
       # c = Classifier(str(temp) +'.json')
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        js = os.path.join(BASE_DIR , '4.json')
        c = Classifier(js)
        tx = str(txt[0])
        print(tx)
        key =  list(c.classify(tx))
        print(key)
        ar_id = key[0]

        ######################################################################################################################################################################################
        ############################# SOLUTION GET REQUEST ##################################################################################################################################
        ######################################################################################################################################################################################
       # r = requests.get("https://"+ self.domain +".freshservice.com/solution/categories/" + id +".json", auth = (self.api_key, self.password))
        # article id - 11000008144
        r = requests.get("https://"+ self.domain +".freshservice.com/solution/categories/" + id + "/folders/11000057342/articles/"+str(ar_id)+".json", auth = (self.api_key, self.password))

        if r.status_code == 200:
             try:
                cat = r.json()
                # print(cat['category'][0]['name'])
                #print(r.content)
                # iterate over the dict cat and find position .....!!!

                        #/solution/categories/[id]/folders/[id]/articles/[id].json 
                    # Exatificator.....!!!!!
                    #tx = tx.split(' ')
                    # user account issues.....
                    #ex_is = int(ex_is)


                        # to find exact soln......
                # ch = {1 :['permission' , 'authenticate' , 'credentials'], 2:[] , 3:[]}
                # for x in tx:
                #         for y in range(1, 3):
                #                 if x in ch[y]:
                #                         dummy = y
                

                # ar_dic = {1:'11000057342' , 2: '1010'}
                
                # for i in ar_dic:
                #     if dummy in dic.keys():
                #         dummy = ar_dic[dummy]
                #         break
                
                s = (cat['article']['description'])
                #s = (cat['category']['folders']['11000057342']['articles'][0]['description'])
                soup = BeautifulSoup(s, 'html.parser')
                txt = str(soup.get_text(strip = True))
                #print(txt)
                return txt

             except:
                print("no solution bhaa!!!")
        else:
            print('error eyy!!!')

    def rep_soln(self,soln , ticket_id):
        


        ######################################################################################################################################################################################
        ############################# REPLY REQUEST ##################################################################################################################################
        ######################################################################################################################################################################################

        headers = { 'Content-Type' : 'application/json' }
        
        note = {
            "body" : soln
        }
        r = requests.post("https://"+self.domain+".freshservice.com/api/v2/tickets/"+str(ticket_id)+"/reply", auth = (self.api_key,self.password), headers = headers, data = json.dumps(note))
        
        if r.status_code == 201:
            print ("Reply added successfully, the response is given below")
            print ("Location Header: " + r.headers['Location'])
        else:
            print ("Failed to add reply, errors are displayed below,")
            response = json.loads(r.content)
            print (response["errors"])

            print ("x-request-id : " + r.headers['x-request-id'])
            print( "Status Code : " + str(r.status_code))
    # def assign_agent(self,soln):
        
    #     r = requests.post("https://"+self.domain+".freshservice.com/api/v2/tickets/"+self.ticket_id+"/reply", auth = (api_key, password), headers = headers, data = json.dumps(soln))
    def ticket_update(self,ticket_id):
            ######################################################################################################################################################################################
            ############################# TICKET UPDATE REQUEST ##################################################################################################################################
            ######################################################################################################################################################################################
            # update the ticket....
            headers = { 'Content-Type' : 'application/json' }

            ticket = {
                    "status":3
                    }
            r = requests.put("https://"+ self.domain +".freshservice.com/api/v2/tickets/"+str(ticket_id), auth = (self.api_key, self.password), headers = headers, data = json.dumps(ticket))
            
            if r.status_code == 200:
                print ("Ticket updated successfully, the response is given below")
            else:
                print ("Failed to update ticket, errors are displayed below,")
               
if __name__ == "__main__":
     obj=pi()
     obj.cap()

