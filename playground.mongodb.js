/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

const database = 'DS-ModelCatalogue';
const collection = 'jsonModels';

// The current database to use.
use(database);

// Create a new collection.
db.createCollection(collection);

db.jsonModels.insertMany([
  {
    "GrahamNotation": {
      "name": "Model 35",
      "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
      "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
      "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime", 
        "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumCompletionTime"
    ],
    "formula": "Pₘ | sᵢⱼ  | Cₘₐₓ, ΣwⱼCⱼ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 36",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
        "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility",
        "https://www.iop.rwth-aachen.de/PPC/1/1/jobFamilies"
    ],
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumTardiness",
        "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumCompletionTime"
    ],
    "formula": "Pₘ | sᵢⱼ, Mⱼ, fmls | ΣwⱼTⱼ, ΣwⱼCⱼ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 37",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/unrelatedMachines",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime", 
        "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumCompletionTime"
    ],
    "formula": "Rₘ | Mⱼ | Cₘₐₓ, ΣwⱼCⱼ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 38",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints":[
        "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
        "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility"
    ],
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
        "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumCompletionTime"
    ],
    "formula": "Pₘ | sᵢⱼ, Mⱼ | ΣwⱼCⱼ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 39",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints":  [
        "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
        "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility",
        "https://www.iop.rwth-aachen.de/PPC/1/1/batch"
    ],
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumTardiness"
    ],
    "formula": "Pₘ | sᵢⱼ, Mⱼ, batch | ΣwⱼTⱼ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 40",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/singleMachine",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints":  [
      "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup"
    ],
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
      "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime",
      "https://www.iop.rwth-aachen.de/PPC/1/1//sumTardiness",
      "https://www.iop.rwth-aachen.de/PPC/1/1//sumEarliness"
    ],
    "formula": "1 | sᵢⱼ, LCⱼ | Cₘₐₓ, ΣTⱼ, ΣEⱼ"
 }
},
{
  "GrahamNotation": {
    "name": "Model 41",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
        "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility"
    ],
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime",
        "https://www.iop.rwth-aachen.de/PPC/1/1//sumTardiness"
    ],
    "formula": "Pₘ | sᵢⱼ, Mⱼ | Cₘₐₓ, ΣTⱼ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 42",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints":  [
        "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup"
    ],
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime",
        "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumTardiness"
    ],
    "formula": "Pₘ | sᵢⱼ  | Cₘₐₓ, ΣwⱼTⱼ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 43",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/flexibleJobShop",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints":  [
        "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
        "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility",
        "https://www.iop.rwth-aachen.de/PPC/1/1/releaseDates",
        "https://www.iop.rwth-aachen.de/PPC/1/1/preemptions",
        "https://www.iop.rwth-aachen.de/PPC/1/1/breakdown"
    ],
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumCompletionTime"
    ],
    "formula": "FJc | sᵢⱼ, Mⱼ, rⱼ, prec, brkdwn  | ΣCⱼ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 44",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints":  [
        "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
        "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility"
    ],
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime"
    ],
    "formula": "Jₘ | sᵢⱼ, Mⱼ | Cₘₐₓ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 45",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumCompletionTime"
    ],
    "formula": "Pₘ | Mⱼ | ΣwⱼCⱼ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 46",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/unrelatedMachines",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints":  [
      "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
      "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility"
   ],
   "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
      "https://www.iop.rwth-aachen.de/PPC/1/1//sumTardiness"
  ],
  "formula": "Rₘ | sᵢⱼ, Mⱼ | ΣTⱼ"
 }
},
{
  "GrahamNotation": {
    "name": "Model 47",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime"
    ],
    "formula": "Pₘ | Mⱼ | Cₘₐₓ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 48",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime"
    ],
    "formula": "Pₘ | Mⱼ | Cₘₐₓ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 49",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/unrelatedMachines",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints":  [
        "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
        "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility",
        "https://www.iop.rwth-aachen.de/PPC/1/1/preemptions",
        "https://www.iop.rwth-aachen.de/PPC/1/1/breakdown"
    ],
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumTardiness"
    ],
    "formula": "Rₘ | sᵢⱼ, Mⱼ, prmp, brkdwn  | ΣwⱼTⱼ"
  }
},
{
  "GrahamNotation": {
    "name": "Model 50",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/singleMachine",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": "https://www.iop.rwth-aachen.de/PPC/1/1/",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumCompletionTimemaschEligibility"
    ],
    "formula": "1 | Mⱼ | ΣwⱼCⱼ"
  }
},
]
  )

// The prototype form to create a collection:
/* db.createCollection( <name>,
  {
    capped: <boolean>,
    autoIndexId: <boolean>,
    size: <number>,
    max: <number>,
    storageEngine: <document>,
    validator: <document>,
    validationLevel: <string>,
    validationAction: <string>,
    indexOptionDefaults: <document>,
    viewOn: <string>,
    pipeline: <pipeline>,
    collation: <document>,
    writeConcern: <document>,
    timeseries: { // Added in MongoDB 5.0
      timeField: <string>, // required for time series collections
      metaField: <string>,
      granularity: <string>,
      bucketMaxSpanSeconds: <number>, // Added in MongoDB 6.3
      bucketRoundingSeconds: <number>, // Added in MongoDB 6.3
    },
    expireAfterSeconds: <number>,
    clusteredIndex: <document>, // Added in MongoDB 5.3
  }
)*/

// More information on the `createCollection` command can be found at:
// https://www.mongodb.com/docs/manual/reference/method/db.createCollection/

