def most_answers(time, diff, timing, deadlines): #timing 1 for hard 0 for easy time
    current_time = 0
    answers = 0
    new_idea = 0
    for i in range(len(diff)):
        new_idea += timing[diff[i]]
    if new_idea <= time:
        return len(diff)
    while time > current_time and diff:
        print("got here", time, diff, timing, deadlines, current_time)
        early = min(deadlines)
        early_index = deadlines.index(early)
        sec_smallest = 2000000000
        for i in range(len(deadlines)):
            if sec_smallest < deadlines[i] and i != early_index:
                sec_smallest = deadlines[i]
        question = diff[early_index]
        if current_time + timing[question] <= early and (min([(early - current_time - 1) // timing[0], diff.count(0)]) < min([(sec_smallest - current_time + timing[question]) // timing[0], diff.count(0)])) :
            current_time += timing[question]
            deadlines.pop(early_index)
            diff.pop(early_index)
            answers += 1
        else:
            all_pos = (early - current_time - 1) // timing[0]
            if all_pos < 0:
                all_pos = 0
            answers += min([all_pos, diff.count(0)]) 
            return answers
    return answers

useless = int(input())
for i in range(useless):
    n, T, a, b = [int(j) for j in input().split()]
    diffs = [int(p) for p in input().split()]
    times = [int(k) for k in input().split()]
    print(most_answers(T, diffs, [a, b], times))
