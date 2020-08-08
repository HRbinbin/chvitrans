import os
import jieba


def cl(ch):
    ch_cut = ' '.join(jieba.cut(ch)).strip()
    file_tmp = open('E:\chvitrans\chvi\\nmt\\tmp.txt', mode='w', encoding='utf-8')
    file_tmp.write(ch_cut)
    file_tmp.close()
    print(ch_cut)
    command = 'onmt-main infer --model_type NMTBig --config E:\chvitrans\chvi\\nmt\data.yml --session_config E:\chvitrans\chvi\\nmt\session_config.txt --features_file E:\chvitrans\chvi\\nmt\\tmp.txt --predictions_file E:\chvitrans\chvi\\nmt\\tmp2.txt'
    os.system(command=command)
    file_tmp2 = open('E:\chvitrans\chvi\\nmt\\tmp2.txt', mode='r', encoding='utf-8')
    result = file_tmp2.read()
    file_tmp2.close()
    os.remove('E:\chvitrans\chvi\\nmt\\tmp.txt')
    os.remove('E:\chvitrans\chvi\\nmt\\tmp2.txt')

    lines = result.replace('_', ' ').split('\n')
    result = []
    for line in lines:
        temp = line.replace('<blank>', '')
        temp = temp.replace('<unk>', '')
        temp = temp.strip()
        if temp == '':
            continue
        result.append((line, len(line.split('.')) - 1))
    return result


def sent(ch):
    return cl(ch)


if __name__ == '__main__':
    result = cl('我们都是神枪手')
    for i in result:
        print(i)
