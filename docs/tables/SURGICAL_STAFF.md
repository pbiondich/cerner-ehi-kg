# SURGICAL_STAFF

> Surgical Staff Table

**Description:** Surgical Staff  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CREATE_APPLCTX` | DOUBLE |  |  | Create Application ContextColumn |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | Create Date and time of the rowColumn |
| 5 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | Prsnl Id of the person creating the rowColumn |
| 6 | `CREATE_TASK` | DOUBLE |  |  | The Application task that created the row. |
| 7 | `DEF_DAYS` | DOUBLE |  |  | Default days the surgical staff person works Saturday is 1, sunday is 2, Monday is 4.. |
| 8 | `DEF_ROLE_CD` | DOUBLE | NOT NULL |  | Default Role for the Personnel |
| 9 | `DEF_SHIFT_CD` | DOUBLE | NOT NULL |  | Default Shift the Person works |
| 10 | `DEF_SURG_OP_LOC_CD` | DOUBLE | NOT NULL |  | Default Operating Room the Person works in |
| 11 | `DEF_TEAM_CD` | DOUBLE | NOT NULL |  | Default team the person works in |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 14 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | Surgical Area the Staff is associated with |
| 15 | `SURG_STAFF_ID` | DOUBLE | NOT NULL |  | Unique Sequence Number for this table |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

