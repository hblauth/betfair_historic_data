cd "C:\OpenSSL-Win32\bin"

openssl genrsa -out client-2048.key 2048

openssl req -new -config openssl.cfg -key client-2048.key -out client-2048.csr

openssl x509 -req -days 365 -in client-2048.csr -signkey client-2048.key -out client-2048.crt -extfile openssl.cfg -extensions ssl_client 

openssl pkcs12 -export -in client-2048.crt -inkey client-2048.key -out client-2048.p12

pause