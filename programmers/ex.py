with open('grade.txt', 'r') as file:
    lines = file.readlines()

    print("** 2023 해외봉사 결과 발표 **")
    print("학            번      이        름       평      균     판    정")
    print("========     ======       =====     ====")

    total_students = 0
    pass_count = 0
    fail_count = 0

    for line in lines:
        data = line.strip().split(',')
        student_id, name, interview_score, english_score = data
        avg_score = (int(interview_score) + int(english_score)) / 2
        result = "PASS" if avg_score >= 90 else ""

        print(f"{student_id}\t{name}\t{avg_score:.2f}\t{result}")

        total_students += 1
        if result == "PASS":
            pass_count += 1
        else:
            fail_count += 1

    summary = f"\n{'='*40}\n지원자 수: {total_students}\n합격자 수: {pass_count}\n불합격자 수: {fail_count}"
    print(summary)