# BR_DATAM_MAPPING_TYPE

> Records types of items that will be mapped from a predefined set of codified terms to a selected Millennium term. All entries apply only to a filter category mean of MAP. Creating this association is required for Millennium data types that are not captured with an automatic association to a standard vocabulary term. These codified terms are used for e-measure submission.

**Description:** Bedrock Datamart Mapping Type  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | The topic that is being mapped. The corresponding value id from the BR_DATAMART_CATEGORY table. Along with the filter category id, this is used to retrieve the available mapping types. |
| 2 | `BR_DATAMART_FILTER_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | The category group that is being mapped. The corresponding value id from the BR_DATAMART_FILTER_CATEGORY table. Along with the category id, this is used to retrieve the available mapping types. |
| 3 | `BR_DATAM_MAPPING_TYPE_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_DATAM_MAPPING_TYPE table. |
| 4 | `DISPLAY_SEQ` | DOUBLE | NOT NULL |  | The sequence that map data types will be displayed. This sequence is applicable per category and filter category. |
| 5 | `MAP_DATA_TYPE_CD` | DOUBLE | NOT NULL |  | This will be the type of mapping to Millennium values. For example, ORDER, CODE SET, EVENT. |
| 6 | `MAP_DATA_TYPE_DISPLAY` | VARCHAR(100) | NOT NULL |  | The display used for the type of mapping. |
| 7 | `MAP_DATA_TYPE_VALUE` | DOUBLE | NOT NULL |  | The value that further defines the mapping type. For example, a codeset number when codeset is the map type. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_CATEGORY_ID` | [BR_DATAMART_CATEGORY](BR_DATAMART_CATEGORY.md) | `BR_DATAMART_CATEGORY_ID` |
| `BR_DATAMART_FILTER_CATEGORY_ID` | [BR_DATAMART_FILTER_CATEGORY](BR_DATAMART_FILTER_CATEGORY.md) | `BR_DATAMART_FILTER_CATEGORY_ID` |

