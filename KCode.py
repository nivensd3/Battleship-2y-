 import RPi.GPIO as gpio
import time


LEDs = {
    green = []
    red = []
}


#gpio stuff
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#set up LEDs as output
for color in LEDs:
    for pin in LEDs[color]:
        GPIO.setup(pin, GPIO.OUT)


#define LED colors
green = (1,0) # green on, red off
red = (0,1) # green off, red on
orange = (1,1) # green on, red on - both have to be on/true, however you see it for orange to on

defining the gameboards (this is basically for visuals on the coding side to make sure everything is going right)
brian_board = [ # player1 3x3 board
    ['','','']
    ['','','']
    ['','','']
]

joe_board = [ # player2 3x3 board
    ['','','']
    ['','','']
    ['','','']
]

function that will update the LEDs on the board
def update_board_leds(board,player):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == '':
                led_color = green # set up green LED for empty space
            elif board[row][column] == 'x':
                led_color = red # set up red LED hit but not sunk
            elif board[row][column] == 'o':
                led_color = orange # set up orange LED for sunken ships


            led_index = row * 3 + column # this will calculate the index of the LED based on the coordinates of the board. 
            # We did the same thing in our SimonSays code, and it helped us keep track of the code
            GPIO.output(LEDs['green'][led_index], led_color[0]) # green side of LED
            GPIO.output(LEDs['red'][led_index], led_color[1]) # red side of LED
            time.sleep(0.1) # pause to update display

now we will get the user input
Unfinidhed Code: '''import RPi.GPIO as gpio
import time


LEDs = {
    green = []
    red = []
}


#gpio stuff
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#set up LEDs as output
for color in LEDs:
    for pin in LEDs[color]:
        GPIO.setup(pin, GPIO.OUT)


#define LED colors
green = (1,0) # green on, red off
red = (0,1) # green off, red on
orange = (1,1) # green on, red on - both have to be on/true, however you see it for orange to on

defining the gameboards (this is basically for visuals on the coding side to make sure everything is going right)
brian_board = [ # player1 3x3 board
    ['','','']
    ['','','']
    ['','','']
]

joe_board = [ # player2 3x3 board
    ['','','']
    ['','','']
    ['','','']
]

function that will update the LEDs on the board
def update_board_leds(board,player):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == '':
                led_color = green # set up green LED for empty space
            elif board[row][column] == 'x':
                led_color = red # set up red LED hit but not sunk
            elif board[row][column] == 'o':
                led_color = orange # set up orange LED for sunken ships


            led_index = row * 3 + column # this will calculate the index of the LED based on the coordinates of the board. 
            # We did the same thing in our SimonSays code, and it helped us keep track of the code
            GPIO.output(LEDs['green'][led_index], led_color[0]) # green side of LED
            GPIO.output(LEDs['red'][led_index], led_color[1]) # red side of LED
            time.sleep(0.1) # pause to update display

now we will get the user input'''