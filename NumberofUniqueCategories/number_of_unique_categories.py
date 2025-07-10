def get_unique_category_count(categories):
    unique_categories = set(categories)
    return len(unique_categories)

if __name__ == "__main__":
    sample_categories_1 = ["Electronics", "Books", "Electronics", "Home & Garden", "Books", "Toys"]
    result_1 = get_unique_category_count(sample_categories_1)
    print(result_1)

    sample_categories_2 = ["Apparel", "Apparel", "Apparel"]
    result_2 = get_unique_category_count(sample_categories_2)
    print(result_2)

    sample_categories_3 = []
    result_3 = get_unique_category_count(sample_categories_3)
    print(result_3)