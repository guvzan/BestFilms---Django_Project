<h1>BestFilms -- веб-сайт, створений за допомогою фреймворку Django</h1>
<h3>
  Цей проект виконано з метою вивчити основи Django та принципи роботи моделі MTV.
</h3>

<hr>

<h3>
  Я використав системи реєстрації та авторизації, вбудовані у Django, але розширив їх. (Для цього я також розширив базову модель користувача).<br>
  ![image](https://user-images.githubusercontent.com/55750045/212624975-7d686463-9ffe-431e-85f9-9457a69a4eb7.png)
  Сайт присвячений фільмам, тому передбачена можливість додання нового фільму. Якщо одна з категорій доданого фільму співпадає з такою, що представлена на головній       сторінці, цей фільм буде автоматично додано на головну сторінку у відповідне місце.
  ![image](https://user-images.githubusercontent.com/55750045/212625744-59ed5603-1214-4740-9b45-8b038ae31364.png)
Сторінка фільму генерується на основі інформації з бази даних і презентує короткий опис фільму, трейлер та коментарі.
![image](https://user-images.githubusercontent.com/55750045/212626619-0a29131b-27ce-451f-b329-d1ff14adf9ea.png)
Кожен коментар має певну кількість позначок 'Подобається', таким чином, чим вище це число, тим вище цей коментар на сторінці.
Коментар також містить інформацію про свого автора та дозволяє перейти на сторінку його профілю.
![image](https://user-images.githubusercontent.com/55750045/212627788-fcb0ba02-a404-4542-8ef3-5a02c48fcb43.png)
Профіль містить інформацію про користувача
</h3>
