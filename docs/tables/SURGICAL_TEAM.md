# SURGICAL_TEAM

> Surgical Team Table

**Description:** Surgical Team  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CREATE_APPLCTX` | DOUBLE |  |  | Application context that was responsible for creating this row |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | Date and Time the row was created |
| 4 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | Person responsible for creation of this row |
| 5 | `CREATE_TASK` | DOUBLE |  |  | Application task responsible for Creating this Row |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 7 | `SURGICAL_TEAM_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the Surgical Team table. It is an internal system assigned number. |
| 8 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | Surgical Area the Team is associated with |
| 9 | `TEAM_CD` | DOUBLE | NOT NULL |  | Surgical Team Code |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

