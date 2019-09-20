import random

def Ask():
	name = input("What is your question\n")
	return name


def Pick_a_random_answer():

	answers = ["It is certain.",
	"It is decidedly so.",
	"Without a doubt.",
	"Yes - definitely.",
	"You may rely on it.",
	"As I see it, yes.",
	"Most likely.",
	"Outlook good.",
	"Yes.",
	"Signs point to yes.",
	"Reply hazy, try again.",
	"Ask again later.",
	"Better not tell you now.",
	"Cannot predict now.",
	"Concentrate and ask again.",
	"Don't count on it.",
	"My reply is no.",
	"My sources say no.",
	"Outlook not so good.",
	"Very doubtful." ]

	answers_number = random.randint(0,19)
	print(answers_number)

	return answers[answers_number]





if __name__ == "__main__":
	print(Ask());
	print(Pick_a_random_answer());
