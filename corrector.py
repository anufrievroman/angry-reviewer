YOUR_FILE = "abstract.txt"


def bad_patterns(line, index):
    '''Check in general dictionary of known errors and suggestions of how to fix them'''
    dictionary = {

        # Hype and cliches

        "excellent agreement": "Usually, the agreement is actually not so excellent. Consider replacing with 'good agreement' or better yet quantify the agreement, e.g. 'A agrees with B within 5%'.",
        "excellent fit": "Sometimes the fit is actually not so excellent. Consider quantifying the fit, e.g. 'Line fits the data within 5% of inaccuracy'.",
        "outstanding": "The word 'outstanding' might be considered hype. Consider alternatives, e.g. 'remarkable'.",
        "groundbreaking": "The word 'groundbreaking' might be considered hype. Consider alternatives, e.g. 'remarkable'.",
        "ground breaking": "The word 'groundbreaking' might be considered hype. Consider alternatives, e.g. 'remarkable'.",
        "new ": "If the word 'new' refers to the results or methods, editors and reviewers often dislike such claims. Consider explaining novelty in some other way. Some helpful words are 'innovative', 'original', 'alternative', 'previously unknown'.",
        "novel ": "If the word 'novel' refers to the results or methods, editors and reviewers often dislike such claims. Consider explaining novelty in some other way. Some helpful words are 'innovative', 'original', 'cutting-edge', 'alternative', 'previously unknown'.",
        " prove ": "Phrases about 'prove' should be considered with caution. Strict proof is possible only in math, whereas science usually operates with evidences. Consider replacing with words like 'evidence', 'demonstration', 'confirmation' etc.",
        " proved ": "Phrases about 'prove' should be considered with caution. Strict proof is possible only in math, whereas science usually operates with evidences. Consider replacing with words like 'evidence', 'demonstration', 'confirmation' etc.",
        " proof ": "Phrases about 'proof' should be considered with caution. Strict proof is possible only in math, whereas science usually operates with evidences. Consider replacing with words like 'evidence', 'demonstration', 'confirmation' etc.",
        " proves ": "Phrases about 'proves' should be considered with caution. Strict proof is possible only in math, whereas science usually operates with evidences. Consider replacing with verbs like 'evidence', 'demonstrate', 'confirm' etc.",
        " never ": "The word 'never' could be considered a hype or exaggeration in instances like 'never shown before', thus it is better to avoid such statements. Consider alternatives: 'rarely', 'seldom', 'remains unclear', 'remains challenging'.",
        "certainly": "Consider if this sentence needs the word 'certainly'. According to The Elements of Style: 'Used indiscriminately by some speakers, much as others use very, to intensify any and every statement. A mannerism of this kind, bad in speech, is even worse in writing'.",
        " fact ": "Check if the word 'fact' is actually applied to a fact. According to The Elements of Style: 'Use this word only of matters of a kind capable of direct verification, not of matters of judgment.'",
        "highly": "The word 'highly' rarely highly contributes to reader's understanding. Consider removing it or if important quantifying it.",
        "greatly": "The word 'greatly' rarely greatly contributes to reader's understanding. Consider removing it or if important quantifying it.",
        "literally": "The word 'literally' is often misused to support an exaggeration, which is hardly appropriate for a scientific paper. Consider if its use is appropriate.",
        "literal ": "The word 'literal' is often misused to support an exaggeration, which is hardly appropriate for a scientific paper. Consider if use is appropriate.",
        "One of the most": "Consider rewriting it without 'One of the most'. According to the Elements of Style: 'There is nothing wrong in this; it is simply threadbare and forcible-feeble.'",
        "one of the most": "Consider rewriting it without 'one of the most'. According to the Elements of Style: 'There is nothing wrong in this; it is simply threadbare and forcible-feeble.'",
        "respectively": "Consider if 'respectively' is really necessary. In clear cases, you can omit it, e.g. 'A and B are equal to 1 and 2.'",
        "correspondingly": "Consider if 'correspondingly' is really necessary. In clear cases, you can omit it, e.g. 'A and B are equal to 1 and 2.'",
        "hallmark": "Phrases like 'A is a hallmark of B' are considered a cliche.",
        "paradigm shift": "Phrases like 'paradigm shift' are considered a cliche.",
        "Holy Grail": "Phrases like 'A is the Holy Grail of B' are considered a cliche.",
        "holy grail": "Phrases like 'A is the holy grail of B' are considered a cliche.",
        "best": "If the word 'best' serves here to qualify results or methods, it will be considered a hype and should be avoided. Consider replacing it with 'optimal' or 'reasonable' or just removing it.",
        "Best": "If the word 'best' serves here to qualify results or methods, it will be considered a hype and should be avoided. Consider replacing it with 'optimal' or 'reasonable' or just removing it.",
        "In a nutshell": "In a nutshell, phrases like 'In a nutshell' are a cliche and should be avoided.",
        "in a nutshell": "In a nutshell, phrases like 'in a nutshell' are a cliche and should be avoided.",
        "at the end of the day": "Phrases like 'at the end of the day' are considered a cliche.",
        "At the end of the day": "Phrases like 'At the end of the day' are considered a cliche.",
        "It is known": "It is known that phrases like 'It is known' are often inappropriate. Often it is not known to the readers. Consider rewriting or at least suppling the references.",
        "it is known": "It is known that phrases like 'it is known' are often inappropriate. Often it is not known to the readers. Consider rewriting or at least suppling the references.",
        "It is well known": "It is well known that phrases like 'It is well known' are often inappropriate. Usually, is it not so well known to the readers. Consider rewriting or at least suppling the references.",
        "it is well known": "It is well known that phrases like 'it is well known' are often inappropriate. Usually, is it not so well known to the readers. Consider rewriting or at least suppling the references.",

        # Inconcise expressions

        "by means of": "Usually, 'by means of' can be replaced with shorter 'by' or 'using'.",
        "By means of": "Usually, 'By means of' can be replaced with shorter 'By' or 'Using'.",
        "It is important to note": "Consider replacing long 'It is important to note' with just 'Note'.",
        "In this work": "You may replace 'In this work' with shorter 'Here' or just start with 'We show that'.",
        "In this article": "You may replace 'In this article' with just 'Here, ...' or just start with 'We show that'.",
        "In this paper": "You may replace 'In this article' with just 'Here, ...' or just start with 'We show that'.",
        "In recent years": "Consider replacing 'In recent years' with shorter 'Recently' or more specific 'Since 1999'.",
        "make it possible": "Consider replacing 'make it possible' with shorter 'enable'.",
        "makes it possible": "Consider replacing 'makes it possible' with shorter 'enables'.",
        "Consequently": "Consider replacing 'Consequently' with shorter 'Thus' or 'Hence'.",
        "Therefore": "Consider replacing 'Therefore' with shorter 'Thus' or 'Hence'.",
        "therefore": "Consider replacing 'therefore' with shorter 'thus' or 'hence'.",
        "Nevertheless": "Consider replacing 'Nevertheless' with shorter 'Yet' or 'But'.",
        "For this reason": "Consider replacing 'For this reason' with shorter 'Thus' or 'Hence'.",
        "For these reasons": "Consider replacing 'For these reasons' with shorter 'Thus' or 'Hence'.",
        "similarly": "Consider replacing 'similarly' with 'alike', e.g. 'A and B look alike'.",
        "Similarly": "Consider replacing 'Similarly' with 'Likewise'.",
        "In contrast to": "Consider replacing 'In contrast to' with shorter 'Unlike'.",
        "In contrast with": "Consider replacing 'In contrast with' with shorter 'Unlike'.",
        "Similarly to this": "Consider replacing 'Similarly to this' with shorter 'Likewise'.",
        "Owning to the fact that": "Consider replacing 'Owning to the fact that' with simple 'Since' or 'Because'.",
        "owning to the fact that": "Consider replacing 'owning to the fact that' with simple 'since' or 'because'.",
        "In spite of the fact that": "Consider replacing 'In spite of the fact that' with simple 'Although'.",
        "in spite of the fact that": "Consider replacing 'in spite of the fact that' with simple 'though'.",
        "Despite the fact that": "Consider replacing 'Despite the fact that' with simple 'Although'.",
        "despite the fact that": "Consider replacing 'despite the fact that' with simple 'though'.",
        "Considering the fact that": "Consider replacing 'Considering the fact that' with simple 'Since' or 'Because'.",
        "considering the fact that": "Consider replacing 'considering the fact that' with simple 'since' or 'because'.",
        "Regardless of the fact that": "Consider replacing 'Regardless of the fact that' with simple 'Although'.",
        "regardless of the fact that": "Consider replacing 'regardless of the fact that' with simple 'although'.",
        "With regard to": "Consider replacing 'With regard to' with shorter 'About' or 'Regarding'.",
        "with regard to": "Consider replacing 'with regard to' with shorter 'about' or 'regarding'.",
        "in the neighborhood of": "Consider replacing 'in the neighborhood of' with shorter 'about'.",
        "Given the fact that": "Consider replacing 'Given the fact that' with simple 'Since' or 'Because'.",
        "given the fact that": "Consider replacing 'given the fact that' with simple 'since' or 'because'.",
        "Due to the fact that": "Consider replacing 'Due to the fact that' with simple 'Because'.",
        "due to the fact that": "Consider replacing 'due to the fact that' with simple 'because'.",
        "the fact that": "Consider replacing 'the fact that' with just 'that'.",
        "as to whether": "Consider shortening 'as to whether' as just 'whether'.",
        "In order to": "Consider shortening 'In order to' as just 'To'.",
        "in order to": "Consider shortening 'in order to' as just 'to'.",
        "utilize": "Consider replacing 'utilize' with simple 'use'.",
        "utilise": "Consider replacing 'utilise' with simple 'use'.",
        "conception": "Consider replacing 'conception' with 'concept'.",
        "the ways in which": "Consider replacing 'the ways in which' with simple 'how'.",
        "on the other hand": "In some cases, might be appropriate to replace 'on the other hand' with shorter 'however'.",
        "On the other hand": "In some cases, might be appropriate to replace 'On the other hand' with shorter 'However'.",
        "for the purpose of": "Consider replacing 'for the purpose of' with shorter 'for'.",
        "For the purpose of": "Consider replacing 'For the purpose of' with shorter 'For'.",
        "For the reason that": "Consider replacing 'For the reason that' with shorter 'Because'.",
        "for the reason that": "Consider replacing 'for the reason that' with shorter 'because'.",
        "not only": "If you use a construction 'not only...but also', there might be a better way to phrase it.",
        "in light of the fact that": "Consider replacing 'in light of the fact that' with simple 'because'.",
        "In light of the fact that": "Consider replacing 'In light of the fact that' with simple 'Because'.",
        "indications of": "Rewrite using the verb 'indicate' instead of construction with 'indications of'.",
        "indication of": "Rewrite using the verb 'indicate' instead of construction with 'indications of'.",
        "suggestive of": "Rewrite using the verb 'suggest' instead of construction with 'suggestive of'.",
        "in the event that": "Consider replacing 'in the event that' with simple 'if' or 'when'.",
        "In the event that": "Consider replacing 'In the event that' with simple 'If' or 'when'.",
        "under circumstances in which": "Consider replacing 'under circumstances in which' with simple 'if' or 'when'.",
        "Under circumstances in which": "Consider replacing 'Under circumstances in which' with simple 'If' or 'When'.",
        "on the occasion of": "Consider replacing 'on the occasion of' with simple 'when'.",
        "On the occasion of": "Consider replacing 'On the occasion of' with simple 'When'.",
        "it is crucial that": "Consider rewriting the phrase with 'it is crucial that' using simple 'must' or 'should'.",
        "it is necessary that": "Consider rewriting the phrase with 'it is necessary that' using simple 'must' or 'should'.",
        "it is important that": "Consider rewriting the phrase with 'it is important that' using simple 'must' or 'should'.",
        "is able to": "Consider replacing 'is able to' with simple 'can'.",
        "has the opportunity to": "Consider replacing 'has the opportunity to' with simple 'can'.",
        "have the opportunity to": "Consider replacing 'have the opportunity to' with simple 'can'.",
        "is in a position to": "Consider replacing 'is in a position to' with simple 'can'.",
        "are in a position to": "Consider replacing 'are in a position to' with simple 'can'.",
        "has the capacity for": "Consider replacing 'has the capacity for' with simple 'can'.",
        "have the capacity for": "Consider replacing 'have the capacity for' with simple 'can'.",
        "has the ability to": "Consider replacing 'has the ability to' with simple 'can'.",
        "have the ability to": "Consider replacing 'have the ability to' with simple 'can'.",
        "it is possible that": "Consider rewriting the phrase with 'it is possible that' using simple 'may', 'might', 'can', or 'could'.",
        "It is possible that": "Consider rewriting the phrase with 'It is possible that' using simple 'may', 'might', 'can', or 'could'.",
        "there is a chance that": "Consider rewriting the phrase with 'there is a chance that' using simple 'may', 'might', 'can', or 'could'.",
        "There is a chance that": "Consider rewriting the phrase with 'There is a chance that' using simple 'may', 'might', 'can', or 'could'.",
        "it could happen that": "Consider rewriting the phrase with 'it could happen that' using simple 'may', 'might', 'can', or 'could'.",
        "It could happen that": "Consider rewriting the phrase with 'It could happen that' using simple 'may', 'might', 'can', or 'could'.",
        "the possibility exists": "Consider rewriting the phrase with 'the possibility exists' using simple 'may', 'might', 'can', or 'could'.",
        "The possibility exists": "Consider rewriting the phrase with 'The possibility exists' using simple 'may', 'might', 'can', or 'could'.",
        "prior to": "Consider replacing 'prior to' with simple 'before'.",
        "Prior to": "Consider replacing 'Prior to' with simple 'Before'.",
        "in anticipation of": "Consider replacing 'in anticipation of' with simple 'before'.",
        "In anticipation of": "Consider replacing 'In anticipation of' with simple 'Before'.",
        "subsequent to": "Consider replacing 'subsequent to' with simple 'after'.",
        "at the same time as": "Consider replacing 'at the same time as' with simple 'as'.",
        "At the same time as": "Consider replacing 'At the same time as' with simple 'As'.",
        "simultaneously with": "Consider replacing 'simultaneously with' with simple 'as'.",
        "Simultaneously with": "Consider replacing 'Simultaneously with' with simple 'As'.",
        "facilitate": "Consider replacing verb 'facilitate' with just 'help'.",
        "great many": "Consider replacing 'great many' with just 'many'.",
        "Great many": "Consider replacing 'Great many' with just 'Many'.",
        "large number of": "Consider replacing 'large number of' with just 'many'.",
        "great number of": "Consider replacing 'great number of' with just 'many'.",
        "Great number of": "Consider replacing 'Great number of' with just 'Many'.",
        "Big number of": "Consider replacing 'Big number of' with just 'Many'.",
        "big number of": "Consider replacing 'big number of' with just 'many'.",
        "has the opportunity to": "Consider replacing 'has the opportunity to' with just 'can'.",
        "have the opportunity to": "Consider replacing 'have the opportunity to' with just 'can'.",
        "end result": "Consider replacing 'end result' with just 'result'.",
        "At this point in time": "Consider replacing 'At this point in time' with just 'Now' or 'Today'.",
        "at this point in time": "Consider replacing 'at this point in time' with just 'now' or 'today'.",
        "At this moment in time": "Consider replacing 'At this moment in time' with just 'Now' or 'Today'.",
        "at this moment in time": "Consider replacing 'at this moment in time' with just 'now' or 'today'.",
        "In a case in which": "Consider replacing 'In a case in which' with just 'If' or 'When'.",
        "in a case in which": "Consider replacing 'in a case in which' with just 'if' or 'when'.",
        "by way of": "Consider replacing 'by way of' with just 'by' or 'using'.",
        "As a matter of fact": "Consider replacing 'As a matter of fact' with 'In fact' or just omitting it.",
        "as a matter of fact": "Consider replacing 'as a matter of fact' with 'in fact' or just omitting it.",
        "at all times": "Consider replacing 'at all times' with shorter 'always'.",
        "In the absence": "Consider replacing 'In the absence' with 'Without'.",
        "in the absence": "Consider replacing 'in the absence' with 'without'.",
        "Because of the fact that": "Consider replacing 'Because of the fact that' with just 'Because'.",
        "because of the fact that": "Consider replacing 'because of the fact that' with just 'because'.",
        "we believe": "Consider writing what you believe directly, without starting with 'we believe'.",
        "We believe": "Consider writing what you believe directly, without starting with 'We believe'.",
        "I believe": "Consider writing what you believe directly, without starting with 'I believe'.",
        "would like to": "Consider removing 'would like to' and writing the next verb directly, e.g. 'We (would like to) emphasize that'",
        "At the temperature of": "Consider shortening 'At the temperature of' to just value, e.g. 'At 4 K'.",
        "At temperature of": "Consider shortening 'At temperature of' to just value, e.g. 'At 4 K'.",
        "at the temperature of": "Consider shortening 'at the temperature of' to just value, e.g. 'At 4 K'.",
        "at temperature of": "Consider shortening 'at temperature of' to just value, e.g. 'at 4 K'.",
        "along the lines of": "Consider replacing 'along the lines of' with shorter 'like'.",
        "majority of": "Consider replacing 'majority of' with shorter 'most'.",
        "adequate number of": "Consider replacing 'adequate number of' with shorter 'enough'.",
        "give an indication": "Consider replacing 'give an indication' with shorter 'show'.",
        "gives an indication": "Consider replacing 'gives an indication' with shorter 'shows'.",
        "has an effect on": "Consider replacing 'has an effect on' with shorter 'affects'.",
        "have an effect on": "Consider replacing 'have an effect on' with shorter 'affect'.",
        "have a tendency": "Consider replacing 'have a tendency' with shorter 'tend'.",
        "has a tendency": "Consider replacing 'has a tendency' with shorter 'tends'.",
        "has the capacity to": "Consider replacing 'has the capacity to' with shorter 'can'.",
        "have the capacity to": "Consider replacing 'have the capacity to' with shorter 'can'.",
        "on a daily basis": "Consider replacing 'on a daily basis' with shorter 'daily'.",
        "have a preference for": "Consider replacing 'have a preference for' with shorter 'prefer'.",
        "has a preference for": "Consider replacing 'has a preference for' with shorter 'prefers'.",
        "had a preference for": "Consider replacing 'had a preference for' with shorter 'preferred'.",

        # Negatives

        "not able": "Consider replacing negative 'not able' with more positive 'unable'.",
        "not different": "Consider replacing negative 'not different' with more positive 'alike'.",
        "did not accept": "Consider replacing negative 'did not accept' with more positive 'rejected'.",
        "does not accept": "Consider replacing negative 'does not accept' with more positive 'rejects'.",
        "do not accept": "Consider replacing negative 'do not accept' with more positive 'reject'.",
        "did not consider": "Consider replacing negative 'did not consider' with more positive 'ignored'.",
        "have not considered": "Consider replacing negative 'have not considered' with more positive 'ignored'.",
        "has not considered": "Consider replacing negative 'has not considered' with more positive 'ignored'.",
        "do not considered": "Consider replacing negative 'do not considered' with more positive 'ignore'.",
        "do not allow": "Consider replacing negative 'do not allow' with more positive 'prevent'.",
        "did not allow": "Consider replacing negative 'did not allow' with more positive 'prevented'.",
        "does not allow": "Consider replacing negative 'does not allow' with more positive 'prevents'.",
        "does not have": "Consider replacing negative 'does not have' with more positive 'lacks'.",
        "do not have": "Consider replacing negative 'do not have' with more positive 'lack'.",
        "did not have": "Consider replacing negative 'did not have' with more positive 'lacked'.",

        # Redundant words

        "necessary requirements": "Consider replacing redundant 'necessary requirements' with just 'requirements'.",
        "necessary requirement ": "Consider replacing redundant 'necessary requirement' with just 'requirement'.",
        "smaller in size": "Consider replacing redundant 'smaller in size' with just 'smaller'.",
        "larger in size": "Consider replacing redundant 'larger in size' with just 'larger'.",
        "bigger in size": "Consider replacing redundant 'bigger in size' with just 'bigger'.",
        "most unique": "Consider replacing redundant 'most unique' with just 'unique'.",
        "resultant effect": "Consider replacing redundant 'resultant effect' with just 'result'.",
        "end result": "Consider replacing redundant 'end result' with just 'result'.",
        "pooled together": "Consider replacing redundant 'pooled together' with just 'pooled'.",
        "joined together": "Consider replacing redundant 'joined together' with just 'joined'.",
        "fewer in number": "Consider replacing redundant 'fewer in number' with just 'fewer'.",
        "exactly the same": "Consider replacing redundant 'exactly the same' with just 'the same'.",
        "repeat again": "Consider replacing redundant 'repeat again' with just 'repeat'.",
        "repeated again": "Consider replacing redundant 'repeated again' with just 'repeated'.",
        "revert back": "Consider replacing redundant 'revert back' with just 'revert'.",
        "reverted back": "Consider replacing redundant 'reverted back' with just 'reverted'.",
        "shorter in length": "Consider replacing redundant 'shorter in length' with just 'shorter'.",
        "longer in length": "Consider replacing redundant 'longer in length' with just 'longer'.",
        "summarize briefly": "Consider replacing redundant 'summarize briefly' with just 'summarize'.",
        "briefly summarize": "Consider replacing redundant 'briefly summarize' with just 'summarize'.",
        "a total of": "In phrases like 'a total of ten samples', you can just write 'Ten samples'.",
        "A total of": "In phrases like 'A total of ten samples', you can just write 'Ten samples'.",
        "close proximity": "Consider replacing redundant 'close proximity' with just 'proximity'.",
        "each and every": "Consider replacing redundant 'each and every' with just 'each'.",
        "Each and every": "Consider replacing redundant 'Each and every' with just 'Each'.",
        "make a study of": "Consider replacing 'make a study of' with just 'study'.",
        "made a study of": "Consider replacing 'made a study of' with just 'studied'.",
        "conduct an investigation of": "Consider replacing 'conduct an investigation of' with just 'investigate'.",
        "conduct investigation of": "Consider replacing 'conduct investigation of' with just 'investigate'.",
        "conduct the investigation of": "Consider replacing 'conduct the investigation of' with just 'investigate'.",
        "conducted an investigation of": "Consider replacing 'conducted an investigation of' with just 'investigated'.",
        "conducted investigation of": "Consider replacing 'conducted investigation of' with just 'investigated'.",
        "conducted the investigation of": "Consider replacing 'conducted the investigation of' with just 'investigated'.",

        # Overused words

        "clearly": "The word 'clearly' is clearly overused in science and often points to things that actually aren't so clear. Consider removing it.",
        "clear ": "The word 'clear' is overused in science and often points to things that actually aren't so clear. Consider if it is necessary here.",
        "obviously": "The word 'obviously' is often misused in science and might describe something that is not so obvious. Consider removing it.",
        "Obviously": "The word 'Obviously' is often misused in science and might describe something that is not so obvious. Obviously, consider removing it.",
        "Basically": "The word 'Basically' is basically not very appropriate for academic writing. Basically, consider removing it.",
        "basically": "The word 'basically' is basically not very appropriate for academic writing. Basically, consider removing it.",
        "obvious ": "The word 'obvious' is often misused in science and might describe something that is not so obvious. It also annoys readers. Consider removing it.",
        "strongly": "The word 'strongly' is often strongly misused to describe not so strong things. Consider removing it and expressing the strength quantitatively, e.g. '50% stronger' or 'increased by 50%'.",
        "strong ": "The word 'strong' is often misused to describe not so strong things. Consider if the usage here is appropriate.",
        "significantly": "The word 'significantly' is often significantly misused in science. It might mean statistically significant or significant to the author, so the meaning is unclear. Consider removing it and describe significance quantitatively, e.g. 'increased by 50%' or '50% different'. Other alternatives: 'substantially, notably'",
        "significant ": "The word 'significant' is often misused in science. It might mean statistically significant or significant to the author, so the meaning is unclear. Consider removing it and writing about significance more quantitatively, e.g. 'by 50%'. Other alternatives: 'substantial, notable'",
        "This shows": "It might be unclear what 'This' points to if previous phrase was complicated. Rewrite with more specific subject, e.g. 'This data show', 'This dependence shows' etc.",
        "This demonstrates": "It might be unclear what 'This' points to if previous phrase was complicated. Rewrite with more specific subject, e.g. 'This data show', 'This dependence shows' etc.",
        "This proves": "It might be unclear what 'This' points to if previous phrase was complicated. Rewrite with more specific subject, e.g. 'This experiment proves'.",
        "This is": "It might be unclear what 'This is' points to if previous phrase was complicated. Rewrite with more specific subject, e.g. 'This result is'.",
        "This leads": "It might be unclear what 'This leads' points to if previous phrase was complicated. Rewrite with more specific subject, e.g. 'This result leads'.",
        "et al ": "Needs period after 'et al', i.e. 'et al.'.",
        " while": "Usually, it is better to replace 'while' with 'whereas', unless something is really happening at the same time.",
        ", while": "Constructions like 'A is white, while B is red' can be simplified as 'A is white; B is red.'",
        "e.g. ": "In American English 'e.g.' should be followed by a comma.",
        "i.e. ": "In American English 'i.e.' should be followed by a comma.",

        # Random rules

        "less then": "Probably 'then' should be changed to 'than' if this is a comparison.",
        "more then": "Probably 'then' should be changed to 'than' if this is a comparison.",
        "higher then": "Probably 'then' should be changed to 'than' if this is a comparison.",
        "lower then": "Probably 'then' should be changed to 'than' if this is a comparison.",
        "bigger then": "Probably 'then' should be changed to 'than' if this is a comparison.",
        "smaller then": "Probably 'then' should be changed to 'than' if this is a comparison.",
        "larger then": "Probably 'then' should be changed to 'than' if this is a comparison.",
        " 0 ": "Simple numbers 0-10 are better to be spelled out, e.g. 'five samples', 'above zero', 'equal to one'.",
        "not important": "Consider using a more positive form and replace 'not important' with 'unimportant' or 'trifling'.",
        "and/or": "Try to say it without 'and/or'. Often, just 'and' or 'or' is enough.",
        "or/and": "Try to say it without 'or/end'. Often, just 'and' or 'or' is enough.",
        "generate ": "Verify that the verb 'generate' really describes a generation process. Otherwise, consider replacing it with 'cause'.",
        "generated": "Verify that the verb 'generated' really describes a generation process. Otherwise, consider replacing it with 'caused'.",
        "generating": "Verify that 'generating' really describes a generation process. Otherwise, consider replacing it with 'causing'.",
        "In conclusions": "Correct as 'In conclusion'.",
        " the the ": "Seems like 'the' is repeated twice,",
        " a a ": "Seems like 'a' is repeated twice,",
        " an an ": "Seems like 'a' is repeated twice,",
        "Dr.": "Full stop is not required after Dr, i.e. just 'Dr Smith' is fine.",
        "Mr.": "Full stop is not required after Mr, i.e. just 'Mr Smith' is fine.",
        "Ms.": "Full stop is not required after Ms, i.e. just 'Ms Smith' is fine.",
        "Co.": "Full stop is not required after Co, i.e. just 'and Co' is fine.",

        # Referring to figures

        " fig.": "Most journals prefer capitalized references to figures, e.g. 'as shown in Fig. 1'.", 
        " figs.": "Most journals prefer capitalized references to figures, e.g. 'as shown in Figs. 1-2'.", 
        "[Fig": "Most journals prefer regular brackets for figure references, e.g. (Fig. 1).", 
        "(see Fig": "You can omit the word 'see' in the figure reference, e.g. (Fig. 1).", 
        "(see fig": "You can omit the word 'see' in the figure reference, e.g. (Fig. 1).", 

        # Shortened units

        "thousands of K ": "Consider spelling our the units as kelvin",
        "hundreds of K ": "Consider spelling our the units as kelvin",
        "tens of K ": "Consider spelling our the units as kelvin",
        "few K ": "Consider spelling our the units as kelvin",
        "several K ": "Consider spelling our the units as kelvin",
        "thousands of µm": "Consider spelling out the units as micrometeres",
        "hundreds of µm": "Consider spelling out the units as micrometeres",
        "tens of µm": "Consider spelling out the units as micrometeres",
        "few µm": "Consider spelling out the units as micrometeres",
        "several µm": "Consider spelling our the units as micrometeres",
        "thousands of nm": "Consider spelling our the units as nanometers instead of nm",
        "hundreds of nm": "Consider spelling our the units as nanometers instead of nm",
        "tens of nm": "Consider spelling our the units as nanometers instead of nm",
        "few nm": "Consider spelling our the units as nanometers instead of mm",
        "several nm": "Consider spelling our the units as nanometers instead of nm",
        "thousands of mm": "Consider spelling our the units as milimeters instead of mm",
        "hundreds of mm": "Consider spelling our the units as milimeters instead of nm",
        "tens of mm": "Consider spelling our the units as milimeters instead of mm",
        "few mm": "Consider spelling our the units as milimeters instead of mm",
        "several mm": "Consider spelling our the units as milimeters instead of mm",

        # Passive voice

        "has been observed": "Consider rewriting the sentence with 'has been observed' in active voice, e.g. 'we observed that'.",
        "have been observed": "Consider rewriting the sentence with 'have been observed' in active voice, e.g. 'we observed that'.",
        "have been demonstrated": "Consider rewriting the sentence with 'have been demonstrated' in active voice, e.g. 'we demonstrated that'.",
        "has been demonstrated": "Consider rewriting the sentence with 'has been demonstrated' in active voice, e.g. 'we demonstrated that'.",
        "has been shown": "Consider rewriting the sentence with 'has been shown' in active voice, e.g. 'we showed that'.",
        "have been shown": "Consider rewriting the sentence with 'have been shown' in active voice, e.g. 'we showed that'.",
        "have been investigated": "Consider rewriting the sentence with 'have been investigated' in active voice, e.g. 'researchers investigated the effect'.",
        "has been investigated": "Consider rewriting the sentence with 'has been investigated' in active voice, e.g. 'researchers investigated the effect'.",
        "have been studied": "Consider rewriting the sentence with 'have been studied' in active voice, e.g. 'researchers studied the effect'.",
        "has been studied": "Consider rewriting the sentence with 'has been studied' in active voice, e.g. 'researchers studied the effect'.",

        "was observed": "Consider rewriting the sentence with 'was observed' in active voice, e.g. 'we observed that'.",
        "were observed": "Consider rewriting the sentence with 'were observed' in active voice, e.g. 'we observed that'.",
        "were demonstrated": "Consider rewriting the sentence with 'were demonstrated' in active voice, e.g. 'we demonstrated that'.",
        "was demonstrated": "Consider rewriting the sentence with 'was demonstrated' in active voice, e.g. 'we demonstrated that'.",
        "was shown": "Consider rewriting the sentence with 'was shown' in active voice, e.g. 'we showed that'.",
        "were shown": "Consider rewriting the sentence with 'were shown' in active voice, e.g. 'we showed that'.",
        "were investigated": "Consider rewriting the sentence with 'were investigated' in active voice, e.g. 'researchers investigated the effect'.",
        "was investigated": "Consider rewriting the sentence with 'was investigated' in active voice, e.g. 'researchers investigated the effect'.",
        "were studied": "Consider rewriting the sentence with 'were studied' in active voice, e.g. 'researchers studied the effect'.",
        "was studied": "Consider rewriting the sentence with 'was studied' in active voice, e.g. 'researchers studied the effect'.",
        "has been attracting a great attention": "Attracted attention is not necessarily a good motivation for research. Consider a stronger motivation.",
        "has attracted a great attention": "Attracted attention is not necessarily a good motivation for research. Consider a stronger motivation.",
        "have attracted a great attention": "Attracted attention is not necessarily a good motivation for research. Consider a stronger motivation.",
        "has attracted great attention": "Attracted attention is not necessarily a good motivation for research. Consider a stronger motivation.",
        "have attracted great attention": "Attracted attention is not necessarily a good motivation for research. Consider a stronger motivation.",
        "has attracted attention": "Attracted attention is not necessarily a good motivation for research. Consider a stronger motivation.",
        "have attracted attention": "Attracted attention is not necessarily a good motivation for research. Consider a stronger motivation.",

        # Inappropriate language

        "it's": "If you mean 'it is', it's better to just write 'it is'. Otherwise, it might need to be corrected as 'its', for example 'material and its properties'.",
        "kind of": "Consider kind of replacing 'kind of' with 'rather' or kind of avoiding it completely.",
        "sort of": "Consider sort of replacing 'sort of' with 'rather' or sort of avoiding it completely.",
        " less ": "Verify that 'less' is not misused for 'fewer' (e.g. 'less time', but 'fewer samples') or cannot be replace with a more precise word like 'thinner', 'shorter', 'weaker' etc.",
        " very ": "Consider if the word 'very' is very very necessary. If emphasis is necessary, use words strong in themselves or quantify the statement.",
        "viewpoint": "Consider replacing with 'point of view'.",
        "don't": "Most academic journals prefer 'do not' instead of 'don't'.",
        "isn't": "Most academic journals prefer 'is not' instead of 'isn't'.",
        "wasn't": "Most academic journals prefer 'was not' instead of 'wasn't'.",
        "doesn't": "Most academic journals prefer 'does not' instead of 'doesn't'.",
        "wouldn't": "Most academic journals prefer 'would not' instead of 'wouldn't'.",
        "shouldn't": "Most academic journals prefer 'should not' instead of 'shouldn't'.",
        "it is": "Avoid constructions with 'it is', since they obscure the main subject and action of a sentence.",
        "there is": "Avoid constructions with 'there is', since they obscure the main subject and action of a sentence.",
        "there are": "Avoid constructions with 'there are', since they obscure the main subject and action of a sentence.",
        "It is": "Avoid constructions with 'It is', since they obscure the main subject and action of a sentence.",
        "There is": "Avoid constructions with 'There is', since they obscure the main subject and action of a sentence.",
        "There are": "Avoid constructions with 'There are', since they obscure the main subject and action of a sentence.",
        "Actually": "The word 'Actually' might actually be unnecessary.",
        "actually": "The word 'actually' might actually be unnecessary.",
        "really": "The word 'really' might be really unnecessary.",
        "years": "Instead of 'years', it might be better to give the exact year of event.",
        "a bit ": "Consider replacing informal 'a bit' with a bit more formal 'somewhat' or removing it completely.",
        "a lot of": "Consider replacing 'a lot of' with 'many' or 'several', or just give exact number.",
        "A lot of": "Consider replacing 'A lot of' with 'Many' or 'Several', or just give exact number.",
        "You ": "Using 'You' might be inappropriate in academic writing. Consider using 'One', e.g. 'One can see...'.",
        "you ": "Using 'you' might be inappropriate in academic writing. Consider using 'One', e.g. 'One can see...'.",
        "And": "Instead of starting this sentence with 'And' try just removing it.",
        " things": "The word 'things' is rather vague, try to be more specific.",
        " thing": "The word 'thing' is rather vague, try to be more specific.",
        "Dear Editor": "Consider to address your dear editor by the real name.",
        "Dear editor": "Consider to address your dear editor by the real name.",
        "Firstly": "In modern English 'First' is preferred to 'Firstly'.",
        "firstly": "In modern English 'first' is preferred to 'firstly'.",
        "Secondly": "In modern English 'Second' is preferred to 'Secondly'.",
        "secondly": "In modern English 'second' is preferred to 'secondly'.",
        "diminish ": "If by 'diminish' you mean that something is decreasing, consider replacing with 'decrease'.",
        "diminishing ": "If by 'diminishing' you mean that something is decreasing, consider replacing with 'decreasing'.",
        "diminished ": "If by 'diminished' you mean that something is decreasing, consider replacing with 'decreased'.",
        "So,": "Beginning with 'So' might seem so informal. So, consider replacing it with 'Thus,'.",
        "So ": "Beginning with 'So' might seem so informal. So, consider replacing it with 'Thus'.",
        "By the way": "'By the way' might seem too informal.",

        # Latin expressions

        "radiuses": "Preferably replace 'radiuses' with 'radii'.",
        "axises": "Correct 'axises' as 'axes'.",
        "thesises": "Correct 'thesises' as 'theses'.",
        "bacteriums": "Correct 'bacteriums' as 'bacteria'.",
        "erratums": "Correct 'erratums' as 'errata'.",
        "ab initio ": "Consider if your readers know the Latin expressions 'ab initio'. Consider replacing with 'from first principles' or similar.",
        "in vitro ": "Consider if your readers know the Latin expressions 'in vitro' or if there might be a more common term.",
        "in vivo ": "Consider if your readers know the Latin expressions 'in vivo' or if there might be a more common term.",
        "e.g.": "Consider if your readers know the Latin expressions 'e.g.'. It might be better to write 'for example'.",
        "i.e.": "Consider if your readers know the Latin expressions 'i.e.'. It might be better to write 'that is'.",
        "in silico ": "Consider if your readers know the Latin expressions 'in silico' or if there might be a more common term.",
        "in utero": "Consider if your readers know the Latin expressions 'in utero' or if there might be a more common term.",
        "in situ ": "Consider if your readers know the Latin expressions 'in situ' or if there might be a more common term.",
        "ex vivo ": "Consider if your readers know the Latin expressions 'ex vivo' or if there might be a more common term.",
        "vs.": "Consider if your readers know the Latin expressions 'vs.'. It might be better to replace with 'against' or 'as a function of'.",
        "a.k.a.": "Consider replacing 'a.k.a.' with 'also known as' for clarity.",
        " aka ": "Consider replacing 'aka' with 'also known as' for clarity.",
    }
    for word in dictionary:
        if word in line:
            output(str("Line " + str(index + 1) + ". " + dictionary[word] + ""))


def comma_after(line, index):
    '''Check for words that usually have comma after them.'''
    dictionary = [
        "However ",
        "Therefore ",
        "Thus ",
        "Yet ",
        "Hence ",
        "Nevertheless ",
        "But ",
        "In this work ",
        "In this article",
        "In this paper ",
        "In this case ",
        "In that case ",
        "Moreover ",
        "In addition ",
        "Consequently ",
        "So ",
        "In conclusion ",
        "In conclusions ",
        "Particularly ",
        "Specifically ",
        "For this reason ",
        "For these reasons ",
        "On the other hand ",
        "On the one hand ",
        "On one hand ",
        ]
    for word in dictionary:
        if word in line:
            output("Line " + str(index + 1) + ". Might need a comma after " + word + "")


def phrases_with_very(line, index):
    dictionary = {
        "very precise": "precise, exact, unimpeachable, perfect, flawless",
        "very basic": "rudimentary, primary, fundamental, simple",
        "very capable": "efficient, proficient, skillful",
        "very clean": "spotless, immaculate, stainless",
        "very clear": "transparent, sheer, translucent",
        "very competitive": "ambitious, driven, cutthroat",
        "very confident": "self-assured, self-reliant, secure",
        "very consistent": "constant, unfailing, uniform, same",
        "very conventional": "conservative, common, predictable, unoriginal",
        "very critical": "vital, crucial, essential, indispensable, integral",
        "very dangerous": "perilous, precarious, unsafe",
        "very dark": "black, inky, ebony, sooty, lightless",
        "very deep": "abysmal, bottomless, vast",
        "very delicate": "subtle, slight, fragile, frail", "very different": "unusual, distinctive, atypical, dissimilar",
        "very difficult": "complicated, complex, demanding",
        "very easy": "effortless, uncomplicated, unchallenging, simple",
        "very fast": "rapid, swift, fleet, blistering",
        "very few": "meager, scarce, scant, limited, negligible",
        "very good": "superb, superior, excellent",
        "very important": "crucial, vital, essential, paramount, imperative",
        "very impressive": "extraordinary, remarkable",
        "very interesting": "fascinating, remarkable, riveting, compelling",
        "very large": "huge, giant",
        "very long": "extended, extensive, interminable, protracted",
        "very new": "innovative, fresh, original, cutting-edge",
        "very obvious": "apparent, evident, plain, visible",
        "very reasonable": "equitable, judicious, sensible, practical, fair",
        "very recent": "the latest, current, fresh, up-to-date",
        "very rough": "coarse, jagged, rugged, craggy, gritty, broken",
        "very severe": "acute, grave, critical, serious, brutal, relentless",
        "very significant": "key, notable, substatial, noteworthy, momentous, major, vital",
        "very similar": "alike, akin, analogous, comparable, equivalent",
        "very simple": "easy, straightforward, effortless, uncomplicated",
        "very small": "tiny, miniscule, infinitesimal, microscopic, wee",
        "very smooth": "flat, glassy, polished, level, even, unblemished",
        "very specific": "precise, exact, explicit, definite, unambiguous",
        "very strange": "weird, eerie, bizarre, uncanny, peculiar, odd",
        "very strict": "stern, austere, severe, rigorous, harsh, rigid",
        "very substantial": "considerable, significant, extensive, ample",
        "very unlikely": "improbable, implausible, doubtful, dubious",
        "very unusual": "abnormal, extraordinary, uncommon, unique",
        "very visible": "conspicuous, exposed, obvious, prominent",
        "very weak": "feeble, frail, delicate, debilitated, fragile",
        "very wide": "vast, expansive, sweeping, boundless",
        }
    for word in dictionary:
        if word in line:
            output(str(
                "Line " + str(index + 1) + ". Consider replacing '" + word + "' with words like " + dict_very[
                    word] + " etc."))


def start_with_numbers(line, index):
    '''Check if the sentence starts with a number'''
    if line[0].isdigit():
        output("Line " + str(index + 1) + ". Avoid starting sentences with numbers. Rewrite spelling out the number, e.g. 'Five samples...'")


def figure_references(line, index):
    '''Check for "Fig." in the beginning of the line or "Figure" in the middle'''
    if "Fig." in line[0:4] or "Figs." in line[0:4]:
        output(str("Line " + str(index + 1) + ". The word Fig. in the beginning of a sentence can usually be spelled out, e.g. 'Figure 1 shows...'."))
    if "Figure " in line and "Figure " not in line[0:4]:
        output("Line " + str(index + 1) + ". Most journals prefer shortening the word Figure as Fig. if it is not opening the sentence.")


def numbers_next_to_units(line, index):
    '''Check if there are units not separated from numbers with a space or % sign is separated'''
    units = ['m.', 'm ', 'mm', 'um', 'nm', 'km', 'cm', 'W', 'V', 'K', 's ', 's.', 'ps', 'us', 'Pa', 'min', 'h', 'Hz', 'GHz', 'THz', 'MHz', 'g'] 
    for number in range(9): 
        for unit in units: 
            if str(number)+unit in line:
                output("Line " + str(index + 1) + ". Put a space between the number " + str(number) + " and the unit " + unit + ".")
        if str(number)+" %" in line:
            output("Line " + str(index + 1) + ". Per cent signs '%' should follow numbers without a space, i.e. " + str(number) + "%.")


def elements(text):
    '''Check how many times chemical elements occur in the text'''
    elements = [" Al ", " Si ", " Cr ", " Ga ", " Ti ", " InP ", " GaAs ", " SiC ", " Cu ", " He ",
                     " Li ", " Ne ", " Na ", " Cl ", " Ar ", " Au ", " VO2 ", " Sc ", " Fe ", " Nb ", " Ni ", 
                     " Sr ", " Zr ", " Ag ", " Ta ", " Pt ", " Hg ", " U ", " O2 ", " H2O ", " Sn ", " Sb ",
                     " SiN ", " SiO2 ", " H ", " N ", " GaN ", " InP ", " InAs ", " SiO$_2$ "]
    for element in elements:
        occurance = 0
        for index, line in enumerate(text):
            occurance += line.count(element)
        if occurance == 1:
            output("The element" + str(element) + "occurs only once. Consider using its full name instead of the symbol." + "")
        if occurance > 1 and occurance < 4:
            output("The element" + str(element) + "occurs only " + str(occurance) + " times. Consider using its full name instead of the symbol." + "")


def abbreviations(text):
    '''Check how many times common abbreviations occur in the text'''
    abbreviations = ["MFP", "TC", "TDTR", "TEM", "AFM", "SEM", "SPP", "SPhP", "XRD",
            "DOS", "CNT", "NW", "PnC", "RMS", "BG", "SAW", "AMM", "RF", "NP",
            "BTU", "1D", "2D", "3D", "HD", "LOC", "JSAP", "PL", "BLS", "RIE",
            "EBL", "FIB", "MFP"]
    for abbreviation in abbreviations:
        occurance = 0
        for index, line in enumerate(text):
            occurance += line.count(abbreviation)
        if occurance == 1:
            output("The abbreviation " + str(abbreviation) + " occurs only once. Since abbreviations are hard to read, consider just spelling it out." + "")
        if occurance > 1 and occurance < 5:
            output("The abbreviation " + str(abbreviation) + " occurs only " + str(occurance) + " times. Because abbreviations are hard to read, consider just spelling it out." + "")


def in_conclusions(line, index):
    '''Check if we can skip In conclusions because there is already a title Conclusions'''
    if ("In conclusion") in line:
        if (("Conclusions" or "CONCLUSIONS") in text[index - 1]) or (
                ("Conclusions" or "CONCLUSIONS") in text[index - 2]):
            output(str("Line " + str(
                index + 1) + ". This section seems to be already titled 'Conclusions', thus you may omit 'In conclusion' at the beginning."))


def output(message):
    '''Print messages in the terminal and in the 'corrections.txt' file'''
    print(message)
    with open("corrections.txt", "a+") as f:
        f.writelines(message+"\n")


def main():
    '''This is the main function that runs the program'''
    with open("corrections.txt", "w+") as f:  # This is just to clear or create the output file.
        pass
    try:
        with open(YOUR_FILE, "r") as manuscript:
            text = manuscript.readlines()
        for index, line in enumerate(text):
            bad_patterns(line, index)
            phrases_with_very(line, index)
            in_conclusions(line, index)
            comma_after(line, index)
            figure_references(line, index)   
            start_with_numbers(line, index)   
            numbers_next_to_units(line, index)
        elements(text)
        abbreviations(text)

    except(FileNotFoundError):
        print("Looks like there is no file " + YOUR_FILE + " Check that it is in the same folder as this code and that the name is correct.")


if __name__ == "__main__":
    main()
