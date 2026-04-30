# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
# Keys are service names (strings), values are hourly rates (integers)
services = {
    "IT Support": 85,
    "Mobile App Development": 165,
    "Database Administration": 140,
    "Website Maintenance": 120,
    "Basic Web Support": 90,
    "Mobile App Support": 130,
    "IT Help Desk": 75,
    "Cloud File Management": 110,
    "Data Entry": 65,
    "System Maintenance": 95
}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {
    "company_name": "Apple",
    "contact_person": "Montel Fish",
    "email": "mfish@apple.com",
    "phone": "555-101-2020"
}
 
customer2 = {
    "company_name": "Walmart",
    "contact_person": "Jack Johnson",
    "email": "jjohnson@walmart.com",
    "phone": "555-202-3030"
}
 
customer3 = {
    "company_name": "Meta",
    "contact_person": "Kayla Goodwin",
    "email": "kgoodwin@meta.com",
    "phone": "555-303-4040"
}
 
customer4 = {
    "company_name": "Tesla",
    "contact_person": "James Okafor",
    "email": "jokafor@tesla.com",
    "phone": "555-404-5050"
}


# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
# String keys (C001, C002...) map to the individual customer dicts above
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
# .items() returns both the key (customer_id) and value (info dict) in each iteration
for cid, info in customers.items():
    print(f"{cid}: {info}")

# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here

# Direct key access retrieves the full nested dictionary for C002
c002_info = customers["C002"]
print(f"Customer C002 Info: {c002_info}")

# Chain two bracket accesses: first get the C003 dict, then get the contact_person field
c003_contact = customers["C003"]["contact_person"]
print(f"Customer C003 Contact Person: {c003_contact}")

# .get() is safe for keys that may not exist — returns the default string instead of raising a KeyError
c999_info = customers.get("C999", "Customer does not exist.")
print(f"Customer C999 Lookup: {c999_info}")

# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
# UPDATE: 
customers["C001"]["phone"] = "800-275-2273"
# ADD: Adding a new key to an existing dict
customers["C002"]["industry"] = "Retail"
#DISPLAY UPDATES
print("\nUpdated C001 (phone changed):")
for key, value in customers["C001"].items():
    print(f"{key}: {value}")

print("\nUpdated C002 (industry field added):")
for key, value in customers["C002"].items():
    print(f"{key}: {value}")

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}

print("\n\nProject Information:")
print("-" * 60)
# Add your code here

projects = {
    "C001": [
        {"name": "Homepage Redesign", "service": "Website Maintenance", "hours": 12, "budget": 600},
        {"name": "Fix Broken Contact Form", "service": "Basic Web Support", "hours": 8, "budget": 350}
    ],
    "C002": [
        {"name": "Update Mobile App Icon", "service": "Mobile App Support", "hours": 6, "budget": 250},
        {"name": "Reset Employee Passwords", "service": "IT Help Desk", "hours": 5, "budget": 200}
    ],
    "C003": [
        {"name": "Organize Shared Drive", "service": "Cloud File Management", "hours": 7, "budget": 300},
        {"name": "Clean Up Sales Spreadsheet", "service": "Data Entry", "hours": 6, "budget": 250}
    ],
    "C004": [
        {"name": "Install Printer Drivers", "service": "IT Support", "hours": 4, "budget": 150},
        {"name": "Software Updates Rollout", "service": "System Maintenance", "hours": 5, "budget": 200}
    ]
}

# Nested loop: outer iterates customers, inner iterates each customer's project list
for customer_id, project_list in projects.items():
    print(f"Projects for {customer_id} ({customers[customer_id]['company_name']}):")
    for project in project_list:
        print(f"  - {project['name']} | Service: {project['service']} | Hours: {project['hours']} | Budget: ${project['budget']:,.2f}")
    print()

# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
for customer_id, project_list in projects.items():
    print(f"{customers[customer_id]['company_name']} ({customer_id}):")
    for project in project_list:
        # Look up the hourly rate from the services dictionary using the project's service field
        hourly_rate = services[project["service"]]
        # Cost = rate per hour multiplied by the number of hours worked
        calculated_cost = hourly_rate * project["hours"]
        print(f"  {project['name']}")
        print(f"    Service: {project['service']} @ ${hourly_rate}/hr x {project['hours']} hrs = ${calculated_cost:,.2f}")
    print()

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here

# .keys() returns all keys in the dictionary (the customer IDs)
print("All Customer IDs:")
for cid in customers.keys():
    print(f"  {cid}")

# .values() returns all value dicts; we extract company_name from each
print("\nAll Company Names:")
for info in customers.values():
    print(f"  {info['company_name']}")

# len() on a dictionary counts the number of key-value pairs
print(f"\nTotal Number of Customers: {len(customers)}")

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here

# Build service_counts by iterating all projects and tallying each service name
service_counts = {}
for project_list in projects.values():
    for project in project_list:
        service = project["service"]
        # If the service is already a key, increment; otherwise initialize to 1
        if service in service_counts:
            service_counts[service] += 1
        else:
            service_counts[service] = 1

for service, count in service_counts.items():
    print(f"  {service}: {count} project(s)")

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here

# Flatten all projects into a single list to make aggregation easier
total_hours = 0
total_budget = 0
all_projects = []

for project_list in projects.values():
    for project in project_list:
        total_hours += project["hours"]
        total_budget += project["budget"]
        all_projects.append(project)

# Divide total budget by number of projects for the average
avg_budget = total_budget / len(all_projects)

# max_budget and min_budget store the numeric budget value of the extreme projects
max_budget = max(p["budget"] for p in all_projects)
min_budget = min(p["budget"] for p in all_projects)

# Also find the project names for display purposes
max_budget_project = max(all_projects, key=lambda p: p["budget"])
min_budget_project = min(all_projects, key=lambda p: p["budget"])

print(f"  Total Hours Across All Projects:  {total_hours} hrs")
print(f"  Total Budget Across All Projects: ${total_budget:,.2f}")
print(f"  Average Project Budget:           ${avg_budget:,.2f}")
print(f"  Most Expensive Project:  {max_budget_project['name']} (${max_budget:,.2f})")
print(f"  Least Expensive Project: {min_budget_project['name']} (${min_budget:,.2f})")

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here
for customer_id, project_list in projects.items():
    info = customers[customer_id]
    num_projects = len(project_list)
    # Generator expressions inside sum() efficiently total numeric fields
    cust_hours = sum(p["hours"] for p in project_list)
    cust_budget = sum(p["budget"] for p in project_list)

    print(f"Customer: {info['company_name']} ({customer_id})")
    print(f"  Contact:        {info['contact_person']}")
    print(f"  Email:          {info['email']}")
    print(f"  Phone:          {info['phone']}")
    print(f"  Number of Projects: {num_projects}")
    print(f"  Total Hours:    {cust_hours} hrs")
    print(f"  Total Budget:   ${cust_budget:,.2f}")
    print()

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
# Dictionary comprehension: {new_key: new_value for key, value in original.items()}
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

for service, rate in adjusted_rates.items():
    print(f"  {service}: ${rate:,.2f}/hr")

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
# The `if cid in projects` condition filters to only customers with a projects entry
active_customers = {cid: info for cid, info in customers.items() if cid in projects}

for customer_id, info in active_customers.items():
    print(f"  {customer_id}: {info['company_name']} - {info['contact_person']}")

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
# sum() inside the comprehension totals the budget field across each customer's project list
customer_budgets = {cid: sum(p["budget"] for p in project_list) for cid, project_list in projects.items()}

for customer_id, budget in customer_budgets.items():
    print(f"  {customer_id} ({customers[customer_id]['company_name']}): ${budget:,.2f}")

# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
# Ternary (conditional) expressions inside a comprehension: value_if_true if condition else value_if_false
service_tiers = {
    service: "Premium" if rate >= 200 else ("Standard" if rate >= 100 else "Basic")
    for service, rate in services.items()
}

for service, tier in service_tiers.items():
    print(f"  {service} (${services[service]}/hr): {tier}")

# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
def validate_customer(customer_dict):
    """Check that all required fields exist and are non-empty. Returns True if valid."""
    required_fields = ["company_name", "contact_person", "email", "phone"]
    for field in required_fields:
        # Return False immediately if a field is missing or empty
        if field not in customer_dict or customer_dict[field] == "":
            return False
    return True

for customer_id, info in customers.items():
    is_valid = validate_customer(info)
    status = "Valid" if is_valid else "Invalid"
    print(f"  {customer_id} ({info['company_name']}): {status}")

# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses

print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here

# Assign a status to each project by iterating all projects with a flat list
# Status values cycle through "active", "completed", and "pending"
all_flat_projects = [p for project_list in projects.values() for p in project_list]
status_options = ["active", "completed", "pending"]
for i, project in enumerate(all_flat_projects):
    # Use modulo to cycle through the three statuses evenly
    project["status"] = status_options[i % len(status_options)]

# Count how many projects fall into each status category
status_counts = {}
for project in all_flat_projects:
    status = project["status"]
    if status in status_counts:
        status_counts[status] += 1
    else:
        status_counts[status] = 1

for status, count in status_counts.items():
    print(f"  {status.capitalize()}: {count} project(s)")

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
def analyze_customer_budgets(projects_dict):
    """
    Aggregate budget statistics per customer.
    Returns a dict mapping customer IDs to {'total', 'average', 'count'}.
    """
    budget_analysis = {}
    for customer_id, project_list in projects_dict.items():
        total = 0
        count = len(project_list)
        # Accumulate each project's budget into the running total
        for project in project_list:
            total += project["budget"]
        # Guard against division by zero for customers with no projects
        average = total / count if count > 0 else 0
        budget_analysis[customer_id] = {
            "total": total,
            "average": average,
            "count": count
        }
    return budget_analysis

budget_analysis_results = analyze_customer_budgets(projects)
for customer_id, stats in budget_analysis_results.items():
    print(f"  {customer_id} ({customers[customer_id]['company_name']}):")
    print(f"    Projects: {stats['count']}  |  Total: ${stats['total']:,.2f}  |  Avg: ${stats['average']:,.2f}")

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
def recommend_services(customer_id, customers, projects, services):
    """
    Recommend services the customer has not yet used.
    Filters recommendations based on whether the estimated cost fits
    within 1.5x the customer's average project budget.
    """
    # Collect services already used by this customer
    used_services = set()
    customer_budget = 0

    if customer_id in projects:
        for project in projects[customer_id]:
            used_services.add(project["service"])
            customer_budget += project["budget"]

    # Calculate average budget per project to estimate affordability
    num_projects = len(projects.get(customer_id, []))
    avg_budget = customer_budget / num_projects if num_projects > 0 else 0

    recommendations = []
    for service, rate in services.items():
        if service not in used_services:
            # Estimate cost assuming a standard 40-hour engagement
            estimated_cost = rate * 40
            # Only recommend if the estimated cost is within 1.5x their average project spend
            if estimated_cost <= avg_budget * 1.5:
                recommendations.append(service)

    return recommendations

for customer_id in customers.keys():
    recs = recommend_services(customer_id, customers, projects, services)
    company = customers[customer_id]["company_name"]
    if recs:
        print(f"  {customer_id} ({company}) - Recommended Services:")
        for rec in recs:
            print(f"    * {rec} (${services[rec]}/hr)")
    else:
        print(f"  {customer_id} ({company}): No additional recommendations at this time.")
    print()