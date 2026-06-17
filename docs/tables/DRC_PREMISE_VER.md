# DRC_PREMISE_VER

> Provides History to the DRC_PREMISE table.

**Description:** DRC PREMISE VER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONCEPT_CKI` | VARCHAR(255) |  |  | Parent CKI to CMT_CONCEPT table. CKI stands for Cerner Knowledge Index. |
| 3 | `DOSE_RANGE_CHECK_ID` | DOUBLE | NOT NULL |  | The high level grouping id of all the premise groups/dose ranges that should be applied to this order. |
| 4 | `DRC_PREMISE_ID` | DOUBLE | NOT NULL |  | Unique Identifier with ver_seq |
| 5 | `MULTUM_CASE_ID` | DOUBLE | NOT NULL |  | The actual identifier for a premise from Multum. |
| 6 | `PARENT_IND` | DOUBLE |  |  | Notes whether this premise is a parent or not. 0 |
| 7 | `PARENT_PREMISE_ID` | DOUBLE | NOT NULL |  | If the premise is part of a premise group this will be the id of the premise group level. |
| 8 | `PREMISE_TYPE_FLAG` | DOUBLE |  |  | Identifies what type of premise this is |
| 9 | `RELATIONAL_OPERATOR_FLAG` | DOUBLE |  |  | Controls the comparison against the premise value . |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VALUE1` | DOUBLE |  |  | Holds any numeric or code value premise values. |
| 16 | `VALUE1_STRING` | VARCHAR(255) |  |  | Holds any textual premise values |
| 17 | `VALUE2` | DOUBLE |  |  | Holds any numeric or code value premise values. |
| 18 | `VALUE2_STRING` | VARCHAR(255) |  |  | Holds any textual premise values |
| 19 | `VALUE_TYPE_FLAG` | DOUBLE |  |  | Controls the type of data that is stored for the premise |
| 20 | `VALUE_UNIT_CD` | DOUBLE | NOT NULL |  | Contains the codified units of measure for the premise |
| 21 | `VER_SEQ` | DOUBLE | NOT NULL |  | Version of the Rule |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

