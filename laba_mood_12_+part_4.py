# Завдання 1
# Створіть програму роботи зі словником.
# Наприклад, англо-іспанський, французько-німецький
# або інша мовна пара.
# Програма має:
# ■ надавати початкове введення даних для словника;
# ■ відображати слово та його переклади;
# ■ дозволяти додавати, змінювати, видаляти
# переклади слова;
# ■ дозволяти додавати, змінювати, видаляти слово;
# ■ відображати топ-10 найпопулярніших слів
# (визначаємо популярність спираючись на лічильник
# звернень);
# ■ відображати топ-10 найнепопулярніших слів
# (визначаємо непопулярність спираючись на лічильник
# звернень).
# Використовуйте дерево для виконання цього
# завдання.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.translations = {}
        self.counter = 0

    def add_translation(self, translation):
        if translation not in self.translations:
            self.translations[translation] = 0

    def remove_translation(self, translation):
        if translation in self.translations:
            del self.translations[translation]

    def increment_counter(self):
        self.counter += 1

    def decrement_counter(self):
        self.counter -= 1

class Dictionary:
    def __init__(self):
        self.root = TreeNode(None)

    def add_word_translation(self, word, translation):
        current_node = self.root
        for char in word:
            if char not in current_node.translations:
                current_node.translations[char] = TreeNode(char)
            current_node = current_node.translations[char]
        current_node.add_translation(translation)
        current_node.increment_counter()

    def remove_word_translation(self, word, translation):
        current_node = self.root
        for char in word:
            if char not in current_node.translations:
                return
            current_node = current_node.translations[char]
        if translation in current_node.translations:
            current_node.remove_translation(translation)
            current_node.decrement_counter()

    def display_word_translations(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.translations:
                print("Word not found in the dictionary.")
                return
            current_node = current_node.translations[char]
        print(f"{word}: {', '.join(current_node.translations.keys())}")

    def add_word(self, word, translations):
        for translation in translations:
            self.add_word_translation(word, translation)

    def remove_word(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.translations:
                return
            current_node = current_node.translations[char]
        current_node.translations.clear()
        current_node.decrement_counter()

    def _traverse_tree(self, node, popular_words):
        if node is None:
            return
        if node.counter > 0:
            popular_words.append((node.value, node.counter))
        for child in node.translations.values():
            self._traverse_tree(child, popular_words)

    def display_top_10_popular_words(self):
        popular_words = []
        self._traverse_tree(self.root, popular_words)
        popular_words.sort(key=lambda x: x[1], reverse=True)
        print("Top 10 most popular words:")
        for i, (word, count) in enumerate(popular_words[:10], 1):
            print(f"{i}. {word}: {count}")

    def display_top_10_unpopular_words(self):
        unpopular_words = []
        self._traverse_tree(self.root, unpopular_words)
        unpopular_words.sort(key=lambda x: x[1])
        print("Top 10 least popular words:")
        for i, (word, count) in enumerate(unpopular_words[:10], 1):
            print(f"{i}. {word}: {count}")

def main():
    dictionary = Dictionary()

    dictionary.add_word("apple", ["яблуко", "manzana"])
    dictionary.add_word("banana", ["банан", "plátano"])
    dictionary.add_word("car", ["автомобіль", "coche"])
    dictionary.add_word("house", ["будинок", "casa"])
    dictionary.display_word_translations("apple")
    dictionary.add_word("dog", ["собака", "perro"])
    dictionary.remove_word_translation("banana", "банан")
    dictionary.display_top_10_popular_words()
    dictionary.display_top_10_unpopular_words()

if __name__ == "__main__":
    main()

