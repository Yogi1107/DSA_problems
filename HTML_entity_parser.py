# class Solution:
#     def entityParser(self, text: str) -> str:
#         entity_map = {
#             "&quot;": "\"",
#             "&apos;": "'",
#             "&amp;": "&",
#             "&gt;": ">",
#             "&lt;": "<",
#             "&frasl;": "/"
#         }
        
#         result = []
#         i = 0
        
#         while i < len(text):
#             if text[i] == '&':
#                 matched = False
#                 for entity, char in entity_map.items():
#                     if text.startswith(entity, i):
#                         result.append(char)
#                         i += len(entity)
#                         matched = True
#                         break
#                 if not matched:
#                     result.append(text[i])
#                     i += 1
#             else:
#                 result.append(text[i])
#                 i += 1
        
#         return "".join(result)

class Solution:
    def entityParser(self, text: str) -> str:
        text = text.replace('&quot;', "\"")
        text = text.replace('&apos;', "\'")
        text = text.replace('&gt;', ">")
        text = text.replace('&lt;', "<")
        text = text.replace('&frasl;', "/")
        text = text.replace('&amp;', "&")
        return text

        
