def glavnoe():
    global vibor, shure_1
    print("Приветствую искатель в главном меню лучшего путеводителя для Авантюристов и Заказчиков", "\n"
          "Но для конспирации официально мы их называем Стартаперами и Инвесторами.", "\n"
          "Для начала нужно выбрать раздел, который будет полезен именно тебе.", "\n \n" 
          "Если ты Авантюрист введи цифру 1. Если Заказчик цифру 2.")
    vibor = int(input())
    if vibor == 1:
        startap()
    elif vibor == 2:
        investor()
    else:
        glavnoe()

def startap():
    global problema, budzet, idea, vibor
    print("Приветствую авантюрист! \n"
          "У наших заказчиков очень много денег. Они щедро заплатят тем, кто исполнит их желания.\n"
          "Но без подготовки не каждый сможет выполнить задание и вернуться живым.\n"
          "Чтобы ты стал готов ты должен выбрать роль в группе, с которой начнешь свой путь\n"
          "и пройти обучение в одной из лучших школ.\n")
    print("Для начала давай узнаем немного о тебе\n" 
          "Не каждый готов стать авантюристом, похоже у тебя возникли большие проблемы. Расскажи о них")
    problema = input()
    print("В таком случае тебе понадобится серьезно вложиться в развитие карьеры авантюриста.\n"
          "Напиши цифрами сумму своего бюджета.")
    budzet = int(input())
    print("Расскажи о твоих идеях, ты ведь стал на этот путь не просто так? Многие считают это дело опасным\n"
          'и без идей как добиться успеха (оставшись живым) мало кто готов "сунуть голову в пасть крокодилу".')
    idea = input()
    print("Я могу тебе посоветовать куда лучше потратить бюджет, для этого перейдем к выбору роли в группе \n"
          "Введи 1 - если желаете продолжить \n"
          "Введи 2 - если желаете рассказать заного информацию о вас \n"
          "Введи 3 - если желаете вернуться к предыдущему разделу\n"
          "Введи 4 - если желаете вернуться в главное меню")
    vibor = int(input())
    if vibor == 1:
        rol()
    elif vibor == 2:
        startap()
    elif vibor == 3:
        glavnoe()
    elif vibor == 4:
        glavnoe()
    else:
        startap()

def rol():
    global rol1, rol2, rol3, rol4, rol5, choose
    rol1 = "1. Защитник"
    rol2 = "2. Целитель"
    rol3 = "3. Маг"
    rol4 = "4. Воин"
    rol5 = "5. Стрелок"

    print("    Группы состоят из следующих ролей:")
    print(rol1, " - если ты хочешь первым бросаться в бой и сдерживать натиск толпы врагов.\n",
          rol2, " - вылечит раны, снимет проклятие, очистит от яда и даже воскресит!\n",
          rol3, " - атакует / замораживает / проклинает сразу множество врагов, призывает в помощь существ.\n",
          rol4, " - самое то для любителей простоты, кто хочет с крутым звуком махать чем то большим и острым.\n",
          rol5, " - если любишь быть тем, кто говорит: 'Они не поймут что их убило'.\n",
          "    Напиши номер роли, которая больше всего тебе нравиться и я дам тебе несколько советов.", sep='')
    choose = int(input())
    if choose == 1:
        #if budzet < 20000
        #print("Хороший выбор! Но т.к. у тебя меньше 20000 золотых, то все что я тебе могу предложить: \n"
        print("Хороший выбор! Данная роль очень конкурентноспособна в наше время. \n"
        "В первую очередь ты должен иметь Щит драконьего сердца. У него конструкция с улучшенным шансом блока \n"
        "А вставки из драконьей чешуи увеличат устойчивость к магии и прибавят регенерацию здоровья.\n"
        "Обучаться советую в Школе защитников: 'Киевский орден паладинов'. \n"
        "Оставшиеся деньги лучше всего потратить на покупку расходников: зелья, свитки и тд")
    elif choose == 2:
        print("Хороший выбор! Данная роль очень конкурентноспособна в наше время. \n"
        "В первую очередь хороший целитель должен иметь Посох сердца леса. \n"
        "Он сделан из древесины особого дерева, которое растет в центре зачарованного леса.\n"
        "Посох увеличит восстановление маны и даст ауру леса, улучшающую регенерацию здоровья группе."
        "Обучаться советую в Школе магии: 'Киевский филиал Хогвартса'. \n"
        "Оставшиеся деньги лучше всего потратить на покупку расходников: зелья, свитки и тд")
    elif choose == 3:
        print("Хороший выбор, но целитель конечно важнее. Маг пользуется средним спросом в наше время \n"
        'В первую очередь хороший маг должен иметь Посох лавы. На его конце камень "Сердце вулкана" \n'
        "Посох увеличит уязвимость врагов к магии и способен выпускать огненные шары во врагов."
        "Обучаться советую в Школе магии: 'Киевский филиал Хогвартса'. \n"
        "Оставшиеся деньги лучше всего потратить на покупку расходников: зелья, свитки и тд")
    elif choose == 4:
        print("Хороший выбор, но защитник конечно важнее. Воин пользуется средним спросом в наше время \n"
        'В первую очередь купи топор закаленный в крови дракона. Его прочность и острота безупречны. \n'
        "Кроме того он добавляет к атакам эффект взрыва, который наносит урон огнем врагам возле цели атаки. \n"
        "Обучаться советую в Школе воинов: 'Киевская арена Спартака'. \n"
        "Оставшиеся деньги лучше всего потратить на покупку расходников: зелья, свитки и тд")
    elif choose == 5:
        print("Хороший выбор! Данная роль очень конкурентноспособна в наше время. \n"
        "В первую очередь ты должен иметь Barrett M82 последней модели. А также урановые разрывные пули. \n"
        "В последней модели добавлена подствольная ракетница, позволяющая наносить массовый урон.\n"
        "Обучаться советую в Школе снайперов: 'Киевский филиал Officio Assassinorum'. \n"
        "Оставшиеся деньги лучше всего потратить на покупку расходников: зелья, свитки и тд")
    print("\nВсе готово чтобы начать твой путь к вершинам славы!\n"
    "Введи 1 - если желаете увидеть всю введенную вами информацию\n"
    "Введи 2 - если желаете изменить выбор роли\n"
    "Введи 3 - если желаете вернуться к предыдущему разделу\n"
    "Введи 4 - если желаете вернуться в главное меню")
    vibor = int(input())
    if vibor == 1:
        info1()
    elif vibor == 2:
        rol()
    elif vibor == 3:
        startap()
    elif vibor == 4:
        glavnoe()
    else:
        rol()


def info1():
    print("\n Данные о начинающем авантюристе: \n",
          "Твоя проблема: ", problema, "\n",
          "Твой бюджет: ", budzet, "\n",
          "Твоя идея: ", idea, sep='')
    if choose == 1:
        print("Твоя роль в группе авантюристов: ", rol1[3:11])
    elif choose == 2:
        print("Твоя роль в группе авантюристов: ", rol2[3:11])
    elif choose == 3:
        print("Твоя роль в группе авантюристов: ", rol3[3:6])
    elif choose == 4:
        print("Твоя роль в группе авантюристов: ", rol4[3:7])
    elif choose == 5:
        print("Твоя роль в группе авантюристов: ", rol5[3:10])

    print("Введи 1 - если желаете вернуться к предыдущему разделу\n"
          "Введи 2 - если желаете вернуться в главное меню")
    vibor = int(input())
    if vibor == 1:
        rol()
    elif vibor == 2:
        glavnoe()
    else:
        info1()

def investor():
    global kat1, kat2, kat3, kat4, kat5, choose
    print('Приветствую "инвестор"! \n'
          "У нас есть много умелых авантюристов, готовых ради золота и славы на самую разную работу .\n"
          "Вне зависимости от вида заказа гарантирована полная анонимность, а оплата только по завершению.\n"
          "Давай я расскажу тебе о самых прибыльных и успешных категориях, а затем дам рекомендации по ним.\n"
          "Мы пройдемся по каждому сегменту и ты узнаешь о лучших в своем деле компаниях авантюристов.\n")
    kat1 = "1. Расхищение древних гробниц"
    kat2 = "2. Отнятие драгоценностей у драконов"
    kat3 = "3. Охота на различных тварей мучающих населенные пункты"
    kat4 = "4. Кража артефактов"
    kat5 = "5. Диверсии, тайные операции"

    print("    Есть 5 ключевых сегментов:")
    print(kat1, " - многие боятся проклятий, но добытые вещи за неплохую цену можно продать коллекционерам\n",
          kat2, " - это то, что действительно ценно у них, а не кучи золота, на которых они сидят.\n",
          kat3, ' - местные власти платят не много, но всегда найдется работа: "Не качеством, а количеством."\n',
          kat4, " - различные люди, ордена и страны имеют свое мнение о том, кому что должно принадлежать.\n",
          kat5, ' - войны никогда не кончаются, также как и те, кому они выгодны. Но если что "НасТамНеБыло".\n',
          "    Напиши номер категории, которая больше всего тебе интересна и я подробней расскажу о ней.", sep='')
    choose = int(input())
    if choose == 1:
        #if budzet < 20000
        #print("Хороший выбор! Но т.к. у тебя меньше 20000 золотых, то все что я тебе могу предложить: \n"
        print("Хороший выбор! Данный сегмент считается самым прибыльным в наше время. \n"
        "В нем не появляются проблемы с властями, ведь грабницы признаны утерянными и захваченными злом.\n"
        "Вероятность успеха очень велика, ведь сильные боссы уровня драконов там встречаются крайне редко.\n"
        "Оплата авантюристам не высокая, ведь они не знают цены найденных там артефактов, а золота там мало.\n"
        "Самые успешные компании в этом сегменте: Грабницехитители, Ничейное - временно не наше, ИндианаДжонсы")
    elif choose == 2:
        print("Хороший выбор! Если повезет - большой навар. Если не повезет - платить некому =) \n"
        "Драконы - сильнейшие в мире существа и хорошо прячутся, поэтому смогли сохранить так много богатств.\n"
        "Но и они могут умереть. Для этого нужна группа с особым составом: защитник, 2 целителя, 2 стрелка\n"
        "Потому что драконам безразлична магия, в ближнем бою сжигают все перед собой."
        "Опасаться что группа кинет не стоит, ведь сокровищ у драконов слишком много. И не всем цена известна.\n"
        "Самые успешные компании в этом сегменте: Драконоборцы, ХусРоТары, Снайперы")
    elif choose == 3:
        print("Выбор консерваторов, медленно но уверено будете ставать богаче. \n"
        'В окрестностях городов часто бывает: то гулям на старом кладбище надоест лежать, то оборотень забредет\n'
        "в поисках вкуснятины, а на вампиров и вовсе десяток новых заказов ежедневно. Власти не охотно ведут дела\n"
        "с людьми, способными бороться с подобными ужасами, ведь авантюристами не от жизни хорошей  стают. Тут то\n"
        "и появляетесь вы - посредники. Да и среди всех у вас времени больше находить самые прибыльные заказы\n"
        "Самые успешные компании в этом сегменте: Осинный кол, Что мертво умереть может, Кусаем волка за бочок")
    elif choose == 4:
        print("Весьма интересный выбор. Как известно политические, религиозные и прочие споры могут длиться века\n"
        'История пишется и снова переписывается, в угоду действующей власти. Некоторые хранят древнюю правду.\n'
        "В этой всей путаннице есть место и для инвесторов. Одни платят, другие добывают что-угодно из музеев,\n"
        "шкатулки принцессы или катакомбах столичного храма. Анонимность - это важно, а золото не пахнет.\n"
        "Самые успешные компании в этом сегменте: Не важно что - важно за сколько, Орден Секретов, Палец короля")
    elif choose == 5:
        print("Выбор для тех, кто не боится влезть в межгосударственную войну. Конечно вероятность этого не высока\n"
        "Говорят золото не пахнет, а когда лес рубят щепки летят. Важные люди могут много платить, но готов ли ты?\n"
        "Сожженные деревни, случайные жертвы, отсутствие различий между целями - если для тебя это не важно, то готов.\n"
        "Самые успешные компании в этом сегменте: Officio Assassinorum, Темные Эльдары, Тзинчиты")
    print("\nВсе готово чтобы начать твой путь к вершинам славы!\n"
    "Введи 1 - если желаете изменить выбор категории\n"
    "Введи 2 - если желаете вернуться в главное меню")
    vibor = int(input())
    if vibor == 1:
        investor()
    elif vibor == 2:
        glavnoe()
    else:
        investor()

glavnoe()


