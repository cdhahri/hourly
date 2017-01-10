#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

pearson_03 = [0.10670731707317073, 0.06097560975609756, 0.0975609756097561, 0.13414634146341464, 0.08841463414634146, 0.11280487804878049, 0.10975609756097561, 0.1524390243902439, 0.20426829268292682, 0.3170731707317073]
pearson_03 = [x * 100 for x in pearson_03]

pearson_05 = [0.08823529411764706, 0.041176470588235294, 0.052941176470588235, 0.08823529411764706, 0.06470588235294118, 0.08235294117647059, 0.052941176470588235, 0.09411764705882353, 0.14705882352941177, 0.3176470588235294]
pearson_05 = [x * 100 for x in pearson_05]

pearson_07 = [0.09401709401709402, 0.05128205128205128, 0.05128205128205128, 0.07692307692307693, 0.03418803418803419, 0.06837606837606838, 0.042735042735042736, 0.07692307692307693, 0.08547008547008547, 0.27350427350427353]
pearson_07 = [x * 100 for x in pearson_07]

bar_width = 0.35
index = range(len(pearson_03))
index = [x+bar_width for x in index]

fig = plt.figure(figsize=(14, 14))

plt.bar(index, pearson_03)
plt.ylabel('%')
plt.title('Percentage of users per feature')
plt.xticks(index, ('Hashtags count', 'Favourites count', 'Media count', 'Source', 'Week day/end', 'Day/night', 'Active/passive', 'Mentions count', 'Mentions', 'Coordinates'), rotation='vertical')
plt.savefig('./plots/2/0_3.png')

plt.clf()

plt.bar(index, pearson_05)
plt.ylabel('%')
plt.xticks(index, ('Hashtags count', 'Favourites count', 'Media count', 'Source', 'Week day/end', 'Day/night', 'Active/passive', 'Mentions count', 'Mentions', 'Coordinates'), rotation='vertical')
plt.savefig('./plots/2/0_5.png')

plt.clf()

plt.bar(index, pearson_07)
plt.ylabel('%')
plt.xticks(index, ('Hashtags count', 'Favourites count', 'Media count', 'Source', 'Week day/end', 'Day/night', 'Active/passive', 'Mentions count', 'Mentions', 'Coordinates'), rotation='vertical')
plt.savefig('./plots/2/0_7.png')
