import tkinter
import customtkinter
from tkinter.filedialog import askdirectory

import pickle

class VideoFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class PeripheralFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class App(customtkinter.CTk):
    def __init__(self):
        
        super().__init__()   
        
        self.state_values = self.load_state()


        #System Settings
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.minsize(1280, 720)
        self.title("Action Recognition Capturing App")

        # create 2x2 grid system
        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure((0,1), weight=2)

        self.cameraFrame = customtkinter.CTkFrame(master=self)
        self.cameraFrame.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 0), sticky="nsew")

        self.dirFrame = customtkinter.CTkFrame(master=self)
        self.dirFrame.grid(row=1, column=0, columnspan=1, padx=20, pady=(20, 20), sticky="swe")
       
        self.controlFrame = customtkinter.CTkFrame(master=self)
        self.controlFrame.grid(row=1, column=1, columnspan=1, padx=20, pady=(20, 20), sticky="swe")

        self.startButton = customtkinter.CTkButton(master=self.controlFrame, command=self.select_directory, text='Start')
        self.startButton.grid(row=1, column=1,  sticky="se")


        self.dirButton = customtkinter.CTkButton(master=self.dirFrame, command=self.select_directory, text='Select Directory')
        self.dirButton.grid(row=1, column=1,  sticky="se")

        self.label = customtkinter.CTkLabel(master=self.dirFrame, width=200,
                               height=25,
                             text_color=("white"),wraplength=0)
        self.label.configure(text= self.dir_label_overflow(self.state_values['Directory']) if any(self.state_values) else 'C://')
        self.label.grid(row=1, column=2,  padx=20, sticky="ew")
        
        


        print((self.dir_label_overflow(self.state_values['Directory']) if self.state_values else 'No Directory Selected'))

        
        #Closing Application
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    def dir_label_overflow(self,path):
        if len(path) >= 90:
            temp = path.split('/')
            return '/'.join(temp[0:9]) + '/...'
        
        return path

    def select_directory(self) -> str:
        dir = Directory()
        folder_path = askdirectory()

        if folder_path != '':
            dir.setPath(folder_path)
            self.state_values['Directory'] = dir.getPath()

        self.label.configure(text=self.dir_label_overflow(self.state_values['Directory'])if any(self.state_values) else 'C://')
      



        
        


    def load_state(self) -> dict:
        state = {}
        try:
            with open('state.pkl', 'rb') as file:
                state = pickle.load(file)
        except:
            pass
        return state
    

    def save_state(self):
        with open('state.pkl', 'wb') as file:
            pickle.dump(self.state_values,file)


    def on_closing(self):
        if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
            #if there is changes, then save state
            if any(self.state_values):
                self.save_state()

            #Close the application
            self.destroy()

            
class Directory:
    def __init__(self) -> None:
        self.folder_path = ''
    
    def getPath(self):
        return self.folder_path
    
    def setPath(self, path):
        self.folder_path = path





    


if __name__ == "__main__":
    app = App()
    app.mainloop()
