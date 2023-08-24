const database = 'ModelCatalog';
const collection = 'jsonFiles';
const outputFolder = 'jsonM';

// The current database to use.
use(database);

// Find all documents in the collection
const allDocumentsCursor = db[collection].find();
const allDocumentsArray = allDocumentsCursor.toArray();

// Create the output folder if it doesn't exist
const fs = require('fs');
if (!fs.existsSync(outputFolder)) {
  fs.mkdirSync(outputFolder);
}

// Save each document as a separate JSON file using synchronous write
allDocumentsArray.forEach((document, index) => {
  const fileName = `${outputFolder}/jsonDocument_${index}.json`;
  const jsonString = JSON.stringify(document, null, 2);
  fs.writeFileSync(fileName, jsonString);
});

print('JSON documents saved to jsonM folder.');
