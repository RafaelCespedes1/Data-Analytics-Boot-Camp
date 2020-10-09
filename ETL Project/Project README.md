I wanted to investigate in detail the population in the United States of America who are of 
Central American and South American origin.  There are a total of 15 countries of origin for these
communitites. For Central American-Americans the countries of origin are Guatemala, El Salvador, 
Honduras, Nicaragua, and Costa Rica, who on September 15, 1821, declared their independence from Spain 
and formed the United Republics of Central America.  Also, I included Panama in the Central America region.
Although Panama geographically is in the Central Isthmus, until the early 1900s, Panama formed part of 
Colombia, and Panama is linguistically, culturally, historically, etc. more like a South American nation.

The countries included in the South American region are the aforementioned Colombia, Venezuela, and Ecuador, 
who together with Panama, also formed another federation when these countries became independent from Spain.
Also included in the South American region are Peru and Bolivia, who were once upon a time also one country.
Argentina, Uruguay and Paraguay also formed another federal entity when these nations became independent from
Spain.  Lastly, Chile is also included in the South American region.  I only included countries whose official
language is Spanish and whose predominant language is Spanish.  I thus excluded other countries situated in
the regions such as Belize in Central America and Brazil in South America.  These 15 countries also share
linguistic characteristics such as the widespread use of the voseo Spanish, which is absent from those 
Spanish varieties spoken in the Caribbean islands, Mexico, and Spain.

I adapted a Jupyter file written in Python by reviewing the documention for the US Census API and pulled the
number of people who self-identified as being of origin of each of the 15 countries of interest at the zip 
code level. I wanted to be able to aggregate the retrieved data at the city, county and state levels. I was 
able to download a free database from https://simplemaps.com/data/us-zips.  I then split the database into
3 pieces.  One contained only those zip codes that had 3 digits in their zip codes.  I added the leading two 
zeroes. I did the same for those zip codes who that had 4 digits in their zip codes.  I added the leading zero.
Finally, I concatenated the previous two files with the one that already had zip codes with five digits. I 
finally, joined the new zip code database with the census database containing the counts of the different
nationalities.  Finally, I cleaned up the data by adding city, county, and state information to some zip code
which had such information missing.  I then added some columns that would give me the total of the Central 
Americans, South Americans, and a grand total of all 15 nationalities at the zip code level.  I also added
columns that calculated the percentages of the 3 sums calculated above as percent of the total population in 
each zip code.  I also added a column calculating the poverty rate at the zip code level.

I finally uploaded the comma delimited file created above in pandas to a pgAdmin SQL database. This will
allow me to do further analysis and illustrations/visualizations in the future.  I calculated that the total
population of Central American and South American origins in the United States of America total some 8.8
million people, which represents about 2.7% of the total U.S. population.  Among people of origin from a 
predominantly Spanish speaking country, Central American-Americans and South American-Americans represent 
approximately 15% of such population in the U.S.  Our Spanish language variety, which uses voseo, is not taught 
in the schools or universities in the United States. Most Spanish language mass media in the United States
also does not cater or target these nationalities. The states with the highest Central American and South 
American populations are California (1,743,039), Florida (1,459,696), New York (1,017,889), and Texas 
(811,097).  These populations are concentrated in the Los Angeles, Miami, New York City, Houston, and 
Washington, D.C. metropolitan areas.  Salvadorans are by far the largest group at 2,197,375, which represents
about 25% of the total of Central and South American origins.  Salvadorans, together with the other Northern
Triangle countries of Guatemala (1,421,645) and Honduras (903,987) make up 51% of the total.  Colombians
are by far the largest South American group at 1,152,714, which is about one-third of the South American 
population in the USA.  Ecuadorans (704,781) and Peruvians (657,103) make up, combined with the aforementioned 
nationalities, almost 80% of the total Central American and South American total population.  The other 9
nationalities slightly make up more than 20%. Central Americans number 5.3 million and South Americans 
number some 3.5 million. The combined population of 8.8 million is comparable in size to the population of
Honduras, and bigger than that of El Salvador, Paraguay, Nicaragua, Costa Rica, Panama, and Uruguay.