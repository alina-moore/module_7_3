import io
from pprint import pprint

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                clean_text = ""
                for x in text:
                    if x not in punctuation:
                        clean_text += x
                words = clean_text.split()
                all_words[file_name] = words

        return all_words


    def find(self, word):
        word = word.lower()
        result_find = {}
        for file_name, words in self.all_words.items():
            position = -1
            for i in range(len(words)):
                if words[i] == word:
                    position = i + 1
                    break
            result_find[file_name] = position
        return result_find


    def count(self, word):
        word = word.lower()
        result_count = {}
        for file_name, words in self.all_words.items():
            counted_word = 0
            for w in words:
                if w == word:
                    counted_word+=1
            result_count[file_name] = counted_word

        return result_count




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

