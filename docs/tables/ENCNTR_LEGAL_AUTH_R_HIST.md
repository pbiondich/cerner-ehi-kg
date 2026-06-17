# ENCNTR_LEGAL_AUTH_R_HIST

> Used for tracking history of changes to encounter legal authority relationship.

**Description:** Encounter Legal Authority Relationship History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 7 | `COMMITMENT_CATEGORY_CD` | DOUBLE | NOT NULL |  | Identifies the category of the patient's commitment to the facility. |
| 8 | `COMMITMENT_PERIOD` | DOUBLE | NOT NULL |  | The length of time specified in the court order by which the facility has legal authority to hold the patient. |
| 9 | `COMMITMENT_PERIOD_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the unit qualifier (days, hours, etc.) for the commitment period. |
| 10 | `COMMITMENT_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason for the patient's commitment to the facility. |
| 11 | `COMMITMENT_TYPE_FLIP_IND` | DOUBLE | NOT NULL |  | The information indicating if the commitment type for the patient has changed with respect to the previous legal authority for the encounter. |
| 12 | `COUNTY_CD` | DOUBLE | NOT NULL |  | The county code is the code set that value that represents the county which provided the legal authority to treat the patient. |
| 13 | `COURT_ORDER_NUMBER` | VARCHAR(50) |  |  | The identifying number of the court order(s) issued for the patient. |
| 14 | `COURT_ORDER_RECEIVE_DT_TM` | DATETIME |  |  | The date and time at which the facility received the issued court order. |
| 15 | `COURT_ORDER_SIGN_DT_TM` | DATETIME |  |  | The date and time at which the issued court order was signed. |
| 16 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 17 | `ENCNTR_LEGAL_AUTH_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the ENCNTR_LEGAL_AUTH_RELTN table. |
| 18 | `ENCNTR_LEGAL_AUTH_R_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ENCNTR_LEGAL_AUTH_R_HIST table. |
| 19 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 20 | `LEGAL_AUTHORITY_ID` | DOUBLE | NOT NULL | FK→ | Identifier from the LEGAL_AUTHORITY table that contains various attributes representing the legal authority. |
| 21 | `NEXT_COURT_HEARING_DT_TM` | DATETIME |  |  | The date and time of the patient's next court hearing. |
| 22 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 23 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 24 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_LEGAL_AUTH_RELTN_ID` | [ENCNTR_LEGAL_AUTH_RELTN](ENCNTR_LEGAL_AUTH_RELTN.md) | `ENCNTR_LEGAL_AUTH_RELTN_ID` |
| `LEGAL_AUTHORITY_ID` | [LEGAL_AUTHORITY](LEGAL_AUTHORITY.md) | `LEGAL_AUTHORITY_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

