# BR_ADO_TOPIC

> Stores Advisor Orders Topics from the Content.

**Description:** Bedrock Advisor Orders Topic  
**Table type:** REFERENCE  
**Primary key:** `BR_ADO_TOPIC_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ADO_TOPIC_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_ADO_TOPIC table. |
| 2 | `TOPIC_DISPLAY` | VARCHAR(100) | NOT NULL |  | Display Value for the Topic. |
| 3 | `TOPIC_MEAN` | VARCHAR(50) | NOT NULL |  | Uniquely identifies the Topics that are being inserted from Readme/Content |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_ADO_TOPIC_SCENARIO](BR_ADO_TOPIC_SCENARIO.md) | `BR_ADO_TOPIC_ID` |

