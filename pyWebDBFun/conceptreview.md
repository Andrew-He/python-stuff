major pieces 

	person <-> computer + browser <-> The Internet <-> server
	
HTML basics: (markup language)

	<tags></tag>
 	<b> contexts </b>  <!--> bold font </-->
 	<em> italic </em>   
 
 	
 HTML Attributes 
 	
 	<Tag ATR="value"> context </Tag>
 	
 	Href tag
 	ex. <a href="www.reddit.com"> derp </a>	
 	
 	Image Tag 
 	<img> - images 
 	<img src="url" alt="text">   //alt = alternate text displayed when image not loaded. broken requests or blind   void tag with no closing tag </img>
 
 	whitespace <br> break     // to get multiple lines
 
 	paragraph tag <p>
 	
 	different rendering 
 	
 	<br> -inline element <b><img><em>
 	<p> -block for text with block height and width  	
 	
 	more elements 
 	<span> <div>
 	
 	<span class ="foo"> text </span>   //bar and foo are the css file to change the style looks of the element inline or block 
 	inline
 	
 	<div class="bar">
 	text
 	</div>
 	
 	Structure of HTML documents 
 	
 	<!DOCTYPE HTML>
 	<html>
 	<head>
 		<title>Title </title>
 	</head>
 	<body>
 	<b> context </b>
 	</body>
 	</html>
 	
 	
 **urls**
 
 http:// www.udacity.com/
 protocol    host		path
 
 protocl : https, ftp, 
 
 more about urls 
 
 Query parameters (GET parameters)
 	
 	http://example.com/foo? p=1 & q =neat
 	
 		Name = value 
 		
 	Fragment (part of page we are looking at)	
 	http://www.example.com/foo#fragment
 	
 	port
 	http://localhost:8000/
 	in order to make an internet connection url and port default = 80 
 	
 	
 	HTTP (hypertext transfer protocol)
 	request line GET /foo HTTP/1.1  -request line 
 				method path   version 
 		
 	get/post
 	
 	what is what request line to GET this url using HTTP/1.1
 	
 	http://example.com/foo/logo.png?p=1#tricky
 	is (fragment stays out)
 		GET /foo/logo?p=1 HTTP/1.1  
 		
 	HTTP request 
 	
 	Host: www.example.com    (why twice because a server might host multiple sites)
 	user-agent: chrome v.17
 	
 	subject-no-whitespace : value 
 	
 **HTTP responses**
 			request
 	browser <-> server
 			response
 			
 	request 
 		GET /foo HTTP/1.1
 		
 	response (status line)
 		HTTP/1.1   200          OK
 				 status code   response phrase 
 				 
 							Status Codes
 								200 		ok
 								302 		found
 								404 		Not found 
 								500 		server error
 								
								
 <headers>
	 
 	HTTP/1.1 200 ok
 	Date: Tue Mar 2012 04:33:00 PST
 	server: Apache /2.2.3
 	content-Type: text/html    (browser knows what to display img/gif)
 	content-Length: 1539       (tell browser)
  
 can use telnet to see the response, 
 	
 	> telnet www.example.com 80
 	> GET / HTTP/1.0
 	> HOST: www.example.com
 	
 	
 Servers:
 
 	purpose: respond to HTTP requests
 	
 			  http
 		http < -- >  static
 						|  
 						pre-written file like image
 					dynamic 
 						made on the fly 	(web application which generates the content)
 	
 	WEB APP: generate context which user request 
 	
 	
 Google App Engine (Python
 
 
 
 
 HTML FORMS
 
 	<form>
 		<input name="q">     // when press enter then url changes .../?q="what youentered"
 	</form>			
 				
 
once click submit then generated the url: 
	http://www.google.com/search?q="what you entered"
 
<center>
<form action = "http://www.google.com/search">
	<input name ="q">
	<input type="submit">
</form>
</center>>
 		
 If you type "good person", in query became "google.com/search?q=good+person"
 		
 		
**GET** 
-params in URL
-fetching data
-2000 characters in GET
-ok to cache
-not ok to change the server 

**POST**
-params in body 
-used for updating data 
-no max length or few mbs 			
-never cache do not cache post request  			
-ok to change the server 	
 				
 				
 		
 		
Validation 

	you -> "q = on" -> servers 	
	another guy -> "q=broken" -> servers
	
	your server can receive junk query like ?q="..... like two megabytes"
	
to handle bad input, can use escaping for certain html chars

	" -> &quot;
	> -> %gt;
	< -> &lt;
	& -> &amp; 


Database:

Tables:
	  int   int     int   string(wchar)     string              
	-----------------------------------   
link	| id | votes |user | title |  url |     column 
	----------------------------------- -----
	   5 | 201   | 11 | do sdad | ww.goo.com|   row   
	
	or 
	
	user 
	ID    name      password
	-------------------------
	   |		|              |
	
types of database:

relational SQL (maniplulate tables)
	postgresSQL - reddit 
	MySQL 	    - popular
	sqLite     

Google AppEngine's Datastore
Amazon Dynamo

NoSQL
	mongo
	couchdb

Could use SQL via an interface to manipulate no-SQL database 


cursor : position in database;



(get all the links ordered by votes with descending or ascending order)
SELECT * FROM links ORDER BY votes {DESC,ASC} 



####create table
create table clebs (id integer, name text, age, integer);

#####insert into
insert into celebs (id, name, age) values (1, "justin", 21);
INSERT INTO celebs (id, name, age) VALUES (2, 'Beyonce Knowles', 33); 
INSERT INTO celebs (id, name, age) VALUES (3, 'Jeremy Lin', 26); 
INSERT INTO celebs (id, name, age) VALUES (4, 'Taylor Swift', 26);

#####SELECT
select * from celebs; 

// select statement are used to fetch data from database

#####UPDATE
UPDATE celebs SET age = 22 where id = 1; 

// update statement edits a row in the table, used to change existing records.  
				   
#####ALTER TABLE 
ALTER TABLE celebs ADD COLUMN twitter_handle TEXT; 

// alter table statement added a new column to the table. 

#####update field for new added column
UPDATE celebs 
SET twitter_handle = '@goodmorning'
WHERE id = 4; 

#####DELETE FROM (rows by conditions)
DELETE FROM celebs 
WHERE twitter_handle IS NULL;

// delete from statement deletes one or more rows from a table. used to delete existing records, IS NULL is a condition returns true if value is NULL


**A little more**

####query multiple columns 
SELECT name, imdb_rating FROM movies; 

####SELECT DISTINCT
SELECT DISTINCT genre FROM movies; 

// is used to return unique values in the result set; 

####filter query in WHERE
SELECT * FROM movies WHERE imdb_rating > 8;     
// we can use =, !=, >, <, >=, <=

####LIKE
SELECT * FROM movies WHERE name LIKE 'Se_en'; 
// Like compare similar values, 'Se_en' will match 'Seven', 'Se7en'
SELECT * FROM movies WHERE name LIKE 'a%'; 
SELECT * FROM movies WHERE name LIKE '%man%'; 

// like pattern % is a wildcard character matches zero or more missing letters


####BETWEEN
SELECT * FROM movies 
WHERE name BETWEEN 'A' AND 'J'; 

SELECT * FROM movies 
WHERE year BETWEEN 1990 AND 2000; 

SELECT * FROM movies 
WHERE year BETWEEN 1990 AND 2000 
AND genre = 'action';

// BETWEEN operator filters the result set within a certain range, {numbers, text or dates}


####ORDER BY
SELECT * FROM movies
ORDER BY imdb_rating DESC; 

// order by indicates sort the result set by particular column {text, number}
// DESC, ASC order type 


####LIMIT
SELECT * FROM movies 
ORDER BY imdb_rating DESC 
LIMIT 5; 

// limit sets maximum number of rows the result set will have

####COUNT
SELECT COUNT(*) FROM fake_apps;  

SELECT COUNT(*) FROM fake_apps WHERE price = 0;    
// count number of free apps

####GROUP BY
SELECT price, COUNT(*) FROM fake_apps
GROUP BY price; 
// count number of apps at each price

> price | count(*)
> 0.0	| 18
> 0.99	| 20
> 1.99	| 12

SELECT price, COUNT(*) FROM fake_apps
WHERE downloads > 2000
GROUP BY price; 

// group by used in collaboration with select to arrange identical data into groups

####SUM
SELECT SUM(downloads) FROM fake_apps; 

//total number of downloads for all apps combined
// SUM is a function take name of column and returns sum of all values in that column, here it adds up downloads column

SELECT category, SUM(downloads) FROM fake_apps 
GROUP BY category; 
//calculate total number of downloads for each category 

####MAX, MIN, AVG, ROUND
SELECT MAX(downloads) 
FROM fake_apps; 
// MAX takes column name and return largest value in that column, also MIN()
// AVG calculates the average value of a particular column 

SELECT name, category, MAX(downloads) 
FROM fake_apps
GROUP BY category;

SELECT price, ROUND(AVG(downloads), 2)
FROM fake_apps 
GROUP BY price; 

// round to two decimal places in the result set

**MULTIPLE TABLES**

####PRIMARY KEY
CREATE TABLE artists(id INTEGER PRIMARY KEY, name TEXT); 
CREATE TABLE albums(id INTEGER, name TEXT, artist_id INTEGER, year INTEGER);

// primary key is a unique identifier for each row in a table. use this value to connect artist table to albums table. a table does not have more than one primary key. 

// a foreign key is a columm that contains the primary key of another table in db. use foreign key and primary key to connect rows in two different tables. One table's foreign key holds the value of another table's primary key. foreign key do not need to be unique and can BE NULL. 

####CROSS JOIN (query from both table)
SELECT albums.name, albums.year, artists.name FROM albums, artists; 


####JOIN
SELECT * FROM albums
JOIN artists ON
  	 albums.artist_id = artists.id;


// JOIN artists ON says the type of join we are going to use
// albums.artist_id = artists.id how the two tables are related. 


####AS
SELECT
  albums.name AS 'Album',
  albums.year,
  artists.name AS 'Artist'
FROM
  albums
JOIN artists ON
  albums.artist_id = artists.id
WHERE
  albums.year > 1980;

// AS allows to rename a colum or table using an alias. (just appera in result set)






