# LH_D_BR_DATAMART_CATEGORY

> This dimension table is used to store Bedrock Category reference data

**Description:** LH_D_BR_DATAMART_CATEGORY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BASELINE_TARGET_IND` | DOUBLE | NOT NULL |  | Determines whether to display baseline/target values. 1 is OFF |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time that the record became effective. |
| 4 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | Unique ID for each category |
| 5 | `CATEGORY_MEAN` | VARCHAR(30) | NOT NULL |  | Unique string for a category |
| 6 | `CATEGORY_NAME` | VARCHAR(100) | NOT NULL |  | Category display name |
| 7 | `CATEGORY_TOPIC_MEAN` | VARCHAR(30) |  |  | Stores a generic meaning for categories that are linked together |
| 8 | `CATEGORY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Stores the type of reports to be setup - 0 = lighthouse 1 = Mpages 2 = nhiqm |
| 9 | `D_BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_D_BR_DATAMART_CATEGORY table. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time that the record became end effective. |
| 11 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 12 | `FLEX_FLAG` | DOUBLE | NOT NULL |  | Store an indicator of how this category is flexed |
| 13 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 14 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 15 | `RELIABILITY_SCORE_IND` | DOUBLE | NOT NULL |  | Determines whether to display Reliability Score Input Fields. 1 is OFF. |
| 16 | `SCRIPT_NAME` | VARCHAR(30) |  |  | Name of the ccl script that will be used by Mpages to return data for the category |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date/time the row was last inserted or updated. |
| 19 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 20 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The application responsible for updating the record. |
| 21 | `VIEWPOINT_CAPABLE_IND` | DOUBLE | NOT NULL |  | Indicates whether a category is eligible to be included in an Mpage viewpoint. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

