import re

def analyze_dna_patterns(samples_table):
    """
    Analyzes DNA sequences for specific patterns and returns a new table
    with pattern indicators.

    Args:
        samples_table: A list of dictionaries, where each dictionary represents
                       a row in the Samples table with keys 'sample_id',
                       'dna_sequence', and 'species'.

    Returns:
        A list of dictionaries, each representing a row in the result table,
        ordered by sample_id in ascending order.
    """
    
    result = []
    for row in samples_table:
        sample_id = row['sample_id']
        dna_sequence = row['dna_sequence']
        species = row['species']

        # Check for 'ATG' start codon
        has_start = 1 if dna_sequence.startswith("ATG") else 0

        # Check for 'TAA', 'TAG', or 'TGA' stop codons
        has_stop = 1 if dna_sequence.endswith("TAA") or \
                        dna_sequence.endswith("TAG") or \
                        dna_sequence.endswith("TGA") else 0

        # Check for 'ATAT' motif
        has_atat = 1 if "ATAT" in dna_sequence else 0

        # Check for at least 3 consecutive 'G's
        # Using regex to find 'GGG' or more (e.g., 'GGGG', 'GGGGG')
        has_ggg = 1 if re.search(r'GGG', dna_sequence) else 0

        result.append({
            'sample_id': sample_id,
            'dna_sequence': dna_sequence,
            'species': species,
            'has_start': has_start,
            'has_stop': has_stop,
            'has_atat': has_atat,
            'has_ggg': has_ggg
        })
    
    # Sort the result by sample_id in ascending order
    result.sort(key=lambda x: x['sample_id'])
    
    return result