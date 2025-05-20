from.  models import Question

def run():
    # Change the question json accordingly to insert
    questions = [
        {
            "text": "What does CPU stand for?",
            "options": ["Central Processing Unit", "Central Program Unit", "Computer Processing Unit", "Control Panel Unit"],
            "correct_option": 0
        },
        {
            "text": "What is the brain of the computer?",
            "options": ["RAM", "Hard Drive", "CPU", "Motherboard"],
            "correct_option": 2
        },
        {
            "text": "Which of these is a web browser?",
            "options": ["Google", "Chrome", "Windows", "Python"],
            "correct_option": 1
        },
        {
            "text": "Which device is used to print hard copies?",
            "options": ["Scanner", "Monitor", "Printer", "Plotter"],
            "correct_option": 2
        },
        {
            "text": "Which one is an input device?",
            "options": ["Speaker", "Monitor", "Keyboard", "Printer"],
            "correct_option": 2
        },
        {
            "text": "What does URL stand for?",
            "options": ["Universal Resource Locator", "Uniform Resource Locator", "Uniform Reference Link", "Universal Reference Link"],
            "correct_option": 1
        },
        {
            "text": "What kind of software is an operating system?",
            "options": ["Application Software", "System Software", "Utility Software", "Database Software"],
            "correct_option": 1
        },
        {
            "text": "Which of the following is a mobile operating system?",
            "options": ["Linux", "Windows", "Android", "Ubuntu"],
            "correct_option": 2
        },
        {
            "text": "Which port is used for HTTP by default?",
            "options": ["20", "21", "80", "443"],
            "correct_option": 2
        }
    ]

    for q in questions:
        Question.objects.create(
            question = q['text'],
            option1 = q['options'][0],
            option2 = q['options'][1],
            option3 = q['options'][2],
            option4 = q['options'][3],
            correct_option = q['correct_option']
        )
    
    print("Successfuly added")