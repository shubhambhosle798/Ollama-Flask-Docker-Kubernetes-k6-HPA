from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

class CustomError(Exception):
    pass

@app.route('/')
def home():
    app.logger.info("Home route accessed")
    return "Welcome to the Ollama Text Generation API"

@app.route('/generate', methods=['POST'])
def generate_text():
    app.logger.info("Generate route accessed")
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        raise CustomError("Prompt is required")

    try:
        # Assuming ollama.generate is a function that generates text based on the prompt
        response = ollama.generate(prompt)
        app.logger.info("Response generated successfully")
        return jsonify({"response": response}), 200
    except Exception as e:
        app.logger.error(f"Error generating response: {str(e)}")
        raise CustomError(str(e))

# Central Error Handler
@app.errorhandler(CustomError)
def handle_custom_error(error):
    response = {
        'success': False,
        'error_type': error.__class__.__name__,
        'message': str(error)
    }
    return jsonify(response), 500

@app.errorhandler(404)
def page_not_found(e):
    return 'Error 404: The requested URL was not found on the server.', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
