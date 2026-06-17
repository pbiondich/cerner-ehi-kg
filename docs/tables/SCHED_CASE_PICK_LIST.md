# SCHED_CASE_PICK_LIST

> Contains the resources scheduled for the case.

**Description:** Scheduled Case Pick List  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CASE_CART_PICK_LIST_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier on the Parent table, CASE_CART_PICK_LIST. This is filled out only if the Case Cart is generated. |
| 7 | `CHANGE_FLAG` | DOUBLE |  |  | The change type for this row from the Preference_Card |
| 8 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 9 | `CREATE_DT_TM` | DATETIME |  |  | The Date and Time this row was created |
| 10 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert or of the row in the table. |
| 11 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The Document Type Code for which the Resource is scheduled for. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `FILL_LOCN_CD` | DOUBLE | NOT NULL |  | The location that the item was scheduled to be filled from. |
| 15 | `HOLD_QTY` | DOUBLE |  |  | The Quantity this item has to be ON-HOLD |
| 16 | `ITEM_ID` | DOUBLE | NOT NULL |  | The Item ID, the unique identifier on the ITEM_MASTER. |
| 17 | `OPEN_QTY` | DOUBLE |  |  | The Quantity of Items that are scheduled to be Open |
| 18 | `ORDER_ID` | DOUBLE | NOT NULL |  | The Order ID, unique identifier of the Order this item is scheduled for. |
| 19 | `PREF_CARD_ID` | DOUBLE | NOT NULL | FK→ | Referenced to a preference card. |
| 20 | `PREF_CARD_PICK_LIST_ID` | DOUBLE | NOT NULL |  | The Preference Card Pick List ID of the item, if it is from a PREFERENCE_CARD. If the item is not on a PREFERENCE_CARD, this will be 0. |
| 21 | `SCHED_CASE_PICK_LIST_ID` | DOUBLE | NOT NULL |  | The unique sequence number that is generated from the surgery_seq |
| 22 | `SCH_EVENT_ID` | DOUBLE | NOT NULL |  | The Scheduled Event Id for this item |
| 23 | `SN_PREF_CARD_ID` | DOUBLE |  | FK→ | A foreign key Value from the sn_pref_card table. |
| 24 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | The Surgical Area this item is scheduled for |
| 25 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | The Surgical Case ID this Item is scheduled for. |
| 26 | `SURG_CASE_PROC_ID` | DOUBLE | NOT NULL | FK→ | The Surgical Case Procedure this item is scheduled for, |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_CART_PICK_LIST_ID` | [CASE_CART_PICK_LIST](CASE_CART_PICK_LIST.md) | `CASE_CART_PICK_LIST_ID` |
| `PREF_CARD_ID` | [PREFERENCE_CARD](PREFERENCE_CARD.md) | `PREF_CARD_ID` |
| `SN_PREF_CARD_ID` | [SN_PREF_CARD](SN_PREF_CARD.md) | `SN_PREF_CARD_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |
| `SURG_CASE_PROC_ID` | [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SURG_CASE_PROC_ID` |

