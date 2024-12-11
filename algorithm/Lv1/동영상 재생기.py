def solution(video_len, pos, op_start, op_end, commands):
    video_len = int(video_len[:2]) * 60 + int(video_len[3:])
    pos = int(pos[:2]) * 60 + int(pos[3:])
    op_start = int(op_start[:2]) * 60 + int(op_start[3:])
    op_end = int(op_end[:2]) * 60 + int(op_end[3:])
    for cm in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if cm == 'prev':
            pos -= 10
            if pos < 0:
                pos = 0
        else:
            pos += 10
            if pos > video_len:
                pos = video_len
    if op_start <= pos <= op_end:
        pos = op_end
    answer = str(pos//60).zfill(2) + ":" + str(pos%60).zfill(2)
    return answer

solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"])