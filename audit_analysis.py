def analyze_results(results):
    report = []
    for row in results:
        username, role, password_policy = row
        if password_policy == "Weak":
            report.append(f"User {username} has a weak password policy. [Risk]")
        else:
            report.append(f"User {username} meets password policy standards. [Compliant]")
    return report
