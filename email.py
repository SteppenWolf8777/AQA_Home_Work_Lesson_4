import datetime

# 1. Создайте словарь email, который содержит поля:
email = {
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "  lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon.\nRegards,\nTeam"
}


# 2. Добавьте дату отправки:
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["send_date"] = send_date
print(send_date)


# 3. Нормализуйте e-mail адреса:
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()
print(email["from"])
print(email["to"])


# 4. Извлеките логин и домен отправителя:
login = email["from"].strip().split("@")[0]
domain = email["from"].split("@")[1]
print(login)
print(domain)


# 5. Создайте сокращённую версию текста:
email["short_body"] = email["body"][:10] + '...'
print(email["short_body"])


# 6. Списки доменов:
domain_personal = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru','company.ru']
domain_corporate = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']
domain_personal = list(set(domain_personal))
domain_corporate = list(set(domain_corporate))
print(domain_personal)
print(domain_corporate)


# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений:
intersection = set(domain_personal) & set(domain_corporate)
print(intersection) # Есть пересечение 'company.ru'


# 8. Проверьте «корпоративность» отправителя:
is_corporate = domain in domain_corporate
print(is_corporate)  # Почему False, если organization.org есть и там и там?


# 9. Соберите «чистый» текст сообщения:
email["clean_body"] = email["body"].replace("\n", " ").replace("\t", " ")
print(email["clean_body"])


# 10. Сформируйте текст отправленного письма:
email["sent_text"] = f'''Кому: {email.get("to", "")}, от {email.get("from", "")} Тема: {email.get("subject", "")}, дата {email.get("send_date", "")} {email.get("clean_body", "")}'''
print(email["sent_text"])


# 11. Рассчитайте количество страниц печати:
text_length = len(email["sent_text"])
pages = (text_length + 499) // 500
print(pages)


# 12. Проверьте пустоту темы и тела письма:
is_subject_empty = len(email["subject"].strip()) == 0
is_body_empty = len(email["body"].strip()) == 0
print(is_subject_empty)


# 13. Создайте «маску» e-mail отправителя:
masked_login = login[:2] + "***"
email["masked_from"] = masked_login + "@" + domain
print(email["masked_from"])


# 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru":
domain_personal.remove("list.ru")
domain_personal.remove("bk.ru")
print(domain_personal)
print(domain_corporate)
