'''functions for fb'''
def get_feedback_for_table():
    '''list of feedback'''
    feedback = []
    with open("./data/feedback.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            feedback1, source, email = line.split(";")
            feedback.append([cnt, feedback1, source, email])
            cnt += 1
    return feedback


def write_feedback(new_feedback, user_name, user_email):
    '''adding fb'''
    new_feedback_line = f"{new_feedback};{user_name};{user_email}"
    with open("./data/feedback.csv", "r", encoding="utf-8") as f:
        existing_feedback = [l.strip("\n") for l in f.readlines()]
        title = existing_feedback[0]
        old_feedback = existing_feedback[1:]
    feedback_sorted = old_feedback + [new_feedback_line]
    # feedback_sorted.sort()
    new_feedback = [title] + feedback_sorted
    with open("./data/feedback.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_feedback))
