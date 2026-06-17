# ABSTRACT_FIELD_DEF

> User defined abstract fields

**Description:** Abstract Field definition table  
**Table type:** REFERENCE  
**Primary key:** `ABSTRACT_FIELD_DEF_CD`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABSTRACT_DESC` | VARCHAR(255) |  |  | Description of the chart abstracting field being added |
| 2 | `ABSTRACT_FIELD_DEF_CD` | DOUBLE | NOT NULL | PK | This is the coded primary identifier for this table |
| 3 | `ABSTRACT_FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | The codes that represent the types of information (string, numeric, etc.). that the abstract field is capturing |
| 4 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CALCULATE_CD` | DOUBLE | NOT NULL |  | To do calculation on abstract field based on the code value from code set 20689 |
| 10 | `CODESET_NBR` | DOUBLE |  |  | The number of the codeset that the data in this abstract field must be a subset of |
| 11 | `CONDITIONAL_IND` | DOUBLE |  |  | Indicates if this is a conditional field or not. |
| 12 | `DATE_CHK_IND` | DOUBLE |  |  | This flexes whether the date should be validated against admit and discharge dates or not |
| 13 | `DISPLAY_LABEL` | VARCHAR(255) |  |  | The label for the abstract field. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `LENGTH` | DOUBLE |  |  | The length for the abstract data being entered. |
| 16 | `OMF_FACT_IND` | DOUBLE |  |  | To represent Fact or Dimension by 1 or 0 |
| 17 | `REQUIRED_IND` | DOUBLE |  |  | Indicates if this is a required abstract field or not. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ABSTRACT_FIELD_FLEX](ABSTRACT_FIELD_FLEX.md) | `ABSTRACT_FIELD_DEF_CD` |

