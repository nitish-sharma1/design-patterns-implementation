from flask import Blueprint, request, jsonify

# Create Blueprint instance
bp = Blueprint('task', __name__)


# Sample route for creating a task
@bp.route('/create', methods=['POST'])
def create_task():
    data = request.get_json()
    task_name = data.get("task_name")

    if not task_name:
        return jsonify({"error": "Task name is required"}), 400

    return jsonify({"message": f"Task '{task_name}' created successfully!"}), 201


# Sample route for fetching tasks
@bp.route('/list', methods=['GET'])
def list_tasks():
    sample_tasks = [
        {"id": 1, "task_name": "Complete Flask Project"},
        {"id": 2, "task_name": "Review Design Patterns"}
    ]
    return jsonify({"tasks": sample_tasks}), 200
