from survey import AnonynousSurvey

#定义一个问题，并创建一个表示调查的AnonynoudSyrvey对象
question = "What language did you first learn to speak?"
language_survey = AnonynousSurvey(question)

#显示问题并储存答案
language_survey.show_question()
print(f"Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

#显示调查结果
print("\nThank you to everyone who participated in the suivey!")
language_survey.show_results()