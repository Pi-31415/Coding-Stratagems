article = "war aggression"

word_list = ['aggression', 'antagonism', 'armed forces', 'arms', 'arms race', 'battle', 
             'belligerency', 'coat of arms', 'combatant', 'competition', 'conflict', 
             'contention', 'contravene', 'difference', 'difference of opinion', 'dispute', 
             'engagement', 'enmity', 'expeditionary', 'fight', 'hostility', 'ill will', 
             'implements of war', 'infringe', 'latent hostility', 'martial', 'militaristic', 
             'munition', 'noncombatant', 'rivalry', 'run afoul', 'soldierlike', 'soldierly', 
             'state of war', 'stress', 'struggle', 'tautness', 'tensity', 'tenseness', 
             'weaponry', 'weapons', 'weapons system', 'war', 'warfare', 'warlike', 'warriorlike']

# Convert all words in the word_list to lowercase
word_list = [word.lower() for word in word_list]

# Convert article to lowercase and split it into a list of words
article_words = article.lower().split()

# Create a dictionary to hold the word frequency for each word in the article
word_frequency = {}

# Iterate over each word in the article_words list and count its frequency
for word in article_words:
    # If the word is in the word_list, increment its frequency
    if word in word_list:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

# Calculate the percentage of each word's frequency and print it out
for word, frequency in word_frequency.items():
    percentage = round(frequency / len(article_words) * 100, 2)
    print(f"'{word}' - {percentage}%")
