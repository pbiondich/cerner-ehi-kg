# CNT_CONDITIONAL_DTA_KEY

> Contains details about working view conditional exression DTA, which are used by Bedrock tool. Imported usig content manager tool.

**Description:** CNT_CONDITIONAL_DTA_KEY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AGE_FROM_NBR` | DOUBLE | NOT NULL |  | Starting age on a range |
| 3 | `AGE_FROM_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for age from |
| 4 | `AGE_FROM_UNIT_CD_UID` | VARCHAR(100) |  |  | UID of Age from CD which is used for versioning |
| 5 | `AGE_TO_NBR` | DOUBLE | NOT NULL |  | Ending age on a range |
| 6 | `AGE_TO_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for age to |
| 7 | `AGE_TO_UNIT_CD_UID` | VARCHAR(100) |  |  | UID of Age to CD which is used for versioning |
| 8 | `CNT_CONDITIONAL_DTA_KEY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `CNT_CONDITIONAL_DTA_KEY_UID` | VARCHAR(100) |  |  | Primary way to distinguish |
| 10 | `CONDITIONAL_ASSAY_CD` | DOUBLE | NOT NULL |  | The DTA that needs to enable/disable |
| 11 | `CONDITIONAL_ASSAY_CD_UID` | VARCHAR(100) |  |  | UID of DTA |
| 12 | `CONDITIONAL_DTA_ID` | DOUBLE | NOT NULL |  | Unique value of the DTA |
| 13 | `COND_EXPRESSION_ID` | DOUBLE | NOT NULL |  | Foreign key on the conditional expression |
| 14 | `DCP_COND_DTA_REF_ID` | DOUBLE | NOT NULL | FK→ | refers to original CONDITIONAL_DTA table which is used by bedrock tool. |
| 15 | `GENDER_CD` | DOUBLE | NOT NULL |  | Sex of the patient |
| 16 | `GENDER_CD_UID` | VARCHAR(100) |  |  | UID of gender code used for versioning |
| 17 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location of the patient |
| 18 | `LOCATION_CD_UID` | VARCHAR(100) |  |  | UID of location code |
| 19 | `POSITION_CD` | DOUBLE | NOT NULL |  | Position code of the documenting user |
| 20 | `POSITION_CD_UID` | VARCHAR(100) |  |  | UID of location code |
| 21 | `PREV_CONDITIONAL_DTA_ID` | DOUBLE | NOT NULL |  | Unique identifier or Original conditional DTA id |
| 22 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | DTA needs documented |
| 23 | `UNKNOWN_AGE_IND` | DOUBLE | NOT NULL |  | age unknown if true |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 29 | `VERSION_DT_TM` | DATETIME |  |  | Date and time when this record was updated, used in versioning of the conditional expression in conjunction with UID column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_COND_DTA_REF_ID` | [CONDITIONAL_DTA](CONDITIONAL_DTA.md) | `CONDITIONAL_DTA_ID` |

