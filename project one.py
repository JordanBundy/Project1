""" A quiz program containing several different topics with no limit to qeuestions to be answered/ added, 
keeping track of your score. Telling you if you're wrong. """

def main():
    total_score = 0
    
    # Single space after # in comments makes them a little more readable
    # storage of topics and questions in dictionaries

    # Use whitespace and new lines for larger dictionaries. Are the art, or the space questions more readable? 
    # Lowercase camelcase for methods, functions, variables.
    questions_dictionary = {
        'art': {         
            'Who painted the Mona Lisa?': 'Leonardo Da Vinci', 
            'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz Lazuli',
            'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'Chicago',
            'Which kid\'s TV characters are named after Renaissance artists?': ' Teenage Mutant Ninja Turtles',
            'The graphite in an artist\'s pencil is made of what chemical element?': 'Carbon'
        },
        'space': {'Which planet is closest to the sun?' : 'Mercury' , 'Which planet spins in the opposite direction to all the others in the solar system?' : 'Venus' , 'How many moons does Mars have?' : '2' ,
       ' What was the first human-made object to leave the solar system?' : 'Voyager 1' , 'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what?' : 'Meteor'}}
    
    # list of the topics in the dictionaries and a for loop to add them to it
    topic_list = []
    for topics, dictionaries in questions_dictionary.items():
        topic_list.append(topics)

    
    print(topic_list)  # can you print this more neatly?

    string_topic_list = ', '.join(topic_list)
    print('Your topic choices are, ')       # explain to the user what they are seeing
    print(string_topic_list)

    #user selects their topic to quiz from, right now only space works and i think i kind of understand why but i'd like to ask questions about it.
    topic = input('Which of these topics would you like to quiz yourself on? Enter it here: ')
    while topic not in topic_list :
        topic = input('That\'s not a choice. Please enter a topic: ') 
    else:

            #running selected quiz questions from the dictionary
            # for i in dictionaries:   # Because of the loop on line 25, the dictionaries variable is always space - the last key-value pair in the dictionary.
            # Can you think of a better variable name than i ?
            questions = questions_dictionary[topic]
            for question, correct_answer in questions.items():  # using items makes the keys and values available in the loop 
                print(question)
                answer = input('Enter your answer: ')
                # There's no way to get the answer correct if the user answer is always converted to lowercase, but the correct answer
                # is "Chicago" or "Leonardo Da Vinci" - a word with uppercase letters. If I enter "Chicago", it's converted to "chicago"
                # and compared to "Chicago" and they will never be equal - "chicago" is not equal to "Chicago". 
                if answer.lower() == correct_answer.lower():  # To fix, convert the correct answer to lowercase too
                    print('Correct')
                    total_score += 1
                else:
                    print('Wrong')  # Also display the correct answer

            print('End of quiz!')
            print(f'Your total score on {topic} questions is {total_score} out of {len(dictionaries)}.')

            if total_score == len(dictionaries):
                print('You got all the answers correct!')

      
main()
