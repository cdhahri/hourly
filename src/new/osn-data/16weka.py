#!/usr/bin/python

import csv
import json
import itertools
        
with open('./ids.json', 'r') as file:
  ids = json.load(file)

ids = [10045092, 1007531, 10449052, 110808568, 111178547, 11346942, 115073079, 117093537, 117567036, 11778632, 118474054, 11922222, 12091872, 121768977, 122737979, 12584222, 1262051, 127828353, 12949482, 1315286089, 13275052, 13385712, 134682826, 13833982, 14000592, 14098915, 14216821, 14223726, 14229632, 14262523, 142683977, 142802575, 14292363, 14372464, 14425872, 14503693, 14555698, 14727300, 14863357, 14945279, 15048222, 15153365, 15164780, 151742290, 151846979, 15226317, 15227820, 153559771, 15413409, 15446261, 15676300, 15725056, 15791092, 15852942, 15868593, 15894712, 15953674, 16188096, 16440181, 16555706, 16561108, 16568592, 16603672, 16679947, 167979424, 16830304, 16885564, 17006237, 172194984, 17264368, 17289508, 17375954, 174727392, 17563699, 176684709, 17680307, 17781987, 178290294, 17850637, 17933990, 18100365, 18107739, 18142778, 18191867, 18209777, 18262261, 18314186, 18332836, 18377613, 18427709, 18467617, 18671170, 1886110453, 189682744, 19007528, 190284308, 19103074, 192285937, 19243536, 19245592, 193877435, 19388800, 19457875, 196140198, 1972501, 19840174, 19864426, 198787694, 20038514, 20421414, 20802652, 20910966, 20993312, 211455134, 21172719, 21285604, 212991627, 21305689, 213170736, 21449222, 214738548, 215464034, 21572497, 216242374, 21690682, 217243955, 21837449, 21846563, 22020614, 22078595, 22097148, 22261883, 22542076, 225671353, 22645597, 22674525, 22804043, 22811768, 22817477, 22884262, 229033311, 22952120, 23118244, 2330667330, 2342442247, 23446307, 23474226, 24096002, 24327327, 24376523, 24383600, 24390992, 2445862754, 24786989, 250272552, 253608676, 25533464, 255570795, 25584144, 25617338, 25777430, 260068676, 260309594, 26059680, 261283186, 26283980, 26299238, 26391913, 26906039, 272932351, 27343715, 275419943, 27560087, 27723901, 27794913, 27803846, 279146998, 28035489, 282400485, 282618471, 28388270, 28457912, 284867370, 28503503, 289677739, 29207028, 29298602, 2940253151, 294149843, 296954894, 299315760, 29934475, 30133362, 30226543, 3025016884, 30298440, 30331250, 306246651, 30863938, 31159879, 314615930, 31512916, 31555593, 31631815, 3166361075, 321141425, 32251134, 32454230, 3270360024, 329359116, 333658600, 33552718, 33577696, 34071208, 351333010, 35170409, 35329667, 35415893, 354899850, 360325583, 36053100, 36432077, 36448706, 365077428, 36947587, 373062772, 37491523, 377551522, 38079841, 38249510, 392894053, 401699169, 405874317, 40820476, 40869137, 410394636, 41163792, 42680864, 42824854, 43772221, 44100334, 442074388, 45088534, 451869026, 45368761, 453800657, 46328692, 466446470, 47133830, 471669821, 481990966, 4893411, 49270310, 493505068, 49578698, 496411172, 50220748, 50356171, 514017846, 516325078, 5415432, 541899796, 543479819, 54449257, 55384716, 565937540, 57043688, 5723252, 57730432, 58270351, 59834599, 60234593, 605291368, 61178222, 612889857, 61532534, 61879870, 6246252, 630768670, 63550078, 63935478, 65114198, 65688198, 65848375, 67679533, 68306612, 70229724, 7078342, 7373072, 74180267, 74558431, 74577773, 74642456, 757492094, 760306657, 76253342, 76464748, 76746082, 77142112, 77147750, 77203118, 782243095, 78705018, 790517, 790958114, 79135413, 803282582, 818155, 82491794, 827297707, 84138140, 867192025, 86924274, 871508102, 87826720, 89361066, 89608638, 90716992, 9131442, 927240422, 930529742, 950435090, 95232266, 95697465, 96147007, 9671232, 96886316, 99586796]

for user_id in ids:
  r = './tweets_selected/features_step3/aggregated/{}.json'.format(user_id)
  w = './tweets_selected/features_step3/aggregated/weka/{}.csv'.format(user_id)

  with open(r, 'r') as file:
    byday_aggregated = json.load(file)

  with open(w, 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(['hashtags_count','mentions_count','favourites_count','media_count','source','week','day_night','active_passive','mentions','top_mentions','coordinates','target'])
    #csv_writer.writerow(['mentions','top_mentions','coordinates','target'])
    for key in sorted(byday_aggregated.keys()):
      mentions = byday_aggregated[key]['mentions']
      if len(mentions) == 0:
        mentions = [-1]
#        continue
      top_mentions = byday_aggregated[key]['top_mentions']
      if len(top_mentions) == 0:
        top_mentions = [-1]
#        continue
      coordinates = byday_aggregated[key]['coordinates']
      if len(coordinates) == 0:
        coordinates = [-1]
#        continue
#      a = [mentions, top_mentions, coordinates]
#      products = list(itertools.product(*a))
#      for prod in products:
      csv_writer.writerow([
        byday_aggregated[key]['hashtags_count'],
        byday_aggregated[key]['mentions_count'],
        byday_aggregated[key]['favourites_count'],
        byday_aggregated[key]['media_count'],
        byday_aggregated[key]['source'],
        byday_aggregated[key]['week'],
        byday_aggregated[key]['day_night'],
        byday_aggregated[key]['active_passive'],
        mentions[0],
        top_mentions[0],
        coordinates[0],
#        prod[0],
#        prod[1],
#        prod[2],
        byday_aggregated[key]['_target']
       ])

'''
w = '/vagrant/data/osn-data/features_step3/aggregated/weka/all.csv'.format(user_id)
with open(w, 'w', newline='', encoding='utf-8') as file:
  csv_writer = csv.writer(file, delimiter=',')
  csv_writer.writerow(['hashtags_count','mentions_count','favourites_count','media_count','source','week','day_night','active_passive','mentions','coordinates','top_mentions','target'])
  for user_id in ids:
    r = '/vagrant/data/osn-data/features_step3/aggregated/{}.json'.format(user_id)
    with open(r, 'r') as file:
      byday_aggregated = json.load(file)

    for key in sorted(byday_aggregated.keys()):
      csv_writer.writerow([
        byday_aggregated[key]['hashtags_count'],
        byday_aggregated[key]['mentions_count'],
        byday_aggregated[key]['favourites_count'],
        byday_aggregated[key]['media_count'],
        byday_aggregated[key]['source'],
        byday_aggregated[key]['week'],
        byday_aggregated[key]['day_night'],
        byday_aggregated[key]['active_passive'],
        byday_aggregated[key]['mentions'],
        byday_aggregated[key]['coordinates'],
        byday_aggregated[key]['top_mentions'],
        byday_aggregated[key]['_target']
      ])
'''
