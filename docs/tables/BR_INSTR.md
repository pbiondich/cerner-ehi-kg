# BR_INSTR

> list of supported instruments

**Description:** BEDROCK INTSTRUMENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE_MEAN` | VARCHAR(12) |  |  | Activity type meaning |
| 2 | `BI_IND` | DOUBLE | NOT NULL |  | Defined as 1 bidirectional indicator |
| 3 | `BR_INSTR_ID` | DOUBLE | NOT NULL |  | Unique table identifier |
| 4 | `CODE_NAME` | VARCHAR(40) |  |  | Coded name for the instrument |
| 5 | `HQ_IND` | DOUBLE | NOT NULL |  | Define as 1 hq indicator |
| 6 | `MANUFACTURER` | VARCHAR(100) | NOT NULL |  | Manufacturer of the instrument |
| 7 | `MANUFACTURER_ALIAS` | VARCHAR(50) |  |  | Manufacturer alias |
| 8 | `MODEL` | VARCHAR(100) | NOT NULL |  | model of the instrument |
| 9 | `MODEL_ALIAS` | VARCHAR(50) |  |  | Model alias |
| 10 | `MULTIPLEXOR_IND` | DOUBLE | NOT NULL |  | indicates if the instrument is a multiplexor |
| 11 | `POINT_OF_CARE_IND` | DOUBLE | NOT NULL |  | Defined as 1 point of care indicator |
| 12 | `PREV_MANUFACTURER` | VARCHAR(100) |  |  | filled in if the instrument used to be manufactured by someone else |
| 13 | `ROBOTICS_IND` | DOUBLE | NOT NULL |  | indicates if the instrument has robotics |
| 14 | `TYPE` | VARCHAR(50) | NOT NULL |  | Kind of instrument |
| 15 | `UNI_IND` | DOUBLE | NOT NULL |  | Defined as 1 unidirectional indicator |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

