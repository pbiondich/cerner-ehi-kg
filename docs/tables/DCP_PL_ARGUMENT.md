# DCP_PL_ARGUMENT

> Defines the arguments for each patient list with the name of argument and value of argument defined during creation of patient list

**Description:** DCP PL ARGUMENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARGUMENT_ID` | DOUBLE | NOT NULL |  | Unique identifier for argument. |
| 2 | `ARGUMENT_NAME` | VARCHAR(50) |  |  | Name of argument |
| 3 | `ARGUMENT_VALUE` | VARCHAR(255) |  |  | Value of argument |
| 4 | `DCP_MP_PATIENT_LIST_ID` | DOUBLE | NOT NULL | FK→ | Identifier of alternate patient list argument defines. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Referenced ID value. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(100) |  |  | Name of parent entity identified within the PARENT_ENTITY_ID field. |
| 7 | `PATIENT_LIST_ID` | DOUBLE | NOT NULL | FK→ | Identifier of patient list argument defines. |
| 8 | `SEQUENCE` | DOUBLE |  |  | Argument Sequence. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_MP_PATIENT_LIST_ID` | [DCP_MP_PATIENT_LIST](DCP_MP_PATIENT_LIST.md) | `DCP_MP_PATIENT_LIST_ID` |
| `PATIENT_LIST_ID` | [DCP_PATIENT_LIST](DCP_PATIENT_LIST.md) | `PATIENT_LIST_ID` |

