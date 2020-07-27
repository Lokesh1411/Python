import wolframalpha
import wikipedia

while (True):
    n=input('Question :')                  #IF TRY DOESN'T WORK, EXCEPT WILL WORK !

    try:
        #wolframalpha code:

        app_id="6LH6EP-H3L33XVTLK"         #pvt app_id created in wolframalpha

        client=wolframalpha.Client(app_id) #creating a client to access

        result=client.query(n)             #searches the given query and stores in resul
        answer=next(result.results).text   #searches the answer for the result and shows oly text answers

        print (answer)
        print('')

    except:
        #wikipedia code:

        wikipedia.set_lang('en')                    #sets the lang of the appl

        print (wikipedia.summary(n, sentences=2))   #sentences=2, gives the first 2 sentences in wiki
        print('')
