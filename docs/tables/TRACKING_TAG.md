# TRACKING_TAG

> Table used to store the cross-reference between a tracking tag and a person

**Description:** TRACKING TAG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BATTERY_STATE` | DOUBLE |  |  | Not used |
| 3 | `BUTTON_STATE` | DOUBLE |  |  | Not UsedColumn |
| 4 | `DUP_HIT_IND` | DOUBLE |  |  | Duplicate Hit IndicatorColumn |
| 5 | `LAST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | The last tracking ID from TRACKING_ITEM to which this passive tracking badge was assigned. |
| 6 | `MANUF_TAG` | VARCHAR(30) |  |  | Manufacture TagColumn |
| 7 | `MANUF_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Manufacture Type Code set by CernerColumn |
| 8 | `MIA_IND` | DOUBLE |  |  | Missing in Action IndicatorColumn |
| 9 | `TAG_IN_USE_IND` | DOUBLE |  |  | Indicates whether or not a tag is in use. |
| 10 | `TAG_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Tag Type Code (Patient, Provider, or Equipment)Column |
| 11 | `TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Tracking IdentifierColumn |
| 12 | `TRACKING_TAG_ID` | DOUBLE | NOT NULL |  | Unique identifier used to define the tracking tagColumn |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAST_TRACKING_ID` | [TRACKING_ITEM](TRACKING_ITEM.md) | `TRACKING_ID` |
| `MANUF_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TAG_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TRACKING_ID` | [TRACKING_ITEM](TRACKING_ITEM.md) | `TRACKING_ID` |

