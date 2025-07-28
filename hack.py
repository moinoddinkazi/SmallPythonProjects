# n=int(input())
# jobs = []
# for i in range(n):
#     jobs.append(int(input()))
# m = int(input())
# lst = []
# skill_dict = {}
# for i in range(m):
#     a = int(input())
#     skill_dict[a] = 0
#     lst.append(a)
# for i in range(m):
#     skill_dict[lst[i]] = max(int(input()),skill_dict[lst[i]])
# if max(jobs) > max(lst):
#     print(-1)
# else:
#     shift = 0
#     skill_selected = 0
#     curr_endurance = 0
#     i = 0
#     j = list(set(lst))
#     j.sort()
#     while(i<n):
#         k = 0
#         while(jobs[i] > j[k] and k < len(j)):
#             k+=1
#         skill_selected = j[k]
#         curr_endurance = skill_dict[j[k]]
#         while(i<n and jobs[i]<=skill_selected and curr_endurance>0):
#             curr_endurance -= 1
#             i += 1
#         shift += 1
#     print(shift)


n = int(input())
req = []
for _ in range(n):
    req.append(int(input()))
m = int(input())
skill = []
for _ in range(m):
    skill.append(int(input()))
end = []
for _ in range(m):
    end.append(int(input()))
d = dict(zip(skill, end))
skill.sort()
end = sorted(d.values())
c=0
for j in req:
    for i in range(m):
        if skill[i]>=j and end[i]>=1:
            skill[i]-=j
            end[i]-=1
            c+=1
            break
c-=1
if(c==0):
    print(-1)
    quit()
print(c)