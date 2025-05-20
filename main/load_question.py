from.  models import Question

def run():
    # Change the question json accordingly to insert
    questions = [
  {
    "question": "Which algorithm is used for page replacement?",
    "options": [
      "Dijkstra",
      "FIFO",
      "LRU",
      "Kruskal"
    ],
    "correct_option": 3,
    "difficulty": "hard"
  },
  {
    "question": "SSH works over which protocol?",
    "options": [
      "TCP",
      "UDP",
      "HTTP",
      "IP"
    ],
    "correct_option": 1,
    "difficulty": "hard"
  },
  {
    "question": "Time complexity of binary search?",
    "options": [
      "O(n)",
      "O(log n)",
      "O(n log n)",
      "O(n²)"
    ],
    "correct_option": 2,
    "difficulty": "hard"
  },
  {
    "question": "Which pattern limits to one instance?",
    "options": [
      "Factory",
      "Observer",
      "Singleton",
      "Strategy"
    ],
    "correct_option": 3,
    "difficulty": "hard"
  },
  {
    "question": "Which CPU scheduling is fastest?",
    "options": [
      "FCFS",
      "SJF",
      "Round Robin",
      "Priority"
    ],
    "correct_option": 2,
    "difficulty": "hard"
  },
  {
    "question": "Pick a NoSQL database.",
    "options": [
      "Oracle",
      "PostgreSQL",
      "MongoDB",
      "SQLite"
    ],
    "correct_option": 3,
    "difficulty": "hard"
  },
  {
    "question": "Which is used in public-key encryption?",
    "options": [
      "AES",
      "SHA",
      "RSA",
      "DES"
    ],
    "correct_option": 3,
    "difficulty": "hard"
  },
  {
    "question": "IP protocol belongs to which OSI layer?",
    "options": [
      "Data Link",
      "Network",
      "Transport",
      "Application"
    ],
    "correct_option": 2,
    "difficulty": "hard"
  },
  {
    "question": "Semaphore is used for?",
    "options": [
      "Scheduling",
      "Deadlock",
      "Memory",
      "Sync"
    ],
    "correct_option": 4,
    "difficulty": "hard"
  },
  {
    "question": "Which sort has O(n log n) best case?",
    "options": [
      "Bubble",
      "Quick",
      "Insertion",
      "Selection"
    ],
    "correct_option": 2,
    "difficulty": "hard"
  },
  {
    "question": "Which is not a DBMS?",
    "options": [
      "MySQL",
      "SQLite",
      "Redis",
      "MongoDB"
    ],
    "correct_option": 3,
    "difficulty": "hard"
  },
  {
    "question": "Port number for SSH?",
    "options": [
      "21",
      "80",
      "22",
      "443"
    ],
    "correct_option": 3,
    "difficulty": "hard"
  },
  {
    "question": "Main goal of OS?",
    "options": [
      "Security",
      "UI",
      "Efficiency",
      "Browsing"
    ],
    "correct_option": 3,
    "difficulty": "hard"
  },
  {
    "question": "Which is statically typed?",
    "options": [
      "Python",
      "Java",
      "JavaScript",
      "Ruby"
    ],
    "correct_option": 2,
    "difficulty": "hard"
  },
  {
    "question": "DNS translates?",
    "options": [
      "MAC to IP",
      "Name to IP",
      "IP to MAC",
      "Port to IP"
    ],
    "correct_option": 2,
    "difficulty": "hard"
  }
]



    for q in questions:
        Question.objects.create(
            question = q['question'],
            option1 = q['options'][0],
            option2 = q['options'][1],
            option3 = q['options'][2],
            option4 = q['options'][3],
            correct_option = q['correct_option'],
            difficulty = q['difficulty']
        )
    
    print("Successfuly added")