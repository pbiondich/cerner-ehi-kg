# CT_BUNDLE_HISTORY

> Charge Transformation Bundle History Table

**Description:** This table contains the bundle history for every bundled charge.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BUNDLE_DT_TM` | DATETIME |  |  | This is the date and time that a charge was bundled away. This date and time will be the same on all the charges that were bundled together. |
| 7 | `BUNDLE_ID` | DOUBLE | NOT NULL |  | This is the id used to associate all charges that were bundled together. |
| 8 | `CT_BUNDLE_HISTORY_ID` | DOUBLE | NOT NULL |  | This the unique primary identifier for the ct_bundle_history table. It is an internal system assigned number. |
| 9 | `CT_RULE_ID` | DOUBLE | NOT NULL |  | This is the unique primary identifier for the ct_rule table. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `FROM_CHARGE_ITEM_ID` | DOUBLE | NOT NULL |  | This is the unique identifier from the charge table for the charges that have a detail_type_cd of PRECURSOR. |
| 12 | `TO_CHARGE_ITEM_ID` | DOUBLE | NOT NULL |  | This is the unique identifier from the charge table for the charges that have a detail_type_cd of RESULT. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

