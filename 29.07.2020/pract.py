import requests, base64

userpass = 'alladin:opensesame'
encoded_u = base64.b64encode(userpass.encode()).decode()
headers = {"Authorization" "Basic %s" % encoded_u}
r=requests.post("https://datasend.webpython.graders.eldf.ru/submissions/1/", headers={"Authorization":"Basic %s" % encoded_u})
print(r.text)
# Вывод
# {"password": "ktotama", "path": "submissions/super/duper/secret/",
#  "instructions": "\u0421\u0434\u0435\u043b\u0430\u0439\u0442\u0435"
# " PUT \u0437\u0430\u043f\u0440\u043e\u0441 \u043d\u0430 \u0442\u043e\u0442"
# " \u0436\u0435 \u0445\u043e\u0441\u0442, \u043d\u043e \u043d\u0430 path "
# "\u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0439 \u0432 \u044d\u0442\u043e\u043c"
# " \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0435 c \u043b\u043e\u0433\u0438\u043d\u043e\u043c"
# " \u0438 \u043f\u0430\u0440\u043e\u043b\u0435\u043c \u0438\u0437 \u044d\u0442\u043e\u0433\u043e"
# " \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430. \u041b\u043e\u0433\u0438\u043d"
# " \u0438 \u043f\u0430\u0440\u043e\u043b\u044c \u0442\u0430\u043a\u0436\u0435"
# " \u043f\u0435\u0440\u0435\u0434\u0430\u0439\u0442\u0435 \u0432"
# " \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0435 Authorization.", "login": "galchonok"}


# перевод текста = ("instructions": "Сделайте PUT запрос на тот же хост,
# но на path указанный в этом документе c логином и паролем из этого документа.
# Логин и пароль также передайте в заголовке Authorization.")

z = requests.put("https://datasend.webpython.graders.eldf.ru/submissions/super/duper/secret/", auth=('galchonok', 'ktotama'))
print(z.text)
# Вывод
# {"answer": "w3lc0m370ch4p73r4.2"}

