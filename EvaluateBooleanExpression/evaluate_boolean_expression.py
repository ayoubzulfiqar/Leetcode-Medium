def evaluate_boolean_expression(expression_str: str) -> bool:
    tokens = []
    i = 0
    while i < len(expression_str):
        if expression_str[i].isspace():
            i += 1
            continue
        
        if expression_str[i] == '(':
            tokens.append('(')
            i += 1
        elif expression_str[i] == ')':
            tokens.append(')')
            i += 1
        elif expression_str[i:i+4] == 'TRUE':
            tokens.append('TRUE')
            i += 4
        elif expression_str[i:i+5] == 'FALSE':
            tokens.append('FALSE')
            i += 5
        elif expression_str[i:i+3] == 'AND':
            tokens.append('AND')
            i += 3
        elif expression_str[i:i+2] == 'OR':
            tokens.append('OR')
            i += 2
        elif expression_str[i:i+3] == 'NOT':
            tokens.append('NOT')
            i += 3
        else:
            raise ValueError(f"Invalid character or token at position {i}: {expression_str[i:]}")
    
    current_token_idx = 0
    
    def peek():
        nonlocal current_token_idx
        if current_token_idx < len(tokens):
            return tokens[current_token_idx]
        return None

    def consume(expected_token=None):
        nonlocal current_token_idx
        if current_token_idx >= len(tokens):
            raise ValueError("Unexpected end of expression")
        
        token = tokens[current_token_idx]
        if expected_token and token != expected_token:
            raise ValueError(f"Expected '{expected_token}' but got '{token}'")
        current_token_idx += 1
        return token

    def parse_factor():
        token = peek()
        if token == 'TRUE':
            consume('TRUE')
            return True
        elif token == 'FALSE':
            consume('FALSE')
            return False
        elif token == 'NOT':
            consume('NOT')
            return not parse_factor()
        elif token == '(':
            consume('(')
            result = parse_expression()
            consume(')')
            return result
        else:
            raise ValueError(f"Unexpected token in factor: {token}")

    def parse_term():
        result = parse_factor()
        while peek() == 'AND':
            consume('AND')
            result = result and parse_factor()
        return result

    def parse_expression():
        result = parse_term()
        while peek() == 'OR':
            consume('OR')
            result = result or parse_term()
        return result

    result = parse_expression()
    
    if current_token_idx != len(tokens):
        raise ValueError("Extra tokens at end of expression")
        
    return result