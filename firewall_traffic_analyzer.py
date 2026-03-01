# FILE NAME - firewall_traffic_analyzer.py

# NAME: Patrick Babb
# DATE: 3/1/2026
# BRIEF DESCRIPTION: using and/or for the first time with conditionals in a functional example 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience


   # Prompt the user for:
    #    The port number as an int (e.g., 80, 22, 443, 3389).
    #    The data transfer size in megabytes as in int (MB).

   # Categorize traffic using if-elif-else:
#    If port 22 (SSH) or port 3389 (RDP) and transfer size >= 100MB output "HIGH RISK: Potential unauthorized
#    remote access detected!"
   # Note: Use parentheses around the or expression to make sure both ports are considered. In Python,
   # the and operator has higher precedence than the or operator.
  #  Else if port 80 (HTTP) with transfer size > 100MB output "MEDIUM RISK: Large unencrypted data
  #  transfer detected."
   # Else if port 443 (HTTPS) output "LOW RISK: Secure encrypted transfer detected."
 #   Else output "UNKNOWN: Unrecognized traffic pattern."

#    Print a firewall log message summarizing the risk level.



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    firewall_traffic_analyser()

def firewall_traffic_analyser():
    print('=== Network Traffic Security Analyzer ===')
    port = int(input('Enter the port number (e.g., 80, 22, 443, 3389): '))
    transfer_size = int(input('Enter the data transfer size in megabytes (MB): '))
    print('FIREWALL LOG:')
    print(f'Port: {port}, Transfer Size: {transfer_size} MB')
    if (port == 22 or port == 3389) and transfer_size >= 100:
        print('Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!')
    elif port == 80 and transfer_size > 100:
        print('Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.')
    elif port == 443:
        print('Risk Assessment: LOW RISK: Secure encrypted transfer detected.')
    else:
        print('Risk Assessment: UNKNOWN: Unrecognized traffic pattern.')

    

main()









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 1200

FIREWALL LOG:
Port: 22, Transfer Size: 1200 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?
Once I started reading the assignment and translating what was said into how it would be said in Python I started to
understand it much better







'''
