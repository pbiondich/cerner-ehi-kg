# DM_XNTR_EXTRACT

> Stores information about data getting retrieved at the file extract level

**Description:** Database Architecture Extract and Transform Retrieve Extract  
**Table type:** ACTIVITY  
**Primary key:** `DM_XNTR_EXTRACT_ID`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_XNTR_EXTRACT_ID` | DOUBLE | NOT NULL | PK | Non-intelligent PK of table |
| 2 | `DM_XNTR_JOB_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the DM_XNTR_JOB table |
| 3 | `EXTRACT_NAME` | VARCHAR(100) |  |  | Holds the name of the extract file |
| 4 | `EXTRACT_PERSON_ID` | DOUBLE | NOT NULL |  | Holds the person identifier the extract file is related to. Different from PERSON_ID on parent table, because of combines |
| 5 | `EXTRACT_START_DT_TM` | DATETIME |  |  | Holds the time, this extract file started being worked on |
| 6 | `EXTRACT_STOP_DT_TM` | DATETIME |  |  | Holds the time this extract file stopped being worked on |
| 7 | `EXTRACT_UUID` | VARCHAR(200) |  |  | Holds the UUID of the file in the CAMM database |
| 8 | `EXTRACT_VERSION` | DOUBLE |  |  | Holds the version number of the extract file in the CAMM database |
| 9 | `STATUS` | VARCHAR(20) |  |  | Holds status of extract file |
| 10 | `STATUS_MSG` | VARCHAR(250) |  |  | Holds detailed information about status |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `XNT_END_DT_TM` | DATETIME |  |  | The date and time the Retrieve Process ended |
| 17 | `XNT_START_DT_TM` | DATETIME |  |  | The date and time the Retrieve Process started |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_XNTR_JOB_ID` | [DM_XNTR_JOB](DM_XNTR_JOB.md) | `DM_XNTR_JOB_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DM_XNTR_DETAIL](DM_XNTR_DETAIL.md) | `DM_XNTR_EXTRACT_ID` |
| [DM_XNTR_EXTRACT_CNT](DM_XNTR_EXTRACT_CNT.md) | `DM_XNTR_EXTRACT_ID` |

