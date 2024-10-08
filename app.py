from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Home route that renders the index page
    return render_template("index.html")

app = Flask(__name__)

# Vulnerable endpoint demonstrating path traversal
@app.route('/view-file', methods=['GET'])
def view_file():
    # Get the filename from the query parameter
    filename = request.args.get('filename')  # Unsafe input retrieval

    try:
        # Open and read the file content (vulnerable part)
        with open(f"files/{filename}", 'r') as file:
            content = file.read()
        return jsonify({"content": content})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)



