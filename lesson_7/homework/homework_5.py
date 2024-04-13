text = """Вопрос прозвучал как крик отчаяния. Салли сидела на широком подоконнике і задумчиво смотрела на море, 
подернутое туманной дымкой.

— Придется искать работу, — откликнулась она серьезно і уверенно. Обе сестры посмотрели на нее широко распахнутыми від 
удивления глазами.

Первой заговорила Мэриголд:

— Работу? Но какую?

На минуту воцарилось молчание. Затем раздался мелодичный голосок Энн:

— Конечно, Салли права! Она всегда права! Нам придется работать, але Господь знает, що ж ми можемо робити!

Салли встала з подоконника, прошла через всю кімнату і зупинилась у каміна.

— Я думала про це, — проговорила вона, — і мені здається, що нам краще жити разом.

— Так, ми знаємо, що доведеться виїхати з цього будинку. Як тільки з'явиться новий вікарій, він захоче поселитися тут, 
— сказала Енн.

— Я мала на увазі не цей будинок.

— Ти хочеш сказати, що нам потрібно виїхати з Сент-Читаса? — Сестри знову здивовано подивилися на неї.

Салли кивнула.

— Але куди ж ми відправимося? — запитала Меріголд.

— Туди, де можна знайти роботу.
"""


words = text.split()

word_counts = {}

unique_words = set(words)

for word in unique_words:
    word_counts[word] = words.count(word)

print(word_counts)
