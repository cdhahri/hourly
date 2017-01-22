#!/usr/bin/python

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]

import csv
import json
import itertools
        
with open('./ids.json', 'r') as file:
  ids = json.load(file)

ids = [1007531, 1021239846, 10449052, 104852013, 10521002, 110808568, 11126582, 111454868, 115073079, 115171979, 11661442, 117093537, 117567036, 11778632, 11922222, 119773854, 11987272, 119979433, 121768977, 122737979, 123059038, 1236198937, 123745496, 126416030, 127828353, 128774572, 12949482, 132191278, 13275052, 13385712, 134682826, 136422661, 13833982, 14000592, 140289159, 14052274, 14098915, 14103278, 141219265, 14216821, 14223726, 14229632, 142683977, 142802575, 14292363, 14372464, 14372827, 14425872, 14555698, 14683259, 14701396, 14863357, 14945279, 14981286, 15121058, 15153365, 151742290, 151846979, 15226317, 15232993, 15276360, 15307110, 153559771, 15413409, 15446261, 15464753, 15791092, 15852942, 15868593, 15894712, 16218208, 16264556, 163554714, 16516286, 1652943942, 16534580, 16568592, 16679947, 167979424, 16830304, 16885564, 17006237, 172194984, 17375954, 17395031, 174727392, 17563699, 176684709, 17680307, 178290294, 18100365, 18191867, 18209777, 18314186, 18332836, 18427709, 184696502, 189682744, 19007528, 190284308, 190676679, 19243536, 19245592, 19257498, 193047373, 193877435, 19388800, 19410596, 19457875, 1956601, 196140198, 1972501, 19864426, 198787694, 19896022, 20038514, 201991499, 202401823, 20421414, 20993312, 21051121, 211455134, 21172719, 21285604, 212991627, 21305689, 213170736, 21449222, 214738548, 2151218504, 21527558, 215464034, 21580279, 21690151, 21833864, 21837449, 21846563, 21946201, 22261883, 22336264, 225671353, 22645597, 22723261, 22800249, 22804043, 22811768, 22817477, 22839859, 229033311, 22952120, 22963405, 231435258, 2330667330, 2342442247, 23446307, 23474226, 23672351, 23879537, 24096002, 24327327, 24376523, 24383600, 24390992, 2445862754, 24691627, 24786989, 2493269757, 249675888, 250272552, 25298225, 25338634, 253608676, 25519141, 25533464, 255570795, 25584144, 25617338, 257719610, 25777430, 25868964, 260068676, 26010109, 26059680, 261283186, 26184260, 26283980, 26299238, 263591835, 26391913, 26906039, 2727484299, 272932351, 27343715, 275419943, 27794913, 27803846, 279146998, 282400485, 282618471, 28388270, 28457912, 28773485, 2885653782, 289677739, 292121179, 29298602, 2940253151, 294893966, 29548394, 2962912317, 299315760, 301664439, 30226543, 3025016884, 30331250, 30576990, 30863938, 31512916, 31631815, 3166361075, 321141425, 32138209, 32251134, 32454230, 3270360024, 331647862, 33190301, 333658600, 33552718, 33577696, 33982553, 33987373, 34262883, 34415580, 350972055, 35135168, 35250045, 35329667, 354045422, 35480471, 354899850, 35611379, 3582641, 35897727, 360325583, 36053100, 36432077, 36448706, 365077428, 367939756, 36947587, 373062772, 37491523, 38079841, 382438785, 38270314, 38342320, 401699169, 405874317, 40820476, 40869137, 409530974, 410394636, 41163792, 41416430, 419311791, 41983195, 423862419, 44100334, 442074388, 44433973, 45088534, 451869026, 45368761, 453800657, 46302278, 46535963, 47133830, 47473194, 474874843, 481990966, 487172765, 4893411, 49270310, 493505068, 49578698, 496411172, 50220748, 50356171, 505463588, 514017846, 516325078, 52382923, 5366432, 5415432, 541899796, 543479819, 54449257, 55384716, 565937540, 5723252, 58270351, 59726300, 5981642, 59834599, 602188797, 605291368, 61012093, 61178222, 612889857, 61879870, 62947925, 63935478, 64035286, 64602223, 65114198, 65545659, 65848375, 65946149, 67679533, 68306612, 70229724, 7078342, 74577773, 74642456, 74765251, 754714, 757492094, 760306657, 76464748, 76746082, 77142112, 782243095, 790958114, 792316573, 812208710, 818155, 820607167, 82491794, 83170594, 867192025, 86924274, 872372707, 874316941, 8776002, 87826720, 90716992, 927240422, 930529742, 95037009, 95697465, 95954693, 96147007, 96886316, 97532492]

for user_id in ids:
  for percentage in percentages:
    r = './tweets_selected/features_step3/aggregated/{}/{}.json'.format(percentage, user_id)
    w = './tweets_selected/features_step3/aggregated/weka/{}/{}.csv'.format(percentage, user_id)

    with open(r, 'r') as file:
      byday_aggregated = json.load(file)

    with open(w, 'w', newline='', encoding='utf-8') as file:
      csv_writer = csv.writer(file, delimiter=',')
      csv_writer.writerow(['hashtags_count','mentions_count','favourites_count','media_count','source','week','day_night','active_passive','mentions','top_mentions','coordinates','target'])
      # csv_writer.writerow(['count_all_capital','count_exclamation_mark','count_question_mark','count_negative_word','count_positive_word','exist_more_than_three_dots','exist_more_than_three_vowels','target'])
      for key in sorted(byday_aggregated.keys()):
        mentions = byday_aggregated[key]['mentions']
        if len(mentions) == 0:
          mentions = [-1]
        top_mentions = byday_aggregated[key]['top_mentions']
        if len(top_mentions) == 0:
          top_mentions = [-1]
        coordinates = byday_aggregated[key]['coordinates']
        if len(coordinates) == 0:
          coordinates = [-1]
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

          # byday_aggregated[key]['count_all_capital'],
          # byday_aggregated[key]['count_exclamation_mark'],
          # byday_aggregated[key]['count_question_mark'],
          # byday_aggregated[key]['count_negative_word'],
          # byday_aggregated[key]['count_positive_word'],
          # byday_aggregated[key]['exist_more_than_three_dots'],
          # byday_aggregated[key]['exist_more_than_three_vowels'],

  #        prod[0], NO
  #        prod[1], NO
  #        prod[2], NO
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
