def find_safe_countries(countries_data):
    safe_countries = []
    
    MIN_GDP_GROWTH = 2.0
    MAX_INFLATION_RATE = 3.0
    MIN_CORRUPTION_INDEX = 70
    MAX_DEBT_TO_GDP = 60.0
    SAFE_CREDIT_RATINGS = {"AAA", "AA+", "AA"}

    for country in countries_data:
        is_safe = True
        
        if country.get("gdp_growth", 0.0) < MIN_GDP_GROWTH:
            is_safe = False
        
        if country.get("inflation_rate", float('inf')) > MAX_INFLATION_RATE:
            is_safe = False
            
        if country.get("corruption_index", 0) < MIN_CORRUPTION_INDEX:
            is_safe = False
            
        if country.get("debt_to_gdp", float('inf')) > MAX_DEBT_TO_GDP:
            is_safe = False
            
        if country.get("credit_rating") not in SAFE_CREDIT_RATINGS:
            is_safe = False
            
        if is_safe:
            safe_countries.append(country["name"])
            
    return safe_countries

if __name__ == "__main__":
    countries_data = [
        {
            "name": "CountryA",
            "gdp_growth": 3.5,
            "inflation_rate": 2.1,
            "corruption_index": 85,
            "debt_to_gdp": 55.0,
            "credit_rating": "AAA"
        },
        {
            "name": "CountryB",
            "gdp_growth": 1.8,
            "inflation_rate": 4.5,
            "corruption_index": 60,
            "debt_to_gdp": 70.0,
            "credit_rating": "A+"
        },
        {
            "name": "CountryC",
            "gdp_growth": 2.5,
            "inflation_rate": 2.8,
            "corruption_index": 75,
            "debt_to_gdp": 50.0,
            "credit_rating": "AA+"
        },
        {
            "name": "CountryD",
            "gdp_growth": 4.0,
            "inflation_rate": 1.5,
            "corruption_index": 90,
            "debt_to_gdp": 65.0,
            "credit_rating": "AAA"
        },
        {
            "name": "CountryE",
            "gdp_growth": 3.0,
            "inflation_rate": 2.0,
            "corruption_index": 72,
            "debt_to_gdp": 58.0,
            "credit_rating": "AA"
        },
        {
            "name": "CountryF",
            "gdp_growth": 1.0,
            "inflation_rate": 1.0,
            "corruption_index": 80,
            "debt_to_gdp": 40.0,
            "credit_rating": "AAA"
        }
    ]

    safe_countries_list = find_safe_countries(countries_data)
    # The result is stored in safe_countries_list.