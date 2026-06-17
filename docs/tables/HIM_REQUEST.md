# HIM_REQUEST

> This is a table that holds top-level information about request

**Description:** HIM REQUEST  
**Table type:** ACTIVITY  
**Primary key:** `HIM_REQUEST_ID`  
**Columns:** 34  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANCEL_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of a prsnl that cancels this request |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the person who created the request. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `HIM_REQUEST_ID` | DOUBLE | NOT NULL | PK | The primary key of this table |
| 11 | `LAST_UPDATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the person who last updated the request |
| 12 | `LOCKED_IND` | DOUBLE |  |  | if the request hast status of cancel, rejected, or completed, then this field will be set to 1 |
| 13 | `ONSITE_IND` | DOUBLE |  |  | Indicator to specify if the request will be executed on-site |
| 14 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The primary key of organization table |
| 15 | `PHONE_ID` | DOUBLE | NOT NULL |  | The primary key of phone table |
| 16 | `PULL_LIST_PRINTED_DT_TM` | DATETIME |  |  | The date and time of the pull list got printed |
| 17 | `PULL_LIST_PRINTED_IND` | DOUBLE |  |  | if pull list is printed, this indicator will be set to 1 |
| 18 | `REQUESTER_ID` | DOUBLE | NOT NULL |  | The id of a person who has requested a request |
| 19 | `REQUEST_DT_TM` | DATETIME |  |  | The date and time of request |
| 20 | `REQUEST_NUMBER` | DOUBLE |  |  | The number of request |
| 21 | `REQUEST_NUMBER_POOL_CD` | DOUBLE | NOT NULL |  | The pool where we get request numbers from |
| 22 | `REQUEST_STATUS_CD` | DOUBLE | NOT NULL |  | The code values of request status |
| 23 | `REQUEST_STATUS_DT_TM` | DATETIME |  |  | The date and time of request status has been changed |
| 24 | `REQUEST_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The id of a person that changed the request status |
| 25 | `REQUEST_TYPE_CD` | DOUBLE | NOT NULL |  | The code values of request type |
| 26 | `REQUIRED_DT_TM` | DATETIME |  |  | The date and time of the request was required |
| 27 | `ROI_REQUESTER_ID` | DOUBLE | NOT NULL |  | The ID of a person or organization requesting and ROI request |
| 28 | `SCH_EVENT_ID` | DOUBLE | NOT NULL |  | This column ties the request to the scheduled appointment that was used by the rules to create the request. |
| 29 | `TO_LOCATION_CD` | DOUBLE | NOT NULL |  | The code_value of location where the request will be sent |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [HIM_REQUEST_CRITERIA](HIM_REQUEST_CRITERIA.md) | `HIM_REQUEST_ID` |
| [HIM_REQUEST_PATIENT](HIM_REQUEST_PATIENT.md) | `HIM_REQUEST_ID` |
| [HIM_RESTRICT_VIEW_HIST](HIM_RESTRICT_VIEW_HIST.md) | `HIM_REQUEST_ID` |
| [REQUEST_EVENT_RELTN](REQUEST_EVENT_RELTN.md) | `HIM_REQUEST_ID` |
| [ROI_REJECT_REASON](ROI_REJECT_REASON.md) | `HIM_REQUEST_ID` |
| [ROI_REQUEST](ROI_REQUEST.md) | `HIM_REQUEST_ID` |

