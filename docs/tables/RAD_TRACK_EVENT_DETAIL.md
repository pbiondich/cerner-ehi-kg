# RAD_TRACK_EVENT_DETAIL

> This table holds activity data for details associated with a tracking event.

**Description:** Rad Track Event Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENTS_IND` | DOUBLE | NOT NULL |  | Indicates if there comments associated with the order. |
| 2 | `EVENT_STATUS_CD` | DOUBLE | NOT NULL |  | Current status of the event. |
| 3 | `IV_IND` | DOUBLE | NOT NULL |  | Indicates if the patient is using an IV. |
| 4 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Defines that location that the patient is to be transported to. |
| 5 | `O2_IND` | DOUBLE | NOT NULL |  | Indicates if the patient is using oxygen apparatus. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL |  | The Order_Id is a foreign key to the Orders table. It is used to uniquely identify an order. |
| 7 | `TRACKING_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the tracking event table. |
| 8 | `TRANSPORT_MODE_CD` | DOUBLE | NOT NULL |  | Describes the transportation type that is associated with the order. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACKING_EVENT_ID` | [TRACKING_EVENT](TRACKING_EVENT.md) | `TRACKING_EVENT_ID` |

