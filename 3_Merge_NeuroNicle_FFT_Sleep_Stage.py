# -*- encoding:utf-8-*-
for fileNum in range(1, 21):
        
    if (fileNum / 10 == 0)  : fileNum = '0' + str(fileNum)          # 일의 자리 
    else                    : fileNum = str(fileNum)                # 십의 자리
    
    print './SleepStage/NeuroNicle_' + fileNum + '_Events.txt file reading...'
    print './NeuroNicleFFT/NeuroNicleFFT_' + fileNum + '_1.csv file reading...'
    
    try:
        SLEEPSTAGE_FILE = open('./SleepStage/NeuroNicle_' + fileNum + '_Events.txt', 'r')
        NEURONICLE_FILE = open('./NeuroNicleFFT/NeuroNicleFFT_' + fileNum + '_1.csv', 'r')
        
        WRITE_FILE = open('./MergedData/NeuroNicleSleepStage_' + fileNum + '_1.csv', 'a')
        
        sleepStageList = list()
        for line in SLEEPSTAGE_FILE:
            if line.startswith('SLEEP-'):
                sleepStageList.append(line[6:line.find('\t')])
            
        secCounter = 0
        listIndex = 10                                              # 앞 10개의 sleep stage 데이터는 FFT 때문에 생략됨
        for line in NEURONICLE_FILE:
            if secCounter == 3:        
                listIndex += 1
                secCounter = 0
                
            try:
                WRITE_FILE.write(line.strip() + ',' + sleepStageList[listIndex] + '\n')
                secCounter +=1
            except IndexError:
                print 'NeuroNicle 데이터가 부족하여 sleep stage를 최대한 채우고 종료합니다.'
                break            

    except IOError:        
        print './NeuroNicle/NeuroNicle_' + fileNum + '_1 파일은 없습니다.'