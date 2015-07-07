from ps4a import *
import time

# ------- HELPER functions start ----------

def isLettersOfWordInHand(word, hand):    
    '''
    hand - dictionary (string, int)
    word - string

    returns - True if word can be constructed using letters from hand
            - False if word cannot be constructed from hand
    '''
    word_len = len(word)
    count = 0
    if word_len == 0:
        return False
    for c in hand:
        clen_hand = hand.get(c, 0)
        clen_word = word.count(c, 0)
        if clen_word in range(1, clen_hand + 1):
            count += clen_word            
        if count == word_len:
            return True                        
    return False

# ------- HELPER functions end ----------

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    total_score = 0

    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None    

    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isLettersOfWordInHand(word, hand):
            # Find out how much making that word is worth
            word_score = getWordScore(word, n)            
            # If the score for that word is higher than your best score
            if word_score > total_score:
                # Update your best score, and best word accordingly
                total_score = word_score
                best_word = word              
    # return the best word you found.
    return best_word                


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total_score = 0    

    while 1:
        if sum(hand.values()) != 0:
            print '\nCurrent Hand:',
            displayHand(hand)
        play_word = compChooseWord(hand, wordList, n);
        if play_word == None:
            print 'Total score: {total_score} points.'.format(**locals())
            break
        score = getWordScore(play_word, n);
        total_score += score
        print '\"{play_word}\" earned {score} points. Total: {total_score} points'.format(**locals())
        hand = updateHand(hand, play_word)


    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    n = HAND_SIZE    
    hand_cache = {}

    while 1:
        game_type = raw_input('\nEnter n to deal a new hand, r to replay the last hand, or e to end game: ').lower()
        if game_type in 'nr':            
            if hand_cache == {} and game_type == 'r':
                print 'You have not played a hand yet. Please play a new hand first!' 
            else:                
                while 1:
                    game_mode = raw_input('\nEnter u to have yourself play, c to have the computer play: ').lower()                    
                    if game_mode in 'uc': 
                        if game_type == 'n':
                            hand = dealHand(n)
                            hand_cache = hand.copy()                
                        else:
                            hand = hand_cache                            
                        if game_mode == 'u':
                            playHand(hand, wordList, n)
                        elif game_mode == 'c': 
                            compPlayHand(hand, wordList, n)
                        break                            
                    else:
                        print 'Invalid command.'
        elif game_type == 'e':
            break
        else:
            print 'Invalid command.'                                
    

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


