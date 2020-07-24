'''
Category: String, Stack
Time Complexity: O(n)
'''


class Solution:
    def entityParser(self, text: str):
        i = 0
        stack = ''
        output = ''
        parser = {
            '&quot;': '"',
            '&apos;': '\'',
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/'
        }

        while i < len(text):
            if text[i] != '&':
                output += text[i]
            else:
                while text[i] != ';':
                    stack += text[i]
                    i += 1
                stack += ';'
                if stack in parser:
                    output += parser[stack]
                else:
                    output += stack
                stack = ''
            i += 1
        return output

    def entityParser2(self, text):
        parser = {
            '&quot;': '"',
            '&apos;': '\'',
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/'
        }

        for k, v in parser.items():
            text = text.replace(k, v)
        return text


cases = [
    "&amp; is an HTML entity but &ambassador; is not.",
    "and I quote: &quot;...&quot;",
    "Stay home! Practice on Leetcode :)",
    "x &gt; y &amp;&amp; x &lt; y is always false",
    "leetcode.com&frasl;problemset&frasl;all"
]

for c in cases:
    s = Solution().entityParser(c)
    print(s)
