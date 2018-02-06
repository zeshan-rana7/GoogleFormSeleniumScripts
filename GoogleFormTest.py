import os
import unittest
from selenium import webdriver
from Form1 import Form1
from Form2 import Form2
from LoginPage import LoginPage
from Form3 import Form3
from Form4 import Form4
from Form5 import Form5
from Form6 import Form6
from Form7 import Form7
from Form8 import Form8
from Form9 import Form9
from FormLastPage import FormLastPage
from CompareScore_Page import CompareScorePage
from Utils import *
import csv

class GoogleFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.url = "https://docs.google.com/forms/u/1/d/e/1FAIpQLSfSGh4qzssK1gnZ6JEUe1D4E3lmGCelVD0VZgdHs_y7K_U7rA/viewform"
        self.login_page = LoginPage(self.driver, self.url)
        self.form1 = Form1(self.driver)
        self.form2 = Form2(self.driver)
        self.form3 = Form3(self.driver)
        self.form4 = Form4(self.driver)
        self.form5 = Form5(self.driver)
        self.form6 = Form6(self.driver)
        self.form7 = Form7(self.driver)
        self.form8 = Form8(self.driver)
        self.form9 = Form9(self.driver)
        self.form_last_page = FormLastPage(self.driver)
        self.compare_score_page = CompareScorePage(self.driver)
        self.login_page.visit()

    # def test_allform_validation(self):
    #     self.login_page.Login(Email, Password)
    #     error_elements = self.form1.fillForm1("", "", "", "")
    #     for element in error_elements:
    #         print element.text
    #         self.assertEqual("This is a required question", element.text)

    # def test_CNIC_validation(self):
    #     self.login_page.Login(Email, Password)
    #     error_elements = self.form1.fillForm1("", "03134147467", "test@test.com", "abcd")
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)
    #     self.form1.clearformvalues()
    #     error_elements = self.form1.fillForm1("313", "03134147467", "test@test.com", "abcd")
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('Must match pattern', element_texts)

    # def test_phone_validation(self):
    #     self.login_page.Login(Email, Password)
    #     error_elements = self.form1.fillForm1("1234567890123", "", "test@test.com", "abcd")
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)
    #     self.form1.clearformvalues()
    #     error_elements = self.form1.fillForm1("1234567890123", "123", "test@test.com", "abcd")
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('Must match pattern', element_texts)

    # def test_Email_validatoin(self):
    #     self.login_page.Login(Email, Password)
    #     error_elements = self.form1.fillForm1("1234567890123", "03134147647", "", "abcd")
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)
    #     self.form1.clearformvalues()
    #     error_elements = self.form1.fillForm1("1234567890123", "03134147647", "test@test", "abcd")
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('Must be a valid email address', element_texts)
    #
    # def test_name_validatoin(self):
    #     self.login_page.Login(Email, Password)
    #     error_elements = self.form1.fillForm1("1234567890123", "03134147647", "test@test.com", "")
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)

    # def test_validate_Form2_with_no_answer(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     error_elements = self.form2.select_answer(0)
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)

    # def test_validate_Form2_with_one_answer(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     error_elements = self.form2.select_answer(1)
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)

    # def test_select_Form2_all_answers(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2, block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem

    # def test_validate_form3_no_answer(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2, block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     error_elements = self.form3.select_no_answer()
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)

    # def test_validate_form3_one_answer(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2, block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     error_elements = self.form3.select_one_answer()
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)

    # def test_select_form3_all_answers(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)

    # def test_validate_form4_no_answers(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     error_elements = self.form4.select_no_answer()
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)

    # def test_validate_form4_one_answers(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     self.form4.click_first_dropdown()
    #     error_elements = self.form4.select_one_answer()
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)

    # def test_select_form4_all_answers(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)

    # def test_validate_form5_no_file(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     error_elements = self.form5.select_no_answer()
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)

    # def test_validate_form5_one_file(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     error_elements = self.form5.upload_one_file()
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)

    # def test_select_form5_all_files(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     self.form5.upload_first_file()
    #     self.form5.upload_second_file()

    # def test_validate_form6_no_answer(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     self.form5.upload_first_file()
    #     self.form5.upload_second_file()
    #     elem = self.form6.verify_page()
    #     assert "Scale" == elem
    #     error_elements = self.form6.select_no_answer()
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)

    # def test_select_form6_all_answers(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     self.form5.upload_first_file()
    #     self.form5.upload_second_file()
    #     elem = self.form6.verify_page()
    #     assert "Scale" == elem
    #     question_elems = self.form6.get_question_elements()
    #     answer1 = get_rate_answer_for_question(question_elems)
    #     self.form6.select_answer_based_on_question(answer1)

    # def test_select_form7_no_answer(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     self.form5.upload_first_file()
    #     self.form5.upload_second_file()
    #     elem = self.form6.verify_page()
    #     assert "Scale" == elem
    #     question_elems = self.form6.get_question_elements()
    #     answer1 = get_rate_answer_for_question(question_elems)
    #     self.form6.select_answer_based_on_question(answer1)
    #     elem = self.form7.verify_page()
    #     assert "Multiple Choice grid" == elem
    #     error_elements = self.form7.select_no_answer()
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This question requires one response per row', element_texts)

    # def test_select_form7_one_answer(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     self.form5.upload_first_file()
    #     self.form5.upload_second_file()
    #     elem = self.form6.verify_page()
    #     assert "Scale" == elem
    #     question_elems = self.form6.get_question_elements()
    #     answer1 = get_rate_answer_for_question(question_elems)
    #     self.form6.select_answer_based_on_question(answer1)
    #     elem = self.form7.verify_page()
    #     assert "Multiple Choice grid" == elem
    #     error_elements = self.form7.select_one_answer()
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This question requires one response per row', element_texts)

    # def test_select_form7_all_answers(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     self.form5.upload_first_file()
    #     self.form5.upload_second_file()
    #     elem = self.form6.verify_page()
    #     assert "Scale" == elem
    #     question_elems = self.form6.get_question_elements()
    #     answer1 = get_rate_answer_for_question(question_elems)
    #     self.form6.select_answer_based_on_question(answer1)
    #     elem = self.form7.verify_page()
    #     assert "Multiple Choice grid" == elem
    #     question_elems = self.form7.get_question_elements()
    #     question_within_question_elems = self.form7.get_question_within_question_elements()
    #     answer1, answer2, answer3 = get_multiple_choic_grid_answer_for_question(question_elems,question_within_question_elems)
    #     self.form7.select_answer_based_on_question(answer1, answer2, answer3)

    # def test_validate_form8_no_answer(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     self.form5.upload_first_file()
    #     self.form5.upload_second_file()
    #     elem = self.form6.verify_page()
    #     assert "Scale" == elem
    #     question_elems = self.form6.get_question_elements()
    #     answer1 = get_rate_answer_for_question(question_elems)
    #     self.form6.select_answer_based_on_question(answer1)
    #     elem = self.form7.verify_page()
    #     assert "Multiple Choice grid" == elem
    #     question_elems = self.form7.get_question_elements()
    #     question_within_question_elems = self.form7.get_question_within_question_elements()
    #     answer1, answer2, answer3 = get_multiple_choic_grid_answer_for_question(question_elems,question_within_question_elems)
    #     self.form7.select_answer_based_on_question(answer1, answer2, answer3)
    #     elem = self.form8.verify_page()
    #     assert "Checkbox Grid" == elem
    #     error_elements = self.form8.select_no_answer()
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This question requires at least one response per row', element_texts)

    # def test_validate_form8_one_answer(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     self.form5.upload_first_file()
    #     self.form5.upload_second_file()
    #     elem = self.form6.verify_page()
    #     assert "Scale" == elem
    #     question_elems = self.form6.get_question_elements()
    #     answer1 = get_rate_answer_for_question(question_elems)
    #     self.form6.select_answer_based_on_question(answer1)
    #     elem = self.form7.verify_page()
    #     assert "Multiple Choice grid" == elem
    #     question_elems = self.form7.get_question_elements()
    #     question_within_question_elems = self.form7.get_question_within_question_elements()
    #     answer1, answer2, answer3 = get_multiple_choic_grid_answer_for_question(question_elems,question_within_question_elems)
    #     self.form7.select_answer_based_on_question(answer1, answer2, answer3)
    #     elem = self.form8.verify_page()
    #     assert "Checkbox Grid" == elem
    #     error_elements = self.form8.select_one_answer()
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This question requires at least one response per row', element_texts)

    # def test_select_form8_all_answer(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     self.form5.upload_first_file()
    #     self.form5.upload_second_file()
    #     elem = self.form6.verify_page()
    #     assert "Scale" == elem
    #     question_elems = self.form6.get_question_elements()
    #     answer1 = get_rate_answer_for_question(question_elems)
    #     self.form6.select_answer_based_on_question(answer1)
    #     elem = self.form7.verify_page()
    #     assert "Multiple Choice grid" == elem
    #     question_elems = self.form7.get_question_elements()
    #     question_within_question_elems = self.form7.get_question_within_question_elements()
    #     answer1, answer2, answer3 = get_multiple_choic_grid_answer_for_question(question_elems,
    #                                                                             question_within_question_elems)
    #     self.form7.select_answer_based_on_question(answer1, answer2, answer3)
    #     elem = self.form8.verify_page()
    #     assert "Checkbox Grid" == elem
    #     question_elems = self.form8.get_question_elements()
    #     question_within_question_elems = self.form8.get_question_within_question_elements()
    #     answer1, answer1_2, answer2, answer2_2, answer3, answer3_2 = get_mrq_grid_answer_for_question(question_elems,
    #                                                                             question_within_question_elems)
    #     self.form8.select_answer_based_on_question(answer1, answer1_2, answer2, answer2_2, answer3, answer3_2)

    # def test_validate_form9_no_value(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     self.form5.upload_first_file()
    #     self.form5.upload_second_file()
    #     elem = self.form6.verify_page()
    #     assert "Scale" == elem
    #     question_elems = self.form6.get_question_elements()
    #     answer1 = get_rate_answer_for_question(question_elems)
    #     self.form6.select_answer_based_on_question(answer1)
    #     elem = self.form7.verify_page()
    #     assert "Multiple Choice grid" == elem
    #     question_elems = self.form7.get_question_elements()
    #     question_within_question_elems = self.form7.get_question_within_question_elements()
    #     answer1, answer2, answer3 = get_multiple_choic_grid_answer_for_question(question_elems,
    #                                                                             question_within_question_elems)
    #     self.form7.select_answer_based_on_question(answer1, answer2, answer3)
    #     elem = self.form8.verify_page()
    #     assert "Checkbox Grid" == elem
    #     question_elems = self.form8.get_question_elements()
    #     question_within_question_elems = self.form8.get_question_within_question_elements()
    #     answer1, answer1_2, answer2, answer2_2, answer3, answer3_2 = get_mrq_grid_answer_for_question(question_elems,
    #                                                                             question_within_question_elems)
    #     self.form8.select_answer_based_on_question(answer1, answer1_2, answer2, answer2_2, answer3, answer3_2)
    #     elem = self.form9.verify_page()
    #     assert "Date & Time" == elem
    #     error_elements = self.form9.select_no_answer()
    #     element_texts = [element.text for element in error_elements]
    #     self.assertIn('This is a required question', element_texts)

    # def test_flow1_complete(self):
    #     self.login_page.Login(Email, Password)
    #     self.form1.fillForm1(CNIC, phone_number, Email, name)
    #     elem = self.form2.verify_page()
    #     assert "Multiple type Questions" == elem
    #     block_questions_answers_elements = self.form2.get_questions_answers_block()
    #     answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
    #     self.form2.select_answer_based_on_question(answer1, answer2)
    #     elem = self.form3.verify_page()
    #     assert "Checkboxes" == elem
    #     question_elems = self.form3.get_question_elements()
    #     answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
    #     self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
    #     elem = self.form4.verify_page()
    #     assert "Dropdown" == elem
    #     question_elems = self.form4.get_question_elements()
    #     self.form4.click_first_dropdown()
    #     answer1, answer2 = get_drop_down_answer_for_question(question_elems)
    #     self.form4.select_first_answer_based_on_question(answer1)
    #     self.form4.click_second_dropdown()
    #     self.form4.select_second_answer_based_on_question(answer2)
    #     elem = self.form5.verify_page()
    #     assert "File Uploading" == elem
    #     self.form5.upload_first_file()
    #     self.form5.upload_second_file()
    #     elem = self.form6.verify_page()
    #     assert "Scale" == elem
    #     question_elems = self.form6.get_question_elements()
    #     answer1 = get_rate_answer_for_question(question_elems)
    #     self.form6.select_answer_based_on_question(answer1)
    #     elem = self.form7.verify_page()
    #     assert "Multiple Choice grid" == elem
    #     question_elems = self.form7.get_question_elements()
    #     question_within_question_elems = self.form7.get_question_within_question_elements()
    #     answer1, answer2, answer3 = get_multiple_choic_grid_answer_for_question(question_elems,
    #                                                                             question_within_question_elems)
    #     self.form7.select_answer_based_on_question(answer1, answer2, answer3)
    #     elem = self.form8.verify_page()
    #     assert "Checkbox Grid" == elem
    #     question_elems = self.form8.get_question_elements()
    #     question_within_question_elems = self.form8.get_question_within_question_elements()
    #     answer1, answer1_2, answer2, answer2_2, answer3, answer3_2 = get_mrq_grid_answer_for_question(question_elems,
    #                                                                             question_within_question_elems)
    #     self.form8.select_answer_based_on_question(answer1, answer1_2, answer2, answer2_2, answer3, answer3_2)
    #     elem = self.form9.verify_page()
    #     assert "Date & Time" == elem
    #     question_elems = self.form9.get_question_elements()
    #     month, day, year, hour, minute, am_pm = get_date_time(question_elems)
    #     self.form9.input_date_time(month, day, year, hour, minute, am_pm)

    def test_compare_score(self):
        self.login_page.Login(Email, Password)
        self.form1.fillForm1(CNIC, phone_number, Email, name)
        elem = self.form2.verify_page()
        assert "Multiple type Questions" == elem
        block_questions_answers_elements = self.form2.get_questions_answers_block()
        answer1, answer2 = get_mcq_answer_for_questions(self.form2,block_questions_answers_elements)
        self.form2.select_answer_based_on_question(answer1, answer2)
        elem = self.form3.verify_page()
        assert "Checkboxes" == elem
        question_elems = self.form3.get_question_elements()
        answer1, answer2, answer3, answer4 = get_mrq_answer_for_question(question_elems)
        self.form3.select_answer_based_on_question(answer1, answer2, answer3, answer4)
        elem = self.form4.verify_page()
        assert "Dropdown" == elem
        question_elems = self.form4.get_question_elements()
        self.form4.click_first_dropdown()
        answer1, answer2 = get_drop_down_answer_for_question(question_elems)
        self.form4.select_first_answer_based_on_question(answer1)
        self.form4.click_second_dropdown()
        self.form4.select_second_answer_based_on_question(answer2)
        elem = self.form5.verify_page()
        assert "File Uploading" == elem
        self.form5.upload_first_file()
        self.form5.upload_second_file()
        elem = self.form6.verify_page()
        assert "Scale" == elem
        question_elems = self.form6.get_question_elements()
        answer1 = get_rate_answer_for_question(question_elems)
        self.form6.select_answer_based_on_question(answer1)
        elem = self.form7.verify_page()
        assert "Multiple Choice grid" == elem
        question_elems = self.form7.get_question_elements()
        question_within_question_elems = self.form7.get_question_within_question_elements()
        answer1, answer2, answer3 = get_multiple_choic_grid_answer_for_question(question_elems,
                                                                                question_within_question_elems)
        self.form7.select_answer_based_on_question(answer1, answer2, answer3)
        elem = self.form8.verify_page()
        assert "Checkbox Grid" == elem
        question_elems = self.form8.get_question_elements()
        question_within_question_elems = self.form8.get_question_within_question_elements()
        answer1, answer1_2, answer2, answer2_2, answer3, answer3_2 = get_mrq_grid_answer_for_question(question_elems,
                                                                                question_within_question_elems)
        self.form8.select_answer_based_on_question(answer1, answer1_2, answer2, answer2_2, answer3, answer3_2)
        elem = self.form9.verify_page()
        assert "Date & Time" == elem
        question_elems = self.form9.get_question_elements()
        month, day, year, hour, minute, am_pm = get_date_time(question_elems)
        self.form9.input_date_time(month, day, year, hour, minute, am_pm)
        elem = self.form_last_page.verify_page()
        self.assertEqual("Your response has been recorded.", elem)
        self.form_last_page.click_view_score()
        elem = self.compare_score_page.verify_page()
        self.assertIn("Total points", elem)
        total_score_text = self.compare_score_page.get_user_total_score()
        each_question_score_elems = self.compare_score_page.get_user_each_attempted_question_score()
        total_score, each_question_score = compare_learner_score(total_score_text, each_question_score_elems)
        self.assertEqual(total_score, each_question_score)

        with open('persons.csv', 'wb') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Name', 'Profession'])
            filewriter.writerow(['Derek', 'Software Developer'])
            filewriter.writerow(['Steve', 'Software Developer'])
            filewriter.writerow(['Paul', 'Manager'])



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()