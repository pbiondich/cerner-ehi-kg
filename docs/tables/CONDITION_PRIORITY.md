# CONDITION_PRIORITY

> Store the user level priority for the conditions associated to a specific patient

**Description:** CONDITION PRIORITY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONDITION_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains a PK value from the table noted in field CONDITION_ENTITY_NAME |
| 3 | `CONDITION_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Identifies the table for field CONDITION_ENTITY_ID( PROBLEM, DIAGNOSIS ) |
| 4 | `CONDITION_PRIORITY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Identifies the ENCOUNTER associated with this condition |
| 6 | `OWNER_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies a row in the table noted in OWNER_ENTITY_NAME) - The PK value |
| 7 | `OWNER_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Identifies the table for field OWNER_ENTITY_ID( PERSON, ENCOUNTER, PCT_CARE_TEAM ) |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The PK value of the PERSON row associated with this condition |
| 9 | `PRIORITY_NBR` | DOUBLE | NOT NULL |  | a numeric value indicating the relative priority |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

