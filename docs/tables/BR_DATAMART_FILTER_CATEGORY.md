# BR_DATAMART_FILTER_CATEGORY

> table to store filter categories

**Description:** Bedrock Datamart Filter Category  
**Table type:** REFERENCE  
**Primary key:** `BR_DATAMART_FILTER_CATEGORY_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_FILTER_CATEGORY_ID` | DOUBLE | NOT NULL | PK | Unique id for each filter category |
| 2 | `CODESET` | DOUBLE | NOT NULL |  | Code set codeset number based on filter_category_type_mean (facility=220,encounter type=71,etc..) |
| 3 | `FILTER_CATEGORY_MEAN` | VARCHAR(30) | NOT NULL |  | unique string for filter category |
| 4 | `FILTER_CATEGORY_TYPE_MEAN` | VARCHAR(30) | NOT NULL |  | unique string for each type of filter category |
| 5 | `SCRIPT_NAME` | VARCHAR(30) |  |  | The script that is called to retrieve a list of custom filter values. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_DATAM_MAPPING_TYPE](BR_DATAM_MAPPING_TYPE.md) | `BR_DATAMART_FILTER_CATEGORY_ID` |

