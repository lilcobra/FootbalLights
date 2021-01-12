from playsound import playsound
import Scores
import sys
import time
import threading


try:
    import wx
except ImportError:
    print("The wxPython module is required to run this program")
    sys.exit()

app = wx.App()

class Home(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id, title, size=wx.Size(700, 600))
        self.parent = parent
        self.initialise()
    def initialise(self):
        panel = wx.Panel(self)
        self.Panel = panel
        self.line = 0.0
        panel.SetBackgroundColour(wx.Colour(46, 46, 46))

        #self.text_ctrl = wx.TextCtrl(panel)
        #my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 50)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        #self.SetSizer(my_sizer, deleteOld=True)

        #image
        imgSizer = wx.BoxSizer(wx.HORIZONTAL)
        image = wx.Image('NFLlogowhite.png', wx.BITMAP_TYPE_ANY)
        image = image.Scale(280,330,quality=wx.IMAGE_QUALITY_HIGH)
        img = wx.StaticBitmap(self.Panel, id = 19, bitmap=wx.Bitmap(image) )
        imgSizer.Add(img)
        my_sizer.Add(imgSizer,proportion= 0, flag=wx.TOP|wx.CENTER, border=10)

        #label(s)
        info_label = wx.StaticText(self.Panel,id = 343, label="Visualise Problem")
        info_label.SetFont(wx.Font(28, wx.SWISS, wx.NORMAL, wx.NORMAL))
        info_label.SetForegroundColour((255,255,255))
        my_sizer.Add(info_label, 0, wx.TOP | wx.CENTER, 10)
        info_label.SetLabel("Select the bet type")
        """for child in self.Panel.GetChildren():
            if child.Id == 343:
                child.SetLabel("Start the program")"""


        #button(s)
        buttonsBox = wx.BoxSizer(wx.HORIZONTAL)
        H2H_btn = wx.Button(self.Panel, label='H2H', size=wx.Size(150, 60))
        H2H_btn.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL, wx.NORMAL))
        H2H_btn.SetBackgroundColour(wx.WHITE)
        buttonsBox.Add(H2H_btn, 0, wx.LEFT , 10)
        H2H_btn.Bind(wx.EVT_BUTTON, self.H2H)

        lineBox = wx.BoxSizer(wx.VERTICAL)
        line_btn = wx.Button(self.Panel, label='Line', size=wx.Size(150, 60))
        line_btn.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL, wx.NORMAL))
        line_btn.SetBackgroundColour(wx.WHITE)
        lineBox.Add(line_btn, 0, wx.TOP | wx.CENTER, 0)
        line_btn.Bind(wx.EVT_BUTTON, self.line_func)

        #text box
        self.line_txt = wx.TextCtrl(self.Panel,id = 18, size=wx.Size(150, 28))
        self.line_txt.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.NORMAL))
        lineBox.Add(self.line_txt, 0, wx.TOP | wx.CENTER, 10)
        self.line_txt.SetHint("Enter line (-4.5)")


        buttonsBox.Add(lineBox, 0, wx.LEFT | wx.CENTER, 10)
        #UploadProblem_btn.Bind(wx.EVT_BUTTON, self.up_prob_Page)


        my_sizer.Add(buttonsBox, 0, wx.ALL | wx.CENTER, 20)
        self.Panel.SetSizerAndFit(my_sizer,deleteOld=True)
        self.Show(True)

        #self.SetSize(size=wx.Size(997, 564))
        #self.SetSize(size=wx.Size(997, 564))
    def H2H(self, event):
        self.Panel.DestroyChildren()

        self.teams()

    def line_func(self, event):
        try:
            self.line = float(self.line_txt.GetValue())
            self.Panel.DestroyChildren()
            self.teams()
        except:
            #pop up window please enter a correct line
            wx.MessageBox('Please enter a correct line!', 'Warning', wx.OK | wx.CANCEL | wx.ICON_WARNING)

    def teams(self):
        my_sizer = wx.BoxSizer(wx.VERTICAL)


        #image
        imgSizer = wx.BoxSizer(wx.HORIZONTAL)
        image = wx.Image('NFLlogowhite.png', wx.BITMAP_TYPE_ANY)
        image = image.Scale(280,330,quality=wx.IMAGE_QUALITY_HIGH)
        img = wx.StaticBitmap(self.Panel, id = 19, bitmap=wx.Bitmap(image) )
        imgSizer.Add(img)
        my_sizer.Add(imgSizer,proportion= 0, flag=wx.TOP|wx.CENTER, border=10)

        my_team_sizer = wx.BoxSizer(wx.HORIZONTAL)

        #label(s)
        info_label = wx.StaticText(self.Panel,id = 343, label="Visualise Problem")
        info_label.SetFont(wx.Font(26, wx.SWISS, wx.NORMAL, wx.NORMAL))
        info_label.SetForegroundColour((255,255,255))
        my_team_sizer.Add(info_label, 0, wx.LEFT | wx.CENTER, 10)
        info_label.SetLabel("Your Team:")

        #text box
        self.team1_txt = wx.TextCtrl(self.Panel,id = 18, size=wx.Size(250, 28))
        self.team1_txt.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.NORMAL))
        my_team_sizer.Add(self.team1_txt, 0, wx.LEFT | wx.CENTER, 10)
        self.team1_txt.SetHint("Please enter your team")

        my_sizer.Add(my_team_sizer, 0, wx.TOP | wx.CENTER, 20)

        other_team_sizer = wx.BoxSizer(wx.HORIZONTAL)

        #label(s)
        info_label2 = wx.StaticText(self.Panel,id = 343, label="Visualise Problem")
        info_label2.SetFont(wx.Font(26, wx.SWISS, wx.NORMAL, wx.NORMAL))
        info_label2.SetForegroundColour((255,255,255))
        other_team_sizer.Add(info_label2, 0, wx.LEFT | wx.CENTER, 10)
        info_label2.SetLabel("Opposition:")

        #text box
        self.team2_txt = wx.TextCtrl(self.Panel,id = 18, size=wx.Size(250, 28))
        self.team2_txt.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.NORMAL))
        other_team_sizer.Add(self.team2_txt, 0, wx.LEFT | wx.CENTER, 19)
        self.team2_txt.SetHint("Please enter opposition")

        my_sizer.Add(other_team_sizer, 0, wx.TOP | wx.CENTER, 20)

        #button
        Start_btn = wx.Button(self.Panel, label='Start', size=wx.Size(150, 60))
        Start_btn.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL, wx.NORMAL))
        Start_btn.SetBackgroundColour(wx.WHITE)
        my_sizer.Add(Start_btn, 0, wx.TOP | wx.CENTER , 10)
        Start_btn.Bind(wx.EVT_BUTTON, self.Start_func)

        self.Panel.SetSizer(my_sizer,deleteOld=True)
        self.Show(True)


        self.SetSize(size=wx.Size(self.GetSize()[0] +1, self.GetSize()[1]))
        self.SetSize(size=wx.Size(self.GetSize()[0] -1, self.GetSize()[1]))

    def Start_func(self, event):
        self.team1 = self.team1_txt.GetValue()
        self.team2 = self.team2_txt.GetValue()
        #print(self.team1, self.team2)
        #team name check


        self.Panel.DestroyChildren()


        my_sizer = wx.BoxSizer(wx.VERTICAL)


        #image
        imgSizer = wx.BoxSizer(wx.VERTICAL)
        image = wx.Image('NFLlogowhite.png', wx.BITMAP_TYPE_ANY)
        image = image.Scale(280,330,quality=wx.IMAGE_QUALITY_HIGH)
        img = wx.StaticBitmap(self.Panel, id = 19, bitmap=wx.Bitmap(image) )
        imgSizer.Add(img)
        my_sizer.Add(imgSizer,proportion= 0, flag=wx.TOP|wx.CENTER, border=10)





        img.Show(True)
        self.Panel.SetSizerAndFit(my_sizer,deleteOld=True)
        self.Show(True)

        self.SetSize(size=wx.Size(self.GetSize()[0] +1, self.GetSize()[1]))
        self.SetSize(size=wx.Size(self.GetSize()[0] -1, self.GetSize()[1]))
        #self.lights()
        x = threading.Thread(target=self.lights)
        x.start()

    def red(self):
        """
        turns logo to red
        """

        self.Panel.DestroyChildren()
        #image - red
        my_sizer1 = wx.BoxSizer(wx.VERTICAL) #red
        imgSizer1 = wx.BoxSizer(wx.VERTICAL)
        image1 = wx.Image('Sketch001.png', wx.BITMAP_TYPE_ANY)
        image1 = image1.Scale(280,330,quality=wx.IMAGE_QUALITY_HIGH)
        img1 = wx.StaticBitmap(self.Panel, id = 19, bitmap=wx.Bitmap(image1) )
        imgSizer1.Add(img1)
        my_sizer1.Add(imgSizer1,proportion= 0, flag=wx.TOP|wx.CENTER, border=10)

        self.Panel.SetSizerAndFit(my_sizer1,deleteOld=True)
        self.SetSize(size=wx.Size(self.GetSize()[0] +1, self.GetSize()[1]))
        self.SetSize(size=wx.Size(self.GetSize()[0] -1, self.GetSize()[1]))



    def green(self):
        """
        turns logo to green
        """
        self.Panel.DestroyChildren()
        #image - green
        my_sizer1 = wx.BoxSizer(wx.VERTICAL) #green
        imgSizer1 = wx.BoxSizer(wx.VERTICAL)
        image1 = wx.Image('Sketch002.png', wx.BITMAP_TYPE_ANY)
        image1 = image1.Scale(280,330,quality=wx.IMAGE_QUALITY_HIGH)
        img1 = wx.StaticBitmap(self.Panel, id = 19, bitmap=wx.Bitmap(image1) )
        imgSizer1.Add(img1)
        my_sizer1.Add(imgSizer1,proportion= 0, flag=wx.TOP|wx.CENTER, border=10)

        self.Panel.SetSizerAndFit(my_sizer1,deleteOld=True)
        self.SetSize(size=wx.Size(self.GetSize()[0] +1, self.GetSize()[1]))
        self.SetSize(size=wx.Size(self.GetSize()[0] -1, self.GetSize()[1]))
    def amber(self):
        """
        turns logo to amber
        """
        self.Panel.DestroyChildren()
        #image - amber
        my_sizer1 = wx.BoxSizer(wx.VERTICAL) #amber
        imgSizer1 = wx.BoxSizer(wx.VERTICAL)
        image1 = wx.Image('Sketch003.png', wx.BITMAP_TYPE_ANY)
        image1 = image1.Scale(280,330,quality=wx.IMAGE_QUALITY_HIGH)
        img1 = wx.StaticBitmap(self.Panel, id = 19, bitmap=wx.Bitmap(image1) )
        imgSizer1.Add(img1)
        my_sizer1.Add(imgSizer1,proportion= 0, flag=wx.TOP|wx.CENTER, border=10)

        self.Panel.SetSizerAndFit(my_sizer1,deleteOld=True)
        self.SetSize(size=wx.Size(self.GetSize()[0] +1, self.GetSize()[1]))
        self.SetSize(size=wx.Size(self.GetSize()[0] -1, self.GetSize()[1]))

    def lights(self):
        """
        light processing
        """

        self.driver = Scores.getDriver(self.team1, self.team2)
        #print(Scores.inGame(self.driver))
        #self.score1, self.score2 = Scores.getScores(self.team1, self.team2, self.driver)

        #print(self.score1, self.score2)

        current = -2
        self.score1 = 0
        self.score2 = 0
        try:
            self.score1, self.score2 = Scores.getScores(self.team1, self.team2, self.driver)
        except:
            while True:
                try:
                    self.score1, self.score2 = Scores.getScores(self.team1, self.team2, self.driver)
                    break
                except:
                    pass

        if (self.score1 + self.line) > self.score2:
            if current != 1:
                playsound('Green.mp3')
                wx.CallAfter(self.green)
                #self.green()
                current = 1
        elif (self.score1 + self.line) == self.score2:
            if current != 0:
                playsound('Amber.mp3')
                wx.CallAfter(self.amber)
                #self.amber()
                current = 0
        else:
            if current != -1:
                playsound('Red.mp3')
                wx.CallAfter(self.red)
                #self.red()
                current = -1


        try:
            while Scores.inGame(self.driver):
                for i in range(60):
                    self.score1, self.score2 = Scores.getScores(self.team1, self.team2, self.driver)
                    if (self.score1 + self.line) > self.score2:
                        if current != 1:
                            playsound('Green.mp3')
                            wx.CallAfter(self.green)
                            #self.green()
                            current = 1
                    elif (self.score1 + self.line) == self.score2:
                        if current != 0:
                            playsound('Amber.mp3')
                            wx.CallAfter(self.amber)
                            #self.amber()
                            current = 0
                    else:
                        if current != -1:
                            playsound('Red.mp3')
                            wx.CallAfter(self.red)
                            #self.red()
                            current = -1
        except:
            try:
                Scores.closeDriver(self.driver)
            except:
                pass
            self.lights()


        Scores.closeDriver(self.driver)





if __name__ == '__main__':
    frame = Home(None,-1,"Football Lights")
    app.MainLoop()
    sys.exit()
