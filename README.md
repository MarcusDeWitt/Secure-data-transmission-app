# Secure-data-transmission-app

## CIA Explanation

### Confidentiality
This app upholds all the values with the CIA triad, Confidentiality, Integrity, and Availability. Starting with Confidentiality, the app encrypts the input from the user first, whether it is a string or file attachment. And the only person who can decrypt it will be someone with the same key, thus protecting it from being read by someone who is not supposed to.

### Integrity
The app also verifies integrity, by checking to make sure hash values match from encryption to decryption. This verifies that no data has been changed anywhere in between, which confirms the data was not changed with in anyway.

### Availability
Availability is presented here through the error handling throughout the application. Not allowing invalid inputs and creating error handling for file erros keeps the app from crashing, which allows the encrypted data to be decrypted as long as the user has the key. 

## Entropy and Key Generation
In this app a random key is generated and used for both the encryption and decryption (symmetric) and prevents the data from being read without having access or knowledge of what this key is. The entropy is shown with the key as well, because a random key is generated everytime and this results in a highly unlikely chance of the key being predicted. Having both of these in an application is sure to provide strong security and protection for data.
