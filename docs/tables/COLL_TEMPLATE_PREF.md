# COLL_TEMPLATE_PREF

> Used to store preferences for collection templates.

**Description:** COLL TEMPLATE PREF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLL_TEMPLATE_CD` | DOUBLE | NOT NULL | FK→ | Contains the code value for the Collection Template. |
| 2 | `MODE_FLAG` | DOUBLE | NOT NULL |  | Stores which mode this preference is applied to. 1 - by location 2 - by list 3 - by accession 4 - by patient |
| 3 | `PREFERENCE` | DOUBLE | NOT NULL |  | This field stores what preference it is. PREF_DATE_FLAG = 10 PREF_LOOK_AHEAD_HOURS = 20 PREF_LOOK_BACK_HOURS = 30 PREF_CUTOFF_HOURS = 40 PREF_NURSE_COLLECT_FLAG = 50 PREF_CUTOFF_HOURS_TYPE_FLAG = 60 PREF_SHOW_NONE_COLL_PRIO = 70 |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VALUE` | DOUBLE |  |  | The value of the given preference |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COLL_TEMPLATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

