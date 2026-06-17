# DRC_PREMISE

> Table stores the premises to be used to see if a patient qualifies to be checked for dose ranges. These premises could range from age, route, patient condition, etc? The table is initially populated with Multum content but a user has the ability to modify the content.

**Description:** Dose Range Checking Premise  
**Table type:** REFERENCE  
**Primary key:** `DRC_PREMISE_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONCEPT_CKI` | VARCHAR(255) |  |  | Parent CKI to CMT_CONCEPT table. CKI stands for Cerner Knowledge Index. |
| 3 | `DOSE_RANGE_CHECK_ID` | DOUBLE | NOT NULL |  | The high level grouping id of all the premise groups/dose ranges that should be applied to this order. |
| 4 | `DRC_IDENTIFIER` | VARCHAR(50) |  |  | Unique identifier for dose range from Multum. Combination of ! . Both fields are from external database. |
| 5 | `DRC_PREMISE_ID` | DOUBLE | NOT NULL | PK | Unique Identifier |
| 6 | `MULTUM_CASE_ID` | DOUBLE | NOT NULL |  | The actual identifier for a premise from Multum. |
| 7 | `PARENT_IND` | DOUBLE |  |  | Notes whether this premise is a parent or not. |
| 8 | `PARENT_PREMISE_ID` | DOUBLE | NOT NULL |  | If the premise is part of a premise group this will be the id of the premise group level. |
| 9 | `PREMISE_TYPE_FLAG` | DOUBLE |  |  | Identifies what type of premise this is |
| 10 | `RELATIONAL_OPERATOR_FLAG` | DOUBLE |  |  | Controls the comparison against the premise value . |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `VALUE1` | DOUBLE |  |  | Holds any numeric or code value premise values. |
| 17 | `VALUE1_STRING` | VARCHAR(255) |  |  | Holds any textual premise values |
| 18 | `VALUE2` | DOUBLE |  |  | Holds any numeric or code value premise values. |
| 19 | `VALUE2_STRING` | VARCHAR(255) |  |  | Holds any textual premise values |
| 20 | `VALUE_TYPE_FLAG` | DOUBLE |  |  | Controls the type of data that is stored for the premise |
| 21 | `VALUE_UNIT_CD` | DOUBLE | NOT NULL |  | Contains the codified units of measure for the premise |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DRC_DOSE_RANGE_VER](DRC_DOSE_RANGE_VER.md) | `DRC_PREMISE_ID` |

