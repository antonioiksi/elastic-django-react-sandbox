#!/bin/bash

rm postgres.sql
cp postgres-origin.sql postgres.sql

echo "Please enter user: "
read input_user
echo "Please enter pwd: "
read input_pwd
echo "Please enter db: "
read input_db
#echo "You entered: $input_variable"

sed -i -e 's/username/'$input_user'/g' postgres.sql
sed -i -e 's/password/'$input_pwd'/g' postgres.sql
sed -i -e 's/database/'$input_db'/g' postgres.sql

#cat postgres.sql
psql -f postgres.sql

