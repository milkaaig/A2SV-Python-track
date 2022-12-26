def swap_case(s):
  
    result=""
    for ptr in s:
        if ptr.isupper():
            result+=ptr.lower()
        else:
            result+=ptr.upper()
    return result
