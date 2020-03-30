import csv
#import pandas as pd

columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
               'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
               'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
               'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate',
               'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
               'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
               'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
               'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label']
dos_lebal = ['back.', 'land.', 'neptune.', 'smurf.', 'teardrop.', 'pod.', 'normal.']


def get_train_dataset(filename):
    normal = 0
    attack = 0
    out = open('111.csv', 'a', newline="")
    csv_write = csv.writer(out, dialect="excel")
    csv_write.writerow(columns) # 写入属性列
    with open(filename, "r") as f:
        for line in f:
            line = line.strip('\n')
            line = line.split(',')
            if line[41] in dos_lebal and line[1] == 'tcp':
                if line[41] == 'normal.':
                    line[41] = '1'
                    normal += 1
                else:
                    attack += 1
                    line[41] = '-1'
                csv_write.writerow(line)
    print("get train dataset success")
    print("normal:", normal)
    print("attack:", attack)

def translate_label(filename):
    out = open('222.csv', 'a', newline="")
    csv_write = csv.writer(out, dialect="excel")
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            line = line.split(',')
            data = []
            data.extend(line[22:42])
            data.extend(line[31:33])
            data.append(line[28])
            data.append(line[35])
            data.append(line[37])
            data.append(line[41])
            csv_write.writerow(data)

if __name__ == "__main__":
    get_train_dataset("kddcup.data.corrected")
    translate_label('111.csv')
