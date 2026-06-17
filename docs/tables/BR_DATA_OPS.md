# BR_DATA_OPS

> BEDROCK OPS DATA

**Description:** BEDROCK DATA OPS  
**Table type:** REFERENCE  
**Primary key:** `RUN_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `DATA_OP_TYPE` | VARCHAR(30) |  |  | Type of operation being performed |
| 3 | `OP_START_DT_TM` | DATETIME |  |  | Time operation started |
| 4 | `RUN_ID` | DOUBLE | NOT NULL | PK | Identifies run with client and start version |
| 5 | `START_VERSION_NBR` | DOUBLE | NOT NULL |  | Identifies which version of start has been loaded |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_DATA_OPS_LOG](BR_DATA_OPS_LOG.md) | `RUN_ID` |

