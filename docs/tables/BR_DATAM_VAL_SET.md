# BR_DATAM_VAL_SET

> Grouping mechanism for EHR Topics.

**Description:** Bedrock Datamart Value Set  
**Table type:** REFERENCE  
**Primary key:** `BR_DATAM_VAL_SET_ID`  
**Columns:** 10  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | The corresponding category from the BR_DATAMART_CATEGORY table. This along with a template_name and a value_set_name make up a unique method of finding a value set's corresponding values. |
| 2 | `BR_DATAM_VAL_SET_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BR_DATAM_VAL_SET table. |
| 3 | `TEMPLATE_NAME` | VARCHAR(50) | NOT NULL |  | QRDA template to be used for e-submission, not currently in Millennium. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `VALUE_SET_NAME` | VARCHAR(255) | NOT NULL |  | The name given to a list of values for the particular data element, not currently in Millennium. |
| 10 | `VOCAB_OID_TXT` | VARCHAR(100) |  |  | Object Identifier for this vocabulary as related to this value set. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BR_DATAMART_FILTER](BR_DATAMART_FILTER.md) | `EXPECTED_ACTION_VALUE_SET_ID` |
| [BR_DATAMART_FILTER](BR_DATAMART_FILTER.md) | `INACTION_REASON_VALUE_SET_ID` |
| [BR_DATAM_VAL_SET_ITEM](BR_DATAM_VAL_SET_ITEM.md) | `BR_DATAM_VAL_SET_ID` |

