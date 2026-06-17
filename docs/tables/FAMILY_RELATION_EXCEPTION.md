# FAMILY_RELATION_EXCEPTION

> Removed suggested family relationships

**Description:** Family relationship exception  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FAMILY_RELATION_EXCEPTION_ID` | DOUBLE | NOT NULL |  | Identifies the relationship exception for a Person |
| 2 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person for whom the relationship exception exists |
| 3 | `SUGGESTED_RELATED_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The related person to Related Person for whom a relation suggestion is an exception. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SUGGESTED_RELATED_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

