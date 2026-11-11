"""Prompt used to generate the Essay-Syntax-Instruct feedback with GPT-3.5-Turbo, kept verbatim.

`{essay}` is replaced with the student essay.
"""

SYNTAX_FEEDBACK_PROMPT = '''
Your objective is to provide feedback on the syntax of the given essay, which a human has written. To achieve this goal, please follow the instructions below:
 
**Essay Evaluation Prompt**
 
** Overall Instructions:**
- First, provide the most constructive, detailed, and precise feedback analyzing the essay sentence by sentence.
- Then include examples (words, sentences, or paragraphs) of all and only identify syntax mistakes and errors in each category.
- Offer suggestions for improvement alongside each example to guide the writer effectively.
- Conclude with overall feedback.
- make a JSON format.
 
*Syntax Categories:*
 
*1. Spelling Errors*
-Identify and provide specific and detailed feedback on any spelling mistakes like omission, insertion, substitution, transposition and grapheme substitution including capitalization errors, to enhance the professionalism and readability of the essay. Include examples for each identified spelling mistake with corrections and suggestions for improvement.
 
 *2. Conjunctions and Connectives*
 - Examine the usage of conjunctions and connecting adverbs like words or phrases that link clauses or sentences, (e.g., and, but, or, so) Provide organized and detailed feedback with examples on their effectiveness in creating logical links between sentences and paragraphs. Include examples demonstrating the correct and incorrect usage of conjunctions and connecting adverbs, along with suggestions for improvement.
 
*3. Modifiers*
-Focus only on the usage of a word, phrase, or clause that modifies - that is, gives information about - another word in the same sentence in the following essay and provide clear bullet-pointed feedback on the usage of adjectives and adverbs that acts as modifiers and misplaced and dangling modifiers. Include examples of misplaced modifiers and suggestions for correction.
 
*4. Prepositions*
-Examine and provide organized and detailed feedback on the usage of a word or group of words used to link nouns, pronouns, and phrases to show direction, time, place, location, and spatial relationships, or introduce an object. Ensure the accurate use of prepositions and maintain clarity and precision in expression. Provide examples of incorrect prepositions and suggestions for correction.
 
*5. Use of Modal Verbs*
-Make sure that the modal verbs are used appropriately in the essay. Provide clear feedback on the accuracy and effectiveness of their usage in expressing possibility, ability, permission, request, likelihood, capacity, suggestion, order, obligation, advice or necessity. Include examples of correct and incorrect usage of modal verbs, along with suggestions for improvement.
 
*6. Punctuation Mistakes*
-Identify and provide specific and detailed feedback on any punctuation errors like misplacing punctuation in a sentence, incorrectly punctuating plural words, and overusing and confusing the uses of different punctuation marks, including commas, periods, semicolons, and other marks, to enhance readability and clarity. Include examples of incorrect punctuation usage with corrections and suggestions for improvement.
 
*7. Articles*
-Provide precise bullet-pointed feedback on the usage of articles that identify a noun as being specific (the) or unspecific (a, an) in this essay. Include examples of incorrect article usage with corrections and suggestions for improvement.
 
*8. Pronouns*
-Identify and provide specific and detailed feedback on a word or a group of words that one may substitute for a noun or a noun phrase. Include examples of ambiguous pronoun usage with corrections and suggestions for improvement.

ESSAY : {essay}
'''
