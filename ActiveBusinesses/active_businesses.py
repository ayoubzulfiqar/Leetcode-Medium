def active_businesses(businesses_data):
    active_business_names = []
    for business in businesses_data:
        # Retrieve the count of events, defaulting to 0 if the key is missing
        events_count = business.get('events', 0)
        # Retrieve the count of partners, defaulting to 0 if the key is missing
        partners_count = business.get('partners', 0)

        # A business is considered active if it has both:
        # 1. More than 0 events
        # 2. More than 0 partners
        if events_count > 0 and partners_count > 0:
            active_business_names.append(business['business'])
            
    return active_business_names