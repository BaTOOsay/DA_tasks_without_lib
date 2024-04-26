# Решение задачи №1: Выборы-выборы:

# 1. Получение данных исследования и их запись:

  # 1.1 Вводим количество районов
quantity_regions = int(input())

  # 1.2 Создадим массивы для:
  # хранения суммы голосов в каждом регионе за каждого участника
a_voters, b_voters = [], []
  # хранения суммы голосовавших в каждом районе
sum_votes = []

  # 1.3 Запишем в каждый массив сумму голосов в каждом районе за каждого участника и сумму голосов в каждом районе
for region in range(quantity_regions):
    n_votes_a, n_votes_b = int(input()), int(input())
    a_voters.append(n_votes_a)
    b_voters.append(n_votes_b)
    sum_votes.append(n_votes_a + n_votes_b)

# 2. Найдём общую сумму голосовавших:
all_sum_votes = sum(sum_votes)

# 3. Отсортируем суммарное количество голосовавших по районам
sum_votes_sorted = sorted(sum_votes, reverse=True)

# 4. Поиск 'грязного'(многовероятно) количества необходимым посещений районов Борисом:
  # Наименьшая сумма голосующих для победы(не учитывается фактор что голосующие могут не голосовать = 'грязное')
accept_sum = 0
  # Наименьшее количество районов
min_quantity_regions = 0
for effort in range(quantity_regions):
    if accept_sum / all_sum_votes < 0.5:
        accept_sum += sum_votes_sorted[effort]
        min_quantity_regions = effort + 1

# 5. Поиск более 'чистого' количества необходимым регионов:
     # p.s полученные значения гарантируют победу, но количество регионов может быть избыточно - оптимизируем

    # 5.1. Если Борис не будет выступать в районе, то все кто за него хотели голосовать не будут голосовать вовсе
    # поэтому уберём этих людей из исследования
quantity_non_voting_in_regions = []

for del_votes_b in range(min_quantity_regions, quantity_regions):
    quantity_non_voting_in_region = b_voters[del_votes_b]
    quantity_non_voting_in_regions.append(quantity_non_voting_in_region)

    # 5.2 Найдём число голосовавших(с учётом отсеянных)
new_sum_votes = all_sum_votes - sum(quantity_non_voting_in_regions)

    # 5.3 Попытка избавиться от возможных лишних регионов

# попытка убрать 1-ин регион

while True:
    new_accept_sum = accept_sum - sum_votes_sorted[min_quantity_regions - 1]
    d_new_sum_votes = new_sum_votes - b_voters[min_quantity_regions - 1]
    if new_accept_sum / d_new_sum_votes > 0.5:
        accept_sum, new_sum_votes = new_accept_sum, d_new_sum_votes
        min_quantity_regions -= 1
    else:
        break

print(f'Минимальное количество районов которые посетит Борис для победы на выборах = {min_quantity_regions}')
print('При условии что мы берём выборку районов с наибольшими населениями(для минимизации количетсва необходимых райнов)')





