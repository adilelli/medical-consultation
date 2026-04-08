# medical-consultation
Users can search medical reference code for disease, users can create consultation, users can view consultation


The front end is in Nuxt because of possibility of server side rendering eventhough now its client side rendering.

The backend is in Fast API with database in Postgres.

Database Model

There are 4 tables. 
1) Diagnosis which containes the diagnstic codes, description
2) Consultation which contains the consultation which links to diagnosis, doctor and patient.
3) User which contains the email, name and roles (1 for doctor and 2 for paitent).
4) Auth which stored hashed password with user id linked to user database

API
1) Search Consultation
2) Save consultation
3) Search Diagnosis
4) Create User
5) Search Users
6) Login

Security Consideration
1) Password hashing to encrypt the password
2) Set JWT as cookie so that it could not be read from javascript in browser
3) Separation of Auth from User DB.

Performance Consideration
1) Preload all consultation data so that when debouncing is performed on empty search string, it will read from memory instead of refetching API.
2) Index frequently queried column to improve db read speed from O(N) to O (log N) complexity.
2) We don't need caching for as we only have 100 diagnostic codes. If we were planning to scale up to tens of thousands of codes, knowing that the data is relatively static wiht little concerns of stale diagnostic codes, consider caching server side to improve minimise database operation. 