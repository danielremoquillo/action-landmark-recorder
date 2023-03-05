import os

class Settings:
    def __init__(self) -> None:
        # Actions that we try to detect
        self.ACTIONS = [
                    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'NG', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
                    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                    ['Kuya', 'Ate', 'Nanay', 'Tatay', 'Kapatid', 'Anak', 'Tiya', 'Tiyo', 'Lolo', 'Lola']
                ]
        
        self.CATEGORIES = ['Alphabets', 'Numbers', 'Family Words']


        # Thirty videos worth of data
        self.NO_SEQUENCES = 30

        # Videos are going to be 30 frames in length
        self.SEQUENCE_LENGTH = 30

        # Folder start
        self.START_FOLDER = 30


        # Path for exported data, numpy arrays
        self.NP_DATA_PATH = os.path.join('NP_DATA')

        #Path for exported data, mp4 format
        self.VID_CLEAR_DATA_PATH = os.path.join('VID_CLEAR_DATA')

        #Path for exported data, mp4 format with MP landmarks
        self.VID_MP_DATA_PATH = os.path.join('VID_MP_DATA')

        #Path for exported data, png format
        self.IMG_CLEAR_DATA_PATH = os.path.join('IMG_CLEAR_DATA')

        #Path for exported data, png format with MP landmarks
        self.IMG_MP_DATA_PATH = os.path.join('IMG_MP_DATA')