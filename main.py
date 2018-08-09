import os
import time

work_dir = 'c:/Intelitek/SCORBASE/Projects/ER4u/chess_ofer_ori/'
log_file_path = 'c:/Program Files/Arena/arena.debug'

def get_moves(path):
    # OPEN THE ARENA.DEBUG FILE ###
    log_file = open(path, 'r')
    log_txt = log_file.read()
    # get last two moves
    white_move_location = log_txt.rfind('go')
    white_origin = log_txt[(white_move_location - 33):(white_move_location - 31)]
    white_destination = log_txt[(white_move_location - 31):(white_move_location - 29)]
    black_move_location = log_txt.rfind('Found move')
    black_origin = log_txt[(black_move_location + 11):(black_move_location + 13)]
    black_destination = log_txt[(black_move_location + 14):(black_move_location + 16)]
    # convert moove to robot's coordinates
    conversion = {'a': '1', 'b': '2', 'c': '3', 'd': '4',
                  'e': '5', 'f': '6', 'g': '7', 'h': '8'}
    white_origin = conversion[white_origin[0]] + white_origin[1] + '1'
    white_destination = conversion[white_destination[0]] + white_destination[1] + '1'
    black_origin = conversion[black_origin[0]] + black_origin[1] + '1'
    black_destination = conversion[black_destination[0]] + black_destination[1] + '1'
    # split to 4 files
    file_wo = open(work_dir + 'file_wo.txt', 'w')
    file_wo.write(white_origin)
    file_wo.close()
    file_wd = open(work_dir + 'file_wd.txt', 'w')
    file_wd.write(white_destination)
    file_wd.close()
    file_bo = open(work_dir + 'file_bo.txt', 'w')
    file_bo.write(black_origin)
    file_bo.close()
    file_bd = open(work_dir + 'file_bd.txt', 'w')
    file_bd.write(black_destination)
    file_bd.close()
    # CLOSE THE ARENA.DEBUG FILE AND DELETE IT ###
    log_file.close()
    os.remove(log_file_path)

if __name__ == '__main__':
    get_moves(log_file_path)
