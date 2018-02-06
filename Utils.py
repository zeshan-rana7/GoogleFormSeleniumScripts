import os
import datetime
import re
now = datetime.datetime.now()
Email = os.environ.get('GOOGLE_EMAIL', "zeeshan.rana@arbisoft.com")
Password = os.environ.get('GOOGLE_PASSWORD', "test123test123afasdf")
CNIC = '3840261531647'
phone_number = '03134147647'
name = 'zeshan'
form2_question1 = "Use of Firebug in Selenium? *"
form2_question2 = "Select the name which is NOT a type of the locater? *"
next_button_css = ".freebirdFormviewerViewNavigationButtons .quantumWizButtonPaperbuttonEl:nth-of-type(2) .quantumWizButtonPaperbuttonLabel.exportLabel"
question_type_title_text = ".freebirdMaterialHeaderbannerPagebreakText.freebirdFormviewerViewItemsPagebreakBannerText.freebirdCustomFont"
question_ans_dict = {'Select the correct answers *':
                         ['63/7 = 54/6', '5*6 = 10*6', '8*7 = 9*9', '72/9 = 64/8', '4*10 = 5*8'],
                     'Select the two numbers that are not prime. *': ['21', '11', '31', '51', '41'],
                     'Capital of Pakistan *': ['Lahore', 'Karachi', 'Quetta', 'Islamabad', 'Peshawar'],
                     'Capital of Punjab *': ['Faisalabad', 'Sargodha', 'Gujranwala', 'Multan', 'Lahore'],
                     'On a scale of 1 to five how hard this assignment is? *': ['1', '2', '3', '4', '5'],
                     'How satisfied are you with the following? *': {'Automation Training Lectures': ['1', '2', '3', '4', '5'],
                                                                     'Assignments': ['1', '2', '3', '4', '5'],
                                                                     'Example scripts': ['1', '2', '3', '4', '5']},
                     'Select your proficiency in following *': {'Urdu': ['Reading', 'Writing', 'Listening'],
                                                                     'English': ['Reading', 'Writing', 'Listening'],
                                                                     'French': ['Reading', 'Writing', 'Listening']},
                     'Enter Current date *': [now.month, now.day, now.year],
                     'Enter Current time *': [now.hour, now.minute]
                     }
question_answer_dict = {}

def get_mrq_answer_for_question(question_elems):
    #for question_elem in question_elems:
    for question, answers in question_ans_dict.items():
        if question == question_elems[0].text:
            answer1,answer2 =  question_ans_dict[question][0],question_ans_dict[question][1]
        elif question == question_elems[1].text:
            answer3,answer4 = question_ans_dict[question][0],question_ans_dict[question][1]
    return answer1,answer2,answer3,answer4


def get_drop_down_answer_for_question(question_elems):
    #for question_elem in question_elems:
    for question, answers in question_ans_dict.items():
        if question == question_elems[0].text:
            answer1 =  question_ans_dict[question][2]
        elif question == question_elems[1].text:
            answer2 = question_ans_dict[question][3]
    return answer1, answer2


def get_mcq_answer_for_questions(form2,block_questions_answers_elements):
    for block_elem in block_questions_answers_elements:
        question_text = form2.get_question_text(block_elem)
        question_answer_dict[question_text] = []
        answers_elements = form2.get_answers_text(block_elem)
        for answers_elem in answers_elements:
            question_answer_dict[question_text].append(answers_elem.text)
    for question, answers in question_answer_dict.items():
        if question == form2_question1:
            for answer in answers:
                if answer == 'Inspecting Elements':
                    answer1 = answer
        elif question == form2_question2:
            for answer in answers:
                if answer == 'Password':
                    answer2 = answer
    return answer1, answer2

def get_rate_answer_for_question(question_elems):
    #for question_elem in question_elems:
    for question, answers in question_ans_dict.items():
        if question == question_elems[0].text:
            answer1 =  question_ans_dict[question][2]
    return answer1

def get_multiple_choic_grid_answer_for_question(question_elems,question_within_question_elems):
    #for question_elem in question_elems:
    for question, answers in question_ans_dict.items():
        if question == question_elems[0].text:
            if isinstance(answers, dict):
                for key, value in answers.iteritems():
                    if key == question_within_question_elems[0].text:
                        answer1 = question_ans_dict[question][key][2]
                    elif key == question_within_question_elems[1].text:
                        answer2 = question_ans_dict[question][key][3]
                    elif key == question_within_question_elems[2].text:
                        answer3 = question_ans_dict[question][key][4]
    return answer1, answer2, answer3

def get_mrq_grid_answer_for_question(question_elems,question_within_question_elems):
    #for question_elem in question_elems:
    for question, answers in question_ans_dict.items():
        if question == question_elems[0].text:
            if isinstance(answers, dict):
                for key, value in answers.iteritems():
                    if key == question_within_question_elems[0].text:
                        answer1, answer1_2 = question_ans_dict[question][key][0], question_ans_dict[question][key][1]
                    elif key == question_within_question_elems[1].text:
                        answer2, answer2_2 = question_ans_dict[question][key][1], question_ans_dict[question][key][2]
                    elif key == question_within_question_elems[2].text:
                        answer3, answer3_2 = question_ans_dict[question][key][2], question_ans_dict[question][key][0]
    return answer1, answer1_2, answer2, answer2_2, answer3, answer3_2

def get_date_time(question_elems):
    #for question_elem in question_elems:
    for question, answers in question_ans_dict.items():
        if question == question_elems[0].text:
            if question == 'Enter Current date *':
                month =  question_ans_dict[question][0]
                day =  question_ans_dict[question][1]
                year =  question_ans_dict[question][2]
        elif question == question_elems[1].text:
            if question == 'Enter Current date *':
                month =  question_ans_dict[question][0]
                day =  question_ans_dict[question][1]
                year =  question_ans_dict[question][2]
    now.strftime("%H:%M")
    formatted_string = now.strftime("%I:%M %p")
    split_time_list = re.split(':| ', formatted_string)
    hour = split_time_list[0]
    minute = split_time_list[1]
    set_am_pm = split_time_list[2]
    return month,day,year,hour,minute,set_am_pm


def compare_learner_score(total_score_text, each_question_score_elems):
    total_score = re.split('/', total_score_text)
    total_score = int(total_score[0])
    tota_score_of_attempted_question = 0
    for each_question_score_elem in each_question_score_elems:
        each_question_score_text = re.split('/', each_question_score_elem.text)
        print each_question_score_text
        each_question_score = each_question_score_text[0]
        tota_score_of_attempted_question += int(each_question_score)
    return total_score, tota_score_of_attempted_question

# def get_answer_for_question(question_elems):
#     for question_elem in question_elems:
#         for question, answers in question_ans_dict.items():
#             if question == question_elem.text:
#                 for answer in answers:
#                     if answer == '21':
#                         answer1=  question_ans_dict[question][answer]
#                     elif answer == '41'
