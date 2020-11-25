'''
Write a function validate_email_id(email_id) to validate email Id
    It should contain one '@' character and '.com'
    '.com' should be present at the end of the email id.
    Domain name should be either 'gmail', 'yahoo' or 'hotmail'
Note: Consider the format of email id to be username@domain_name.com 
'''

def validate_email_id(email_id):
    if '@' in email_id and email_id.endswith(".com") and ('gmail' in email_id or 'yahoo' in email_id or 'hotmail' in email_id):
        return True
    else:
        return False
        
print(validate_email_id("atulpunde@gmail.com ww"))