#Author: Tyler Snelgrove
#Date: 11/12/2020
#Description: Program that is the abstract board game called Focus/Domination

class FocusGame:
    '''Creates FocusGame, has move makers, captures, shows captures, reserves moves, works with player class '''
    def __init__(self,tuple_1,tuple_2):
        self._player_1=Player(tuple_1) #sends to player class to create player
        self._player_2=Player(tuple_2) #sends to player class to create player
        self._the_board=[[[tuple_1[1]],[tuple_1[1]],[tuple_2[1]],[tuple_2[1]],[tuple_1[1]],[tuple_1[1]]]
        ,[[tuple_2[1]],[tuple_2[1]],[tuple_1[1]],[tuple_1[1]],[tuple_2[1]],[tuple_2[1]]],
        [[tuple_1[1]],[tuple_1[1]],[tuple_2[1]],[tuple_2[1]],[tuple_1[1]],[tuple_1[1]]],
        [[tuple_2[1]],[tuple_2[1]],[tuple_1[1]],[tuple_1[1]],[tuple_2[1]],[tuple_2[1]]],
        [[tuple_1[1]],[tuple_1[1]],[tuple_2[1]],[tuple_2[1]],[tuple_1[1]],[tuple_1[1]]],
        [[tuple_2[1]],[tuple_2[1]],[tuple_1[1]],[tuple_1[1]],[tuple_2[1]],[tuple_2[1]]]]
        self._turn=tuple_1[0]
        self._color_guard = self._player_1

    def print_the_board(self):
        '''Prints board'''
        for i in self._the_board:
            print(i)
        return

    def move_maker(self,tuple_start,tuple_end,num_of_pieces):
       '''Actual makes the moves of the pieces, checks for win'''
       try:#Try and except for if player tries to move outisde of board
           start_pos = self._the_board[tuple_start[0]][tuple_start[1]]
           for i in start_pos[-num_of_pieces:]: #Iterate through remaining elements in start postion
               self._the_board[tuple_end[0]][tuple_end[1]].append(i)
               start_pos.pop(-1)
           self.bottom_piece_capture(tuple_end) #sends for capture of reserve or other player pieces
           if self._turn ==Player.get_player_name(self._player_1):# updates whos turn it is
               self._turn = Player.get_player_name(self._player_2)
           else:
               self._turn = Player.get_player_name(self._player_1)
           if self._color_guard==self._player_1:#updates the color to match that of whos turn it is
               self._color_guard=self._player_2
               return Player.win_check(self._player_1)#sends for win check in player class
           else:
               self._color_guard=self._player_1
               return Player.win_check(self._player_2)#sends for win check in player class
       except:
           self._the_board[tuple_start[0]][tuple_start[1]]=start_pos
           return False

    def bottom_piece_capture(self,tuple_end):
       '''Captures bottom piece of stack and send to appropriate stash'''
       while len(self._the_board[tuple_end[0]][tuple_end[1]])>5:
           bottom_piece = self._the_board[tuple_end[0]][tuple_end[1]][0]
           if Player.get_color(self._color_guard)==bottom_piece:
               Player.reserve_stash_add(self._color_guard,bottom_piece) #if piece belongs to player, sends to reserve
           else:
               Player.captured_stash_add(self._color_guard, bottom_piece) #if other player piece, sends to capture
           del self._the_board[tuple_end[0]][tuple_end[1]][0]

    def move_piece(self,name, tuple_start,tuple_end,num_of_pieces):
       '''Runs a few checks to makes sure moves are valid and player turn, sends to move maker if good to go'''
       try:
           if num_of_pieces<1:
               return False
           if self._turn!=name:
               return False
           if self._the_board[tuple_start[0]][tuple_start[1]]==[] or Player.get_color(self._color_guard)!=self._the_board[tuple_start[0]][tuple_start[1]][-1]:
               #if the start location doesn't have a piece or player tries to move wrong color
               return False
           if len(self._the_board[tuple_start[0]][tuple_start[1]])<num_of_pieces:
               #if player tries to move fewer places than he is moving
               return False
           else:
               if tuple_start[0] == tuple_end[0] or tuple_start[1] == tuple_end[1]: #makes sure moves are not diagnol
                   if (num_of_pieces+tuple_start[0]==tuple_end[0] or num_of_pieces+tuple_start[1]==tuple_end[1] or
                       tuple_start[0]-num_of_pieces==tuple_end[0] or tuple_start[1]-num_of_pieces==tuple_end[1]):  #makes sure moves are not
                       # diagnol and correct spaces moved based off pieces moving
                       return self.move_maker(tuple_start,tuple_end,num_of_pieces)
                   else:
                       return False
               else:
                   return False
       except:
           return False


    def show_captured(self,player):
       '''Shows player captured stash when caleed'''
       player_a=Player.get_player_name(self._player_1)
       if player_a==player:
           return Player.get_cap_stash(self._player_1)#calls for player stash
       else:
           return Player.get_cap_stash(self._player_2)#calls for player stash

    def show_reserve(self,player):
       '''Shows player resereve stash when called'''
       player_a=Player.get_player_name(self._player_1)
       if player_a==player:
           return Player.get_res_stash(self._player_1)#calls for player stash
       else:
           return Player.get_res_stash(self._player_2)#calls for player stash

    def show_pieces(self,position):
       '''Shows pieces at given plactions'''
       return self._the_board[position[0]][position[1]]

    def reserved_move(self, player, location):
       '''Places move player calls from their reserve, sneds to helper to make move'''
       if player==Player.get_player_name(self._player_1):#checks player class
           res_stash=Player.get_res_stash(self._player_1)
           if res_stash==0:
               return False
           if player != self._turn:
               return False
           else:
               return self.reserved_move_helper(self._player_1,location,res_stash) #if pieces in reserve sends to helper
       else:
           res_stash = Player.get_res_stash(self._player_2)#checks player class
           if res_stash == 0:
               return False
           if player != self._turn:
               return False
           else:
               return self.reserved_move_helper(self._player_2,location,res_stash)#if pieces in reserve sends to helper

    def reserved_move_helper(self,player,location,res_stash):
       piece = res_stash.pop()#pops from reserve stash
       self._the_board[location[0]][location[1]].append(piece) #gets start postion
       Player.set_res_stash(player, res_stash) #sends updated stash back to player class
       self.bottom_piece_capture(location) #sends for piece capture
       if self._turn == Player.get_player_name(self._player_1):  # updates whos turn it is
           self._turn = Player.get_player_name(self._player_2)
       else:
           self._turn = Player.get_player_name(self._player_1)
       if self._color_guard == self._player_1:  # updates the color to match that of whos turn it is
           self._color_guard = self._player_2
           return Player.win_check(self._player_1)  # sends for win check in player class
       else:
           self._color_guard = self._player_1
           return Player.win_check(self._player_2)


class Player:
    '''Creates player class to be used with FocusGames, stores stashes, color, name'''
    def __init__(self,player):
       '''Creates player, stashs, color, name '''
       self._player_name=player[0]
       self._player_color=player[1]
       self._reserve_stash=[]
       self._captured_stash=[]

    def get_player_name(self):
       '''Returns player name when called'''
       return self._player_name

    def get_color(self):
       '''Returns player color when called'''
       return self._player_color

    def reserve_stash_add(self,piece):
       '''Adds to player reserve stash, takes piece from FocusGame class as parameter'''
       self._reserve_stash.append(piece)

    def captured_stash_add(self,piece):
       '''Adds to player capture stash, takes piece from FocusGame class as parameter'''
       self._captured_stash.append(piece)

    def get_res_stash(self):
       '''Returns reserve stash when called'''
       if self._reserve_stash==[]:
           return 0 #returns 0 if stash is empty
       else:
           return self._reserve_stash

    def get_cap_stash(self):
       '''Returns reserve stash when called'''
       if self._captured_stash==[]:
           return 0 #returns 0 if stash is empty
       else:
           return len(self._captured_stash)

    def win_check(self):
       '''Check so see if player won'''
       print(len(self._captured_stash))
       if len(self._captured_stash)>5: #if captured stash is bigger than 5
           name=self.get_player_name() #gets player name
           return name + ' Wins' #returns name concatinated with wins
       else:
           return 'successfully moved' #else returns move was successfull

    def set_res_stash(self,res_stash):
       '''Sets reserve stash, takes res_stash as parameter from FocusGame class'''
       self._reserve_stash=res_stash

game = FocusGame(('PlayerA', 'R'), ('PlayerB','G'))
print(game.move_piece('PlayerA',(0,0), (0,1), 1))  #Returns message "successfully moved"
game.show_pieces((0,1)) #Returns ['R','R']
game.show_captured('PlayerA') # Returns 0
print(game.reserved_move('PlayerA', (0,0))) # Returns message "No pieces in reserve"
game.show_reserve('PlayerA')






