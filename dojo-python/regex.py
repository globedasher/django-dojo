# Regex Assignment
#
#  .	Matches any character except a new line.
# \w 	Matches any letter or digit.
#  +	The pattern before it can appear 1 or more times.
#  *	The pattern can appear any number of times, including none.
#
#   if re.search(r"a.*a"):
#    print("That string had at least two 'a's in it!")
#   else:
#    print("No more than one 'a' found!")

import re
 
def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna",
            "cannonball", "crybaby", "denver", "embraceable", "facetious",
            "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue",
            "kebab", "kilo", "laundered", "mattress", "millennia", "natural",
            "obsessive", "paranoia", "queen", "rabble", "reabsorb",
            "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable",
            "union", "videotape", "zzzz"]
    return [word for word in words if re.search(regex, word)]

# Print words with v
print(get_matching_words(r"(v)"))
# Print words with double s
print(get_matching_words(r"(ss)"))
# Print words ending with e
print(get_matching_words(r"(e$)"))
# b, any char, then another b
print(get_matching_words(r"(b.b)")) 
# b, at least one char, then another b
print(get_matching_words(r"(b.+b)")) 
# b, any number of char (0), the another b
print(get_matching_words(r"(b.*b)")) 
#print(get_matching_words(r"facetious")) # This is the only word in english
print(get_matching_words(r"(^.\wa*\we*\wi*\wo*\wu.$)"))
# I added "zzzz" to ensure this function works. 
print(get_matching_words(r"([regularexpression])")) 
# Show words with double letters
print(get_matching_words(r"(\w)(\1)"))
