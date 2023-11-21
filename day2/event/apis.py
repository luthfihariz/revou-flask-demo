from flask import Blueprint, request
from datetime import datetime
from event.constants import EVENT_DATE_FORMAT

event_blueprint = Blueprint('event_blueprint', __name__)

events = [{'name': 'Lecture 1 Flask Fundamentals', 'start_date': datetime(2023, 4, 15, 12, 30, 0)}]

@event_blueprint.route("", methods=["GET"])
def get_event_list():
    return __get_event_responses()

@event_blueprint.route("", methods=["POST"])
def create_event():    
    if not request.is_json:
        return {"error": "Bukan json!!"}, 400

    data = request.get_json()

    if "name" not in data:
        return {"error": "Name is not available"}, 400
    
    if "start_date" not in data:
        return {"error": "Start date is not available"}, 400
    
    event_name = data.get("name")
    start_date_string = data.get("start_date")
    start_date = datetime.strptime(start_date_string, EVENT_DATE_FORMAT)

    events.append({
        'name': event_name,
        'start_date': start_date
    })

    return __get_event_responses()


def __get_event_responses():
    print(events)
    return list(map(lambda item: {'name': item['name'], 'start_date': datetime.strftime(item['start_date'], EVENT_DATE_FORMAT)}, events))