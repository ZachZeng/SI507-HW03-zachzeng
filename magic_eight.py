def Ask():
	while(1):
		answer = "";
		name = input("What is your question\n");
		if(name == "quit"):
			break;
		if(name[len(name)-1] != "?"):
			answer = "I’m sorry, I can only answer questions.";
		print(answer);

if __name__ == "__main__":
	Ask();
