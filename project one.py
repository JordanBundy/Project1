""" A quiz program containing several different topics with no limit to qeuestions to be answered/ added, keeping track of your score. Telling you if you're wrong. """

def main():
    total_score = 0
    #storage of topics and questions in dictionaries
    Questions_Dictionary = {'art': {'Who painted the Mono Lisa?': 'Leonardo Da Vinci', 'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz Lazuli' ,
     'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'Chicago' ,'Which kid\'s TV characters are named after Renaissance artists?' : ' Teenage Mutant Ninja Turtles' ,
      'The graphite in an artist\'s pencil is made of what chemical element?' : 'Carbon'},
      'space': {'Which planet is closest to the sun?' : 'Mercury' , 'Which planet spins in the opposite direction to all the others in the solar system?' : 'Venus' , 'How many moons does Mars have?' : '2' ,
       ' What was the first human-made object to leave the solar system?' : 'Voyager 1' , 'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what?' : 'Meteor'}}
    #list of the topics in the dictionaries and a for loop to add them to it
    topic_list = []
    for topics, dictionaries in Questions_Dictionary.items():
        topic_list.append(topics)

        
        
        
    
    print(topic_list)
    #user selects their topic to quiz from, right now only space works and i think i kind of understand why but i'd like to ask questions about it.
    topic = input('Which of these topics would you like to quiz yourself on? Enter it here: ')
    while topic not in topic_list :
        topic = input('Please enter A topic')
    else:

            #running selected quiz questions from the dictionary
            for i in dictionaries:
                print(i)
                answer = input('Enter your answer: ')
                if answer.lower() == dictionaries[i]:
                    print('Correct')
                    total_score += 1
                else:
                    print('Wrong')

            print('End of quiz!')
            print(f'Your total score on {topic} questions is {total_score} out of {len(dictionaries)}.')

            if total_score == len(dictionaries):
                print('You got all the answers correct!')

      
main()
