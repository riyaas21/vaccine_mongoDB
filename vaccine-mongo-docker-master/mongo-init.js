db = db.getSiblingDB('vaccination');

db.createCollection('vaccination_status');

db.vaccination_status.insertMany([
    { "reg_no": "1", "vaccination_status": true, "name" : "ksi" },
    { "reg_no": "2", "vaccination_status": false, "name" : "pewdiepie" },
    { "reg_no": "3", "vaccination_status": true, "name" : "Dom" },
    { "reg_no": "4", "vaccination_status": false, "name" : "goku" },
]);