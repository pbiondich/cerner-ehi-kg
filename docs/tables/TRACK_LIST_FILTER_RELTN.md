# TRACK_LIST_FILTER_RELTN

> Stores which tracking filters are available and defaulted for a tracking list.

**Description:** Tracking List Filter Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | 1 if filter is active upon initial loading of tracking list |
| 2 | `TRACK_FILTER_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from TRACK_FILTER table |
| 3 | `TRACK_LIST_FILTER_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `TRACK_LIST_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from TRACK_LIST table |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACK_FILTER_ID` | [TRACK_FILTER](TRACK_FILTER.md) | `TRACK_FILTER_ID` |
| `TRACK_LIST_ID` | [TRACK_LIST](TRACK_LIST.md) | `TRACK_LIST_ID` |

