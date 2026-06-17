# BR_DATAMART_DEFAULT

> table to store default data for each filter

**Description:** Bedrock Datamart Default  
**Table type:** REFERENCE  
**Primary key:** `BR_DATAMART_DEFAULT_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_DEFAULT_ID` | DOUBLE | NOT NULL | PK | Unique id for default data |
| 2 | `BR_DATAMART_FILTER_ID` | DOUBLE | NOT NULL | FK→ | id from br_datamart_filter |
| 3 | `CODE_SET` | DOUBLE |  |  | code set column |
| 4 | `CV_DESCRIPTION` | VARCHAR(255) | NOT NULL |  | Long name for a result |
| 5 | `CV_DISPLAY` | VARCHAR(100) | NOT NULL |  | short name for a result |
| 6 | `GROUP_CE_CONCEPT_CKI` | VARCHAR(255) |  |  | Concept cki for an event code |
| 7 | `GROUP_CE_NAME` | VARCHAR(100) |  |  | description for an event code |
| 8 | `GROUP_NAME` | VARCHAR(100) |  |  | Bedrock display name for group of events |
| 9 | `ORDER_DETAIL_IND` | DOUBLE |  |  | Indicates if a default has order details |
| 10 | `QUALIFIER_FLAG` | DOUBLE |  |  | indicates how the result is to be compared to an event - greater than, equal to, less than,etc. 1=Equal to 2=Not equal to 3=Greater than 4=Less than 5=Greater than or equal to 6=Less than or equal to |
| 11 | `RESULT_TYPE_FLAG` | DOUBLE |  |  | indicates the type of result - numeric,alpha,free text 1=Alpha 2=Numeric |
| 12 | `RESULT_VALUE` | VARCHAR(255) |  |  | the actual result that an event will be linked to - could be a free textnumber or a string value |
| 13 | `UNIQUE_IDENTIFIER` | VARCHAR(255) | NOT NULL |  | unique string for results |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_FILTER_ID` | [BR_DATAMART_FILTER](BR_DATAMART_FILTER.md) | `BR_DATAMART_FILTER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_DATAMART_DEFAULT_DETAIL](BR_DATAMART_DEFAULT_DETAIL.md) | `BR_DATAMART_DEFAULT_ID` |

