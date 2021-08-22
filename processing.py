import re
from datetime import date
from rules import elements_list, units_list, exceptions_list, comma_after_list
from rules import british_dictionary, very_dictionary, bad_patterns_dictionary, overused_intro_dictionary


def number_to_words(number):
    '''Convert number into word'''
    if number == 1:
        word = "once"
    elif number == 2:
        word = "twice"
    elif number > 2:
        word = str(number)+" times"
    else:
        word = ''
    return word


def bad_patterns(line, index):
    '''Cross-check with the dictionary of known errors and suggest fixes'''
    mistakes = []
    for word in bad_patterns_dictionary:
        if word in line:
            mistakes.append(f'Line {index + 1}. {bad_patterns_dictionary[word]}')
    return mistakes


def comma_after(line, index):
    '''Check for words that usually have comma after them'''
    mistakes = []
    for word in comma_after_list:
        if word in line:
            mistakes.append(f'Line {index + 1}. Might need a comma after "{word[:-1]}"')
    return mistakes


def phrases_with_very(line, index):
    '''Check for patterns like "very ..." in the dictionary'''
    mistakes = []
    for word in very_dictionary:
        if word in line:
            mistakes.append(f'Line {index + 1}. Consider replacing "{word}" with words like "{very_dictionary[word]}" etc')
    return mistakes


def start_with_numbers(line, index):
    '''Check if a non-empty line starts with a number'''
    mistakes = []
    if len(line) > 5:
        if line[0].isdigit():
            mistakes.append(f'Line {index + 1}. Avoid starting sentences with numbers. Rewrite spelling out the number, e.g. "Five samples..."')
    return mistakes


def figure_references(line, index):
    '''Check for 'Fig.' in the beginning of the line or 'Figure' in the middle'''
    mistakes = []
    if len(line) > 5:
        if 'Fig.' in line[0:4] or 'Figs.' in line[0:4]:
            mistakes.append(f'Line {index + 1}. The word "Fig." in the beginning of a sentence can usually be spelled out, e.g. "Figure 1 shows"')
        if 'Figure ' in line[7:]:
            mistakes.append(f'Line {index + 1}. Most journals prefer shortening the word "Figure" as "Fig." if it is not opening the sentence')
    return mistakes


def numbers_next_to_units(line, index):
    '''Check if units separated or not separated from numbers with a space'''
    mistakes = []
    for number in range(9):
        for unit in units_list:
            if (str(number)+unit in line) and (str(number)+unit+"}" not in line):
                mistakes.append(f'Line {index + 1}. Put a space between the number {number} and the unit {unit}')
        if (str(number)+' %' in line) or (str(number)+' \%' in line):
            mistakes.append(f'Line {index + 1}. Per cent signs "%" should follow numbers without a space, i.e. {number}%')
    return mistakes


def elements(text):
    '''Check how many times chemical elements occur in the text'''
    mistakes = []
    entire_text = ' '.join(text)
    for element in elements_list:
        occurance = entire_text.count(" "+element+" ")
        if occurance > 0 and occurance < 5:
            mistakes.append(f'The element {element} occurs only {number_to_words(occurance)}. Consider using its full name instead of the symbol.')
    return mistakes


def abbreviations(text):
    '''Check how many times abbreviations occur in the text'''
    # Find abbreviations as ALLCAPS or ALLCaPs strings and cut "s" at the ends
    entire_text = ' '.join(text)
    all_abbreviations = re.findall(r"\b(?:[A-Z][a-z]*){2,}", entire_text)
    filtered_abbreviations = []
    for abbreviation in all_abbreviations:
        trimmed_abbreviation = abbreviation[:-1] if abbreviation[-1] == 's' else abbreviation
        filtered_abbreviations.append(trimmed_abbreviation)
    mistakes = []

    # Check how often each abbreviation occurs and comment if less than five
    for unique_abbreviation in set(filtered_abbreviations):
        if (unique_abbreviation not in elements_list) and (unique_abbreviation not in exceptions_list) and (unique_abbreviation not in units_list):
            occurance = filtered_abbreviations.count(unique_abbreviation)
            if occurance > 0 and occurance < 5:
                mistakes.append(f'Abbreviation {unique_abbreviation} occurs only {number_to_words(occurance)}. Since abbreviations are hard to read, consider just spelling it out.')
    return mistakes


def in_conclusions(line, index, text):
    '''Check if we can skip In conclusions because there is already a title Conclusions'''
    mistakes = []
    if ('In conclusion') in line:
        if (('Conclusion' or 'CONCLUSION') in text[index - 1]) or (('Conclusion' or 'CONCLUSION') in text[index - 2]):
            mistakes.append(f'Line {index + 1}. This section seems to be already titled "Conclusions", thus you may omit "In conclusion" at the beginning.')
    return mistakes


def british_spelling(line, index, english):
    '''Check if spelling of some words is american/british'''
    mistakes = []
    if english == 'american':
        for word in british_dictionary:
            if word in line:
                mistakes.append(f'Line {index + 1}. In American English, word "{word}" is spelled as "{british_dictionary[word]}".')
    if english == 'british':
        for word in british_dictionary:
            if british_dictionary[word] in line:
                mistakes.append(f'Line {index + 1}. In British English, word "{british_dictionary[word]}" is spelled as "{word}".')
    return mistakes


def abstract_lenght(text):
    '''Find the abstract, check its length and advise if it's too long'''
    # First search for begin{abstract}. If nothing, search for abstract{
    try:
        entire_text = ' '.join(text)
        pattern = '+++'
        abstract = entire_text.replace("begin{abstract", pattern).split(pattern)
        abstract = abstract[1].replace("end{abstract", pattern).split(pattern)
        abstract = abstract[0][1:-1]
    except:
        abstract = ""
        pass
    if abstract == "":
        for line in text:
            if "abstract{" in line:
                abstract  = line[9:-1]

    # Check the abstract length and comment accordingly
    words = len(abstract.split())
    symbols = len(abstract)
    mistakes = []
    if len(abstract) > 1:
        if words > 150:
            mistakes.append(f"Your abstract has {words} words or {symbols} characters. Many journals limit abstracts by 150 words only. Check if this is within limitations of your journal.")
        elif words < 50:
            mistakes.append(f"Your abstract has only {words} words or {symbols} characters. Seems a bit short.")
        else:
            mistakes.append(f"Your abstract has {words} words or {symbols} characters. It seems fine, but double-check if this is within limitations of your journal.")
    return mistakes


def title_lenght(text):
    '''Find the title, check its length and advise if it's too long'''
    title = ""
    for line in text:
        if "title{" in line:
            title  = line[6:-1]
    words = len(title.split())
    symbols = len(title)
    mistakes = []
    if words > 15 and words > 1:
        mistakes.append(f'Your title has {words} words or {symbols} characters. Consider making it shorter. Some journals limit the title by 15 words only.')
    return mistakes


def references(text):
    '''Find references and check their number and age. Comment if they are too old or too many'''
    # Find all unique references in the text as cite{...}
    entire_text = ' '.join(text)
    all_citations = re.findall(r'cite\{[^\}]+}', entire_text)
    references = []
    for citation in all_citations:
        citation_splitted = citation.split(',')
        for reference in citation_splitted:
            reference = re.sub(r'cite\{', '', reference)
            reference = re.sub(r'\}', '', reference)
            reference = re.sub(r' ', '', reference)
            references.append(reference)
    references = list(set(references))

    # Analyse the age of the references and comment if more than 40% are old
    years = []
    try:
        years = [int(re.findall(r'\d\d\d\d', ref)[0]) for ref in references]
    except:
        pass
    mistakes = []
    if len(years) > 0:
        this_year = int(date.today().year)
        reference_ages = [this_year - year for year in years]
        older_than_ten = 100*len([age for age in reference_ages if age > 10])//len(years)
        older_than_five = 100*len([age for age in reference_ages if age > 5])//len(years)
        if older_than_five > 50 or older_than_ten > 20 :
            mistakes.append(f"Looks like {older_than_five}% of your references are older than five years and {older_than_ten}% are even older than ten years. Mostly old references might signal poor actuality of your work to journal editors. Consider if you can use newer references.")
        if len(references) > 50:
            mistakes.append(f"You have {len(references)} references, while most journals allow maximum of 50. Check the guidelines to see how many your journal allows.")

        # Analyse self-citation. Find authors and cross-check with references.
        all_authors_lines = re.findall(r'\\author[\[\]abcdefg\* ,\d]*{[^}]+}', entire_text)
        names = []
        for author_line in all_authors_lines:
            author_line = re.sub(r'\\author[\[\]abcdefg,\d]*{', '', author_line)
            author_line_splitted = author_line.split(',')
            for each_author in author_line_splitted:
                each_author_splitter = each_author.split(' ')
                for name in each_author_splitter:
                    name = re.sub(r'\}', '', name)
                    name = re.sub(r' ', '', name)
                    names.append(name)
        selfcitations = 0
        for name in names:
            for reference in references:
                if name.upper() in reference.upper():
                    selfcitations += 1
        selfcitation_percentage = 100*selfcitations//len(references)
        if selfcitation_percentage > 0 and selfcitation_percentage < 20:
            mistakes.append(f"At least {selfcitations} out of {len(references)} of your references appears to be self-citations. This is acceptable, but keep it in check.")
        if selfcitation_percentage >= 20:
            mistakes.append(f"At least {selfcitations} out of {len(references)} of your references appears to be self-citations. Consider if you need so many self references, it might not look good.")
    return mistakes


def overcitation(line, index):
    '''Check if there are too many citations in one place'''
    all_citations = re.findall(r'\\cite{[^}]+}', line)
    mistakes = []
    for citation in all_citations:
        number_of_references = len(citation.split(','))
        if number_of_references > 4:
            mistakes.append(f"Line {index}. There are {number_of_references} references in one place. Bloated references neither make the statement stronger nor help the reader. Consider reducing citations or just citing one review instead.")
    return mistakes


def intro_patterns(text):
    '''Check if some introduction words occur too often times'''
    mistakes = []
    entire_text = ' '.join(text)
    for word in overused_intro_dictionary:
        occurance = entire_text.count(word)
        occurance_percentage = occurance/len(entire_text.split(" "))
        if occurance_percentage > 0.0012 and occurance_percentage < 0.002 and occurance > 1:
            mistakes.append(f'Sentences often start with {word}. Try alternatives like {overused_intro_dictionary[word]}.')
        if occurance_percentage > 0.002 and occurance > 1:
            mistakes.append(f'Sentences start with {word} too often. Try alternatives like {overused_intro_dictionary[word]}.')
    return mistakes


def main(text, english):
    '''This is the main function that runs tall checks and returns the results to the web app'''

    # General checks
    results = []
    results += title_lenght(text)
    results += abstract_lenght(text)
    results += references(text)
    results += intro_patterns(text)

    # Checks for each line
    for index, line in enumerate(text):
        results += bad_patterns(line, index)
        results += phrases_with_very(line, index)
        results += in_conclusions(line, index, text)
        results += comma_after(line, index)
        results += figure_references(line, index)
        results += start_with_numbers(line, index)
        results += numbers_next_to_units(line, index)
        results += british_spelling(line, index, english)
        results += overcitation(line, index)

    # Additional checks
    results += elements(text)
    results += abbreviations(text)

    if len(results) == 0:
        results = ["Looks like this text is perfect!"]
    return results
