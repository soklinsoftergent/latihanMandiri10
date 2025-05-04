def run_quiz(filename):
    print(f"nama file1: {filename}")
    
    with open(filename, 'r') as file:
        questions = file.readlines()
    
    for question in questions:
        if '||' not in question:
            continue
            
        q, a = question.split('||')
        q = q.strip()
        correct_answer = a.strip().lower()
        
        print(q)
        user_answer = input("Jawab: ").strip().lower()
        
        if user_answer == correct_answer:
            print("Jawaban benar!")
        else:
            print("Jawaban salah!")

run_quiz('soal.txt')