# ONC_II_AUTO_ACTIVITY

> Stores the oncology infusion injection automation activity

**Description:** ONCOLOGY INFUSION INJECTION AUTOMATION ACTIVITY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_ROUTE_TYPE_TXT` | VARCHAR(100) |  |  | A short display string to indicate the type of the rpoute selected for the event. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | encounter for which this event is charted |
| 7 | `EVENT_STATUS_TXT` | VARCHAR(100) |  |  | A short display string to indicate the status of the event documeneted. |
| 8 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | This field is the current patient location with a location type of nurse unit. |
| 9 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of Long Text table. |
| 10 | `ONC_II_AUTO_ACTIVITY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 11 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | order id for which event is charted. |
| 12 | `PARENT_EVENT_ID` | DOUBLE | NOT NULL |  | highest level event id from the CLINICAL_EVENT table for the documented order. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person whom this event is charted. |
| 14 | `REASON_SHORT_DESC` | LONGTEXT |  |  | Medication disqualify reason. |
| 15 | `START_DT_TM` | DATETIME |  |  | Date and time of the event charted. |
| 16 | `STOP_DT_TM` | DATETIME |  |  | Event enddDate and time of the medication administration. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

