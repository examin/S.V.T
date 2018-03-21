quick readme>>>>>>>>>>>>>>>>>>>>>>>>>

requirements:
 1. python3
 2. mangobd: for initial store of vulnerbility information
 3. sax :xml parsing

 a) db_mgmt.py: -p = populate the database, A demo of database at bugzilla.redhat.com
   Note.run this on the first time  only .
 b) search.py : -p = search for product "Apache Tomcat 7" or "Apache Tomcat 8" should work, ideal is using CPE notation
                -o = output (currently html,csv,json are supported)
examples:
./search.py -p apache:Tomcta:7 -o html