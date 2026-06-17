# SN_PRIV

> Contains all privileging information for SurgiNet applications.

**Description:** SN PRIV  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESS_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of access to the specified application for a given person or position. |
| 2 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | The application that this privilege applies to. |
| 3 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was initially inserted. |
| 5 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 6 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary key ID of the table in the PARENT_ENTITY_NAME that this privilege belongs to. |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The name of the table this privilege is associated with. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 10 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position code value that this privilege applies to. |
| 11 | `PRIV_ID` | DOUBLE | NOT NULL |  | The primary key ID for this table. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

