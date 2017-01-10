#!/usr/bin/python

import json
from scipy.stats import pearsonr
from scipy import stats

with open('./ids.json', 'r') as file:
  ids = json.load(file)

ids = [10045092, 1007531, 10449052, 110808568, 111178547, 11346942, 115073079, 117093537, 117567036, 11778632, 118474054, 11922222, 12091872, 121768977, 122737979, 12584222, 1262051, 127828353, 12949482, 1315286089, 13275052, 13385712, 134682826, 13833982, 14000592, 14098915, 14216821, 14223726, 14229632, 14262523, 142683977, 142802575, 14292363, 14372464, 14425872, 14503693, 14555698, 14727300, 14863357, 14945279, 15048222, 15153365, 15164780, 151742290, 151846979, 15226317, 15227820, 153559771, 15413409, 15446261, 15676300, 15725056, 15791092, 15852942, 15868593, 15894712, 15953674, 16188096, 16440181, 16555706, 16561108, 16568592, 16603672, 16679947, 167979424, 16830304, 16885564, 17006237, 172194984, 17264368, 17289508, 17375954, 174727392, 17563699, 176684709, 17680307, 17781987, 178290294, 17850637, 17933990, 18100365, 18107739, 18142778, 18191867, 18209777, 18262261, 18314186, 18332836, 18377613, 18427709, 18467617, 18671170, 1886110453, 189682744, 19007528, 190284308, 19103074, 192285937, 19243536, 19245592, 193877435, 19388800, 19457875, 196140198, 1972501, 19840174, 19864426, 198787694, 20038514, 20421414, 20802652, 20910966, 20993312, 211455134, 21172719, 21285604, 212991627, 21305689, 213170736, 21449222, 214738548, 215464034, 21572497, 216242374, 21690682, 217243955, 21837449, 21846563, 22020614, 22078595, 22097148, 22261883, 22542076, 225671353, 22645597, 22674525, 22804043, 22811768, 22817477, 22884262, 229033311, 22952120, 23118244, 2330667330, 2342442247, 23446307, 23474226, 24096002, 24327327, 24376523, 24383600, 24390992, 2445862754, 24786989, 250272552, 253608676, 25533464, 255570795, 25584144, 25617338, 25777430, 260068676, 260309594, 26059680, 261283186, 26283980, 26299238, 26391913, 26906039, 272932351, 27343715, 275419943, 27560087, 27723901, 27794913, 27803846, 279146998, 28035489, 282400485, 282618471, 28388270, 28457912, 284867370, 28503503, 289677739, 29207028, 29298602, 2940253151, 294149843, 296954894, 299315760, 29934475, 30133362, 30226543, 3025016884, 30298440, 30331250, 306246651, 30863938, 31159879, 314615930, 31512916, 31555593, 31631815, 3166361075, 321141425, 32251134, 32454230, 3270360024, 329359116, 333658600, 33552718, 33577696, 34071208, 351333010, 35170409, 35329667, 35415893, 354899850, 360325583, 36053100, 36432077, 36448706, 365077428, 36947587, 373062772, 37491523, 377551522, 38079841, 38249510, 392894053, 401699169, 405874317, 40820476, 40869137, 410394636, 41163792, 42680864, 42824854, 43772221, 44100334, 442074388, 45088534, 451869026, 45368761, 453800657, 46328692, 466446470, 47133830, 471669821, 481990966, 4893411, 49270310, 493505068, 49578698, 496411172, 50220748, 50356171, 514017846, 516325078, 5415432, 541899796, 543479819, 54449257, 55384716, 565937540, 57043688, 5723252, 57730432, 58270351, 59834599, 60234593, 605291368, 61178222, 612889857, 61532534, 61879870, 6246252, 630768670, 63550078, 63935478, 65114198, 65688198, 65848375, 67679533, 68306612, 70229724, 7078342, 7373072, 74180267, 74558431, 74577773, 74642456, 757492094, 760306657, 76253342, 76464748, 76746082, 77142112, 77147750, 77203118, 782243095, 78705018, 790517, 790958114, 79135413, 803282582, 818155, 82491794, 827297707, 84138140, 867192025, 86924274, 871508102, 87826720, 89361066, 89608638, 90716992, 9131442, 927240422, 930529742, 950435090, 95232266, 95697465, 96147007, 9671232, 96886316, 99586796]

#ids = [10045092, 1007531, 110808568, 11346942, 11922222, 12091872, 121768977, 12949482, 1315286089, 13385712, 134682826, 14223726, 14229632, 142683977, 14292363, 14425872, 14503693, 14727300, 14863357, 15048222, 15153365, 15164780, 151742290, 15413409, 15676300, 15791092, 15894712, 15953674, 16568592, 17006237, 17289508, 17563699, 176684709, 17680307, 17850637, 17933990, 18100365, 18142778, 18191867, 18209777, 18262261, 18314186, 18377613, 18467617, 1886110453, 19007528, 190284308, 19103074, 19243536, 19245592, 193877435, 196140198, 1972501, 20038514, 20421414, 20802652, 211455134, 21172719, 21305689, 213170736, 21449222, 214738548, 215464034, 21572497, 217243955, 21837449, 22261883, 22645597, 22811768, 22952120, 23118244, 2330667330, 24096002, 24327327, 24376523, 24383600, 2445862754, 24786989, 250272552, 253608676, 25533464, 25777430, 260309594, 26059680, 26283980, 26299238, 26391913, 26906039, 272932351, 27343715, 275419943, 27560087, 27723901, 27794913, 282400485, 282618471, 28388270, 28457912, 284867370, 29207028, 2940253151, 299315760, 3025016884, 30863938, 314615930, 32454230, 3270360024, 33552718, 351333010, 35170409, 35329667, 360325583, 37491523, 377551522, 405874317, 40820476, 40869137, 410394636, 41163792, 42824854, 43772221, 442074388, 45088534, 453800657, 46328692, 471669821, 481990966, 49270310, 493505068, 49578698, 496411172, 50220748, 50356171, 5415432, 543479819, 57043688, 5723252, 59834599, 60234593, 605291368, 61178222, 61879870, 6246252, 63935478, 65114198, 67679533, 68306612, 70229724, 74180267, 74577773, 74642456, 757492094, 760306657, 76746082, 77142112, 782243095, 78705018, 79135413, 818155, 82491794, 867192025, 87826720, 89361066, 9131442, 930529742, 95232266, 95697465, 96147007, 9671232, 96886316]

#ids = [110808568, 11922222, 12091872, 121768977, 12949482, 13385712, 134682826, 142683977, 14503693, 14727300, 14863357, 15153365, 15413409, 15953674, 16568592, 17006237, 17563699, 176684709, 17680307, 17850637, 18100365, 18142778, 18191867, 18209777, 18262261, 18314186, 18377613, 18467617, 19007528, 190284308, 19243536, 19245592, 193877435, 196140198, 20038514, 20421414, 211455134, 21172719, 21449222, 215464034, 21572497, 21837449, 22261883, 22811768, 22952120, 23118244, 2330667330, 24096002, 24327327, 24383600, 2445862754, 24786989, 250272552, 253608676, 25777430, 260309594, 26059680, 26283980, 26299238, 272932351, 27343715, 275419943, 27560087, 27794913, 282400485, 282618471, 28388270, 28457912, 284867370, 29207028, 2940253151, 299315760, 3025016884, 314615930, 33552718, 351333010, 35170409, 35329667, 360325583, 377551522, 405874317, 40820476, 410394636, 41163792, 45088534, 453800657, 46328692, 481990966, 49270310, 493505068, 49578698, 496411172, 50220748, 5415432, 543479819, 57043688, 5723252, 59834599, 61178222, 6246252, 68306612, 74180267, 74577773, 760306657, 782243095, 78705018, 79135413, 818155, 867192025, 87826720, 89361066, 9131442, 930529742, 95232266, 96147007, 9671232, 96886316]

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
  r = './tweets_selected/features_step3/aggregated/{}.json'.format(user_id)

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
      total_hashtags_count += 1
#      print(percentage)
#      print(user_id)
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
      total_mentions_count += 1
#      print(percentage)
#      print(user_id)
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
      total_favourites_count += 1
#      print(percentage)
#      print(user_id)
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
      total_media_count += 1
#      print(percentage)
#      print(user_id)
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
      total_source += 1
#      print(percentage)
#      print(user_id)
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
      total_week += 1
#      print(percentage)
#      print(user_id)
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
      total_day_night += 1
#      print(percentage)
#      print(user_id)
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
      total_active_passive += 1
#      print(percentage)
#      print(user_id)
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
      total_mentions += 1
#      print(percentage)
#      print(user_id)
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
      total_coordinates += 1
#      print(percentage)
#      print(user_id)
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
      total_top_mentions += 1
#      print(percentage)
#      print(user_id)
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

