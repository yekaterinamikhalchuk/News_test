from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    bad_words = ['shit', 'whore', 'fuck', 'harlot', 'nigger', 'bitch', 'freak']
    text = set(value.split())
    for word in text:
        for bad_word in bad_words:
            if word == bad_word:
                return value.replace(word, '*' * len(word))
    return value
