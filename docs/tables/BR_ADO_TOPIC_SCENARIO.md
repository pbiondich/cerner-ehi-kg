# BR_ADO_TOPIC_SCENARIO

> Stores Scenarios and their relation with Topics

**Description:** Bedrock Advisor Orders Topic Scenario  
**Table type:** REFERENCE  
**Primary key:** `BR_ADO_TOPIC_SCENARIO_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ADO_TOPIC_ID` | DOUBLE | NOT NULL | FK→ | Topic ID of the Topic that this Scenario is related to. |
| 2 | `BR_ADO_TOPIC_SCENARIO_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_ADO_TOPIC_SCENARIO table. |
| 3 | `SCENARIO_DISPLAY` | VARCHAR(255) | NOT NULL |  | Display Value for the Scenario. |
| 4 | `SCENARIO_MEAN` | VARCHAR(50) | NOT NULL |  | Uniquely identifies the Scenario rows that are being inserted from Readme/Content |
| 5 | `SCENARIO_SECTION_NAME` | VARCHAR(50) | NOT NULL |  | Provides a mechanism grouping scenarios for a topic. |
| 6 | `SCENARIO_SEQ` | DOUBLE | NOT NULL |  | Sequence of the Scenario within a Topic |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_ADO_TOPIC_ID` | [BR_ADO_TOPIC](BR_ADO_TOPIC.md) | `BR_ADO_TOPIC_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_ADO_PROPOSED_DETAIL](BR_ADO_PROPOSED_DETAIL.md) | `BR_ADO_TOPIC_SCENARIO_ID` |

