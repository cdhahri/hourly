#!/usr/bin/python

import json
from scipy.stats import pearsonr
from scipy import stats

with open('./ids.json', 'r') as file:
  ids = json.load(file)

ids = [10045092, 101496212, 1021239846, 102464379, 103114245, 103695733, 104852013, 10521002, 106104712, 108944858, 109223169, 10929372, 109485267, 111178547, 11126582, 111454868, 112490071, 112858627, 11312992, 113441429, 11346942, 11437162, 115138473, 11661442, 117562901, 117567036, 1177083624, 11778632, 117870724, 117987103, 118459389, 118474054, 119436439, 119773854, 119979433, 120268489, 12091872, 121768977, 1231465759, 1236198937, 124849194, 12584222, 1260994465, 1262051, 12681982, 12736092, 12865902, 129720477, 1297731522, 132191278, 13234182, 133165344, 133794989, 13460112, 13630552, 1371201120, 137123695, 13746182, 13833982, 13955342, 14000592, 14052274, 14238085, 142406505, 14262523, 142683977, 14311409, 14326247, 14329827, 14341596, 14353656, 14372827, 14506340, 14558776, 14610613, 14683259, 14685524, 147029225, 14727300, 14760624, 14812945, 14863357, 14900774, 14901281, 1498798484, 15030109, 150693965, 15121058, 15136898, 15164780, 151742290, 151846979, 15227820, 15261709, 15295567, 15300227, 15307110, 15370082, 15412985, 15473636, 15479048, 15482020, 15526160, 15646009, 15676300, 15844952, 15941891, 15953674, 16059345, 16090559, 16097172, 16133557, 16188096, 16205956, 16242432, 16381466, 16427456, 16440181, 16516286, 16525053, 1652943942, 16539750, 16555706, 16561108, 16679947, 16721983, 16754274, 167544646, 168752747, 1690021310, 16925606, 169359222, 16983823, 1707284881, 17073407, 17264368, 17289508, 173246653, 17395031, 174727392, 17500378, 17611773, 17638843, 176684709, 17679900, 17781987, 178183112, 17850637, 17997140, 18034005, 18100387, 18107739, 18142778, 18162777, 18262261, 18342516, 18377613, 18467617, 186710373, 18671170, 18701575, 18727385, 18774603, 18802512, 18853460, 1886110453, 19051137, 19103074, 192285937, 19245592, 19257498, 19273553, 193047373, 193055620, 19429282, 194460357, 194844686, 1956601, 19640038, 19840174, 199082056, 19981283, 20022522, 20061458, 20071366, 20193817, 201991499, 20224255, 202401823, 20405425, 20540225, 20802652, 20910966, 20920548, 20993312, 21018190, 21051121, 21210758, 212732867, 21522245, 21551845, 215538575, 2155451028, 21572497, 21580279, 216242374, 21645721, 21668323, 21689878, 21690151, 21690682, 217243955, 21820444, 21841580, 218915630, 22020614, 22078595, 22087330, 220900238, 22097148, 22186481, 222793383, 22336264, 2235343141, 224119575, 22542076, 225671353, 2259666550, 22653653, 22674525, 22738480, 22804043, 22835967, 22884262, 229191240, 23118244, 231435258, 231850668, 23474226, 234838196, 2361416437, 23645346, 23957246, 24071954, 2421127980, 24272045, 2431492819, 24637189, 24656873, 247140396, 248969328, 24916659, 25023487, 251801850, 25298225, 25338634, 253608676, 25519141, 255570795, 25772199, 25794087, 2587937208, 260309594, 261096069, 26110977, 26111925, 26412887, 26598221, 27015204, 270542169, 271549247, 272932351, 27312014, 27328412, 275419943, 27560087, 276363610, 27723901, 27797696, 27817688, 27906446, 28035489, 281800166, 281987255, 28207983, 28258368, 282618471, 28359041, 28388270, 2840628328, 284867370, 28503503, 285877073, 28667128, 28744549, 28773485, 2885653782, 2900512275, 29046663, 292121179, 29263484, 294149843, 29548394, 296954894, 2971829547, 29838696, 29873471, 29892110, 299315760, 29934475, 30133362, 30226543, 30298440, 30347402, 30576990, 306246651, 31159879, 314424424, 314615930, 31555593, 32251134, 32549410, 329359116, 33506364, 33552718, 33667217, 3394771, 34071208, 34415580, 348307387, 348356792, 351333010, 35135168, 35170409, 352061150, 35415893, 354899850, 35637918, 35704124, 3582641, 362355201, 36432077, 365077428, 367939756, 37222902, 37491523, 381280010, 381671017, 38249510, 38364927, 385525679, 391740160, 391780847, 392894053, 39316272, 39487901, 39944028, 403046769, 406171575, 40687730, 4080133834, 409530974, 41043058, 41097402, 41416430, 419411767, 42074324, 42680864, 430100347, 433995523, 43787354, 43893817, 44318556, 44363833, 44536674, 46328692, 4655791161, 47011143, 471669821, 47332084, 47473194, 47505761, 476016333, 48404991, 48522285, 49578698, 49698488, 50281618, 51355424, 521091861, 52418570, 525324664, 52733565, 531084450, 54463831, 54991079, 5565592, 56597284, 566866170, 56784216, 57043688, 57730432, 578435610, 58652731, 59673118, 59699232, 5976352, 59809965, 59947676, 60061084, 60234593, 608315409, 61532534, 61879870, 622391163, 625299965, 62743668, 630768670, 631406811, 6314782, 63191823, 63550078, 64375952, 65647574, 65688198, 65869518, 65946149, 66576457, 66833407, 71154429, 71422674, 71450773, 723615044, 73000498, 734303, 7373072, 738786882, 74558431, 754714, 76024450, 76253342, 770922379, 77147750, 77203118, 7827172, 78503065, 78705018, 790517, 791125, 794330748, 79684030, 8030212, 803282582, 812208710, 820607167, 827297707, 83170594, 8395322, 84138140, 85419044, 8546332, 86228984, 874316941, 87967892, 89608638, 902226338, 91165750, 9131442, 92623, 927771, 92819377, 95037009, 950435090, 9644892, 98119947, 99586796]

total = 0
total_hashtags_count = 0
total_mentions_count = 0
total_favourites_count = 0
total_media_count = 0
total_source = 0
total_week = 0
total_day_night = 0
total_active_passive = 0
total_mentions = 0
total_coordinates = 0
total_top_mentions = 0

hashtags_count_pearsons = []
mentions_count_pearsons = []
favourites_count_pearsons = []
media_count_pearsons = []
source_pearsons = []
week_pearsons = []
day_night_pearsons = []
active_passive_pearsons = []
mentions_pearsons = []
coordinates_pearsons = []
top_mentions_pearsons = []

for user_id in ids:
  r = './tweets_selected/features_step3/aggregated/10/{}.json'.format(user_id)

#  try:
  with open(r, 'r') as file:
    byday_aggregated = json.load(file)
#  except FileNotFoundError:
#    continue

  target = []
  hashtags_count = []      
  mentions_count = []
  favourites_count = []
  media_count = []
  source = []
  week = []
  day_night = []
  active_passive = []
  mentions = []
  coordinates = []
  top_mentions = []
  for key in sorted(byday_aggregated.keys()):
    target.append(byday_aggregated[key]['_target'])
    hashtags_count.append(byday_aggregated[key]['hashtags_count'])
    mentions_count.append(byday_aggregated[key]['mentions_count'])
    favourites_count.append(byday_aggregated[key]['favourites_count'])
    media_count.append(byday_aggregated[key]['media_count'])
    source.append(byday_aggregated[key]['source'])
    week.append(byday_aggregated[key]['week'])
    day_night.append(byday_aggregated[key]['day_night'])
    active_passive.append(byday_aggregated[key]['active_passive'])
    mentions.append(byday_aggregated[key]['mentions'])
    coordinates.append(byday_aggregated[key]['coordinates'])
    top_mentions.append(byday_aggregated[key]['top_mentions'])

  if len(set(target)) < 2:
    continue

  total += 1

#  target = stats.zscore(target).tolist()

  #'''
  hashtags_count = stats.zscore(hashtags_count).tolist()
  hashtags_count_pearson = pearsonr(target, hashtags_count)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(hashtags_count_pearson[0]) > percentage and abs(hashtags_count_pearson[1]) < 0.05:
      hashtags_count_pearsons.append(abs(hashtags_count_pearson[0]))
#      total_hashtags_count += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(hashtags_count_pearson[0]))
#    print('@{}'.format(hashtags_count_pearson[1]))
  #'''

  #'''
  mentions_count = stats.zscore(mentions_count).tolist()
  mentions_count_pearson = pearsonr(target, mentions_count)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(mentions_count_pearson[0]) > percentage and abs(mentions_count_pearson[1]) < 0.05:
      mentions_count_pearsons.append(abs(mentions_count_pearson[0]))
#      total_mentions_count += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(mentions_count_pearson[0]))
#    print('@{}'.format(mentions_count_pearson[1]))
  #'''

  #'''
  favourites_count = stats.zscore(favourites_count).tolist()
  favourites_count_pearson = pearsonr(target, favourites_count)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(favourites_count_pearson[0]) > percentage and abs(favourites_count_pearson[1]) < 0.05:
      favourites_count_pearsons.append(abs(favourites_count_pearson[0]))
#      total_favourites_count += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(favourites_count_pearson[0]))
#    print('@{}'.format(favourites_count_pearson[1]))
  #'''

  #'''
  media_count = stats.zscore(media_count).tolist()
  media_count_pearson = pearsonr(target, media_count)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(media_count_pearson[0]) > percentage and abs(media_count_pearson[1]) < 0.05:
      media_count_pearsons.append(abs(media_count_pearson[0]))
#      total_media_count += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(media_count_pearson[0]))
#    print('@{}'.format(media_count_pearson[1]))
  #'''

  #'''
  if len(set(source)) < 2:
    continue
  source = stats.zscore(source).tolist()
  source_pearson = pearsonr(target, source)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(source_pearson[0]) > percentage and abs(source_pearson[1]) < 0.05:
      source_pearsons.append(abs(source_pearson[0]))
#      total_source += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(source_pearson[0]))
#    print('@{}'.format(source_pearson[1]))
  #'''

  #'''
  week = stats.zscore(week).tolist()
  week_pearson = pearsonr(target, week)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(week_pearson[0]) > percentage and abs(week_pearson[1]) < 0.05:
      week_pearsons.append(abs(week_pearson[0]))
#      total_week += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(week_pearson[0]))
#    print('@{}'.format(week_pearson[1]))
  #'''

  #'''
  if len(set(day_night)) < 2:
    continue
  day_night = stats.zscore(day_night).tolist()
  day_night_pearson = pearsonr(target, day_night)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(day_night_pearson[0]) > percentage and abs(day_night_pearson[1]) < 0.05:
      day_night_pearsons.append(abs(day_night_pearson[0]))
#      total_day_night += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(active_passive_pearson[0]))
#    print('@{}'.format(active_passive_pearson[1]))
  #'''

  #'''
  if len(set(active_passive)) < 2:
    continue
  active_passive = stats.zscore(active_passive).tolist()
  active_passive_pearson = pearsonr(target, active_passive)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(active_passive_pearson[0]) > percentage and abs(active_passive_pearson[1]) < 0.05:
      active_passive_pearsons.append(abs(active_passive_pearson[0]))
#      total_active_passive += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(active_passive_pearson[0]))
#    print('@{}'.format(active_passive_pearson[1]))
  #'''

  #'''
  target_mentions = []
  mentions_mentions = []
  for i in range(len(target)):
    for j in range(len(mentions[i])):
      #?
      #if mentions[i][j] == -100:
      #  continue
      target_mentions.append(target[i])
      mentions_mentions.append(mentions[i][j])
  if len(set(mentions_mentions)) < 2:
    continue
  mentions_mentions = stats.zscore(mentions_mentions).tolist()
  mentions_pearson = pearsonr(target_mentions, mentions_mentions)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(mentions_pearson[0]) > percentage and abs(mentions_pearson[1]) < 0.05:
      mentions_pearsons.append(abs(mentions_pearson[0]))
#      total_mentions += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(mentions_pearson[0]))
#    print('@{}'.format(mentions_pearson[1]))
  #'''

  #'''
  target_coordinates = []
  coordinates_coordinates = []
  for i in range(len(target)):
    for j in range(len(coordinates[i])):
      if coordinates[i][j] == -100:
        continue
      target_coordinates.append(target[i])
      coordinates_coordinates.append(coordinates[i][j])
  if len(set(coordinates_coordinates)) < 2:
    continue
  coordinates_coordinates = stats.zscore(coordinates_coordinates).tolist()
  coordinates_pearson = pearsonr(target_coordinates, coordinates_coordinates)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(coordinates_pearson[0]) > percentage and abs(coordinates_pearson[1]) < 0.05:
      coordinates_pearsons.append(abs(coordinates_pearson[0]))
#      total_coordinates += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(coordinates_pearson[0]))
#    print('@{}'.format(coordinates_pearson[1]))
  #'''

  #'''
  target_top_mentions = []
  top_mentions_mentions = []
  for i in range(len(target)):
    for j in range(len(top_mentions[i])):
      #?
      #if top_mentions[i][j] == -100:
      #  continue
      target_top_mentions.append(target[i])
      top_mentions_mentions.append(top_mentions[i][j])
  if len(set(top_mentions_mentions)) < 2:
    continue
  top_mentions_mentions = stats.zscore(top_mentions_mentions).tolist()
  top_mentions_pearson = pearsonr(target_top_mentions, top_mentions_mentions)
#  for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
  for percentage in [0.3]:
    if abs(top_mentions_pearson[0]) > percentage and abs(top_mentions_pearson[1]) < 0.05:
      top_mentions_pearsons.append(abs(top_mentions_pearson[0]))
#      total_top_mentions += 1
#      print(percentage)
      print(user_id)
#    print('@{}'.format(top_mentions_pearson[0]))
#    print('@{}'.format(top_mentions_pearson[1]))
  #'''

'''
print('{}'.format(total_hashtags_count/total))
print('{}'.format(total_mentions_count/total))
print('{}'.format(total_favourites_count/total))
print('{}'.format(total_media_count/total))
print('{}'.format(total_source/total))
print('{}'.format(total_week/total))
print('{}'.format(total_day_night/total))
print('{}'.format(total_active_passive/total))
print('{}'.format(total_mentions/total))
print('{}'.format(total_coordinates/total))
print('{}'.format(total_top_mentions/total))
'''

'''
import numpy as np

a = np.array([hashtags_count_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([mentions_count_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([favourites_count_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([media_count_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([source_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([week_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([day_night_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([active_passive_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([mentions_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
print('')
a = np.array([coordinates_pearsons])
print(len(list(a)[0]))
print(np.mean(a))
print(np.var(a))
'''
