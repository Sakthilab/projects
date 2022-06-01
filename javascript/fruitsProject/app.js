const mongoose = require("mongoose");
// mongoose.connect("mongodb://localhost:27017/fruitsDB");

const fruitSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, "Please check your data entry , no fruit name added"]
    },
    rating: {
        type: Number,
        min: 1,
        max: 10
        },
    review: String,
});

const Fruit = mongoose.model("Fruit", fruitSchema);

const pineapple = new Fruit({
    name: "Pineapple",
    score: 9,
    review: "Great fruit."
})

pineapple.save()

// const fruit = new Fruit({
//     rating: 10,
//     review: "Pretty solid as a fruit."
// });


// const  kiwi = new Fruit({
//     name: "kiwi",
//     score: 10,
//     review: "The best Fruit"
// });

// const orange = new Fruit({
//     name: "Orange",
//     score: 4,
//     review: "Too soure for me"
// })

// const banana = new Fruit({
//     name: "Banana",
//     score: 3,
//     review: "weird texture"
// })

// Fruit.insertMany([ kiwi, orange, banana], function(err){
//     if(err){
//         console.log(err);
//     } else {
//         console.log("Succesfully saved all fruits to fruitsDB")
//     }
// });

// Fruit.deleteMany({_id: "62785efa7f4b0c2e69709d3d"}, function(err){
//     if(err){
//         console.log(err)
//     } else {
//         console.log("Succesfully deleted")
//     }
// });

// fruit.save();

// Fruit.find(function(err, fruits){
//     if(err){
//         console.log(err);
//     } else {
        
//         fruits.forEach(function(fruit){
//             console.log(fruit.name);
//         })
//         mongoose.connection.close();
//     }
// });

mongoose.connect("mongodb://localhost:27017/personDB");

const personSchema = new mongoose.Schema({
    name: String,
    age: Number,
    favouriteFruit: fruitSchema
});

const Person = mongoose.model("Person", personSchema);


const person = new Person({
    name: "Stewie Griffin",
    age: 42,
    favouriteFruit: pineapple
});

person.save();





// const findDocuments = function(db, callback) {
//     const collection = db.collection("fruits");
    
//     collection.find({}).toArray(function(err, fruits){
//         assert.equal(err, null);
//         console.log("Found the following records");
//         console.log(fruits);
//         callback(fruits);
//     })
// }
