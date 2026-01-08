def extract_intent(user_input):
    user_input = user_input.lower()

    if "appointment" in user_input or "book" in user_input:
        return "BOOK_APPOINTMENT"
    
    if "doctor" in user_input:
        return "FIND_DOCTOR"
    
    if "service" in user_input or "treatment" in user_input:
        return "CHECK_SERVICE"
    
    return "UNKNOWN"
