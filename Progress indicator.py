import random,time

BAR = chr(9608)

def main():
    bytesDownloaded = 0
    downloadSize = 4096 #if you want, change it to input
    while bytesDownloaded < downloadSize:
        bytesDownloaded += random.randint(0,100)

        barStr = getProgressBar(bytesDownloaded,downloadSize)

        print(barStr,end='',flush=True)

        time.sleep(0.2)

        print('\b' *  len(barStr),end='',flush=True)

    print('Download is end')
def getProgressBar(progress,total,barWidth=40):
    progressBar = ''
    progressBar += '['

    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    numberOfBar = int((progress / total) * barWidth)

    progressBar += BAR * numberOfBar
    progressBar += ' ' * (barWidth - numberOfBar)

    progressBar += ']'

    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(progress) +'/' + str(total)

    return progressBar



if __name__ == '__main__':
    main()