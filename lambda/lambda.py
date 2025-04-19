import json

def lambda_handler(event, context):

    school = "CSUF"
    Session = "Spring 2025"
    ClassName = "CPSC-362"
    class_time = "S 1:00 PM"
    registration_status = "full"

    # Response object
    response = {
        "school": school,
        "Session": Session,
        "ClassName": ClassName,
        "class_time": class_time,
        "registration_status": registration_status
    }

    return response
