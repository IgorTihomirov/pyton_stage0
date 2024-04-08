import pandas
import seaborn

data = pandas.read_csv('support_data.csv')

segments_new = ['Потенциальные клиенты', 'Обычные клиенты', 'VIP-клиенты']
intervals = ['До внедрения роботов', 'После внедрения роботов']

# для каждой пары сегмент-интервал считаем сумму продолжительностей
duration_sum = data.groupby(['segment', 'interval'])['duration'].sum()
# для каждой пары сегмент-интервал считаем количество записей
duration_count = data.groupby(['segment', 'interval'])['duration'].count()

# считаем среднее: делим сумму на количество
mean_duration = duration_sum / duration_count
print(mean_duration)

# строим тепловую карту для длительности ответов
# столбец mean_duration получился вложенным из-за группировки по двум столбцам,
# поэтому его нужно «развернуть» методом unstack()
seaborn.heatmap(mean_duration.unstack('interval'), xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn')