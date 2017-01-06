#!/usr/bin/python

import csv
import json
import itertools
        
with open('./ids.json', 'r') as file:
  ids = json.load(file)

#ids = [112858627, 113441429, 115073079, 117093537, 11922222, 119773854, 123745496, 126416030, 127828353, 12865902, 134682826, 13833982, 14000592, 14341596, 14852278, 14900774, 15121058, 151742290, 15413409, 15446261, 15473636, 15676300, 15894712, 16097172, 16440181, 1644226526, 16603672, 168752747, 1690021310, 17006237, 172194984, 178290294, 17850637, 18034005, 18107739, 18262261, 18314186, 18332836, 18467617, 18671170, 18701575, 19243536, 19257498, 193055620, 193877435, 19388800, 1956601, 19981283, 20910966, 20920548, 20993312, 21172719, 21210758, 21449222, 21522245, 21572497, 21846563, 21946201, 22097148, 222793383, 224119575, 23647445, 24096002, 2421127980, 24272045, 24376523, 24383600, 24691627, 247140396, 248969328, 25197017, 253608676, 25519141, 25533464, 26059680, 26110977, 26111184, 26906039, 272932351, 27312014, 27723901, 27906446, 28359041, 28388270, 285877073, 28744549, 292121179, 2940253151, 294149843, 299315760, 3025016884, 30331250, 30863938, 321141425, 3270360024, 329359116, 35135168, 35250045, 36432077, 36448706, 365077428, 37208269, 381280010, 38249510, 38364927, 403046769, 405874317, 40869137, 41097402, 41416430, 44363833, 44536674, 45088534, 451869026, 46328692, 487172765, 4893411, 49698488, 541899796, 56784216, 5723252, 65848375, 7078342, 71422674, 73000498, 74765251, 760306657, 76746082, 770922379, 7827172, 8395322, 85419044, 859417921, 86924274, 871508102, 874316941, 89361066, 92623, 927240422, 927771, 95037009, 950435090, 95232266, 95697465, 97532492]

#ids = [1007531, 101496212, 10449052, 109485267, 110808568, 111454868, 117093537, 11778632, 118474054, 11922222, 119773854, 123059038, 12949482, 1315286089, 132191278, 13385712, 14103278, 141219265, 14216821, 14223726, 142683977, 142802575, 14292363, 14372827, 14425872, 14555698, 14863357, 15226317, 15232993, 15276360, 153559771, 15370082, 15413409, 15464753, 15791092, 15852942, 15868593, 15894712, 163554714, 16525053, 16603672, 16830304, 17006237, 17289508, 17375954, 17563699, 17680307, 178290294, 17850637, 18100365, 18142778, 18191867, 18209777, 18314186, 18332836, 18701575, 1886110453, 189682744, 19007528, 190284308, 19243536, 193877435, 19388800, 19457875, 194844686, 196140198, 1972501, 20038514, 202401823, 20421414, 211455134, 211543157, 21285604, 21305689, 213170736, 21449222, 214738548, 2151218504, 21522245, 21527558, 21580279, 21833864, 21837449, 21846563, 218915630, 21946201, 22087330, 220900238, 224950158, 22645597, 22811768, 22839859, 22884262, 229033311, 22952120, 2330667330, 2342442247, 23879537, 24376523, 24390992, 2445862754, 24786989, 25023487, 250272552, 25533464, 25584144, 25617338, 25772199, 25777430, 25868964, 260068676, 26059680, 26110977, 261283186, 26184260, 26299238, 26906039, 27723901, 27803846, 279146998, 282400485, 28457912, 284867370, 29298602, 2940253151, 3025016884, 30331250, 30863938, 31512916, 31631815, 3270360024, 331647862, 333658600, 33577696, 33706211, 3394771, 33982553, 35170409, 35329667, 354045422, 35480471, 35897727, 360325583, 36432077, 365077428, 367939756, 36947587, 37208269, 382438785, 38342320, 401699169, 403046769, 405874317, 40820476, 410394636, 41163792, 41416430, 41983195, 423862419, 42824854, 44100334, 44433973, 45088534, 451869026, 453800657, 46535963, 47473194, 481990966, 4893411, 49270310, 496411172, 50356171, 505463588, 514017846, 52382923, 5366432, 5415432, 541899796, 543479819, 54449257, 5723252, 58270351, 5981642, 59834599, 602188797, 60234593, 605291368, 61178222, 612889857, 63935478, 64602223, 65545659, 65848375, 68306612, 7078342, 74577773, 74642456, 754714, 757492094, 76746082, 77142112, 77147750, 782243095, 818155, 82491794, 867192025, 86924274, 872372707, 8776002, 89361066, 90716992, 927240422, 930529742, 95037009, 95697465, 96147007]

for user_id in ids:
  r = './tweets_selected/features_step3/aggregated/{}.json'.format(user_id)
  w = './tweets_selected/features_step3/aggregated/weka/{}.csv'.format(user_id)

  with open(r, 'r') as file:
    byday_aggregated = json.load(file)

  with open(w, 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file, delimiter=',')
    #csv_writer.writerow(['hashtags_count','mentions_count','favourites_count','media_count','source','week','day_night','active_passive','mentions','top_mentions','coordinates','target'])
    csv_writer.writerow(['mentions','top_mentions','coordinates','target'])
    for key in sorted(byday_aggregated.keys()):
      mentions = byday_aggregated[key]['mentions']
      if len(mentions) == 0:
        #mentions = [-1]
        continue
      top_mentions = byday_aggregated[key]['top_mentions']
      if len(top_mentions) == 0:
        #top_mentions = [-1]
        continue
      coordinates = byday_aggregated[key]['coordinates']
      if len(coordinates) == 0:
        #coordinates = [-1]
        continue
      a = [mentions, top_mentions, coordinates]
      products = list(itertools.product(*a))
      for prod in products:
        csv_writer.writerow([
#          byday_aggregated[key]['hashtags_count'],
#          byday_aggregated[key]['mentions_count'],
#          byday_aggregated[key]['favourites_count'],
#          byday_aggregated[key]['media_count'],
#          byday_aggregated[key]['source'],
#          byday_aggregated[key]['week'],
#          byday_aggregated[key]['day_night'],
#          byday_aggregated[key]['active_passive'],
          prod[0],
          prod[1],
          prod[2],
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
