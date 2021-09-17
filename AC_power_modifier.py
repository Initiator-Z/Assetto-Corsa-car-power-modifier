import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default='D:/Steam/steamapps/common/assettocorsa/content/cars/', help='Assetto Corsa cars path.')
parser.add_argument('--carname', type=str, help='name of the car folder to modify.')
parser.add_argument('--initial_power', type=float, default=200,  help='Initial power(hp) of the car, can be examined via content manager.')
parser.add_argument('--target_power', type=float, default=300,  help='desired power(hp) of the car.')
args = parser.parse_args()

path = args.path + args.carname + '/data/power.lut'
power_init = args.initial_power
power_target = args.target_power

def load_doc(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    return text.split()

def write_doc(path, current_pr, target_pr):
    rpm_file = load_doc(path)
    rpm_list = read_rpm(rpm_file)
    multiplier = get_modifier(current_pr, target_pr)
    power_list = get_rpm(rpm_list, multiplier)
    final_file = final_power(rpm_file,power_list)
    with open(path, 'w') as file:
        for item in final_file:
            file.write('%s\n' % item)
    print('Car power modified successfully!')

def read_rpm(file):
    rpmlist = list()
    for i in range(len(file)):
        pt = file[i].find('|')
        rpm = float(file[i][pt+1:])
        rpmlist.append(rpm)
    return rpmlist

def get_modifier(current_pr, target_pr):
    multiplier = target_pr / current_pr
    return multiplier

def get_rpm(power, multiplier):
    final = []
    for x in power:
        final.append(round((x * multiplier)))
    return final

def final_power(initial_list, power_list):
    final_power_list = list()
    for i in range(len(initial_list)):
        pt = initial_list[i].find('|')
        rpm = initial_list[i][:pt] + '|' + str(power_list[i])
        final_power_list.append(rpm)
    return final_power_list

if __name__ == '__main__':
     write_doc(path, power_init, power_target)
