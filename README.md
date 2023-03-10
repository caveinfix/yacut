# Проект: Cервис укорачивания ссылок и API к нему. 
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

### Ключевые возможности сервиса:

- Генерация коротких ссылок и связь их с исходными длинными ссылками.
- Переадресация на исходный адрес при обращении к коротким ссылкам.

## API для проекта
Доступны следующие эндпоинты:

```http
  POST /api/id/ 
```
```http
  GET /api/id/<short_id>/
```

## Установка и запуск

#### Скачать проект:

```http
  git@github.com:caveinfix/yacut.git
```

#### Установить виртуальное окружение и зависимости:

```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
```

#### Запуск:
```bash
  flask run
```
Сервис будет доступен по адесу http://127.0.0.1:5000/

## Автор
Филипп @caveinfix

e-mail: caveinfix@gmail.com