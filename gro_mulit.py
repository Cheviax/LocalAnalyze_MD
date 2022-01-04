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