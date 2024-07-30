from flask import Blueprint, request, jsonify
from tracking.service.visit_service import VisitService

visit_bp = Blueprint('visit', __name__)
visit_service = VisitService()


@visit_bp.route('/track', methods=['POST'])
def create_visit() -> jsonify:
    """
    Handle POST request to track a new visit.

    :return: A JSON response containing the visit_id of the newly created visit.
    """
    data = request.get_json()
    user_id = data.get('user_id')
    url = data.get('url')
    duration = data.get('duration')

    if not all([user_id, url, duration]):
        return jsonify({"error": "Missing data"}), 400

    visit_id = visit_service.create_visit(user_id, url, duration)
    return jsonify({"visit_id": visit_id}), 201


@visit_bp.route('/visits/<string:user_id>', methods=['GET'])
def get_visits_by_user(user_id) -> jsonify:
    """
    Handle GET request to retrieve visits for a specific user.

    :param user_id: The ID of the user whose visits are to be retrieved.
    :return: A JSON response containing a list of visits.
    """
    visits = visit_service.get_visits_by_user(user_id)
    return jsonify([visit.to_db() for visit in visits])


@visit_bp.route('/visit/<string:visit_id>', methods=['GET'])
def get_visit(visit_id) -> jsonify:
    """
    Handle GET request to retrieve a visit.

    :return: A JSON response containing the visit details.
    """
    visit = visit_service.get_visit_by_id(visit_id)
    if visit is None:
        return jsonify({"error": "Visit not found"}), 404
    return jsonify(visit.to_dict()), 200


@visit_bp.route('/visit/<string:visit_id>', methods=['DELETE'])
def delete_visit(visit_id) -> jsonify:
    """
    Handle DELETE request to delete a visit.

    :return: A JSON response containing the visit_id of the deleted visit.
    """
    deleted_count = visit_service.delete_visit(visit_id)
    return jsonify({"deleted_count": deleted_count}), 200


@visit_bp.route('/visits/<string:visit_id>', methods=['PUT'])
def update_visit(visit_id) -> jsonify:
    """
    Handle PUT request to update a visit.

    :param visit_id: The ID of the visit to be updated.
    :return: A JSON response containing the number of modified documents.
    """
    update_fields = request.get_json()
    modified_count = visit_service.update_visit(visit_id, update_fields)
    return jsonify({"modified_count": modified_count}), 200