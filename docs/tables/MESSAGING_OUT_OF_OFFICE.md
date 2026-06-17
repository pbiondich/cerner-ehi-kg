# MESSAGING_OUT_OF_OFFICE

> Used to tell whether a personnel or personnel group is in the office or out of the office. The existence of a row on this table indicates that the personnel or personnel group is out of the office. The non-existence of a row indicates that the personnel or personnel group is in the office.

**Description:** Messaging Out of Office  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MESSAGING_OUT_OF_OFFICE_ID` | DOUBLE | NOT NULL |  | Unique, generated number to identify a single row on the MESSAGING_OUT_OF_OFFICE table. |
| 2 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The personnel group that is out of the office. |
| 3 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that is out of the office. |
| 4 | `RETURN_DT_TM` | DATETIME |  |  | The projected date and time that the personnel or personnel group will return to the office. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

