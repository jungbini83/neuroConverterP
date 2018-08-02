# -*- encoding:utf-8-*-
for fileNum in range(1, 21):
        
    if (fileNum / 10 == 0)  : fileNum = '0' + str(fileNum)          # 일의 자리 
    else                    : fileNum = str(fileNum)                # 십의 자리
    
    print './NeuroNicle/NeuroNicle_' + fileNum + '_1 file reading...'
    
    try:
        NEURONICLE_FILE = open('./NeuroNicle/NeuroNicle_' + fileNum + '_1', 'r')
        WRITE_FILE = open('./NeuroNicleRaw/NeuroNicle_' + fileNum + '_1.csv', 'a')
            
        sensorData = list()
        for line in NEURONICLE_FILE:
            sensorData = line.split()
            
        for data in sensorData:            
            WRITE_FILE.write(str( int(round((float(data.strip()) / 24.04 * 1000) + 16384) )) + '\n')    # 변환인자 (24.04nV)로 나누고 중앙값 16000 더하기

    except IOError:        
        print './NeuroNicle/NeuroNicle_' + fileNum + '_1 파일은 없습니다.'