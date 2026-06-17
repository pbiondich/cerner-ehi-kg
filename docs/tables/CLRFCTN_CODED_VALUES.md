# CLRFCTN_CODED_VALUES

> Coded vocabulary identifiers returned in Clarification Responses

**Description:** Clarification Coded Values  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLRFCTN_CODED_VALUES_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the Table |
| 2 | `DISPLAY_TEXT` | VARCHAR(255) | NOT NULL |  | Vocabulary Display |
| 3 | `ENTITY_ID` | DOUBLE | NOT NULL |  | ID of the row on the linked clarification table identified in ENTITY_NAME |
| 4 | `ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the Clarification table being linked |
| 5 | `EXST_POTEN_CONDITION_FLAG` | DOUBLE | NOT NULL |  | Indicates whether exiting condition OR New Diagnosis 0 - Not Applicable; 1 - Existing Condition; 2 - New Diagnosis |
| 6 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | Source Vocabulary code from Code Set 400 |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `VOCABULARY_CODE` | VARCHAR(20) | NOT NULL |  | Vocabulary Code |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

