
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
	 	

flash_card1 = flash_card("\n\nHow is a tuple different from a list?\n\ta. A tuple is the same as a list.\n\tb. A tuple uses square brackets.\n\tc. A tuple is immutable.","c")
flash_card2 = flash_card("\n\nWhat is debugging?\n\ta. The process of finding and removing any of the three kinds of programming errors.\n\tb. Stepping on insects\n\tc. Debugging is not a thing.","a")
flash_card3	= flash_card("\n\nWhat is a print statement?\n\ta. an instruction that causes the Python interpreter to display a value on the screen.\n\tb. Generates a piece of paper.\n\tc. A statement that creates a new file.","a")
flash_card4	= flash_card("\n\nWhat is a program?	\n\ta. A support group for people who drink to much. \n\tb. A set of instructions that specifies a computation.\n\tc. A workout routine.","b")
flash_card5 = flash_card("\n\nWhich are not python operators?\n\ta. Arithmatic, Comparison, Bitwise\n\tb. Assignment, Logical, Membership, Identity\n\tc. GUI, Algebra, Geometry","c")
flash_card6 = flash_card("\n\nWhat does ** perform?\n\ta. I don't know.\n\tb. Performs exponential calculation on operators.\n\tc. Multiplication","b")
flash_card7 = flash_card("\n\nWhat does % perform?\n\ta. Divides left hand oeprand by right hand operand and returns the remainder.\n\tb. Divides the left hand operand by the right.\n\tc. Changes the calculation to percentage.","a")
flash_card8 = flash_card("\n\nWhat does the operator == do?\n\ta. Syntax error\n\tb.  If the values of two operands are equal, then the condition becomes true. \n\tc. Generates the sum of the two operands.","b")
flash_card9 = flash_card("\n\nWhat does the operator += do?\n\ta.Error\n\tb.Performs exponential calculation\n\tc.It adds right operand to the left operand and assign the result to left operand.","c")
flash_card10 = flash_card("\n\nWhat are membership operators?\n\ta.Test for membership in a sequence, such as strings, lists, or tuples\n\tb.They compare the memory locations of two objects.\n\tc.Tests all operators from highest precedence to lowest.","a")
flash_card11 = flash_card("\n\nWhen can you update a Tuple? \n\ta. On Mondays \n\tb. Duh, you can't tuples are immutable. \n\tc. When you append the tuple.","b")
flash_card12 = flash_card("\n\nWhat does min(tuple) do? \n\ta. Returns item from the tuple with min value. \n\tb. Nothing \n\tc. Creates an empty list.","a")
flash_card13 = flash_card("\n\nWhat does tuple(seq) do? \n\ta. Creates another tuple. \n\tb. Generates a list. \n\tc. Converts a list into a tuple","c")
flash_card14 = 
flash_card15 =
flash_card16 =
flash_card17 =
flash_card18 =
flash_card19 =
flash_card20 =




general_list=[flash_card1,flash_card2,flash_card3,flash_card4,flash_card5,flash_card6,flash_card7,flash_card8,flash_card9,flash_card10,flash_card11,flash_card12,flash_card13]

print "\tWELCOME TO FLASH PYTHON!\n"


index = 0
while index < len(general_list):
	general_list[index].print_question()
	general_list[index].check_answer()
	


	index += 1


