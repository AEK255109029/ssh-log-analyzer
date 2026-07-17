def get_risk(count):
    if count >= 5:
        return "HIGH"
    elif count >= 3:
        return "MEDIUM"
    else:
        return "LOW"


def risk_summary(attackers):

    summary = {
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0
    }

    for count in attackers.values():
        summary[get_risk(count)] += 1

    return summary


def top_attackers(attackers, limit=10):

    result = []

    for ip, count in attackers.items():
        result.append(
            (
                ip,
                count,
                get_risk(count)
            )
        )

    result.sort(key=lambda x: x[1], reverse=True)

    return result[:limit]


def top_users(users, limit=10):

    return sorted(
        users.items(),
        key=lambda x: x[1],
        reverse=True
    )[:limit]
