# BR_OF_PARENT_RELTN

> When a new order folder is created, a row is added to this table to track the source from which the order folder was created.

**Description:** Bedrock Order Folder Parent Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALT_SEL_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Provides a link between the br_of_parent_reltn table and the alt_sel_cat table |
| 2 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 3 | `SOURCE_ID` | DOUBLE | NOT NULL |  | If the value in the source_name field is a table name, then the value in the source_id field provides a link between the br_of_parent_reltn table and the table indicated in the source_name field. If the value in the source_name field is not a table name, then the source_id field will have a value of 0. |
| 4 | `SOURCE_NAME` | VARCHAR(32) | NOT NULL |  | The source_name field indicates the source of a new order folder. The source_name can be a table on which the value in the source_id field is a key or it can be free-text. If free-text, then the source_id will have a value of 0. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALT_SEL_CATEGORY_ID` | [ALT_SEL_CAT](ALT_SEL_CAT.md) | `ALT_SEL_CATEGORY_ID` |

