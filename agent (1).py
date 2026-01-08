from website_structure import website_structure

def handle_intent(intent, user_input):
    if intent == "BOOK_APPOINTMENT":
        return (
            "To book an appointment:\n"
            "1. Go to 'Appointments'\n"
            "2. Click on 'Book Appointment'\n"
            "3. Select ENT doctor\n"
            "4. Choose available time slot"
        )

    if intent == "FIND_DOCTOR":
        doctors = ", ".join(website_structure["doctors"])
        return f"Available ENT doctors are: {doctors}"

    if intent == "CHECK_SERVICE":
        services = ", ".join(website_structure["services"])
        return f"The clinic provides these ENT services: {services}"

    return "Sorry, I couldn't understand your request. Please try again."
