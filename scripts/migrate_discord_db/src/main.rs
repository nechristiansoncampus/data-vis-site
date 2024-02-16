use csv::{Error, Reader};
use mongodb::{bson::doc, Client, Collection};
use serde::{Deserialize, Serialize};
use std::env;

// A record in the form used in our CSV file. Used to Deserialize
#[derive(Serialize, Deserialize, Debug)]
struct Record {
    timestamp: String,
    fulltimers: String,
    students: String,
    date: String,
    summary: String,
}

// A record in the form we want to upload to mongo db. Used to Serialize
#[derive(Serialize, Deserialize, Debug, Clone)]
struct MongoRecord {
    fulltimers: Vec<String>,
    students: Vec<String>,
    date: String,
    note: String,
}

#[tokio::main]
async fn write_doc(record: MongoRecord) -> mongodb::error::Result<()> {
    let mongodb_uri = env::var("MONGO_URI").unwrap_or_else(|_| {
        eprintln!("MONGODB_URI environment variable not set. Exiting...");
        std::process::exit(1);
    });

    let client = Client::with_uri_str(mongodb_uri).await?;
    let my_coll: Collection<MongoRecord> = client.database("stats-test").collection("appointments");

    let res = my_coll.insert_one(record, None).await?;
    println!("Inserted a document with _id: {}", res.inserted_id);
    Ok(())
}

fn main() -> Result<(), csv::Error> {
    let mut reader = csv::Reader::from_path("student_updates_edited.csv")?;
    let mut records: Vec<MongoRecord> = Vec::new();
    for record in reader.deserialize() {
        let record: Record = record?;

        //Convert CSV Data into preferred format for mongo DB
        //Convert Strings with comma seperated students and fters into Array<String>
        let fulltimer_array: Vec<String> = record
            .fulltimers
            .split(',')
            .map(|s| s.to_string())
            .collect();
        let student_array: Vec<String> =
            record.students.split(',').map(|s| s.to_string()).collect();

        let mongo_record: MongoRecord = MongoRecord {
            fulltimers: fulltimer_array,
            students: student_array,
            date: record.date,
            note: record.summary,
        };

        let doc = mongo_record.clone();
        match write_doc(doc) {
            Ok(_) => println!("Successfully wrote to MongoDB"),
            Err(e) => eprintln!("Failed to write to MongoDB: {}", e),
        }
    }
    Ok(())
}
