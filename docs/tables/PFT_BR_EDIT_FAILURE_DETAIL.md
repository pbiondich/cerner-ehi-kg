# PFT_BR_EDIT_FAILURE_DETAIL

> Stores a list of claim scrubbing detail information for an edit failure for a bill record.

**Description:** ProFit Bill Record Edit Failure Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FAILURE_ALIAS_NAME` | VARCHAR(40) | NOT NULL |  | The alias for the edit failure error that was returned from the scrubbing service. |
| 5 | `FAILURE_ALIAS_NAME_KEY` | VARCHAR(40) | NOT NULL |  | The indexed alias for the edit failure error that was returned from the scrubbing service. |
| 6 | `FAILURE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Provides information about the category of the edit failure. |
| 7 | `FAILURE_CATEGORY_GROUP_CD` | DOUBLE | NOT NULL |  | This column provides information about the category group of the edit failure. |
| 8 | `FAILURE_DESC` | VARCHAR(2000) |  |  | The description for the edit failure that was returned from the scrubbing service. |
| 9 | `LINE_ITEM_INDEX_NBR` | DOUBLE | NOT NULL |  | The clain line item to which this failure is associated. |
| 10 | `PFT_BR_EDIT_FAILURE_DETAIL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies detail information from the claim scrubbing for an edit failurefor a bill record. |
| 11 | `PFT_BR_EDIT_FAILURE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing record failure to which this detail is related. |
| 12 | `PROVIDER_ENROLLMENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related provider enrollment to which an edit failure detail is related. |
| 13 | `RESOLUTION_ACTION_DT_TM` | DATETIME |  |  | the date time of a resolution action being applied |
| 14 | `RESOLUTION_ACTION_FLAG` | DOUBLE | NOT NULL |  | the indicator denoting the resolution action applied. 0 = Default, 1 = Cancel and Regenerate Claim, 2 = Ignore |
| 15 | `RESOLUTION_ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | the personnel Id applying the resolution action |
| 16 | `SEVERITY_CATEGORY_TEXT` | VARCHAR(100) |  |  | The severity reason category for the edit failure. |
| 17 | `SEVERITY_CD` | DOUBLE | NOT NULL |  | Contains the severity code of the edit failure. |
| 18 | `SEVERITY_TEXT` | VARCHAR(100) |  |  | *** OBSOLETE *** This field is no longer supported and should not be used. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_BR_EDIT_FAILURE_ID` | [PFT_BR_EDIT_FAILURE](PFT_BR_EDIT_FAILURE.md) | `PFT_BR_EDIT_FAILURE_ID` |
| `PROVIDER_ENROLLMENT_ID` | [PROVIDER_ENROLLMENT](PROVIDER_ENROLLMENT.md) | `PROVIDER_ENROLLMENT_ID` |
| `RESOLUTION_ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

