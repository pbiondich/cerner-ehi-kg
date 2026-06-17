# ORG_PROFILE

> This table holds the profile for contributor systems.

**Description:** This table holds the profile for contributor systems.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_POSITION` | DOUBLE |  |  | Denotes the beginning position for a field in a flat text file. |
| 2 | `CONTRIBUTOR_SYSTEM` | VARCHAR(100) | NOT NULL |  | Name of the profile. |
| 3 | `DELIMITER` | DOUBLE |  |  | Delimiter used to delimit the text file. |
| 4 | `FIELD_NAME` | VARCHAR(50) | NOT NULL |  | The name of the field. |
| 5 | `FIELD_ORDER` | DOUBLE |  |  | The order of the field in the text file. |
| 6 | `ITEMDATA` | DOUBLE |  |  | Itemdata consists of the itemdata property corresponding to each field in the profile |
| 7 | `ORG_PROFILE_ID` | DOUBLE | NOT NULL |  | The unique identifier for each record in the table. It is a system generated number. |
| 8 | `PROFILE_TYPE` | VARCHAR(40) |  |  | Denotes the type of profile |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

