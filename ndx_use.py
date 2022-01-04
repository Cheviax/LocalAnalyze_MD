for i in range(87):
    ii = 16 + i * 2
    io = 17 + i * 2
  #  print(ii)
 #   print(io)
    print('echo ' + str(ii) + ' ' + str(ii) + ' | '
          + 'gmx hbond -f nvtt.xtc -n nvtt.ndx -s nvt.tpr -dist dist_xtc_' + str(i + 2) + 'i'
          + ' -b 19900 -e 20000 -dt 0.1 -num num_xtc_' + str(i + 2) + 'i'
          + ' -ang ang_xtc_'  + str(i + 2) + 'i')
    print('echo ' + str(ii) + ' ' + str(io) + ' | '
          + 'gmx hbond -f nvtt.xtc -n nvtt.ndx -s nvt.tpr -dist dist_xtc_' + str(i + 2) + 'o'
          + ' -b 19900 -e 20000 -dt 0.1 -num num_xtc_' + str(i + 2) + 'o'
          + ' -ang ang_xtc_'  + str(i + 2) + 'o')

'''
 echo 100 100 | gmx hbond -f nvtt.gro -n nvtt.ndx -s nvt.tpr -num try_h_11
'''
for i in range(10):
    gro = i+1
    for j in range(87):
        ji = 16 + j * 2
        jo = 17 + j * 2
        print('echo ' + str(ji) + ' ' + str(ji) + ' | '
              + 'gmx hbond -f multi' + str(gro)
              + '.gro -n multi' + str(gro)
              + '.ndx -s nvt.tpr -num num_i_' + str(gro) + '_' + str(j)
              + ' -dist dist_i_' + str(gro) + '_' + str(j)
              + ' -ang ang_i_' +str(gro) + '_' + str(j))
        print('echo ' + str(ji) + ' ' + str(jo) + ' | '
              + 'gmx hbond -f multi' + str(gro)
              + '.gro -n multi' + str(gro)
              + '.ndx -s nvt.tpr -num num_o_' + str(gro) + '_' + str(j)
              + ' -dist dist_o_' + str(gro) + '_' + str(j)
              + ' -ang ang_o_' + str(gro) + '_' + str(j))
