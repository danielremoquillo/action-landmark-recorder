import os
from settings import Settings


def setupFolders(NO_SEQUENCES, ACTIONS, CATEGORIES, DATA_PATH):
    
    for x in range(len(ACTIONS)):
        for action in ACTIONS[x]: 
            for sequence in range(1,NO_SEQUENCES+1):
                try: 
                    os.makedirs(os.path.join(DATA_PATH, CATEGORIES[x], action, str(sequence)))
                except:
                    pass




if __name__ == '__main__':

    #Access the constants needed for the frame manipulations and folder setup
    settings = Settings()
    

    # Path Storage for numpy landmarks
    setupFolders(settings.NO_SEQUENCES, settings.ACTIONS, settings.CATEGORIES, settings.NP_DATA_PATH)
    setupFolders(settings.NO_SEQUENCES, settings.ACTIONS, settings.CATEGORIES, settings.VID_CLEAR_DATA_PATH)
    setupFolders(settings.NO_SEQUENCES, settings.ACTIONS, settings.CATEGORIES, settings.VID_MP_DATA_PATH)
    setupFolders(settings.NO_SEQUENCES, settings.ACTIONS, settings.CATEGORIES, settings.IMG_CLEAR_DATA_PATH)
    setupFolders(settings.NO_SEQUENCES, settings.ACTIONS, settings.CATEGORIES, settings.IMG_MP_DATA_PATH)