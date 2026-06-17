# PRESENTING_PROBLEM

> Reference Data to store the Presenting Problem Content from Lynx

**Description:** presenting_problem  
**Table type:** REFERENCE  
**Primary key:** `PRESENTING_PROBLEM_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGE_MASK_VAL` | DOUBLE | NOT NULL |  | Masked age - age is split into 10 age ranges |
| 2 | `GENDER_MASK_VAL` | DOUBLE | NOT NULL |  | Masked gender values |
| 3 | `KEY_VAL` | DOUBLE | NOT NULL |  | Unique presenting problem key value |
| 4 | `PRESENTING_PROBLEM_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the presenting_problem table. |
| 5 | `PROBLEM_HINTS` | VARCHAR(1000) | NOT NULL |  | Gives additional information concerning the presenting problem |
| 6 | `PROBLEM_NAME` | VARCHAR(255) | NOT NULL |  | Name of the presenting problem |
| 7 | `PROBLEM_NAME_KEY` | VARCHAR(255) | NOT NULL |  | Name key of the presenting problem |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALUE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines type of presenting problem [facility or clinic] |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PRESENTING_PROBLEM_RELTN](PRESENTING_PROBLEM_RELTN.md) | `PRESENTING_PROBLEM_ID` |

