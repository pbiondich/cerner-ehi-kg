# ORDER_DAILY_REVIEW_RSPNL

> This table stores information about the daily review responsibilities associated to orders.

**Description:** order daily review responsibility  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_DAILY_REVIEW_RSPNL_ID`  
**Columns:** 25  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGNED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who is filtered to view this daily review responsibility. |
| 2 | `DAILY_REVIEW_RSPNL_BIT` | DOUBLE | NOT NULL |  | A bitmask which indicates additional attributes about the daily review responsibility. The 1st bit (2^0) indicates if all daily reviews are resolved. The 2nd bit (2^1) indicates if any resolved when overdue daily reviews exist. The 3rd bit (2^2) indicates that this responsibility was deferred to another responsibility. The 4th bit (2^3) indicates that this responsibility was deferred from another responsibility. |
| 3 | `DAILY_REVIEW_STATUS_FLAG` | DOUBLE | NOT NULL |  | The flag used to indicate the status of the daily review responsibility. 0 = inactive, 1 = active. |
| 4 | `DUE_TM_TXT` | VARCHAR(4) |  |  | The due time of the daily review for this responsibility. |
| 5 | `EFFECTIVE_START_DT_TM` | DATETIME | NOT NULL |  | The start date time of this daily review responsibility. |
| 6 | `EFFECTIVE_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 7 | `EFFECTIVE_STOP_DT_TM` | DATETIME |  |  | The stop date time of this daily review responsibility. |
| 8 | `EFFECTIVE_STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The persons encounter id. |
| 10 | `ORDER_DAILY_REVIEW_RSPNL_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the order_daily_review_rspnl table. |
| 11 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order associated to this daily review responsibility. |
| 12 | `PATIENT_LOCATION_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | The patient facility location that is responsible for this daily review responsibility. |
| 13 | `PATIENT_LOCATION_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | The patient nurse unit location that is responsible for this daily review responsibility. |
| 14 | `PATIENT_LOC_TZ` | DOUBLE |  |  | The time zone of the patient's location. |
| 15 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person whom this daily review is for. |
| 16 | `REVIEW_TRACKING_VALUE_TXT` | VARCHAR(512) |  |  | The review tracking string used to determine if a daily review has been resolved |
| 17 | `RSPNL_BEGIN_DT_NBR` | DOUBLE | NOT NULL |  | The date number when daily reviews for the responsibility are active. |
| 18 | `RSPNL_END_DT_NBR` | DOUBLE |  |  | The date number when daily reviews for the responsibility end. |
| 19 | `RSPNL_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The personnel group responsible for this daily review responsibility. |
| 20 | `RSPNL_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel who is responsible for this daily review responsibility. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSIGNED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PATIENT_LOCATION_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PATIENT_LOCATION_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RSPNL_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `RSPNL_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ORDER_DAILY_REVIEW_DEFER](ORDER_DAILY_REVIEW_DEFER.md) | `FROM_DAILY_REVIEW_RSPNL_ID` |
| [ORDER_DAILY_REVIEW_DEFER](ORDER_DAILY_REVIEW_DEFER.md) | `TO_DAILY_REVIEW_RSPNL_ID` |

