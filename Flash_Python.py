class flash_card(object):
	def __init__(self, question,answer):
		self.question = question
		self.answer = answer

	def print_question(self):
		print self.question
	def check_answer(self):
		
		while True:
			answer = raw_input("Answer: ")

			if answer.lower() == self.answer: 
		 		print("Correct!") 
		 		return
			else: 
		 		print("Wrong!")
	 	

# def new_question(self,next_question):
# 	self.question.append(next_question)

#flash_card={"question":"How is a tuple different from a list?","a":"A tuple is the same as a list.","b":"A tuple uses square brackets.","c":"A tuple is immutable."}
QUESTION1=("How is a tuple different from a list?\n\ta. A tuple is the same as a list.\n\tb. A tuple uses square brackets.\n\tc. A tuple is immutable.")  


# #def prompt(card_dict):
# 	question[0] += a[1] += b[2] += c += [3]


flash_card1 = flash_card("How is a tuple different from a list?\n\ta. A tuple is the same as a list.\n\tb. A tuple uses square brackets.\n\tc. A tuple is immutable.","c")
flash_card2 = flash_card
flash_card3	= flash_card
flash_card4	= flash_card
flash_card5 = flash_card

general_list=[flash_card1]*5

print "\tWELCOME TO FLASH PYTHON!\n"


index = 0
while index < len(general_list):
	general_list[index].print_question()
	general_list[index].check_answer()
	


	index += 1


