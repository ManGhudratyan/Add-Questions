def read_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def ask_to_add(filename):
    answer = input("Do you want to add a question (yes/no): ")
    if answer.lower() == 'yes':
        question = input('Please write the question: ')

        with open(filename, 'r') as file:
            quest = file.read()
            if question in quest:
                print('Question already exists. Please write another question.')
                return

        answers = input('Please write the answers: ')
        rightAnswer = input('Please write the right answer: ')

        with open(filename, 'a') as file:
            splited = ','.join(answers.split())
            file.write(f'{question}:?{rightAnswer},{splited}\n')
    else:
        print("No new question added.")

def main():
    filename = 'datas.txt'
    data = read_from_file(filename)
    print(data)
    ask_to_add(filename)

if __name__ == "__main__":
    main()

