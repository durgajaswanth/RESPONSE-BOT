import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!\n WELCOME TO VELTECH UNIVERSITY\n  THIS IS VELBOT!!!\n  HOW CAN I HELP YOU ?', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response("SCHOOL OF COMPUTING-CSE & IT\n SCHOOL OF ELECTRICAL AND COMMUNICATION-EEE & ECE & BIO-MEDICAL & BIO-TECH\n SCHOOL OF MECHANICAL AND CONSTRUCTION-CIVIL & AERO & AUTO & MECH\nSCHOOL OF LAW\n", ["branches", "academics", "groups"], single_response=True)
    response("UG\nPG\nPh.D.\nSports Quota\nInternational Admission", ["admissions"], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('CDIO first member in INDIA', ['speciality', 'in', 'veltech'], single_response=True)
    response('Conceive Design Implement Operate', ['full', 'form', 'cdio'], single_response=True)
    response('STUDENT LOGIN PAGE (LINK)', ['results'], single_response=True)

    response('ACCORDING TO NIRF 2021 WE ARE IN 93rd PLACE IN INDIA', ['rank', 'rankings'], single_response=True)
    response('NICE!!!!!', ['im', 'fine', 'good'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'veltech', 'university'], required_words=['veltech', 'university'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('VELTECH: ' + get_response(input('You: ')))
