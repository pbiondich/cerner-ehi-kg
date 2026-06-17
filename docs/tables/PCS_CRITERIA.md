# PCS_CRITERIA

> Stores the criteria used for a specific Review Criteria for Clinical Validation.

**Description:** PCS CRITERIA  
**Table type:** REFERENCE  
**Primary key:** `CRITERIA_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AND_GROUPING_DISPLAY` | VARCHAR(25) | NOT NULL |  | Pattern name for Microbiology pattern matching. |
| 6 | `AND_GROUPING_NBR` | DOUBLE | NOT NULL |  | Signifies that the relationship between two selected criteria is now an AND instead of the default OR |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CRITERIA_ID` | DOUBLE | NOT NULL | PK | Contains the internal identification code that uniquely identifies the criteria. |
| 9 | `CRITERIA_TYPE_CD` | DOUBLE | NOT NULL |  | Code value of selected criteria type (i.e. Service Resource, Result Flag, ¿). Code set 29161. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | id number of the selected criteria located on table . |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Table name where selected criteria is stored. Valid names include:CODE_VALUE, PRSNL, ORDER_CATALOG, LOCATION, SERVICE_RESOURCE |
| 13 | `REVIEW_CRITERIA_ID` | DOUBLE | NOT NULL | FK→ | Contains the foreign key to the pcs_review_criteria table. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REVIEW_CRITERIA_ID` | [PCS_REVIEW_CRITERIA](PCS_REVIEW_CRITERIA.md) | `REVIEW_CRITERIA_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PCS_QUALIFYING_CRITERIA](PCS_QUALIFYING_CRITERIA.md) | `CRITERIA_ID` |
| [PCS_SUB_CRITERIA](PCS_SUB_CRITERIA.md) | `CRITERIA_ID` |

