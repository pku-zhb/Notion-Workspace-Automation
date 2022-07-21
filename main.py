import schedule
import time
import json
import os

SCEDULE_TIME = 5 # in seconds

class jobClass():
    def __init__(self, name, freq_type, freq_para):
        self.name = name
        self.freq_type = freq_type
        self.freq_para = freq_para
    
    def do(self):
        print(self.name, " executed")
        os.system("python ./scripts/" + self.name + ".py")


def loadJobs():
    with open("./data/jobs.json", 'r') as f:
        _jobs = json.load(f)

    for key, value in _jobs['configurations'].items():
        jobs.append(jobClass(key,value['freq_type'],value['freq_para']))

    for job in jobs:
        if job.freq_type == 'repeatMinutes':
            schedule.every(job.freq_para).minutes.do(job.do)
        elif job.freq_type == 'atFixedTime':
            schedule.every().day.at(job.freq_para).do(job.do)


def main():
    loadJobs()
    while True:
        print("program is running")
        schedule.run_pending()
        time.sleep(SCEDULE_TIME)


if __name__ == '__main__':
    jobs = []
    main()

