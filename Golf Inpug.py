import numpy as np
import pandas as pd
import os
from num2words import num2words

#assigning appropriate csvs to variables
master18csv = "18holemaster.csv"
pars18csv = "18holepars.csv"
fwys18csv = "18holefwys.csv"
gir18csv = "18holegir.csv"
putts18csv = "18holeputts.csv"
scores18csv = "18holescores.csv"
yards18csv = "18holeyardages.csv"
hdcps18csv = "18holehandicaps.csv"
#assigning appropriate csvs to variables
master9csv = "9holemaster.csv"
pars9csv = "9holepars.csv"
fwys9csv = "9holefwys.csv"
gir9csv = "9holegir.csv"
putts9csv = "9holeputts.csv"
scores9csv = "9holescores.csv"
yards9csv = "9holeyardages.csv"
hdcps9csv = "9holehandicaps.csv"

#function that asks user for the number of holes played, and loads in appropriate data files
def howmanyholes():
    while True:
        num_holes = int(input('How many holes did you play? '))
        if num_holes not in (9, 18):
            print('Only enter 9 or 18 hole scores.')
        else:
            if num_holes == 9:
                 master_df = pd.read_csv(master9csv, index_col = 0)
                 pars_df = pd.read_csv(pars9csv, index_col = 0)
                 fwys_df = pd.read_csv(fwys9csv, index_col = 0)
                 gir_df = pd.read_csv(gir9csv, index_col = 0)
                 putts_df = pd.read_csv(putts9csv, index_col = 0)
                 scores_df = pd.read_csv(scores9csv, index_col = 0)
                 yards_df = pd.read_csv(yards9csv, index_col = 0)
                 hdcps_df = pd.read_csv(hdcps9csv, index_col = 0)
                 num_rounds = len(master_df) + 1
                 print('This is your ' + num2words(num_rounds, lang = 'en', to = 'ordinal_num') + ' 9 hole round')
            elif num_holes == 18:
                 master_df = pd.read_csv(master18csv, index_col = 0)
                 pars_df = pd.read_csv(pars18csv, index_col = 0)
                 fwys_df = pd.read_csv(fwys18csv, index_col = 0)
                 gir_df = pd.read_csv(gir18csv, index_col = 0)
                 putts_df = pd.read_csv(putts18csv, index_col = 0)
                 scores_df = pd.read_csv(scores18csv, index_col = 0)
                 yards_df = pd.read_csv(yards18csv, index_col = 0)
                 hdcps_df = pd.read_csv(hdcps18csv, index_col = 0)
                 num_rounds = len(master_df) + 1
                 print('This is your ' + num2words(num_rounds, lang = 'en', to = 'ordinal_num') + ' 18 hole round')            
            break
    return num_holes, master_df, pars_df, fwys_df, gir_df, putts_df, scores_df, yards_df, hdcps_df

#function that asks about relevant course information, (date, course, tees, yardage, slope/rating, weather)
#eventually, want this to pull from data of existing courses to save user time
def courseinfo():
#     print(master_df)
    while True:
        date = input('What date was the round? (mm/dd/yy) ')
        course = input('What course did you play? ')
        if course.lower() == 'cantigny':
            cantigny_nines = input('Which Routing?\n1. Woodside/Lakeside\n2. Woodside/Hillside\n3. Lakeside/Hillside\n')
        tees = input('What tees did you play? ')
        course_yardage = int(input('What is the course yardage? '))
        rating = float(input('What is the course rating? '))
        slope = int(input('What is the course slope? '))
        temp_lo = int(input('Low temperature during the round? '))
        temp_hi = int(input('High temperature during the round? '))
        wind_speed = int(input('Wind speed during the round? '))
        gust_speed = int(input('Gust speeds during the round? '))
        round_info = {'Date':date, 'Course':course, 'Tees':tees,
                                   'Yardage':course_yardage, 'Rating':rating, 'slope':slope,
                                   'Low Temperature':temp_lo, 'High Temperature':temp_hi,
                     'Wind Speed':wind_speed, 'Gust Speed':gust_speed}
        print(round_info)
        cont = input('Is this correct? ')
        if cont.lower() == 'y':
            round_info = np.array([date, course, tees, course_yardage, rating, slope, temp_lo, temp_hi, wind_speed,
                         gust_speed])
            break
        else:
            print('Ok, redo it')
    return course, round_info

#function that gets par, yardage, handicap, fwy, gir, putts, and score for each hole
def holebyhole():
    hole = 0
    round_dic = {'Course':course}
    round_hdcps = np.array([course])
    round_yards = np.array([course])
    round_pars = np.array([course])
    round_fwys = np.array([course])
    round_girs = np.array([course])
    round_putts = np.array([course])
    round_scores = np.array([course])
    
    while hole < num_holes:
        
        while True:
            
            hdcp = int(input('Hole ' + str(hole +1 ) + ' handicap '))
            hole_yards = int(input('Hole ' + str(hole + 1) + ' yardage '))
            hole_par = int(input('Hole ' + str(hole + 1) + ' par '))
            hole_fwy = input('Hole ' + str(hole + 1) + ' fairway? (Y/L/R/S/D, NA for par 3s) ')
            hole_gir = input('Hole ' + str(hole + 1) + ' green in regulation? (Y/L/R/S/D) ')
            hole_putts = int(input('Hole ' + str(hole + 1) + ' putts '))
            hole_score = int(input('Hole ' + str(hole + 1) + ' score '))
            which_hole = 'hole ' + str(hole + 1)
            hole_info = {'HDCP':hdcp, 'Yargage':hole_yards, 'Par':hole_par,
                                   'FWY':hole_fwy, 'GIR':hole_gir, 'Putts':hole_putts,
                                   'Score':hole_score}
            print(hole_info)
            cont = input('Is this correct? ')
            if cont.lower() == 'y':
                round_hdcps = np.append(round_hdcps, hdcp)
                round_yards = np.append(round_yards, hole_yards)
                round_pars = np.append(round_pars, hole_par)
                round_fwys = np.append(round_fwys, hole_fwy)
                round_girs = np.append(round_girs, hole_gir)
                round_putts = np.append(round_putts, hole_putts)
                round_scores = np.append(round_scores, hole_score)
                round_dic[which_hole] = hole_info
                break
            else:
                print('Ok, redo it.')
        hole += 1
    round_ls = [round_hdcps, round_yards, round_pars, round_fwys, round_girs, round_putts, round_scores]
    hdcps_df.loc[len(hdcps_df)] = round_hdcps
    yards_df.loc[len(yards_df)] = round_yards
    pars_df.loc[len(pars_df)] = round_pars
    fwys_df.loc[len(fwys_df)] = round_fwys
    gir_df.loc[len(gir_df)] = round_girs
    putts_df.loc[len(putts_df)] = round_putts
    scores_df.loc[len(scores_df)] = round_scores

    return round_dic, round_ls, round_scores, round_pars, round_putts, round_fwys, round_girs

#function that gets stats to be entered into master data table
def roundstats():
    round_scores_np = np.array(round_scores[1:]).astype(int)
    round_pars_np = np.array(round_pars[1:]).astype(int)
    round_putts_np = np.array(round_putts[1:]).astype(int)
    #to account for 9 hole and 18 hole rounds
    if num_holes == 18:
#         front_score = np.sum(round_scores_np[0:9])
#         back_score = np.sum(round_scores_np[9:])
        scores_arr = np.array([np.sum(round_scores_np[1:10]), np.sum(round_scores_np[10:]), np.sum(round_scores[1:])])
#     score = np.sum(round_scores[0:])
    else:
        scores_arr = np.array([np.sum(round_scores_np[1:])])
    diff = np.sum(round_scores_np[1:]) - round_info[4].astype(float)
    hole_diffs = round_scores_np - round_pars_np #scores to par on each hole
    eagles = sum(np.less_equal(hole_diffs, -2)).astype(int)
    birdies = sum(np.equal(hole_diffs, -1)).astype(int)
    pars = sum(np.equal(hole_diffs, 0)).astype(int)
    bogies = sum(np.equal(hole_diffs, 1)).astype(int)
    doubles = sum(np.greater_equal(hole_diffs, 2)).astype(int)
    fwys = np.count_nonzero(round_fwys == 'Y').astype(int)
    fwy_per = fwys / (num_holes - sum(np.equal(round_pars_np, 3)))
    fwy_per = round(fwy_per, 2)
    gir = np.count_nonzero(round_gir == 'Y').astype(int)
    gir_per = gir / num_holes
    gir_per = round(gir_per, 2)
    putts = sum(round_putts_np).astype(int)
    putts3 = sum(np.equal(round_putts_np, 3)).astype(int)
    
    
    #finding indexes for par 3s, 4s, 5s
    par3_idxs = np.where(round_pars_np == 3)
    par4_idxs = np.where(round_pars_np == 4)
    par5_idxs = np.where(round_pars_np == 5)
    
    #diff and averages 
    par3_diff = sum(np.subtract(round_scores_np[par3_idxs], 3))
    par4_diff = sum(np.subtract(round_scores_np[par4_idxs], 4))
    par5_diff = sum(np.subtract(round_scores_np[par5_idxs], 5))
    
    par3_avg = round(np.average(round_scores_np[par3_idxs]), 2)
    par4_avg = round(np.average(round_scores_np[par4_idxs]), 2)
    par5_avg = round(np.average(round_scores_np[par5_idxs]), 2)
    
   
    master_arr_v1 = np.array([diff, eagles, birdies, pars, bogies, doubles,
                                  fwys, fwy_per, gir, gir_per, putts, putts3,
                                  par3_diff, par3_avg, par4_diff, par4_avg, par5_diff, par5_avg])
    print(master_arr_v1)
    
    master_arrv2 = np.append(scores_arr, master_arr_v1)
    print(master_arrv2)
    
    master_arr = np.append(round_info, master_arrv2)
    print(master_arr)
    
    master_df.loc[len(master_df)] = master_arr


#runs all of the other functions
def getScore():
    num_holes, master_df, pars_df, fwys_df, gir_df, putts_df, scores_df, yards_df, hdcps_df = howmanyholes()
    
    course, round_info = courseinfo()
    
    round_dic, round_ls, round_scores, round_pars, round_putts, round_fwys, round_gir = holebyhole()
    
    roundstats()
    
    #writing to the csvs

