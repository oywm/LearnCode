# def salary_search():
#     b = True
#     di_pi = {}
#     salary = []
#     # di_pi_list_2 = []
#     work_nums, person_nums = map(int, (input('请输入工作的数量和输入小伙伴的数量以空格隔开：').split()))
#     for i in range(work_nums):
#         # di, pi = map(int, (input('请输入工作难度和对应的薪水以空格隔开：').split()))
#         di_pi_list_2 = list(map(int, (input('请输入工作难度和对应的薪水以空格隔开：').split())))
#         if not di_pi_list_2:
#             continue
#         else:
#             di_pi[di_pi_list_2[1]] = di_pi_list_2[0]
#         # di_pi[pi] = di
#     ai = map(int, (input('请依次输入小伙伴的能力值用空格隔开：').split()))
#     ai = list(ai)
#     di_pi_list = sorted(di_pi.keys())[::-1]
#     for i in range(len(ai)):
#         for j in range(len(di_pi_list)):
#             if ai[i] >= di_pi[di_pi_list[j]] and b == True:
#                 salary.append(di_pi_list[j])
#                 b = False
#             else:
#                 if j == len(di_pi_list) - 1 and b == True:
#                     salary.append(None)
#
#         b = True
#     for i in range(len(salary)):
#         if i <= len(salary) - 1:
#             print(salary[i])
#
#     # return salary_search()
#
#
# salary_search()
#
#
