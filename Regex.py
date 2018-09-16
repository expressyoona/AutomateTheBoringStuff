"""
Regex
- abc(text)?def => abcdef or abctextdef
- (abc)?def => abc-def or def
- abc(text)* => abc or abctext or abctexttext
- abc(text)+def => abctextdef
- re.compile(r'(Ha){3}') => HaHaHa
- r'^Hello': Begin with Hello
- r'\d$s': End with any digit.
Character classes:
\d: [0,9]. Or use: [0-9]
\D: any character that is not a number digit from 0 to 9
\w: Any letter, numberic digit, or the underscore _. [A-Za-z]
\W: ^ \w
\s: Any space, tab, or newline character
\S: ^ \s
. : Any character, ^\n
(.*): Everything
"""
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('dfz znxcmz z xncnzc 123-456-8910')
print('Phone number found: ', mo.group())
print(phoneNumRegex.findall('Tel: 123-456-8910 Fax: 924-124-2122'))
"""
The + matches one or more of the preceding group.

The {n} matches exactly n of the preceding group.

The {n,} matches n or more of the preceding group.

The {,m} matches 0 to m of the preceding group.

The {n,m} matches at least n and at most m of the preceding group.

{n,m}? or *? or +? performs a nongreedy match of the preceding group.

^spam means the string must begin with spam.

spam$ means the string must end with spam.

The . matches any character, except newline characters.

\d, \w, and \s match a digit, word, or space character, respectively.

\D, \W, and \S match anything except a digit, word, or space character, respectively.

[abc] matches any character between the brackets (such as a, b, or c).

[^abc] matches any character that isn’t between the brackets.


"""
