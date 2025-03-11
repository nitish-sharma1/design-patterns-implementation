from flask import Blueprint,request,jsonify


bp = Blueprint('auth', __name__)


# Sample Login Route
@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Simple authentication logic (for demo)
    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

# Sample Signup Route
@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    return jsonify({"message": f"User {data.get('username')} signed up successfully!"}), 201