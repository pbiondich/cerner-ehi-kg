# EXT_DATA_GROUP

> This table stores information about grouped external data.

**Description:** external data group  
**Table type:** ACTIVITY  
**Primary key:** `EXT_DATA_GROUP_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_CONTRIB_CD` | DOUBLE | NOT NULL |  | DATA CONTRIBUTOR CODE |
| 2 | `DATA_GROUP_SOURCE_CD` | DOUBLE | NOT NULL |  | The source of the grouped external data. |
| 3 | `DATA_GROUP_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the grouped external data. Values include SUBMITTED, INPROGRESS, RECONCILED |
| 4 | `EXT_DATA_GROUP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person related to the grouped external data. |
| 6 | `SOURCE_REFERENCE_ID` | DOUBLE | NOT NULL |  | The id on the table of the source of the grouped external data (from table named in SOURE_REFERENCE_NAME) |
| 7 | `SOURCE_REFERENCE_NAME` | VARCHAR(30) |  |  | The table name of the source of the grouped external data. |
| 8 | `SUBMITTED_DT_TM` | DATETIME |  |  | The date and time the grouped external data was submitted. |
| 9 | `SUBMITTED_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter related to the grouped external data. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SUBMITTED_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EXT_DATA_INFO](EXT_DATA_INFO.md) | `EXT_DATA_GROUP_ID` |

