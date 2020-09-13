def solution(companies, applicants):
    answer = []
    companies_dict = {}
    apply = {}

    for i in range(len(companies)):
        company,priority,hire = companies[i].split()
        companies_dict[company] = [{j:priority[j] for j in range(len(priority))},int(hire)]
        apply[company] = set()
        
    applicants_dict = {}
    maximum_cnt = 0

    for i in range(len(applicants)):
        applicant,priority,cnt = applicants[i].split()
        if int(cnt)>maximum_cnt:
            maximum_cnt = int(cnt)
        applicants_dict[applicant] = [{j:priority[j] for j in range(len(priority))},int(cnt),0]

    for i in range(maximum_cnt):
        for j in range(len(applicants)):
            applyer = chr(j+97)
            if applicants_dict[applyer][1]<=i or applicants_dict[applyer][2] == 1:
                continue
            apply_company = applicants_dict[applyer][0][i]
            apply[apply_company].add(applyer)
        for j in range(len(companies)):
            company = chr(j+65)
            if len(apply[company]) <= companies_dict[company][1]:
                for k in apply[company]:
                    applicants_dict[k][2] = 1
            else:
                hire_set = set()
                fail_set = set()
                for k in range(len(applicants)):
                    if companies_dict[company][0][k] in apply[company]:
                        hire_set.add(companies_dict[company][0][k])
                    if len(hire_set)>=companies_dict[company][1]:
                        break
                fail_set = apply[company] - hire_set
                apply[company] = apply[company] & hire_set
                for k in fail_set:
                    applicants_dict[k][2] = 0
                for k in hire_set:
                    applicants_dict[k][2] = 1
    
    for i in range(len(companies)):
        company = chr(i+65)
        hire_list = ""
        for i in apply[company]:
            hire_list += i
        company += "_" + ''.join(sorted(hire_list))
        answer.append(company)
    return answer