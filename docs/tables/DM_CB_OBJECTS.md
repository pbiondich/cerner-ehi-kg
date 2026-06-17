# DM_CB_OBJECTS

> Holds objects to be built or dropped for the customized object drop/build process.

**Description:** CM conditional build objects.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `OBJECT_NAME` | VARCHAR(30) | NOT NULL |  | Object name. |
| 3 | `OBJECT_STATUS` | VARCHAR(30) |  |  | STATUS OF THE OBJECT 'BUILD','DROP','ERROR' |
| 4 | `OBJECT_TYPE` | VARCHAR(20) | NOT NULL |  | TYPE OF OBJECT (INDEX,TRIGGER,TABLE) |
| 5 | `QUESTION_NBR` | DOUBLE | NOT NULL | FK→ | QUESTION THE OBJECTS REFER TO. |
| 6 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | TABLE NAME THE OBJECT RESIDES ON |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUESTION_NBR` | [DM_CB_QUESTIONS](DM_CB_QUESTIONS.md) | `QUESTION_NBR` |

