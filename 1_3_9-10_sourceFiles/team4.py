team_name = 'E5'
strategy_name = 'Collude first 50 rounds unless betrayed. Betray 60th round forward.'
strategy_description = '''\
Betray if ever betrayed.
If I haven't been betrayed yet, I'll betray starting with the 60th round.
'''

import random
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    # If the other player has betrayed or this is the last half of the game, 
    if 'b' in their_history or len(their_history)>50: 
        return 'b'               # Betray.
    else:
        return 'c'       
    
    if my_score<-750 and len(my_history)%2 == 0:
        return 'c'
    else:
        return 'b'