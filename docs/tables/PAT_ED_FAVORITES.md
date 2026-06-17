# PAT_ED_FAVORITES

> Contains patient education favorites

**Description:** PAT ED FAVORITES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FAVORITE_TYPE_CD` | DOUBLE | NOT NULL |  | Defines what type of Favorite from code set 20531 |
| 2 | `PAT_ED_FAVR_ID` | DOUBLE | NOT NULL |  | Primary Field |
| 3 | `PAT_ED_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Contains patient education relation idColumn |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 5 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL |  | Tracking Group Code from code set 16370 |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PAT_ED_RELTN_ID` | [PAT_ED_RELTN](PAT_ED_RELTN.md) | `PAT_ED_RELTN_ID` |
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

