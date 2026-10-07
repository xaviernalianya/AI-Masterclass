def calculate_project_rate(
    hours_estimated,
    hourly_target,       # what you want to earn per hour
    complexity_factor,   # 1.0 = standard, 1.3 = complex, 1.5 = very complex
    revision_buffer=0.2, # 20% buffer for revisions
    market_floor=150,    # minimum charge for any project
):
    """Calculate a project price from time estimate and target rate."""
    base_cost  = hours_estimated * hourly_target
    with_complexity = base_cost * complexity_factor
    with_buffer     = with_complexity * (1 + revision_buffer)
    final_price = max(with_buffer, market_floor)

    return {
        "hours_estimated":  hours_estimated,
        "hourly_target":    hourly_target,
        "base_cost":        round(base_cost),
        "with_complexity":  round(with_complexity),
        "with_buffer":      round(with_buffer),
        "quote_price":      round(final_price / 50) * 50,  # round to nearest $50
    }

# Define the projects to quote
projects = [
    {
        "name":               "Automated weekly CSV report",
        "hours_estimated":    8,
        "hourly_target":      35,
        "complexity_factor":  1.0,
    },
    {
        "name":               "FastAPI + Supabase integration",
        "hours_estimated":    20,
        "hourly_target":      40,
        "complexity_factor":  1.3,
    },
    {
        "name":               "Full SMP tracker tool with dashboard",
        "hours_estimated":    50,
        "hourly_target":      45,
        "complexity_factor":  1.5,
    },
]

SEPARATOR = "=" * 58
print(SEPARATOR)
print("  PROJECT QUOTE CALCULATOR")
print(SEPARATOR)

for p in projects:
    result = calculate_project_rate(
        hours_estimated   = p["hours_estimated"],
        hourly_target     = p["hourly_target"],
        complexity_factor = p["complexity_factor"],
    )
    print(f"\nProject: {p['name']}")
    print(f"  Hours estimated: {result['hours_estimated']}h")
    print(f"  Base cost:       ${result['base_cost']:,}  ({result['hours_estimated']}h x ${result['hourly_target']}/h)")
    print(f"  With complexity: ${result['with_complexity']:,}  (x{p['complexity_factor']} factor)")
    print(f"  With 20% buffer: ${result['with_buffer']:,}")
    print(f"  Quote price:     ${result['quote_price']:,}  (rounded to nearest $50)")

print()
print(SEPARATOR)
