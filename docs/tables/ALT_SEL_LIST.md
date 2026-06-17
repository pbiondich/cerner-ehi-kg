# ALT_SEL_LIST

> Alternate Selection List. Contains the parent-child associations between alternate selection categories and other categories, synonyms, home-health problems and reference tasks.

**Description:** Alternate Selection List.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALT_SEL_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the parent alternate selection category. |
| 2 | `CHILD_ALT_SEL_CAT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the child alternate selection category. |
| 3 | `LIST_TYPE` | DOUBLE |  |  | Indicates what type of child the record references. Valid values are: 1 - alternate selection category, 2 - synonym, 3 - home health problem, 4- reference task, 5 - IV favorites, 6 - plan, 7 - Regimen Synonym |
| 4 | `ORDERED_AS_SYNONYM_ID` | DOUBLE |  | FK→ | The id of the order catalog synonym for the orderable for this ingredient when it's originally ordered.; The id of the order catalog synonym for the orderable for this ingredient when it's originally ordered. |
| 5 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL | FK→ | Favorite order sentence id. |
| 6 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | The identifier for a Plan Child item. This field is valued if the list type is 6. |
| 7 | `PW_CAT_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The plan synonym that the entry is representing |
| 8 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the reference task. |
| 9 | `REGIMEN_CAT_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the REGIMEN_CAT_SYNONYM table. The identifier for a regimen synonym chld item. This field is valued if the list type is 7. |
| 10 | `SEQUENCE` | DOUBLE | NOT NULL |  | Specifies the sort order of all the children of a category. |
| 11 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the synonym child. This field is valued if the list type is 2 or 3. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALT_SEL_CATEGORY_ID` | [ALT_SEL_CAT](ALT_SEL_CAT.md) | `ALT_SEL_CATEGORY_ID` |
| `CHILD_ALT_SEL_CAT_ID` | [ALT_SEL_CAT](ALT_SEL_CAT.md) | `ALT_SEL_CATEGORY_ID` |
| `ORDERED_AS_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |
| `ORDER_SENTENCE_ID` | [ORDER_SENTENCE](ORDER_SENTENCE.md) | `ORDER_SENTENCE_ID` |
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |
| `PW_CAT_SYNONYM_ID` | [PW_CAT_SYNONYM](PW_CAT_SYNONYM.md) | `PW_CAT_SYNONYM_ID` |
| `REFERENCE_TASK_ID` | [ORDER_TASK](ORDER_TASK.md) | `REFERENCE_TASK_ID` |
| `REGIMEN_CAT_SYNONYM_ID` | [REGIMEN_CAT_SYNONYM](REGIMEN_CAT_SYNONYM.md) | `REGIMEN_CAT_SYNONYM_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

