import logging
from flask import Flask, jsonify
from src.interfaces.controllers.people_controller import get_sorted_people
from src.infrastructure.logging_config import setup_logging
"""
Simple API server based on python.

Endpoints:

/sorted-people: Return a JSON of the star wars characters sorted by their names on ascending order [A->Z]
"""
setup_logging()
logger = logging.getLogger('star_wars_logger')

app = Flask(__name__)

@app.route('/sorted-people', methods=['GET'])
def sorted_people():
    try:
        data = get_sorted_people()
        return jsonify(data)
    except Exception as e:
        logger.exception("An error occurred while processing /sorted-people request.")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 Not Found: {error}")
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 Internal Server Error: {error}")
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
