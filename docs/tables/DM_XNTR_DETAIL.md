# DM_XNTR_DETAIL

> Stores information about wht processes get ran against the retrieved data

**Description:** Database Architecture Extract and Transform Retrieve Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_XNTR_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DM_XNTR_DETAIL table. |
| 2 | `DM_XNTR_EXTRACT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to DM_XNTR_EXTRACT table. Holds the pointer to each extract for a given job. |
| 3 | `END_DT_TM` | DATETIME |  |  | Holds the time the detail row completed |
| 4 | `INSTANCE_NBR` | DOUBLE | NOT NULL |  | Holds the instance of the TASK_ENTITY_ID where applicable |
| 5 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Holds the order inwhich tasks should be ran |
| 6 | `START_DT_TM` | DATETIME |  |  | Holds the time the detail row started |
| 7 | `STATUS` | VARCHAR(20) |  |  | Holds Status of detail data |
| 8 | `STATUS_MSG` | VARCHAR(250) |  |  | Holds message about status |
| 9 | `TASK_ENTITY_ID` | DOUBLE | NOT NULL |  | Holds the Identifier of the task that needs to be re-ran on retrieved data |
| 10 | `TASK_ENTITY_NAME` | VARCHAR(30) |  |  | Holds the type of task that needs to be re-ran (README, PERSON COMBINE, etc.) |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_XNTR_EXTRACT_ID` | [DM_XNTR_EXTRACT](DM_XNTR_EXTRACT.md) | `DM_XNTR_EXTRACT_ID` |

