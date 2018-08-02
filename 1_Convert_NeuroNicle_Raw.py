# -*- encoding:utf-8-*-
for fileNum in range(1, 21):
        
    if (fileNum / 10 == 0)  : fileNum = '0' + str(fileNum)          # ���� �ڸ� 
    else                    : fileNum = str(fileNum)                # ���� �ڸ�
    
    print './NeuroNicle/NeuroNicle_' + fileNum + '_1 file reading...'
    
    try:
        NEURONICLE_FILE = open('./NeuroNicle/NeuroNicle_' + fileNum + '_1', 'r')
        WRITE_FILE = open('./NeuroNicleRaw/NeuroNicle_' + fileNum + '_1.csv', 'a')
            
        sensorData = list()
        for line in NEURONICLE_FILE:
            sensorData = line.split()
            
        for data in sensorData:            
            WRITE_FILE.write(str( int(round((float(data.strip()) / 24.04 * 1000) + 16384) )) + '\n')    # ��ȯ���� (24.04nV)�� ������ �߾Ӱ� 16000 ���ϱ�

    except IOError:        
        print './NeuroNicle/NeuroNicle_' + fileNum + '_1 ������ �����ϴ�.'