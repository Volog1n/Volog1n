import json

def create_funnel_report():
    """
    Creates a funnel report by matching user visits with their purchases.
    Reads from purchase_log.txt and visit_log.csv, writes results to funnel.csv.
    """
    # Create purchases dictionary from purchase_log.txt
    purchases = {}
    purchase_count = 0
    with open('Downloads/purchase_log.txt', encoding='utf-8') as f:
        next(f)  # skip header
        for line in f:
            record = json.loads(line)
            purchases[record['user_id']] = record['category']
            purchase_count += 1

    print(f"Loaded purchase records: {purchase_count}")

    # Process visits and create funnel.csv
    visit_count = 0
    match_count = 0
    with open('Downloads/visit_log.csv') as visits, \
         open('Downloads/funnel.csv', 'w') as funnel:
        
        # Write header
        funnel.write('user_id,source,category\n')
        
        # Skip header in visit_log.csv
        next(visits)
        
        # Process each line from visit_log.csv
        for line in visits:
            visit_count += 1
            user_id, source = line.strip().split(',')
            if user_id in purchases:  # if user made a purchase
                match_count += 1
                category = purchases[user_id]
                funnel.write(f'{user_id},{source},{category}\n')

    print(f"\nProcessed visits: {visit_count}")
    print(f"Found matches (visits with purchases): {match_count}")

if __name__ == '__main__':
    create_funnel_report()
