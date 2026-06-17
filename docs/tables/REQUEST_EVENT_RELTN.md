# REQUEST_EVENT_RELTN

> Requester event reltn ties event_cd to a roi_request

**Description:** Request Event reltn stores the event codes that are tied to a request  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

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
| 7 | `EVENT_CD` | DOUBLE | NOT NULL |  | This is the event code that is tied to a request |
| 8 | `EVENT_CD_DISP` | VARCHAR(40) |  |  | This is the display value for the event code |
| 9 | `EVENT_CD_DISP_KEY` | VARCHAR(40) |  |  | The display key for event cd |
| 10 | `HIM_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | The primary key of him_request table |
| 11 | `REQUEST_EVENT_RELTN_ID` | DOUBLE | NOT NULL |  | This is the unique identifier to the request event_reltn table, it is a internal system assigned number. |
| 12 | `REQUEST_STATUS_CD` | DOUBLE | NOT NULL |  | This is the status of the requested event reltn row. |
| 13 | `REQUEST_STATUS_DT_TM` | DATETIME |  |  | This is the date and time that the request was last updated |
| 14 | `REQUEST_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | This is the unique identifier to the person who last updated the status. |
| 15 | `ROI_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier to the roi_request table It is not being used any more. It was replaced by him_request_id |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HIM_REQUEST_ID` | [HIM_REQUEST](HIM_REQUEST.md) | `HIM_REQUEST_ID` |
| `ROI_REQUEST_ID` | [ROI_REQUEST](ROI_REQUEST.md) | `ROI_REQUEST_ID` |

