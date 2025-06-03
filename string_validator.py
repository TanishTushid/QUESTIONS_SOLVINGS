if __name__ == '__main__':
    s = input()
    
    #alphanumeric characters
    alpha_numeric = any(c.isalnum() for c in s )
    print(alpha_numeric)
    
    # alphabetical characters
    alpha_betical_ch = any(c.isalpha() for c in s )
    print(alpha_betical_ch)
    
    #digits
    is_digit = any(c.isdigit() for c in s )
    print(is_digit)
    
    #lowercase characters
    lower_ch = any(c.islower() for c in s )
    print(lower_ch)
    
    #uppercase characters
    upper_ch = any(c.isupper() for c in s )
    print(upper_ch)