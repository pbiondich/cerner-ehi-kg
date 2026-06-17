# PRSNL_SUSPENSION

> Stores physician suspension data for a given doctor for multiple facilities.

**Description:** Personnel Suspension Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FREETEXT_COMMENT` | VARCHAR(255) |  |  | Comment field for suspensions. |
| 8 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for Organization table. |
| 9 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for Prsnl table. |
| 10 | `PRSNL_SUSPENSION_ID` | DOUBLE | NOT NULL |  | Unique identifier for Prsnl_Suspension table. |
| 11 | `SUSPENDED_CHARTS` | DOUBLE |  |  | The number of charts for the personnel that qualified for suspension when the suspension was created. |
| 12 | `SUSPENDED_DOCUMENTS` | DOUBLE |  |  | The number of documents for the personnel that qualified for suspension when the suspension was created. |
| 13 | `SUSPENDED_ORDERS` | DOUBLE | NOT NULL |  | The number of orders for the personnel that qualified for suspension when the suspension was created. |
| 14 | `SUSP_BEGIN_DT_TM` | DATETIME |  |  | Beginning date and time for a suspension. Will always have a time of "00:00:00.00" |
| 15 | `SUSP_BEGIN_TZ` | DOUBLE | NOT NULL |  | suspension begin time zone |
| 16 | `SUSP_END_DT_TM` | DATETIME |  |  | Ending date and time for a suspension. Will always have a time of "23:59:59.00" |
| 17 | `SUSP_END_TZ` | DOUBLE | NOT NULL |  | suspension end time zone |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

