from flask import Flask, render_template, request, jsonify
from card_utils import parse_card
from probability_calculator import get_hand_probabilities
from treys import Evaluator
import logging

app = Flask(__name__)
evaluator = Evaluator()

# Enable logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        app.logger.debug(f"Received data: {data}")
        
        # Parse hand
        hand = [parse_card(card) for card in data['hand']]
        app.logger.debug(f"Parsed hand: {hand}")
        
        # Parse board
        if data['board']:
            board = [parse_card(card) for card in data['board']]
        else:
            board = []
        app.logger.debug(f"Parsed board: {board}")
        
        # Parse number of players
        num_players = int(data['num_players'])
        app.logger.debug(f"Number of players: {num_players}")
        
        # Check if final round
        is_final_round = data.get('is_final_round', False)
        app.logger.debug(f"Is final round: {is_final_round}")
        
        # Calculate probabilities
        user_probabilities, opponent_probabilities, win_probability, tie_probability = get_hand_probabilities(evaluator, hand, board, num_players, is_final_round)
        app.logger.debug(f"Calculated probabilities")
        
        return jsonify({
            'user_probabilities': user_probabilities,
            'opponent_probabilities': opponent_probabilities,
            'win_probability': win_probability,
            'tie_probability': tie_probability
        })
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
