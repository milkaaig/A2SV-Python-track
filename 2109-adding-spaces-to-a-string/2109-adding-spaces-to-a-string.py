class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = []
        length = len(s)
        start = 0
        for end in spaces:
#             appends till the last space so the last word remains appended
            output.append(s[start:end])
            start = end
#         append the last word after the last space
        output.append(s[start:length])
#     join the elements with space using space
        output = " ".join(output)
        return output