# PFT_CA_CRITERIA_VALUE

> Collection Agency Criteria Values

**Description:** PFT CA CRITERIA VALUE  
**Table type:** REFERENCE  
**Primary key:** `PFT_CA_CRITERIA_VALUE_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CLIENT_NUMBER` | VARCHAR(20) |  |  | The reference that the collection/precollection agency assigns to the billing entity |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EVALUATOR_TXT` | VARCHAR(250) |  |  | The value that the criteria is to be evaluated upon |
| 9 | `EVALUATOR_TYPE` | DOUBLE |  |  | Value of the type of evaluation used. This enumeration is defines as 0 >, 1 >=, 2 =, 3 <=, 4 < , 5 Is Not Defined , 6 Is Not Defined or Not Equal to Itself |
| 10 | `ORDER_SEQ` | DOUBLE |  |  | Sequence Criteria that was originally entered |
| 11 | `PFT_CA_CRITERIA_VALUE_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 12 | `PFT_COLLECTION_AGENCY_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to PFT_collection_agency table |
| 13 | `PFT_TASK_CRITERIA_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the Task_Criteria table |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_COLLECTION_AGENCY_ID` | [PFT_COLLECTION_AGENCY](PFT_COLLECTION_AGENCY.md) | `PFT_COLLECTION_AGENCY_ID` |
| `PFT_TASK_CRITERIA_ID` | [TASK_CRITERIA](TASK_CRITERIA.md) | `PFT_TASK_CRITERIA_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PFT_ENCNTR_COLLECTION_RELTN](PFT_ENCNTR_COLLECTION_RELTN.md) | `PFT_CA_CRITERIA_VALUE_ID` |

