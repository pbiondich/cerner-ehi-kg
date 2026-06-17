# PCS_REVIEW_CRITERIA

> Stores the review criteria for clinical validation.

**Description:** PCS REVIEW CRITERIA  
**Table type:** REFERENCE  
**Primary key:** `REVIEW_CRITERIA_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CORR_PREF_FLAG` | DOUBLE |  |  | Indicates the corrections preference of this review item. Values are: 0 - Apply to verified, 1 = Apply to corrected, 2 = Apply to both. |
| 7 | `CRITERIA_NAME` | VARCHAR(100) | NOT NULL |  | Contains the display name of the review criteria |
| 8 | `CRITERIA_NAME_KEY` | VARCHAR(100) | NOT NULL |  | Display key of the review criteria display name. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `HIERARCHY_ID` | DOUBLE | NOT NULL | FK→ | Contains the foreign key to the pcs_hierarchy table. Defines where the result is sent upon qualifying |
| 11 | `HOLIDAY_SCHEDULE_CD` | DOUBLE | NOT NULL |  | The schedule associated with this instrument for autoverification and clinical validatin. |
| 12 | `PRECEDENCE_NBR` | DOUBLE | NOT NULL |  | Within each PathNet product, there is a specific order or precedence that the review criteria must be checked. It will be up to the clients to build the criteria from most restrictive to least restrictive. For example, if a result is 'Abnormal', it will be sent to Dr. Ruth Strong for review unless it came from 'Instrument A', 'Bench B' - in which case, the first review criteria would qualify and send the result to the Chemistry Hierarchy |
| 13 | `PRODUCT_TYPE_CD` | DOUBLE | NOT NULL |  | Code value of product associated with this criteria (Gen Lab, Micro, ...). Code set 28961. |
| 14 | `RESULT_POST_PREF_FLAG` | DOUBLE |  |  | Indicates the result posting personnel preferences of this review item. When a review item is approved this flag will determine whether the verifying personnel will be used to post the verified/corrected results. |
| 15 | `REVIEW_CRITERIA_ID` | DOUBLE | NOT NULL | PK | Contains the internal identification code that uniquely identifies the review criteria. |
| 16 | `ROUTE_PREF_FLAG` | DOUBLE |  |  | Flag value to indicate the route preference of this review item. Flag values are: 0 - Micro Task 1 = Order Level Route2 = All Assay Level Route3 = Assay Level Route |
| 17 | `SCHEDULE_CD` | DOUBLE | NOT NULL |  | The schedule associated with this instrument for autoverification and clinical validation. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HIERARCHY_ID` | [PCS_HIERARCHY](PCS_HIERARCHY.md) | `HIERARCHY_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PCS_CRITERIA](PCS_CRITERIA.md) | `REVIEW_CRITERIA_ID` |
| [PCS_REVIEW_ITEM](PCS_REVIEW_ITEM.md) | `REVIEW_CRITERIA_ID` |

