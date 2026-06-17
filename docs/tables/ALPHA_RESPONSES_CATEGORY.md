# ALPHA_RESPONSES_CATEGORY

> Allows categorization of Alpha Responses.

**Description:** Alpha Responses Category  
**Table type:** REFERENCE  
**Primary key:** `ALPHA_RESPONSES_CATEGORY_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALPHA_RESPONSES_CATEGORY_ID` | DOUBLE | NOT NULL | PK | Unique, generated key for ALPHA_RESPONSES_CATEGORY. |
| 2 | `CATEGORY_NAME` | VARCHAR(100) | NOT NULL |  | The identifier and display value for the category. |
| 3 | `DISPLAY_SEQ` | DOUBLE | NOT NULL |  | Identifies the order the categories will be displayed. |
| 4 | `EXPAND_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the category is expanded or contracted to show the associated Alpha Responses.0 |
| 5 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific row in the reference_range_factor table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REFERENCE_RANGE_FACTOR_ID` | [REFERENCE_RANGE_FACTOR](REFERENCE_RANGE_FACTOR.md) | `REFERENCE_RANGE_FACTOR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ALPHA_RESPONSES](ALPHA_RESPONSES.md) | `ALPHA_RESPONSES_CATEGORY_ID` |

