hand1 = ["9H", "JS", "AC", "3H", "10S", "9C", "5H", "7C", "4S", "QS", "2D", "2S", "8H", "9D", "3D", "7H", "7S", "AS", "10H"]
hand2 = ["AS", "JC", "7H", "8D", "KH", "JC", "5C", "9H", "10D", "2S", "7S", "6H"]
hand3 = ["JH", "KD", "10D", "10H", "2H", "AH", "8D", "7H", "5H", "4D", "9H", "3D", "KH"]


# leftmost is two. Rightmost is ace
numberCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def cardCounter(hand):
    #colors
    red = 0
    black = 0
    #suits
    clubs = 0
    diamonds = 0
    hearts = 0
    spades = 0

    # leftmost is two. Rightmost is ace
    cardCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for card in hand:
        if card[-1] == "D" or card[-1] == "H":
            cardCounts[0] += 1
        elif card[-1] == "C" or card[-1] == "S":
            cardCounts[1] += 1
        
        cardVals = {
            "C" : 2,
            "D" : 3,
            "H" : 4,
            "S" : 5,
            "2" : 6,
            "3" : 7,
            "4" : 8,
            "5" : 9,
            "6" : 10,
            "7" : 11,
            "8" : 12,
            "9" : 13,
            "1" : 14,
            "J" : 15,
            "Q" : 16,
            "K" : 17,
            "A" : 18
        }
        
        # Color
        cardVal = cardVals[card[-1]]
        cardCounts[cardVal] += 1
        
        # Value
        cardVal = cardVals[card[0]]
        cardCounts[cardVal] += 1

    return cardCounts

def cardCountPrinter(cardVals):
    print(f"""
    RED : {cardVals[0]}
    BLACK : {cardVals[1]}
    CLUBS : {cardVals[2]}
    DIAMONDS : {cardVals[3]}
    HEARTS : {cardVals[4]}
    SPADES : {cardVals[5]}
    TWO : {cardVals[6]}
    THREE : {cardVals[7]}
    FOUR : {cardVals[8]}
    FIVE : {cardVals[9]}
    SIX : {cardVals[10]}
    SEVEN : {cardVals[11]}
    EIGHT : {cardVals[12]}
    NINES : {cardVals[13]}
    TENS : {cardVals[14]}
    JACKS : {cardVals[15]}
    QUEENS : {cardVals[16]}
    KINGS : {cardVals[17]}
    ACES : {cardVals[18]}    
    """)
            

# can we make it into a function so it isn't pain
# maybe, we might need to make it a class

print("HAND 1")
cardCountPrinter(cardCounter(hand1))
print("HAND 2")
cardCountPrinter(cardCounter(hand2))
print("HAND 3")
cardCountPrinter(cardCounter(hand3))
# print("HAND 4")
# cardCountPrinter(cardCounter(hand4))


#output count for color varient, suit, and base card dec


    # RED : 9
    # BLACK : 10
    # CLUBS : 3
    # DIAMONDS : 3
    # HEARTS : 6
    # SPADES : 7
    # TWO : 2
    # THREE : 2
    # FOUR : 1
    # FIVE : 1
    # SIX : 0
    # SEVEN : 3
    # EIGHT : 1
    # NINES : 3
    # TENS : 2
    # JACKS : 1
    # QUEENS : 1
    # KINGS : 0
    # ACES : 2