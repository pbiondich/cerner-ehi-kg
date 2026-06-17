# BR_ADO_PROPOSED_DETAIL

> Stores Advisor Order Topics, Scenarios and category relations from Proposed Content.

**Description:** Bedrock Advisor Order Proposed Detail  
**Table type:** REFERENCE  
**Primary key:** `BR_ADO_PROPOSED_DETAIL_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ADO_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Category, Foreign Key from BR_ADO_CATEGORY |
| 2 | `BR_ADO_PROPOSED_DETAIL_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_ADO_PROPOSED_DETAIL table. |
| 3 | `BR_ADO_TOPIC_SCENARIO_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Scenario, Foreign Key from BR_ADO_TOPIC_SCENARIO |
| 4 | `NOTE_TXT` | VARCHAR(255) |  |  | Any required Notes at the Category Level. |
| 5 | `SELECT_IND` | DOUBLE | NOT NULL |  | 1-Single Select, 2-Multi Select |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_ADO_CATEGORY_ID` | [BR_ADO_CATEGORY](BR_ADO_CATEGORY.md) | `BR_ADO_CATEGORY_ID` |
| `BR_ADO_TOPIC_SCENARIO_ID` | [BR_ADO_TOPIC_SCENARIO](BR_ADO_TOPIC_SCENARIO.md) | `BR_ADO_TOPIC_SCENARIO_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_ADO_PROPOSED_OPTION](BR_ADO_PROPOSED_OPTION.md) | `BR_ADO_PROPOSED_DETAIL_ID` |

