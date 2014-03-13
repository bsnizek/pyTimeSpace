-- run this script in an empty database
-- (c) Bernhard Snizek

CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;

-- run legacy.sql

CREATE TABLE dots(gid SERIAL PRIMARY KEY
   , geography geometry(POINT,4326)
   , time timestamp);