Snowballs = int(input())
best = 0

for i in range(1, Snowballs + 1):
    weight = int(input())
    timeNeeded = int(input())
    quality = int(input())

    final_score = (weight / timeNeeded) ** quality

    if final_score > best:
        weight_best = weight
        timeNeeded_best = timeNeeded
        quality_best = quality
        final_score_best = final_score
        best = final_score


print(f"{weight_best} : {timeNeeded_best} = {int(final_score_best)} ({quality_best})")
