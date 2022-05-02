import numpy as np
import tkinter as tk
import tkinter.messagebox
import time
import os
from pathlib import Path

Dir = Path('.', 'Data')
os.chdir(Dir)
# 主窗口设计
w1 = tk.Tk()
w1.title('CSV Data Generator V2.0 by Python')
w1.geometry('920x550')
tk.Label(w1, text='实验布点数据生成器 V2.0', font=('microsoft yahei', 20)).pack()
tk.Label(w1, text='by  戴以恒 厦门大学     最后更新: 2022/02/14', font=('microsoft yahei', 16), fg='grey').pack()
time_var = tk.StringVar()
time_var.set(time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()))
time_title_label = tk.Label(w1, text='启动时间:', font=('microsoft yahei', 14), width=12).place(x=0, y=80, anchor='nw')
time_label = tk.Label(w1, textvariable=time_var, bg='grey', fg='white',
                      font=('Arial', 14), width=20, height=1).place(x=120, y=80, anchor='nw')
filename_note = tk.StringVar()
filename_note.set('Exp')
entry_filename_note_title = tk.Label(w1, text='文件名前缀:', font=('microsoft yahei', 14), width=8).place(x=380, y=80, anchor='nw')
entry_filename_note = tk.Entry(w1, textvariable=filename_note, font=('Arial', 14),
                               width=6).place(x=490, y=80, anchor='nw')
groups_count = tk.IntVar()
groups_count.set(6)
entry_groups_count_title = tk.Label(w1, text='组数:', font=('microsoft yahei', 14), width=6).place(x=550, y=80, anchor='nw')
entry_groups_count = tk.Entry(w1, textvariable=groups_count, font=('Arial', 14), width=3).place(x=620, y=80, anchor='nw')
samples_count = tk.IntVar()
samples_count.set(6)
entry_samples_count_title = tk.Label(w1, text='单组样品数:', font=('microsoft yahei', 14), width=8).place(x=680, y=80, anchor='nw')
entry_samples_count = tk.Entry(w1, textvariable=samples_count, font=('Arial', 14), width=3).place(x=790, y=80, anchor='nw')
frame_m = tk.Frame(w1)
frame_m.place(x=330, y=120, anchor='n')
frame_left = tk.Frame(frame_m)
frame_right = tk.Frame(frame_m)
frame_left.pack(side='left')
frame_right.pack(side='right')
frame_1 = tk.Frame(frame_left)
frame_2 = tk.Frame(frame_left)
frame_3 = tk.Frame(frame_right)
frame_4 = tk.Frame(frame_right)
frame_1.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()
frame_1_1 = tk.Frame(frame_1)
frame_1_2 = tk.Frame(frame_1)
frame_1_1.pack()
frame_1_2.pack()
agent_1_name = tk.StringVar()
agent_1_con = tk.DoubleVar()
agent_1_name_title = tk.Label(frame_1_1, text='试剂1名称:', font=('microsoft yahei', 14), width=10).pack(side='left')
entry_agent_1_name = tk.Entry(frame_1_1, textvariable=agent_1_name, font=('Arial', 14), width=15).pack(side='right')
agent_1_con_title = tk.Label(frame_1_2, text='试剂1浓度(mmol/L):', font=('microsoft yahei', 14), width=15).pack(side='left')
entry_agent_1_con = tk.Entry(frame_1_2, textvariable=agent_1_con, font=('Arial', 14), width=9).pack(side='right')
frame_2_1 = tk.Frame(frame_2)
frame_2_2 = tk.Frame(frame_2)
frame_2_1.pack()
frame_2_2.pack()
agent_2_name = tk.StringVar()
agent_2_con = tk.DoubleVar()
agent_2_name_title = tk.Label(frame_2_1, text='试剂2名称:', font=('microsoft yahei', 14), width=10).pack(side='left')
entry_agent_2_name = tk.Entry(frame_2_1, textvariable=agent_2_name, font=('Arial', 14), width=15).pack(side='right')
agent_2_con_title = tk.Label(frame_2_2, text='试剂2浓度(mmol/L):', font=('microsoft yahei', 14), width=15).pack(side='left')
entry_agent_2_con = tk.Entry(frame_2_2, textvariable=agent_2_con, font=('Arial', 14), width=9).pack(side='right')
frame_3_1 = tk.Frame(frame_3)
frame_3_2 = tk.Frame(frame_3)
frame_3_1.pack()
frame_3_2.pack()
agent_3_name = tk.StringVar()
agent_3_con = tk.DoubleVar()
agent_3_name_title = tk.Label(frame_3_1, text='试剂3名称:', font=('microsoft yahei', 14), width=10).pack(side='left')
entry_agent_3_name = tk.Entry(frame_3_1, textvariable=agent_3_name, font=('Arial', 14), width=15).pack(side='right')
agent_3_con_title = tk.Label(frame_3_2, text='试剂3浓度(mmol/L):', font=('microsoft yahei', 14), width=15).pack(side='left')
entry_agent_3_con = tk.Entry(frame_3_2, textvariable=agent_3_con, font=('Arial', 14), width=9).pack(side='right')
frame_4_1 = tk.Frame(frame_4)
frame_4_2 = tk.Frame(frame_4)
frame_4_1.pack()
frame_4_2.pack()
agent_4_name = tk.StringVar()
agent_4_con = tk.DoubleVar()
agent_4_name_title = tk.Label(frame_4_1, text='试剂4名称:', font=('microsoft yahei', 14), width=10).pack(side='left')
entry_agent_4_name = tk.Entry(frame_4_1, textvariable=agent_4_name, font=('Arial', 14), width=15).pack(side='right')
agent_4_con_title = tk.Label(frame_4_2, text='试剂4浓度(mmol/L):', font=('microsoft yahei', 14), width=15).pack(side='left')
entry_agent_4_con = tk.Entry(frame_4_2, textvariable=agent_4_con, font=('Arial', 14), width=9).pack(side='right')
oven_temp_title = tk.Label(w1, text='烘箱温度(℃):', font=('microsoft yahei', 14), width=10).place(x=630, y=120, anchor='nw')
oven_temp = tk.DoubleVar()
entry_oven_temp = tk.Entry(w1, textvariable=oven_temp, font=('Arial', 14), width=12).place(x=755, y=120, anchor='nw')
oven_time_title = tk.Label(w1, text='加热时长(h):', font=('microsoft yahei', 14), width=10).place(x=630, y=150, anchor='nw')
oven_time = tk.DoubleVar()
entry_oven_time = tk.Entry(w1, textvariable=oven_time, font=('Arial', 14), width=12).place(x=755, y=150, anchor='nw')
other_notes_title = tk.Label(w1, text='其他备注:', font=('microsoft yahei', 14), width=8).place(x=630, y=185, anchor='nw')
other_notes = tk.StringVar()
other_notes.set('Nope.')
entry_other_notes = tk.Entry(w1, textvariable=other_notes, font=('Arial', 14), width=25).place(x=630, y=215, anchor='nw')
tk.Label(w1, text='请选择布点算法：', font=('microsoft yahei', 20)).place(x=30, y=260, anchor='nw')
a1_sum = 0.0
a2_sum = 0.0
a3_sum = 0.0
a4_sum = 0.0
log_name = ''


def generate_log(log_out_name):
    global a1_sum, a2_sum, a3_sum, a4_sum, log_name
    a1_n = agent_1_name.get()
    a1_c = agent_1_con.get()
    a2_n = agent_2_name.get()
    a2_c = agent_2_con.get()
    a3_n = agent_3_name.get()
    a3_c = agent_3_con.get()
    a4_n = agent_4_name.get()
    a4_c = agent_4_con.get()
    o_temp = oven_temp.get()
    o_time = oven_time.get()
    o_notes = other_notes.get()
    if a1_c != 0:
        a1_cs = str(a1_c) + ' mmol/L'
    else:
        a1_cs = 'Pure solvent'
    if a2_c != 0:
        a2_cs = str(a2_c) + ' mmol/L'
    else:
        a2_cs = 'Pure solvent'
    if a3_c != 0:
        a3_cs = str(a3_c) + ' mmol/L'
    else:
        a3_cs = 'Pure solvent'
    if a4_c != 0:
        a4_cs = str(a4_c) + ' mmol/L'
    else:
        a4_cs = 'Pure solvent'
    f1 = open(log_out_name, 'w+')
    f1.write('Reagent 1: ' + a1_n + '    ' + str(a1_cs) + '\n')
    f1.write('Reagent 2: ' + a2_n + '    ' + str(a2_cs) + '\n')
    f1.write('Reagent 3: ' + a3_n + '    ' + str(a3_cs) + '\n')
    f1.write('Reagent 4: ' + a4_n + '    ' + str(a4_cs) + '\n')
    f1.write('\n\n')
    f1.write('Oven: ' + str(o_temp) + '℃    ' + str(o_time) + 'hour(s)\n')
    f1.write('\n#\n')
    f1.write('Other notes:\n')
    f1.write(o_notes + '\n#\n\n')
    f1.close()


def w2_random():
    global a1_sum, a2_sum, a3_sum, a4_sum, log_name
    w2 = tk.Toplevel()
    w2.title('随机布点算法')
    w2.geometry('750x330')
    agent_1_upper_limit = tk.DoubleVar()
    agent_1_upper_limit.set(1.0)
    agent_1_lower_limit = tk.DoubleVar()
    agent_1_lower_limit.set(0.0)
    tk.Label(w2, text='1#体积上限(mL):', font=('microsoft yahei', 14), width=13).place(x=20, y=10, anchor='nw')
    tk.Entry(w2, textvariable=agent_1_upper_limit, font=('Arial', 14), width=15).place(x=180, y=10, anchor='nw')
    tk.Label(w2, text='1#体积下限(mL):', font=('microsoft yahei', 14), width=13).place(x=20, y=35, anchor='nw')
    tk.Entry(w2, textvariable=agent_1_lower_limit, font=('Arial', 14), width=15).place(x=180, y=35, anchor='nw')
    agent_2_upper_limit = tk.DoubleVar()
    agent_2_upper_limit.set(1.0)
    agent_2_lower_limit = tk.DoubleVar()
    agent_2_lower_limit.set(0.0)
    tk.Label(w2, text='2#体积上限(mL):', font=('microsoft yahei', 14), width=13).place(x=20, y=70, anchor='nw')
    tk.Entry(w2, textvariable=agent_2_upper_limit, font=('Arial', 14), width=15).place(x=180, y=70, anchor='nw')
    tk.Label(w2, text='2#体积下限(mL):', font=('microsoft yahei', 14), width=13).place(x=20, y=95, anchor='nw')
    tk.Entry(w2, textvariable=agent_2_lower_limit, font=('Arial', 14), width=15).place(x=180, y=95, anchor='nw')
    agent_3_upper_limit = tk.DoubleVar()
    agent_3_upper_limit.set(1.0)
    agent_3_lower_limit = tk.DoubleVar()
    agent_3_lower_limit.set(0.0)
    tk.Label(w2, text='3#体积上限(mL):', font=('microsoft yahei', 14), width=13).place(x=370, y=10, anchor='nw')
    tk.Entry(w2, textvariable=agent_3_upper_limit, font=('Arial', 14), width=15).place(x=530, y=10, anchor='nw')
    tk.Label(w2, text='3#体积下限(mL):', font=('microsoft yahei', 14), width=13).place(x=370, y=35, anchor='nw')
    tk.Entry(w2, textvariable=agent_3_lower_limit, font=('Arial', 14), width=15).place(x=530, y=35, anchor='nw')
    agent_4_upper_limit = tk.DoubleVar()
    agent_4_upper_limit.set(1.0)
    agent_4_lower_limit = tk.DoubleVar()
    agent_4_lower_limit.set(0.0)
    tk.Label(w2, text='4#体积上限(mL):', font=('microsoft yahei', 14), width=13).place(x=370, y=70, anchor='nw')
    tk.Entry(w2, textvariable=agent_4_upper_limit, font=('Arial', 14), width=15).place(x=530, y=70, anchor='nw')
    tk.Label(w2, text='4#体积下限(mL):', font=('microsoft yahei', 14), width=13).place(x=370, y=95, anchor='nw')
    tk.Entry(w2, textvariable=agent_4_lower_limit, font=('Arial', 14), width=15).place(x=530, y=95, anchor='nw')
    tk.Label(w2, text='数据点调零(格式:列号,起始样本号,结束样本号;):', font=('microsoft yahei', 14), width=34).place(x=20, y=130, anchor='nw')
    tk.Label(w2, text='Examples: 1,0,6;4,7,13;', fg='grey', font=('Arial', 12), width=20).place(x=430, y=135, anchor='nw')
    zeros_str = tk.StringVar()
    entry_zeros = tk.Entry(w2, textvariable=zeros_str, font=('Arial', 14), width=62)
    entry_zeros.place(x=20, y=160, anchor='nw')
    fps_switch_var = tk.IntVar()
    fps_switch_var.set(1)
    tk.Checkbutton(w2, text='最远点采样', variable=fps_switch_var, onvalue=1, offvalue=0,
                   font=('microsoft yahei', 14)).place(x=20, y=190, anchor='nw')
    fps_ratio = tk.DoubleVar()
    fps_ratio.set(3.0)
    tk.Label(w2, text='FPS样本倍数:', font=('microsoft yahei', 14), width=11).place(x=150, y=195, anchor='nw')
    tk.Entry(w2, textvariable=fps_ratio, font=('Arial', 14), width=15).place(x=290, y=195, anchor='nw')

    def generate_random():
        time_var.set(time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()))
        time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        fps_s = fps_switch_var.get()
        data_notes = filename_note.get()
        log_out_name = 'ExpData-Rand_' + time_str + '_' + data_notes + '.txt'
        data_out_name = 'ExpData-Rand_' + time_str + '_' + data_notes + '.csv'
        g = groups_count.get()
        s = samples_count.get()
        n_samples = g * s
        up1 = agent_1_upper_limit.get()
        low1 = agent_1_lower_limit.get()
        up2 = agent_2_upper_limit.get()
        low2 = agent_2_lower_limit.get()
        up3 = agent_3_upper_limit.get()
        low3 = agent_3_lower_limit.get()
        up4 = agent_4_upper_limit.get()
        low4 = agent_4_lower_limit.get()
        if fps_s:
            fps_r = fps_ratio.get()
            data = np.zeros((int(n_samples*fps_r), 4), dtype=float)
            for i in range(data.shape[0]):
                data[i, 0] = low1 + (up1 - low1) * np.random.rand()
                data[i, 1] = low2 + (up2 - low2) * np.random.rand()
                data[i, 2] = low3 + (up3 - low3) * np.random.rand()
                data[i, 3] = low4 + (up4 - low4) * np.random.rand()
            dd = data.copy()
            for i in range(dd.shape[1]):
                dd[:, i] = (dd[:, i] - min(dd[:, i])) / (max(dd[:, i]) - min(dd[:, i]))
            final_idx = []
            d_m = np.zeros((dd.shape[0], dd.shape[0]))
            for i in range(dd.shape[0]):
                for j in range(dd.shape[0]):
                    if i != j:
                        d_m[i, j] = np.sqrt(np.sum((dd[i, :] - dd[j, :]) ** 2))
            final_idx.append(np.random.randint(dd.shape[0]))
            for i in range(n_samples - 1):
                max_dis_dataset = 0
                new_id = 0
                for j in range(dd.shape[0]):
                    if j not in final_idx:  # 从剩余数据集中搜索
                        min_dis = np.min(d_m[j, final_idx])  # 到点集的最小距离
                        if min_dis > max_dis_dataset:
                            max_dis_dataset = min_dis  # 更新剩余数据集中的最大的距离点集的最小距离
                            new_id = j
                final_idx.append(new_id)
            data = dd[final_idx, :]
        else:
            data = np.zeros((n_samples, 4), dtype=float)
            for i in range(data.shape[0]):
                data[i, 0] = low1 + (up1 - low1) * np.random.rand()
                data[i, 1] = low2 + (up2 - low2) * np.random.rand()
                data[i, 2] = low3 + (up3 - low3) * np.random.rand()
                data[i, 3] = low4 + (up4 - low4) * np.random.rand()
        z_str = entry_zeros.get()
        z_str_list = z_str.split(';')
        for i in range(len(z_str_list)-1):
            l = z_str_list[i]
            c_i = int(l.split(',')[0])-1
            l_i_b = int(l.split(',')[1])
            l_i_e = int(l.split(',')[2])
            for j in range(l_i_e-l_i_b+1):
                data[l_i_b+j, c_i] = 0
        np.savetxt(data_out_name, data, fmt='%8.3f', delimiter=',')
        a1_sum = sum(data[:, 0])
        a2_sum = sum(data[:, 1])
        a3_sum = sum(data[:, 2])
        a4_sum = sum(data[:, 3])
        generate_log(log_out_name)
        tkinter.messagebox.showinfo(title='实验数据已生成',
                                    message='实验数据成功生成!\n数据文件名: ' + data_out_name +
                                            '\nLog: ' + log_out_name)
    tk.Button(w2, text='生成数据', font=('microsoft yahei', 16), width=25, height=2,
              command=generate_random, fg='red').place(x=20, y=230, anchor='nw')


tk.Button(w1, text='随机布点算法', font=('microsoft yahei', 18), width=18, height=2, command=w2_random, fg='red').place(x=30, y=300, anchor='nw')


def w3_lh():
    global a1_sum, a2_sum, a3_sum, a4_sum, log_name
    w3 = tk.Toplevel()
    w3.title('拉丁超立方抽样布点算法')
    w3.geometry('750x330')
    agent_1_upper_limit_lh = tk.DoubleVar()
    agent_1_upper_limit_lh.set(1.0)
    agent_1_lower_limit_lh = tk.DoubleVar()
    agent_1_lower_limit_lh.set(0.0)
    tk.Label(w3, text='1#体积上限(mL):', font=('microsoft yahei', 14), width=13).place(x=20, y=10, anchor='nw')
    tk.Entry(w3, textvariable=agent_1_upper_limit_lh, font=('Arial', 14), width=15).place(x=180, y=10, anchor='nw')
    tk.Label(w3, text='1#体积下限(mL):', font=('microsoft yahei', 14), width=13).place(x=20, y=35, anchor='nw')
    tk.Entry(w3, textvariable=agent_1_lower_limit_lh, font=('Arial', 14), width=15).place(x=180, y=35, anchor='nw')
    agent_2_upper_limit_lh = tk.DoubleVar()
    agent_2_upper_limit_lh.set(1.0)
    agent_2_lower_limit_lh = tk.DoubleVar()
    agent_2_lower_limit_lh.set(0.0)
    tk.Label(w3, text='2#体积上限(mL):', font=('microsoft yahei', 14), width=13).place(x=20, y=70, anchor='nw')
    tk.Entry(w3, textvariable=agent_2_upper_limit_lh, font=('Arial', 14), width=15).place(x=180, y=70, anchor='nw')
    tk.Label(w3, text='2#体积下限(mL):', font=('microsoft yahei', 14), width=13).place(x=20, y=95, anchor='nw')
    tk.Entry(w3, textvariable=agent_2_lower_limit_lh, font=('Arial', 14), width=15).place(x=180, y=95, anchor='nw')
    agent_3_upper_limit_lh = tk.DoubleVar()
    agent_3_upper_limit_lh.set(1.0)
    agent_3_lower_limit_lh = tk.DoubleVar()
    agent_3_lower_limit_lh.set(0.0)
    tk.Label(w3, text='3#体积上限(mL):', font=('microsoft yahei', 14), width=13).place(x=370, y=10, anchor='nw')
    tk.Entry(w3, textvariable=agent_3_upper_limit_lh, font=('Arial', 14), width=15).place(x=530, y=10, anchor='nw')
    tk.Label(w3, text='3#体积下限(mL):', font=('microsoft yahei', 14), width=13).place(x=370, y=35, anchor='nw')
    tk.Entry(w3, textvariable=agent_3_lower_limit_lh, font=('Arial', 14), width=15).place(x=530, y=35, anchor='nw')
    agent_4_upper_limit_lh = tk.DoubleVar()
    agent_4_upper_limit_lh.set(1.0)
    agent_4_lower_limit_lh = tk.DoubleVar()
    agent_4_lower_limit_lh.set(0.0)
    tk.Label(w3, text='4#体积上限(mL):', font=('microsoft yahei', 14), width=13).place(x=370, y=70, anchor='nw')
    tk.Entry(w3, textvariable=agent_4_upper_limit_lh, font=('Arial', 14), width=15).place(x=530, y=70, anchor='nw')
    tk.Label(w3, text='4#体积下限(mL):', font=('microsoft yahei', 14), width=13).place(x=370, y=95, anchor='nw')
    tk.Entry(w3, textvariable=agent_4_lower_limit_lh, font=('Arial', 14), width=15).place(x=530, y=95, anchor='nw')
    tk.Label(w3, text='数据点调零(格式:列号,起始样本号,结束样本号;):', font=('microsoft yahei', 14), width=34).place(x=20, y=130, anchor='nw')
    tk.Label(w3, text='Examples: 1,0,6;4,7,13;', fg='grey', font=('Arial', 12), width=20).place(x=430, y=135, anchor='nw')
    zeros_str = tk.StringVar()
    entry_zeros = tk.Entry(w3, textvariable=zeros_str, font=('Arial', 14), width=62)
    entry_zeros.place(x=20, y=160, anchor='nw')
    fps_switch_var = tk.IntVar()
    fps_switch_var.set(1)
    tk.Checkbutton(w3, text='最远点采样', variable=fps_switch_var,
                   onvalue=1, offvalue=0, font=('microsoft yahei', 14)).place(x=20, y=190, anchor='nw')
    fps_ratio = tk.DoubleVar()
    fps_ratio.set(3.0)
    tk.Label(w3, text='FPS样本倍数:', font=('microsoft yahei', 14), width=11).place(x=150, y=195, anchor='nw')
    tk.Entry(w3, textvariable=fps_ratio, font=('Arial', 14), width=15).place(x=290, y=195, anchor='nw')

    def generate_lh():
        time_var.set(time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()))
        time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        fps_s = fps_switch_var.get()
        data_notes = filename_note.get()
        log_out_name = 'ExpData-LHS_' + time_str + '_' + data_notes + '.txt'
        data_out_name = 'ExpData-LHS_' + time_str + '_' + data_notes + '.csv'
        g = groups_count.get()
        s = samples_count.get()
        n_samples = g * s
        up1 = agent_1_upper_limit_lh.get()
        low1 = agent_1_lower_limit_lh.get()
        up2 = agent_2_upper_limit_lh.get()
        low2 = agent_2_lower_limit_lh.get()
        up3 = agent_3_upper_limit_lh.get()
        low3 = agent_3_lower_limit_lh.get()
        up4 = agent_4_upper_limit_lh.get()
        low4 = agent_4_lower_limit_lh.get()
        v_limit = [[low1, up1], [low2, up2], [low3, up3], [low4, up4]]
        if fps_s:
            fps_r = fps_ratio.get()
            data = np.zeros((int(n_samples*fps_r), 4), dtype=float)
            for i in range(4):
                num_generate = int(n_samples * fps_r)
                index = np.random.choice(num_generate, num_generate, replace=False)
                inter = (v_limit[i][1] - v_limit[i][0]) / num_generate
                for j in range(num_generate):
                    data[j, i] = np.random.rand() * inter + v_limit[i][0] + index[j] * inter

            dd = data.copy()
            dd_t = data.copy()
            for i in range(dd.shape[1]):
                dd[:, i] = (dd[:, i] - min(dd[:, i])) / (max(dd[:, i]) - min(dd[:, i]))
            final_idx = []
            d_m = np.zeros((dd.shape[0], dd.shape[0]))
            for i in range(dd.shape[0]):
                for j in range(dd.shape[0]):
                    if i != j:
                        d_m[i, j] = np.sqrt(np.sum((dd[i, :] - dd[j, :]) ** 2))
            final_idx.append(np.random.randint(dd.shape[0]))
            for i in range(n_samples - 1):
                max_dis_dataset = 0
                new_id = 0
                for j in range(dd.shape[0]):
                    if j not in final_idx:  # 从剩余数据集中搜索
                        min_dis = np.min(d_m[j, final_idx])  # 到点集的最小距离
                        if min_dis > max_dis_dataset:
                            max_dis_dataset = min_dis  # 更新剩余数据集中的最大的距离点集的最小距离
                            new_id = j
                final_idx.append(new_id)
            data = dd_t[final_idx, :]
        else:
            data = np.zeros((n_samples, 4), dtype=float)
            for i in range(4):
                num_generate = n_samples
                index = np.random.choice(num_generate, num_generate, replace=False)
                inter = (v_limit[i][1] - v_limit[i][0]) / num_generate
                for j in range(num_generate):
                    data[j, i] = np.random.rand() * inter + v_limit[i][0] + index[j] * inter
        z_str = entry_zeros.get()
        z_str_list = z_str.split(';')
        for i in range(len(z_str_list)-1):
            l = z_str_list[i]
            c_i = int(l.split(',')[0])-1
            l_i_b = int(l.split(',')[1])
            l_i_e = int(l.split(',')[2])
            for j in range(l_i_e-l_i_b+1):
                data[l_i_b+j, c_i] = 0
        np.savetxt(data_out_name, data, fmt='%8.3f', delimiter=',')
        a1_sum = sum(data[:, 0])
        a2_sum = sum(data[:, 1])
        a3_sum = sum(data[:, 2])
        a4_sum = sum(data[:, 3])
        generate_log(log_out_name)
        tkinter.messagebox.showinfo(title='实验数据已生成',
                                    message='实验数据成功生成!\n数据文件名: ' + data_out_name +
                                            '\nLog: ' + log_out_name)
    tk.Button(w3, text='生成数据', font=('microsoft yahei', 16), width=25, height=2,
              command=generate_lh, fg='red').place(x=20, y=230, anchor='nw')


generate2_button = tk.Button(w1, text='拉丁超立方算法', font=('microsoft yahei', 18), width=18, height=2,
                             command=w3_lh, fg='red').place(x=330, y=300, anchor='nw')


def w4_jy():
    global a1_sum, a2_sum, a3_sum, a4_sum, log_name
    w4 = tk.Toplevel()
    w4.title('均匀布点算法')
    w4.geometry('750x290')
    tk.Label(w4, text='对4种试剂，默认使用U*9_4四因素九水平正交表，行列互换生成36个数据点',
             font=('microsoft yahei', 16), fg='grey').place(x=20, y=10, anchor='nw')
    tk.Label(w4, text='请输入4种试剂的9个水平，以半角逗号分隔(例：0.0,0.1,0.2......): ',
             font=('microsoft yahei', 16), fg='grey').place(x=20, y=40, anchor='nw')
    agent_1_s = tk.StringVar()
    agent_1_s.set('0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8')
    tk.Label(w4, text='1#的9水平列表(mL):', font=('microsoft yahei', 14), width=16).place(x=20, y=70, anchor='nw')
    entry_agent_1_s = tk.Entry(w4, textvariable=agent_1_s, font=('Arial', 14), width=40)
    entry_agent_1_s.place(x=230, y=75, anchor='nw')
    agent_2_s = tk.StringVar()
    tk.Label(w4, text='2#的9水平列表(mL):', font=('microsoft yahei', 14), width=16).place(x=20, y=100, anchor='nw')
    entry_agent_2_s = tk.Entry(w4, textvariable=agent_2_s, font=('Arial', 14), width=40)
    entry_agent_2_s.place(x=230, y=105, anchor='nw')
    agent_3_s = tk.StringVar()
    tk.Label(w4, text='3#的9水平列表(mL):', font=('microsoft yahei', 14), width=16).place(x=20, y=130, anchor='nw')
    entry_agent_3_s = tk.Entry(w4, textvariable=agent_3_s, font=('Arial', 14), width=40)
    entry_agent_3_s.place(x=230, y=135, anchor='nw')
    agent_4_s = tk.StringVar()
    tk.Label(w4, text='4#的9水平列表(mL):', font=('microsoft yahei', 14), width=16).place(x=20, y=160, anchor='nw')
    entry_agent_4_s = tk.Entry(w4, textvariable=agent_4_s, font=('Arial', 14), width=40)
    entry_agent_4_s.place(x=230, y=165, anchor='nw')

    def generate_jy():
        time_var.set(time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()))
        time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        data_notes = filename_note.get()
        log_out_name = 'ExpData-UNI_' + time_str + '_' + data_notes + '.txt'
        data_out_name = 'ExpData-UNI_' + time_str + '_' + data_notes + '.csv'
        id_list = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
                   [2, 5, 8, 1, 4, 7, 0, 3, 6],
                   [6, 3, 0, 7, 4, 1, 8, 5, 2],
                   [8, 7, 6, 5, 4, 3, 2, 1, 0]]
        s1 = entry_agent_1_s.get()
        list_1 = s1.split(',')
        if len(list_1) != 9:
            tkinter.messagebox.showinfo(title='水平数错误！', message='请检查输入的1#水平数是否为9个!\n')
        s2 = entry_agent_2_s.get()
        list_2 = s2.split(',')
        if len(list_2) != 9:
            tkinter.messagebox.showinfo(title='水平数错误！', message='请检查输入的2#水平数是否为9个!\n')
        s3 = entry_agent_3_s.get()
        list_3 = s3.split(',')
        if len(list_3) != 9:
            tkinter.messagebox.showinfo(title='水平数错误！', message='请检查输入的3#水平数是否为9个!\n')
        s4 = entry_agent_4_s.get()
        list_4 = s4.split(',')
        if len(list_4) != 9:
            tkinter.messagebox.showinfo(title='水平数错误！', message='请检查输入的4#水平数是否为9个!\n')
        full_list = [list_1, list_2, list_3, list_4]
        data = np.zeros((36, 4))
        for i in range(4):
            for j in range(9):
                data[j, i] = float(full_list[i][int(id_list[i][j])])
        for i in range(4):
            for j in range(9):
                if i == 0 or i == 1:
                    i_id = i
                elif i == 2:
                    i_id = 3
                else:
                    i_id = 2
                data[j+9, i] = float(full_list[i][int(id_list[i_id][j])])
        for i in range(4):
            for j in range(9):
                if i == 2 or i == 3:
                    i_id = i
                elif i == 0:
                    i_id = 1
                else:
                    i_id = 0
                data[j+18, i] = float(full_list[i][int(id_list[i_id][j])])
        for i in range(4):
            for j in range(9):
                if i == 2:
                    i_id = 3
                elif i == 3:
                    i_id = 2
                elif i == 0:
                    i_id = 1
                else:
                    i_id = 0
                data[j+27, i] = float(full_list[i][int(id_list[i_id][j])])
        np.savetxt(data_out_name, data, fmt='%8.3f', delimiter=',')
        a1_sum = sum(data[:, 0])
        a2_sum = sum(data[:, 1])
        a3_sum = sum(data[:, 2])
        a4_sum = sum(data[:, 3])
        generate_log(log_out_name)
        tkinter.messagebox.showinfo(title='实验数据已生成',
                                    message='实验数据成功生成!\n数据文件名: ' + data_out_name +
                                            '\nLog: ' + log_out_name)

    tk.Button(w4, text='生成数据', font=('microsoft yahei', 16), width=25, height=2,
              command=generate_jy, fg='red').place(x=20, y=200, anchor='nw')


generate3_button = tk.Button(w1, text='均匀布点算法', font=('microsoft yahei', 18), width=18, height=2,
                             command=w4_jy, fg='red').place(x=630, y=300, anchor='nw')
tk.Label(w1, text='布点后可用的辅助工具：', font=('microsoft yahei', 20)).place(x=30, y=400, anchor='nw')


def w5_cal_wt():
    global a1_sum, a2_sum, a3_sum, a4_sum, log_name
    w5 = tk.Toplevel()
    w5.title('辅助质量计算')
    w5.geometry('750x420')
    agent_1_volume_c = tk.DoubleVar()
    agent_1_volume_c.set(a1_sum)
    tk.Label(w5, text='1#所需体积(mL):', font=('microsoft yahei', 14), width=12).place(x=20, y=30, anchor='nw')
    tk.Label(w5, textvariable=agent_1_volume_c, font=('Arial', 14), width=15, bg='grey').place(x=175, y=33, anchor='nw')
    agent_1_volume_t = tk.DoubleVar()
    agent_1_wt = tk.DoubleVar()
    tk.Label(w5, text='1#实配体积(mL):', font=('microsoft yahei', 14), width=12).place(x=20, y=60, anchor='nw')
    tk.Entry(w5, textvariable=agent_1_volume_t, font=('Arial', 14), width=15).place(x=175, y=63, anchor='nw')
    tk.Label(w5, text='1#分子量(g/mol):', font=('microsoft yahei', 14), width=12).place(x=20, y=90, anchor='nw')
    tk.Entry(w5, textvariable=agent_1_wt, font=('Arial', 14), width=15).place(x=175, y=93, anchor='nw')
    agent_2_volume_c = tk.DoubleVar()
    agent_2_volume_c.set(a1_sum)
    tk.Label(w5, text='2#所需体积(mL):', font=('microsoft yahei', 14), width=12).place(x=20, y=130, anchor='nw')
    tk.Label(w5, textvariable=agent_2_volume_c, font=('Arial', 14), width=15, bg='grey').place(x=175, y=133, anchor='nw')
    agent_2_volume_t = tk.DoubleVar()
    agent_2_wt = tk.DoubleVar()
    tk.Label(w5, text='2#实配体积(mL):', font=('microsoft yahei', 14), width=12).place(x=20, y=160, anchor='nw')
    tk.Entry(w5, textvariable=agent_2_volume_t, font=('Arial', 14), width=15).place(x=175, y=163, anchor='nw')
    tk.Label(w5, text='2#分子量(g/mol):', font=('microsoft yahei', 14), width=12).place(x=20, y=190, anchor='nw')
    tk.Entry(w5, textvariable=agent_2_wt, font=('Arial', 14), width=15).place(x=175, y=193, anchor='nw')
    agent_3_volume_c = tk.DoubleVar()
    agent_3_volume_c.set(a1_sum)
    tk.Label(w5, text='3#所需体积(mL):', font=('microsoft yahei', 14), width=12).place(x=370, y=30, anchor='nw')
    tk.Label(w5, textvariable=agent_3_volume_c, font=('Arial', 14), width=15, bg='grey').place(x=525, y=33, anchor='nw')
    agent_3_volume_t = tk.DoubleVar()
    agent_3_wt = tk.DoubleVar()
    tk.Label(w5, text='3#实配体积(mL):', font=('microsoft yahei', 14), width=12).place(x=370, y=60, anchor='nw')
    tk.Entry(w5, textvariable=agent_3_volume_t, font=('Arial', 14), width=15).place(x=525, y=63, anchor='nw')
    tk.Label(w5, text='3#分子量(g/mol):', font=('microsoft yahei', 14), width=12).place(x=370, y=90, anchor='nw')
    tk.Entry(w5, textvariable=agent_3_wt, font=('Arial', 14), width=15).place(x=525, y=93, anchor='nw')
    agent_4_volume_c = tk.DoubleVar()
    agent_4_volume_c.set(a1_sum)
    tk.Label(w5, text='4#所需体积(mL):', font=('microsoft yahei', 14), width=12).place(x=370, y=130, anchor='nw')
    tk.Label(w5, textvariable=agent_4_volume_c, font=('Arial', 14), width=15, bg='grey').place(x=525, y=133, anchor='nw')
    agent_4_volume_t = tk.DoubleVar()
    agent_4_wt = tk.DoubleVar()
    tk.Label(w5, text='4#实配体积(mL):', font=('microsoft yahei', 14), width=12).place(x=370, y=160, anchor='nw')
    tk.Entry(w5, textvariable=agent_4_volume_t, font=('Arial', 14), width=15).place(x=525, y=163, anchor='nw')
    tk.Label(w5, text='4#分子量(g/mol):', font=('microsoft yahei', 14), width=12).place(x=370, y=190, anchor='nw')
    tk.Entry(w5, textvariable=agent_4_wt, font=('Arial', 14), width=15).place(x=525, y=193, anchor='nw')
    a1_wt = 0.0
    a2_wt = 0.0
    a3_wt = 0.0
    a4_wt = 0.0

    def calculate_weights():
        global a1_wt, a2_wt, a3_wt, a4_wt, log_name
        time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        data_notes = filename_note.get()
        log_name = 'ExpData-CalcWt_' + time_str + '_' + data_notes + '.txt'
        a1_n = agent_1_name.get()
        a1_c = agent_1_con.get()
        a2_n = agent_2_name.get()
        a2_c = agent_2_con.get()
        a3_n = agent_3_name.get()
        a3_c = agent_3_con.get()
        a4_n = agent_4_name.get()
        a4_c = agent_4_con.get()
        a1_v = agent_1_volume_t.get()
        a2_v = agent_2_volume_t.get()
        a3_v = agent_3_volume_t.get()
        a4_v = agent_4_volume_t.get()
        a1_mwt = agent_1_wt.get()
        a2_mwt = agent_2_wt.get()
        a3_mwt = agent_3_wt.get()
        a4_mwt = agent_4_wt.get()
        a1_wt = a1_mwt * a1_v * a1_c / 1000
        a2_wt = a2_mwt * a2_v * a2_c / 1000
        a3_wt = a3_mwt * a3_v * a3_c / 1000
        a4_wt = a4_mwt * a4_v * a4_c / 1000
        if a1_c != 0:
            a1_ws = str(round(a1_wt, 1)) + ' mg'
        else:
            a1_ws = str(round(a1_v, 2)) + ' mL 纯溶剂'
        if a2_c != 0:
            a2_ws = str(round(a2_wt, 1)) + ' mg'
        else:
            a2_ws = str(round(a2_v, 2)) + ' mL 纯溶剂'
        if a3_c != 0:
            a3_ws = str(round(a3_wt, 1)) + ' mg'
        else:
            a3_ws = str(round(a3_v, 2)) + ' mL 纯溶剂'
        if a4_c != 0:
            a4_ws = str(round(a4_wt, 1)) + ' mg'
        else:
            a4_ws = str(round(a4_v, 2)) + ' mL 纯溶剂'
        f1 = open(log_name, 'a+')
        f1.write('#\n')
        f1.write(a1_n + '    ' + a1_ws + '\n')
        f1.write(a2_n + '    ' + a2_ws + '\n')
        f1.write(a3_n + '    ' + a3_ws + '\n')
        f1.write(a4_n + '    ' + a4_ws + '\n')
        f1.write('#\n\n')
        f1.close()
        tkinter.messagebox.showinfo(title='Log updated',
                                    message='Weights Calculated and log updated!\nLog file name ' + log_name)
        agent_1_weight_n.set(round(a1_wt, 1))
        agent_2_weight_n.set(round(a2_wt, 1))
        agent_3_weight_n.set(round(a3_wt, 1))
        agent_4_weight_n.set(round(a4_wt, 1))

    tk.Button(w5, text='计算质量', font=('microsoft yahei', 15), width=30, height=2,
              command=calculate_weights, fg='red').place(x=375, y=240, anchor='n')

    agent_1_weight_n = tk.DoubleVar()
    agent_1_weight_n.set(a1_wt)
    tk.Label(w5, text='1#所需质量(mg):', font=('microsoft yahei', 14), width=12).place(x=20, y=330, anchor='nw')
    tk.Label(w5, textvariable=agent_1_weight_n, font=('Arial', 14), width=15, bg='grey').place(x=175, y=333, anchor='nw')
    agent_2_weight_n = tk.DoubleVar()
    agent_2_weight_n.set(a1_wt)
    tk.Label(w5, text='2#所需质量(mg):', font=('microsoft yahei', 14), width=12).place(x=20, y=370, anchor='nw')
    tk.Label(w5, textvariable=agent_2_weight_n, font=('Arial', 14), width=15, bg='grey').place(x=175, y=373, anchor='nw')
    agent_3_weight_n = tk.DoubleVar()
    agent_3_weight_n.set(a1_wt)
    tk.Label(w5, text='3#所需质量(mg):', font=('microsoft yahei', 14), width=12).place(x=370, y=330, anchor='nw')
    tk.Label(w5, textvariable=agent_3_weight_n, font=('Arial', 14), width=15, bg='grey').place(x=525, y=333, anchor='nw')
    agent_4_weight_n = tk.DoubleVar()
    agent_4_weight_n.set(a1_wt)
    tk.Label(w5, text='4#所需质量(mg):', font=('microsoft yahei', 14), width=12).place(x=370, y=370, anchor='nw')
    tk.Label(w5, textvariable=agent_4_weight_n, font=('Arial', 14), width=15, bg='grey').place(x=525, y=373, anchor='nw')


calwt_button = tk.Button(w1, text='质量计算器', font=('microsoft yahei', 18), width=18, height=2,
                         command=w5_cal_wt, fg='red').place(x=30, y=440, anchor='nw')

tk.mainloop()
