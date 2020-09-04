import re

black_list = [
    'is there anything else interesting?', 'what else happened during this period?', 'was anyone else involved?',
    'is there anything else?', 'is there anything else notable?', 'anything else interesting?', 'anything else?',
    'who else', 'what else did you find interesting?', 'is there anything else that is notable?',
    'what else did he do during this time?', 'what else did he do at this time?',
    'what else did he do?', 'what else happened during this time?', 'did he win anything else',
    'who else did he work with?', 'what else did she do?', 'what else happened during this time period?',
    'who else?', 'anyone else?', 'what else can you tell me interesting?', 'what else was he known for?',
    'what else happen?', 'is there anything else i should know?', 'what else did she do in her career?',
    'was there anything else you found interesting?', 'what else can you tell me interesting',
    'did he do anything else?', 'what else can you tell me from the article?', 'what else did it win',
    'what else was he known for', 'how else was he involved?', 'what else did he do in his career',
    'what else is notable about this time?', 'can you share anything else about the article?',
    'did he work with anyone else?', 'what else happened?', 'what else can you tell me about the article?',
    'what else?', 'is there anything else notable about the article?', 'did he do anything else important',
    'did anything else happen?', 'is there anything else interesting i should know?', 'what else is interesting?',
    'did she work anywhere else?', 'what else was she known for',
    'what else did he do during those years?', 'what else did he do in this time period',
    'who else was there', 'what else does he support?', 'did he accomplish anything else?',
    'did they do anything else?', 'where else did he attend school?', 'what else can you tell me about this article?',
    'was there anything else interesting?', 'what else happened', 'did she do anything else?',
    'what else did he achieve?', 'is there anything else of note?', 'what else is significant?',
    'what else did it include?', 'what else did they do during this time?', 'what else did they say',
    'what else did she act in?', 'what else did he work on', 'did she write anything else?',
    'what else did he do there?', 'did he manage anyone else?', 'did anything else happen during this time period?',
    'what else is significant about this article ?', 'what else interesting can you tell me?',
    'what else can you tell me', 'what else can you tell me about this time period?',
    'what else can you tell me about it?', 'is there anything else of significance?', 'anything else in the article?',
    'did he play with anyone else?', 'what else did he say?', 'what else did he have to say?',
    'what else can you tell me about his personal life?', 'what else can you tell me about him?',
    'was there anyone else?', 'can you tell me anything else interesting?', 'what else did they do?',
    'who else was in it?', 'and what else?', 'anything else you found interesting?', 'what else has he done?',
    'did he do anything else during this time period?', 'what else is of note in this section?',
    'what else did they do ?', 'what else can you share about the article?',
    'what else interesting happened during this time?', 'what else was said?', 'who else did they work with?',
    'did he do anything else interesting?', 'what else changed', 'is there anything else important?',
    'anything else i should know?', 'anyone else', 'what else should i know', 'what else stood out in this article',
    'is there anything else significant during this time?', 'is there anything else interesting about his early life?',
    'who else starred in it?', 'is there anything else interesting about her?', 'did he produce anything else?',
    'what else did she do during this time?', 'was he involved in anything else?',
    'is there anything else significant about this?', 'what else did he do', 'what else stood out to you',
    'what else is interesting', 'what else', 'who else did she work with?', 'did anyone else join?',
    'did anyone else leave?', 'where else did he work?', 'what else can you tell me about them?',
    'what else did she do', 'what else was she known for?', 'what else is interesting about him?',
    'what else was they known for', 'what else is notable?', 'what else did she do at that time?',
    'what else did you find interesting about this?', 'did they work with anyone else?',
    'what else is notable about this part of his life?', 'did he collaborate with anyone else?',
    'what else did he say', 'what else did you see that stood out in this article',
    'what else is significant during this time?', 'what else happen in her personal life',
    'what else did he find?', 'what else did he do there', 'what else is he known for?',
    'anything else that was interesting?', 'and who else?', 'what else is interesting about his early life?',
    'was he known for anything else?', 'anything else interesting about him?', 'what else stood out',
    'what else did they do at this time?', 'did anything else interesting happen?',
    'what else is significant about this?', 'anybody else?', 'what else was said about it?',
    'is there anything else interesting', 'what else did he do in his early years?',
    'anything else of interest?', 'what else has he done in his career?', 'is there anything else interesting about him?',
    'did he win anything else?', 'what else did he do that stood out', 'what else is significant about this time?',
    'is there anything else significant?', 'what else can you share with me about the article?',
    'what else is notable about her personal life?', 'what else can you tell me about this',
    'what else is notable in the article?', 'what else did he accomplish?', 'what else did he believe?',
    'where else?', 'did he appear in anything else?', 'what else is significant about this part of his career?',
    'is there anything else important to know?', 'what else did he write about?',
    'what else can you tell me of note?', 'did they collaborate with anyone else?', 'did he do anything else there?',
    'what else did he do in his early career?', 'did he work with anyone else notable?',
    'is there anything else of importance?', 'what else did you find interesting about her?',
    'what else was important in this article', 'what else can you tell me about his career?',
    'did you find anything else interesting?', 'what else stood out in this article?',
    'what else did he have to say about it?', 'what else did he do in his later years?',
    'anything else you can share about the article?', 'what else is significant about this year?',
    'what else is interesting about her?', 'did he work with anyone else',
    'what else can you tell me that is interesting?', 'what else did she do there?',
    'did she work with anyone else?']

black_list_patterns = [
    re.compile(r'what happened in \d\d\d\d')
]
