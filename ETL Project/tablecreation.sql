DROP TABLE central_and_south;

CREATE TABLE central_and_south(
	zipcode             int,
	population			int,
	median_age          real,	
	household_income    real,
	per_capita_income   real,
	poverty_count       int,
	nicaraguans         int,
	costa_ricans        int,
	guatemalans         int,
	hondurans           int,
	panamanians         int,
	salvadorans         int,
	argentineans        int,
	bolivians           int,
	chileans            int,
	colombians          int,
	ecuadorians         int,
	paraguayans         int,
	peruvians           int,
	uruguayans          int,
	venezuelans         int,
	lat                 real,
	lng                 real,
	city                varchar,
	state_id            varchar,
	state_name          varchar,
	population_zip      int,
	density             real,
	county_fips         int,
	county_name         varchar,
	county_weights      varchar,
	county_names_all    varchar,
	county_fips_all     varchar,
	timezone            varchar,
	poverty_rate        real,
	central_americans	int,
	south_americans	 	int,
	total				int,
	percent_central_american	real,
	percent_south_american		real,
	percent_total				real
	);
	
SELECT * FROM central_and_south;

SELECT (
	state_id, 
	sum(total),
	sum(nicaraguans), 
	sum(hondurans), 
	sum(salvadorans), 
	sum(guatemalans),
	sum(costa_ricans),
	sum(panamanians),
	sum(colombians),
	sum(venezuelans),
	sum(ecuadorians),
	sum(peruvians),
	sum(bolivians),
	sum(chileans),
	sum(paraguayans),
	sum(uruguayans),
	sum(argentineans))
			FROM central_and_south
	GROUP BY state_id 
	ORDER BY  
	sum(total) desc,
	sum(nicaraguans), 
	sum(hondurans), 
	sum(salvadorans), 
	sum(guatemalans),
	sum(costa_ricans),
	sum(panamanians),
	sum(colombians),
	sum(venezuelans),
	sum(ecuadorians),
	sum(peruvians),
	sum(bolivians),
	sum(chileans),
	sum(paraguayans),
	sum(uruguayans),
	sum(argentineans)
	;
	
SELECT (
	city, 
	state_id,
	sum(nicaraguans), 
	sum(population)
	) 
	FROM central_and_south
	GROUP BY city, state_id 
	ORDER BY  sum(nicaraguans) desc; 
	