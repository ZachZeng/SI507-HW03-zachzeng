import random

def Ask():
	while(1):
		answer = "";
		name = input("What is your question\n");
		if(name == "quit"):
			break;
		if(name[len(name)-1] != "?"):
			answer = "I’m sorry, I can only answer questions.";
		else:
			answer = Pick_a_random_answer();
		print(answer);


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

	return answers[answers_number]





if __name__ == "__main__":
	Ask();

