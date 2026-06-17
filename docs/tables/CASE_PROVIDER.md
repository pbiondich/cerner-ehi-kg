# CASE_PROVIDER

> This activity table contains entries for all current cases having copy to physicians associated. The case/physician relationships are stored.

**Description:** Case Provider  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CASE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to case information stored on the PATHOLOGY_CASE activity table. |
| 2 | `PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique internal identifier of the physician who was designated as a copy to physician. This ID could be used to access user information by joining to the PRSNL or PERSON tables. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |
| `PHYSICIAN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

