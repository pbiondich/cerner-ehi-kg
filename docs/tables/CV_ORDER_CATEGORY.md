# CV_ORDER_CATEGORY

> Categories for orders viewed in cv patient profile

**Description:** CV Order Category  
**Table type:** REFERENCE  
**Primary key:** `CV_ORDER_CATEGORY_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY_LIMIT` | DOUBLE | NOT NULL |  | Default number of orders displayed for category |
| 2 | `CATEGORY_NAME` | VARCHAR(40) | NOT NULL |  | Category name created by the user |
| 3 | `COLLATION_SEQ` | DOUBLE | NOT NULL |  | Sequence in which order category can be ordered |
| 4 | `CV_ORDER_CATEGORY_ID` | DOUBLE | NOT NULL | PK | Primary key, unique identifier for the category |
| 5 | `SECTION_ENUM` | DOUBLE | NOT NULL |  | Indicates that the category or Section for the type of order (historical, current, etc.) |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CV_ORDER_CATEGORY_R](CV_ORDER_CATEGORY_R.md) | `CV_ORDER_CATEGORY_ID` |

