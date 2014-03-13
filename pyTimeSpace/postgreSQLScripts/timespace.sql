CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;

-- run legacy.sql

CREATE TABLE dots(gid SERIAL PRIMARY KEY
   , geom geometry(POINT,4326)
   , time timestamp);
   
SELECT AddGeometryColumn('dots', 'geom_2160', 2160, 'POINT', 2, false);