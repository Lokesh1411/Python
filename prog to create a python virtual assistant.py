import wx                #for creating GUI Interface
import wolframalpha
import wikipedia
import speech_recognition as sr

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame. __init__ (self, None, pos=wx.DefaultPosition, size=wx.Size(450,100), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, title='YOUR VIRTUAL ASSISTANT')

        panel=wx.Panel(self)      #initial panel setup
        my_sizer=wx.BoxSizer(wx.VERTICAL)   #size of the box
        lbl=wx.StaticText(panel,label = ' Hello, Im Your Digital Assistant..How can I Help You ? ')     #label to be displayed

        my_sizer.Add(lbl,0,wx.ALL,5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,300))       #size of panel

        self.txt.SetFocus()  #to focus the text
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter) #combining the OnEnter func which as wolfram nd wikipedia
        my_sizer.Add(self.txt,0,wx.ALL,5)

        panel.SetSizer(my_sizer)

        self.Show()

    def OnEnter(self, event):
        n=self.txt.GetValue()             #getting input from the user
        n=n.lower()                       #converting into lowercase

        if n=="":
            r=sr.Recognizer()                   #using Speech Recognition to convert speech to text/ to give speech as input
            with sr.Microphone() as source:
                audio= r.listen(source)
            try:
                self.txt.SetValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print('Google Speech Recognition could not understand the audio !')
            except sr.RequestError as e:
                print('Could not request results from Google Speech Recognition service; {0}'.format(e))

        else:
            try:
                #wolframalpha code:
                app_id="6LH6EP-H3L33XVTLK"                #pvt app_id created in wolframalpha
                client=wolframalpha.Client(app_id)        #creating a client to access

                result=client.query(n)                    #searches the given query and stores in resul
                answer=next(result.results).text          #searches the answer for the result and shows oly text answers

                print (answer)

            except:
                #wikipedia code:
                n=n.split(' ')     #split the input by spacing
                n=' '.join(n[2:])  #join them except the first 2 words, so the first 2 words is our search query.

                print (wikipedia.summary(n))   
            

#run the app:

if __name__ == '__main__':
    app=wx.App(True)
    frame=MyFrame()
    app.MainLoop()
        
