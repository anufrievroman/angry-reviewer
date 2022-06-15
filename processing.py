import re
from datetime import date

from rules import *


def bad_patterns(line, index):
    '''Cross-check with the dictionary of known errors and suggest fixes'''
    mistakes = []
    for word in BAD_PATTERNS:
        if word in line:
            mistakes.append(f'Line {index + 1}. {BAD_PATTERNS[word]}')
    return mistakes


def comma_after(line, index):
    '''Check for words that usually have comma after them'''
    mistakes = []
    for word in COMMA_AFTER:
        if word in line:
            mistakes.append(
                f'Line {index + 1}. Might need a comma after "{word[:-1]}".')
    return mistakes


def phrases_with_very(line, index):
    '''Check for patterns like "very ..." in the dictionary'''
    mistakes = []
    for word in VERY:
        if word in line:
            mistakes.append(
                f'Line {index + 1}. Consider replacing "{word}" with words like "{VERY[word]}" etc'
            )
    return mistakes


def start_with_numbers(line, index):
    '''Check if a non-empty line starts with a number'''
    # Need to fix this function. It make many false positives if there is a reference list
    mistakes = []
    if line[0].isdigit():
        mistakes.append(
            f'Line {index + 1}. Avoid starting sentences with numbers. Rewrite spelling out the number, e.g. "Five samples..."'
        )
    return mistakes


def figure_references(line, index):
    '''Check for 'Fig.' in the beginning of the line or 'Figure' in the middle'''
    mistakes = []
    if len(line) > 5:
        if 'Fig.' in line[0:4] or 'Figs.' in line[0:4]:
            mistakes.append(
                f'Line {index + 1}. The word "Fig." in the beginning of a sentence can usually be spelled out, e.g. "Figure 1 shows"'
            )
        if 'Figure ' in line[7:]:
            mistakes.append(
                f'Line {index + 1}. Most journals prefer shortening the word "Figure" as "Fig." if it is not opening the sentence.'
            )
    return mistakes


def numbers_next_to_units(line, index):
    '''Check if units separated or not separated from numbers with a space'''
    mistakes = []
    for number in range(9):
        for unit in UNITS:
            if (f'{number}{unit} ' in line) or (f'{number}{unit}.' in line) or (f'{number}{unit},' in line):
                mistakes.append(
                    f'Line {index + 1}. Put a space between the digit {number} and the unit {unit}'
                )
        if (str(number) + ' %' in line) or (str(number) + ' \%' in line):
            mistakes.append(
                f'Line {index + 1}. Percent sign "%" should follow numberals without a space, i.e. {number}%'
            )
    return mistakes


def elements(text):
    '''Check how many times chemical elements occur in the text'''
    mistakes = []
    entire_text = unite_valid_lines(text)
    found_elements = []
    for element in ELEMENTS:
        occurance = entire_text.count(" " + element + " ")
        if 0 < occurance < 5:
            found_elements.append(element)

    # Advise is constructed depending on how many elements were found
    if len(found_elements) == 1:
        mistakes.append(
            f'The symbol {found_elements[0]} occurs only a few times. Since most readers do not know how to read all chemical symbols, just write actual name of the element each time. For example "silicon wafer".'
        )
    if len(found_elements) > 1:
        output_string = found_elements[0]
        found_elements[-1] = ' and ' + found_elements[-1]
        for name in found_elements[1:]:
            output_string += f', {name}'
        mistakes.append(
            f'The symbols {output_string} occur only a few times each. Since most readers do not know how to read all chemical symbols, just write actual names of the elements each time. For example "silicon wafer".'
        )
    return mistakes


def abbreviations(text):
    '''Check how many times abbreviations occur in the text'''
    # Find abbreviations as ALLCAPS or ALLCaPs strings and cut "s" at the ends
    entire_text = unite_valid_lines(text)
    all_abbreviations = re.findall(r"\b(?:[A-Z][a-z]?){2,}", entire_text)
    filtered_abbreviations = []
    for abbreviation in all_abbreviations:
        trimmed_abbreviation = abbreviation[:-1] if abbreviation[-1] == 's' else abbreviation
        filtered_abbreviations.append(trimmed_abbreviation)
    mistakes = []

    # Check how often each abbreviation occurs and comment if less than five
    found_abbreviations = []
    for unique_abbreviation in set(filtered_abbreviations):
        if (unique_abbreviation not in ELEMENTS) and (unique_abbreviation
                not in EXCEPTIONS) and (unique_abbreviation not in UNITS):
            occurance = filtered_abbreviations.count(unique_abbreviation)
            if 0 < occurance < 5:
                found_abbreviations.append(unique_abbreviation)

    # Advise is constructed depending on how many abbreviations were found
    if len(found_abbreviations) == 1:
        mistakes.append(
            f'The abbreviation {found_abbreviations[0]} occurs only a few times. Since abbreviations are hard to decrypt, just spell it out each time. It is easier to read a few words than to search for meanings of abbreviations.'
        )
    if len(found_abbreviations) > 1:
        output_string = found_abbreviations[0]
        found_abbreviations[-1] = ' and ' + found_abbreviations[-1]
        for name in found_abbreviations[1:]:
            output_string += f', {name}'
        mistakes.append(
            f'The abbreviations {output_string} occur only a few times each. Since abbreviations are hard to decrypt, just spell them out each time. It is easier to read a few words than to search for meanings of abbreviations.'
        )
    return mistakes


def in_conclusions(line, index, text):
    '''Check if we can skip In conclusions because there is already a title Conclusions'''
    mistakes = []
    if ('In conclusion') in line:
        if (('Conclusion' or 'CONCLUSION') in text[index - 1]) or (
            ('Conclusion' or 'CONCLUSION') in text[index - 2]):
            mistakes.append(
                f'Line {index + 1}. This section seems to be already titled "Conclusions", thus you may omit "In conclusion" at the beginning.'
            )
    return mistakes


def british_spelling(line, index, english):
    '''Check if spelling of some words is american/british'''
    mistakes = []
    if english == 'american':
        for word in BRITISH:
            if word in line:
                mistakes.append(
                    f'Line {index + 1}. In American English, word "{word}" is spelled as "{BRITISH[word]}".'
                )
    if english == 'british':
        for word in BRITISH:
            if BRITISH[word] in line:
                mistakes.append(
                    f'Line {index + 1}. In British English, word "{BRITISH[word]}" is spelled as "{word}".'
                )
    return mistakes


def abstract_lenght(text):
    '''Find the abstract, check its length and advise if it's too long'''
    # First search for begin{abstract}. If nothing, search for abstract{
    try:
        entire_text = unite_valid_lines(text)
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
                abstract = line[9:-1]

    # Check the abstract length and comment accordingly
    words = len(abstract.split())
    symbols = len(abstract)
    mistakes = []
    if len(abstract) > 1:
        if words > 150:
            mistakes.append(
                f"Your abstract has {words} words or {symbols} characters. Many journals limit abstracts by 150 words only. Check if this is within limitations of your journal."
            )
        elif words < 50:
            mistakes.append(
                f"Your abstract has only {words} words or {symbols} characters. Seems a bit short."
            )
        else:
            mistakes.append(
                f"Your abstract has {words} words or {symbols} characters. It seems fine, but double-check if this is within limitations of your journal."
            )
    return mistakes


def title_lenght(text):
    '''Find the title, check its length and advise if it's too long'''
    title = ""
    for line in text:
        if "title{" in line:
            title = line[6:-1]
    words = len(title.split())
    symbols = len(title)
    mistakes = []
    if 1 < words > 15:
        mistakes.append(
            f'Your title has {words} words or {symbols} characters. Consider making it shorter. Some journals limit the title by 15 words only.'
        )
    return mistakes


def references(text):
    '''Find references and check their number and age. Comment if they are too old or too many'''
    # Find all unique references in the text as cite{...}
    entire_text = unite_valid_lines(text)
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
        older_than_ten = 100 * len([age for age in reference_ages if age > 10]) // len(years)
        older_than_five = 100 * len([age for age in reference_ages if age > 5]) // len(years)
        if older_than_five > 50 or older_than_ten > 20:
            mistakes.append(
                f"Looks like {older_than_five}% of your references are older than five years and {older_than_ten}% are even older than ten years. Mostly old references might signal poor actuality of your work to journal editors. Try to use newer references."
            )
        if len(references) > 50:
            mistakes.append(
                f"You have {len(references)} references, while most journals allow maximum of 50. Check the guidelines to see how many your journal allows."
            )

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
                    if name != '':
                        names.append(name)
        selfcitations = 0
        for name in names:
            for reference in references:
                if name.upper() in reference.upper():
                    selfcitations += 1
        selfcitation_percentage = 100 * selfcitations // len(references)
        if 0 < selfcitation_percentage < 20:
            mistakes.append(
                f"At least {selfcitations} out of {len(references)} references seems to be self-citations. This is acceptable, but keep it in check."
            )
        if selfcitation_percentage >= 20:
            mistakes.append(
                f"At least {selfcitations} out of {len(references)} references seems to be self-citations. Consider if you need so many self-references, it might not look good."
            )
    return mistakes


def overcitation(line, index):
    '''Check if there are too many citations in one place'''
    all_citations = re.findall(r'\\cite{[^}]+}', line)
    mistakes = []
    for citation in all_citations:
        number_of_references = len(citation.split(','))
        if number_of_references > 4:
            mistakes.append(
                f"Line {index}. There are {number_of_references} references in one place. Bloated references neither make the statement stronger nor help the reader. Consider reducing citations or just citing one review instead."
            )
    return mistakes


def intro_patterns(text):
    '''Check if some introduction words occur too often times'''
    mistakes = []
    entire_text = unite_valid_lines(text)
    for word in OVERUSED_INTRO:
        occurance = entire_text.count(word)
        occurance_percentage = occurance / len(entire_text.split(" "))
        if (0.0012 < occurance_percentage < 0.002) and (occurance > 1):
            mistakes.append(
                f'Sentences often start with "{word}". Try alternatives like "{OVERUSED_INTRO[word]}".'
            )
        if occurance_percentage > 0.002 and occurance > 1:
            mistakes.append(
                f'Sentences start with "{word}" too often. Try alternatives like "{OVERUSED_INTRO[word]}".'
            )
    return mistakes


def line_is_valid(line):
    '''Check if the line is not empty and not a Latex comment'''
    validation = False
    if len(line) > 1:
        if line[0] != '%':
            validation = True
    return validation


def unite_valid_lines(text):
    '''Remove lines that are empty or a Latex comment and unite the rest'''
    entire_text = ''
    for line in text:
        if len(line) > 1:
            if line[0] != '%':
                entire_text += line
    return entire_text


def redundancy(line, index):
    '''Check for the redundancies'''
    mistakes = []
    for word in REDUNDANT:
        if word in line:
            mistakes.append(
                f'Line {index + 1}. Replace likely redundant "{word}" with just "{REDUNDANT[word]}".'
            )
    return mistakes


def negatives(line, index):
    '''Check for the negatives'''
    mistakes = []
    for word in NEGATIVES:
        if word in line:
            mistakes.append(
                f'Line {index + 1}. Replace negative "{word}" with a more positive "{NEGATIVES[word]}".'
            )
    return mistakes


def remove_latex_syntax(line):
    '''Remove latex stuff containing dots and long syntax from the line'''
    line = re.sub(r'Fig\.', '', line)
    line = re.sub(r'Figs\.', '', line)
    line = re.sub(r'Eq\.', '', line)
    line = re.sub(r'i\.e\.', '', line)
    line = re.sub(r'et al\.', '', line)
    line = re.sub(r'e\.g\.', '', line)
    line = re.sub(r'vs\.', '', line)
    line = re.sub(r'a\.k\.a\.', '', line)
    line = re.sub(r'\d.\d', '', line)
    line = re.sub(r'\.[^ ]', '', line)
    line = re.sub(r'\\cite{[^}]+}', '', line)
    line = re.sub(r'\\ref{[^}]+}', '', line)
    line = re.sub(r'\$[^\$]+\$', '', line)
    return line


def latex_best_practices(text):
    '''Check if sentences are not on separate lines in LaTeX'''
    mistakes = []
    dots_in_line = 0
    useful_lines = 0
    for line in text:
        if line_is_valid(line):
            line = remove_latex_syntax(line)
            dots_in_line += line.count('.')
            useful_lines += 1
    if dots_in_line / useful_lines > 1.2:
        mistakes.append(
            f'In LaTeX, it is considered a best practice to start each sentence from a new line.'
        )
    return mistakes


def sentence_lenght(line, index):
    '''Check if the sentence is too long'''
    mistakes = []
    line = remove_latex_syntax(line)
    sentences = line.split('.')
    if any([len(sentence) > 240 for sentence in sentences]):
        mistakes.append(
            f'Line {index + 1}. The sentence seems to be too long. Consider shortening or splitting it in two.'
        )
    return mistakes


def it_is_latex_text(text):
    '''Check if this is LaTeX document'''
    entire_text = unite_valid_lines(text)
    it_is_latex_text = (('\\begin{document}' in entire_text)
                        or ('\\documentclass' in entire_text))
    return it_is_latex_text


def absolutes(line, index):
    '''Check for words like 'always' or 'never' but except exceptions'''
    mistakes = []
    for num, word in enumerate(ABSOLUTES):
        not_exception = [
            exception not in line for exception in ABSOLUTES_EXCEPTIONS[num]
        ]
        if (word in line) and all(not_exception):
            mistakes.append(f'Line {index + 1}. {ABSOLUTES[word]}')
    return mistakes


def comparing_absolutes(line, index):
    '''Check if there are comperative absolutes like "nearly infinite"'''
    all_absolutes = re.findall(
        r"((a little( bit)?|almost|astonishingly|completely|exceedingly|extremely|highly|incredibly|more than|nearly|partly|partially|quite|somewhat|totally|unbelievably|very) (dead|disappeared|false|gone|illegal|infinite|invaluable|legal|perfect|pervasive|pregnant|professional|true|whole|vanished))",
        line)
    mistakes = []
    for phrase in all_absolutes:
        phrase = str(phrase[0])
        absolute = phrase.split(" ")[-1]
        mistakes.append(
            f'Line {index + 1}. In "{phrase}" comprative degree is applied to an absolute. Usually, it is either {absolute} or not.'
        )
    return mistakes


def number_of_times(line, index):
    '''Check if there are phrases like "hundreds of times"'''
    mistakes = []

    # Patterns like "thousands of times":
    all_patterns = re.findall(
        r"((millions|hundreds|thousands|dozens) of (times|samples))",
        line)
    for phrase in all_patterns:
        phrase_wrong = str(phrase[0])
        phrase_corrected = phrase_wrong.split(" of ")[0][:-1] + " " + phrase_wrong.split(" of ")[1]
        mistakes.append(
            f'Line {index + 1}. Consider replacing "{phrase_wrong}" with "a few {phrase_corrected}".'
        )

    # Patterns like "thousands meters":
    all_patterns = re.findall(
        r"((millions|hundreds|thousands|dozens) (times|microns|micrometers|meters|hours|people|years))",
        line)
    for phrase in all_patterns:
        phrase_wrong = str(phrase[0])
        phrase_corrected = phrase_wrong.split(" ")[0][:-1] + " " + phrase_wrong.split(" ")[1]
        mistakes.append(
            f'Line {index + 1}. Replace "{phrase_wrong}" with "a {phrase_corrected}".'
        )
    return mistakes


def in_the_name_of_law(line, index):
    '''Check if names of laws mistakenly start with an article'''
    pattern = re.compile("((T|t)he [^ ]*'s (law|distribution|equation|formula|wavelength|rule|limit|theory|radiation))")
    all_matches = pattern.findall(line)
    mistakes = []
    for match in all_matches:
        mistakes.append(f'Line {index + 1}. In "{match[0]}" probably no article "the" is needed.')
    return mistakes


def extreme_quantities(line, index):
    '''Check if adjectives like big or small match the type of quantity'''
    # Quantities that should be high or low:
    pattern = re.compile("(big|large|small) ((conductivity|conductance|resistance|diffusivity)|(thermal|electrical|interface|boundary) (conductivity|conductance|resistance|resistivity|diffusivity)|frequency|value|temperature|concentration|pressure|altitude)")
    all_matches = pattern.findall(line)
    mistakes = []
    for match in all_matches:
        mistakes.append(f'Line {index + 1}. Usually "{match[1]}" is high/low rather than "{match[0]}".')

    # Quantities that should be long or short:
    pattern = re.compile("(big|large|small) (wavelength|lifespan|length|period|time frame|time period|distance|path|mean free path|MFP)")
    all_matches = pattern.findall(line)
    for match in all_matches:
        mistakes.append(f'Line {index + 1}. Usually "{match[1]}" is long/short rather than "{match[0]}".')

    # Quantities that should be wide or narrow:
    pattern = re.compile("(big|large|small) (range|spectrum)")
    all_matches = pattern.findall(line)
    for match in all_matches:
        mistakes.append(f'Line {index + 1}. Usually "{match[1]}" is wide/narrow rather than "{match[0]}".')
    return mistakes


def cliches(line, index):
    '''Check for cliches'''
    mistakes = []
    for phrase in CLICHES:
        if phrase in line:
            mistakes.append(
                f'Line {index + 1}. The phrase "{phrase}" is considered a cliché and should be avoided.'
            )
    return mistakes


def numbers_with_s(line, index):
    '''Check for number ending with 's like in 10's'''
    mistakes = []
    error = re.findall(r"\d's", line)
    if error != []:
        mistakes.append(
            f"Line {index + 1}. Placing 's after a number might be a mistake. For example, these were 2000s with three 0s, and number 0's influence on 2000s' days was clear."
        )
    return mistakes


def difficult_words(text):
    '''Check if there are some complex word with simple synonyms'''
    mistakes = []
    found_words = []
    entire_text = unite_valid_lines(text)
    for word in COMPLEX_WORDS:
        occurance = entire_text.count(word)
        if (occurance > 0):
            found_words.append(word)
    if found_words != []:
        synonyms = ''
        errors = ''
        for word in found_words:
            synonyms += '"' + COMPLEX_WORDS[word] + '", '
            errors += '"' + word + '", '
        mistakes.append(
                f'You used some difficult words like {errors[:-2]}. Try using simple synonyms, like {synonyms[:-2]} because most readers of scientific papers are not native English speakers.'
        )
    return mistakes


def main(text, english='american'):
    '''This is the main function that runs all checks and returns the results'''
    results = []
    # Checks for LaTeX-specific issues:
    if it_is_latex_text(text):
        results += title_lenght(text)
        results += abstract_lenght(text)
        results += references(text)
        results += latex_best_practices(text)

    # General checks:
    results += intro_patterns(text)
    results += elements(text)
    results += abbreviations(text)
    results += difficult_words(text)

    # Checks for each line which is not a comment:
    for index, line in enumerate(text):
        if line_is_valid(line):
            results += bad_patterns(line, index)
            results += phrases_with_very(line, index)
            results += in_conclusions(line, index, text)
            results += comma_after(line, index)
            results += figure_references(line, index)
            # results += start_with_numbers(line, index)
            results += numbers_next_to_units(line, index)
            results += british_spelling(line, index, english)
            results += overcitation(line, index)
            results += redundancy(line, index)
            results += negatives(line, index)
            results += absolutes(line, index)
            results += sentence_lenght(line, index)
            results += comparing_absolutes(line, index)
            results += cliches(line, index)
            results += numbers_with_s(line, index)
            results += in_the_name_of_law(line, index)
            results += extreme_quantities(line, index)
            results += number_of_times(line, index)

    if len(results) == 0:
        results = ["Looks like this text is perfect!"]
    return results


def standalone_run():
    '''This runs program in the standalone regime, just as a python script'''
    path = "your_text.txt"
    with open(path, "r") as manuscript:
        text = manuscript.readlines()
    results = main(text)
    for line in results:
        print(line + "\n")


if __name__ == "__main__":
    standalone_run()
