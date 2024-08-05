from treys import Card

def parse_card(card_str):
    # Convert to the format expected by treys
    rank_dict = {
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': 'T',
        'j': 'J',
        'q': 'Q',
        'k': 'K',
        'a': 'A'
    }
    suit_dict = {
        'h': 'h',  # Hearts
        'd': 'd',  # Diamonds
        'c': 'c',  # Clubs
        's': 's'   # Spades
    }
    try:
        rank = rank_dict[card_str[:-1]]
        suit = suit_dict[card_str[-1]]
        formatted_card = rank + suit
        return Card.new(formatted_card)
    except KeyError:
        raise ValueError(f"Invalid card format: {card_str}")
