def findManagersWithAtLeastFiveDirectReports(employees: list[dict]) -> list[dict]:
    """
    Finds managers with at least five direct reports.

    Args:
        employees: A list of dictionaries, where each dictionary represents an employee
                   with keys 'id', 'name', 'department', and 'managerId'.

    Returns:
        A list of dictionaries, where each dictionary contains the 'name'
        of a manager who has at least five direct reports.
    """
    
    manager_reports_count = {}
    for employee in employees:
        manager_id = employee.get("managerId")
        if manager_id is not None:
            manager_reports_count[manager_id] = manager_reports_count.get(manager_id, 0) + 1

    qualified_manager_ids = set()
    for manager_id, count in manager_reports_count.items():
        if count >= 5:
            qualified_manager_ids.add(manager_id)

    id_to_name_map = {employee["id"]: employee["name"] for employee in employees}

    result = []
    for manager_id in qualified_manager_ids:
        if manager_id in id_to_name_map:
            result.append({"name": id_to_name_map[manager_id]})

    return result