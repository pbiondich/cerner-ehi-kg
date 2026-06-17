# TRACKING_HOLD

> Table used to hold a listing of all locations that are being held for a patient

**Description:** TRACKING HOLD  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BED_STATUS_CD` | DOUBLE | NOT NULL | FK→ | Bed Status CodeColumn |
| 3 | `HOLD_DT_TM` | DATETIME |  |  | Hold Date and TimeColumn |
| 4 | `HOLD_ID` | DOUBLE | NOT NULL | FK→ | Person ID of the user who set the hold status on this locationColumn |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Location being heldColumn |
| 6 | `TRACKING_HOLD_COMMENT` | VARCHAR(200) |  |  | Comment as to why the bed is being held.Column |
| 7 | `TRACKING_HOLD_ID` | DOUBLE | NOT NULL |  | Unique id used to define the relation between the tracking id and the locationColumn |
| 8 | `TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Tracking IdentifierColumn |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BED_STATUS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `HOLD_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOCATION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TRACKING_ID` | [TRACKING_ITEM](TRACKING_ITEM.md) | `TRACKING_ID` |

