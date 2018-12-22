db.earthquakes.find({"COUNTRY":"MEXICO"}).count()

db.earthquakes.find({"COUNTRY":"MEXICO"},{_id:0,"YEAR":1,"COUNTRY":1,"EQ_MAG":1,"LOCATION_NAME":1}).sort({"EQ_MAG":-1}).limit(5)

db.earthquakes.find({"STATE":"AK"},{_id:0,"YEAR":1,"COUNTRY":1,"STATE":1,"EQ_MAG":1,"LOCATION_NAME":1}).sort({"EQ_MAG":-1}).limit(3)

db.earthquakes.find({"STATE":{$in:["CA","OR","WA","AK"]}},{}).count()

db.earthquakes.find({"COUNTRY":"CANADA","YEAR":{$lt:1960}},{_id:0,"YEAR":1,"EQ_MAG":1,"LOCATION_NAME":1}).sort({"YEAR":1})

//find the total count of earthquakes happened at each location

db.earthquakes.aggregate({$group: {_id:"$STATE",TOTAL:{$sum:1}}},{$sort: {"TOTAL": -1 }})

//find the average earthquake magnitude happened within each country
db.earthquakes.aggregate({$group:{_id:"$COUNTRY",AVG_EQ_MAG:{$avg:"$EQ_MAG"}}},{$sort:{"AVG_EQ_MAG":-1}})
