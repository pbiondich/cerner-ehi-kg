# NOMEN_CAT_LIST

> Identifies the children for each Nomenclature Category.

**Description:** Nomenclature Category List  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_CATEGORY_ID` | DOUBLE | NOT NULL |  | Unique Identifier for child categories. |
| 2 | `CHILD_FLAG` | DOUBLE |  |  | Flag used to identify the kind of list item. |
| 3 | `LIST_SEQUENCE` | DOUBLE |  |  | The sequence of the child objects with the parent. |
| 4 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Identifies the Nomenclature Item in the category. |
| 5 | `NOMEN_CAT_LIST_ID` | DOUBLE | NOT NULL |  | Unique identifier for a row in the Nomenclature Category List table. |
| 6 | `PARENT_CATEGORY_ID` | DOUBLE | NOT NULL |  | Identifies the "owner", or parent, category for the list item. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

