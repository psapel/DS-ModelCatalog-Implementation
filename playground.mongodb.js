/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

const database = 'DS-ModelCatalog';
const collection = 'jsonModels';

// The current database to use.
use(database);

// Create a new collection.
db.createCollection(collection);

db.jsonModels.insertMany([
  {
    "name": "model_35",
    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
        "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime", 
        "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumCompletionTime"
    ],
    "formula": "Pₘ | sᵢⱼ  | Cₘₐₓ, ΣwⱼCⱼ"
},
{
  "name": "model_36",
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
},
{
  "name": "model_37",
  "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/unrelatedMachines",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
      "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime", 
      "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumCompletionTime"
  ],
  "formula": "Rₘ | Mⱼ | Cₘₐₓ, ΣwⱼCⱼ"
},
{
  "name": "model_38",
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
},
{
  "name": "model_39",
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
},
{
  "name": "model_40",
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
},
{
  "name": "model_41",
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
},
{
  "name": "model_42",
  "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints":  [
      "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup"
  ],
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
      "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime",
      "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumTardiness"
  ],
  "formula": "Pₘ | sᵢⱼ  | Cₘₐₓ, ΣwⱼTⱼ"
},
{
  "name": "model_43",
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
},
{
  "name": "model_44",
  "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints":  [
      "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
      "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility"
  ],
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
      "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime"
  ],
  "formula": "Jₘ | sᵢⱼ, Mⱼ | Cₘₐₓ"
},
{
  "name": "model_45",
  "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
      "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumCompletionTime"
  ],
  "formula": "Pₘ | Mⱼ | ΣwⱼCⱼ"
},
{
  "name": "model_46",
  "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/unrelatedMachines",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints":  [
      "https://www.iop.rwth-aachen.de/PPC/1/1/seqDepSetup",
      "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility"
  ],
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
      "https://www.iop.rwth-aachen.de/PPC/1/1//sumTardiness"
  ],
  "formula": "Rₘ | sᵢⱼ, Mⱼ | ΣTⱼ"
},
{
  "name": "model_47",
  "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
      "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime"
  ],
  "formula": "Pₘ | Mⱼ | Cₘₐₓ"
},
{
  "name": "model_48",
  "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
      "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime"
  ],
  "formula": "Pₘ | Mⱼ | Cₘₐₓ"
},
{
  "name": "model_49",
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
},
{
  "name": "model_50",
  "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/singleMachine",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": "https://www.iop.rwth-aachen.de/PPC/1/1/",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
      "https://www.iop.rwth-aachen.de/PPC/1/1/weightedSumCompletionTimemaschEligibility"
  ],
  "formula": "1 | Mⱼ | ΣwⱼCⱼ"
},
{
  "name": "model_51",
  "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": "https://www.iop.rwth-aachen.de/PPC/1/1/parallelMachines",
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints":  [
      "https://www.iop.rwth-aachen.de/PPC/1/1/maschEligibility"
  ],
  "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": [
      "https://www.iop.rwth-aachen.de/PPC/1/1/maxCompletionTime"
  ],
  "formula": "Pₘ | Mⱼ, oprtr | Cₘₐₓ"
}
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

