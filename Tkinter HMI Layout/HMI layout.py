import tkinter as tk

class Demo1:
    global LblCnt
    LblCnt = 1
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'New Label', width = 25, command = self.NewLabel)
        self.button2.pack()
        self.button3 = tk.Button(self.frame, text = 'Delete Label', width = 25, command = self.DeleteLabel)
        self.button3.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)
    def NewLabel(self):
        global LblCnt
        self.lbl = tk.Label(text = " New Label" + str(LblCnt))
        LblCnt = LblCnt + 1
        self.lbl.pack()
        
    def DeleteLabel(self):
        global LblCnt
        LblCnt = LblCnt - 1
        self.lbl.destroy()

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()



class Tabs:
    def Tab1 (self):
        # Clear Window
        try:
            self.ClearFrame()
        except:pass
        
        # Create insance of window
        self.Window = tk.Frame(self.master)
        
        # Create Tabs at top
        
        #Label the current tab open
        self.lbl = tk.Label(self.Window,text = " You are in Tab 1",width = 20 )
        self.lbl.pack(padx=1, pady=1,side=tk.LEFT)
        
        self.Tab_1 = tk.Button(self.Window, text = 'Go to Tab 2', width = 15, command = self.Tab2)
        self.Tab_1.pack(padx=1, pady=1,side=tk.LEFT)
        
        self.Tab_3 = tk.Button(self.Window, text = 'Go to Tab 3', width = 15,command = self.Tab3)
        self.Tab_3.pack(padx=1, pady=1,side=tk.LEFT)
        
        self.Tab_4 = tk.Button(self.Window, text = 'Go to Tab 4', width = 15,command = self.Tab4)
        self.Tab_4.pack(padx=1, pady=1,side=tk.LEFT)

        self.Window.pack(anchor =tk.NW)
        
        
        self.Content = tk.Frame(self.master)
        
        
        def CustomLabel (self,Lbl_Text):
            
            self.lbl = tk.Label(self.Content,text = Lbl_Text ,width = 20, bg="#78909c", fg="white" )
            self.lbl.pack(padx=1, pady=1,side=tk.LEFT)
            C = tk.Canvas(self.Content, bg="blue", height=50, width=50)
            coord = 10, 20, 30, 40
            arc = C.create_arc(coord, start=0, extent=50, fill="red")
            C.pack()
          
        CustomLabel(self,"Custom Label text")
        self.Content.pack(side =tk.BOTTOM)
        # Tab Content

        
    def Tab2(self):
        # Clear Screen

        try:
            self.ClearFrame()
        except:pass
        
        # Create insance of window
        self.Window = tk.Frame(self.master)
        
        # Create Tabs at top
        self.Tab_1 = tk.Button(self.Window, text = 'Go to Tab 1', width = 15, command = self.Tab1)
        self.Tab_1.pack(padx=1, pady=1,side=tk.LEFT)
        
        #Label the current tab open
        self.lbl = tk.Label(self.Window,text = " You are in Tab 2",width = 20 )
        self.lbl.pack(padx=1, pady=1,side=tk.LEFT)
        
        self.Tab_3 = tk.Button(self.Window, text = 'Go to Tab 3', width = 15,command = self.Tab3)
        self.Tab_3.pack(padx=1, pady=1,side=tk.LEFT)
        
        self.Tab_4 = tk.Button(self.Window, text = 'Go to Tab 4', width = 15,command = self.Tab4)
        self.Tab_4.pack(padx=1, pady=1,side=tk.LEFT)

        self.Window.pack(anchor =tk.NW)

        
    def Tab3(self):
        # Clear Screen

        try:
            self.ClearFrame()
        except:pass
        
        # Create insance of window
        self.Window = tk.Frame(self.master)
        
        # Create Tabs at top
        self.Tab_1 = tk.Button(self.Window, text = 'Go to Tab 1', width = 15, command = self.Tab1)
        self.Tab_1.pack(padx=1, pady=1,side=tk.LEFT)
        
        self.Tab_2 = tk.Button(self.Window, text = 'Go to Tab 2', width = 15,command = self.Tab2)
        self.Tab_2.pack(padx=1, pady=1,side=tk.LEFT)
        
        #Label the current tab open
        self.lbl = tk.Label(self.Window,text = " You are in Tab 3",width = 20 )
        self.lbl.pack(padx=1, pady=1,side=tk.LEFT)
        
        self.Tab_4 = tk.Button(self.Window, text = 'Go to Tab 4', width = 15,command = self.Tab4)
        self.Tab_4.pack(padx=1, pady=1,side=tk.LEFT)

        self.Window.pack(anchor =tk.NW)

    def Tab4(self):
        # Clear Screen

        try:
            self.ClearFrame()
        except:pass
        
        # Create insance of window
        self.Window = tk.Frame(self.master)
        
        # Create Tabs at top
        self.Tab_1 = tk.Button(self.Window, text = 'Go to Tab 1', width = 15, command = self.Tab1)
        self.Tab_1.pack(padx=1, pady=1,side=tk.LEFT)
        
        self.Tab_2 = tk.Button(self.Window, text = 'Go to Tab 2', width = 15,command = self.Tab2)
        self.Tab_2.pack(padx=1, pady=1,side=tk.LEFT)
        
        self.Tab_3 = tk.Button(self.Window, text = 'Go to Tab 3', width = 15,command = self.Tab3)
        self.Tab_3.pack(padx=1, pady=1,side=tk.LEFT)
        
        #Label the current tab open
        self.lbl = tk.Label(self.Window,text = " You are in Tab 4",width = 20 )
        self.lbl.pack(padx=1, pady=1,side=tk.LEFT)

        self.Window.pack(anchor =tk.NW)
        
    def CustomWindow (self):
        self.NewWin = tk.Frame(self.master)
        
        Tabs.CustomLabel(self,"CustomText")
        self.lbl.pack(padx=1, pady=1,side=tk.LEFT)
        
        self.NewWin.pack(anchor =tk.SW)
        
    def ClearFrame(self):
        self.Window.destroy()
        self.Window = None
        self.Content.destroy()
        self.Content = None
        
    def ClearContent(self):
        self.NewWin.destroy()
        self.NewWin = None
    
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.Tab1()
        
        

        

def main(): 
    root = tk.Tk()
    root.geometry("500x400")
    root.config(bg='#78909c')
    root.title('TKinter Class Test')
    app = Tabs(root)
    root.mainloop()

if __name__ == '__main__':
    main()