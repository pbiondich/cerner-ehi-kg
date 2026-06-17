# DA_CALC_ELEM_RELTN

> Contains the Discern Analytics 2.0 parent/child relationships for calculated elements.

**Description:** Discern Analytics Calculation Element Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_ELEMENT_ID` | DOUBLE | NOT NULL | FK→ | An element within a calculation (when an element contains a calculation that includes elements from the logical view). |
| 2 | `DA_CALC_ELEM_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the DA_CALC_ELEM_RELTN table. |
| 3 | `PARENT_ELEMENT_ID` | DOUBLE | NOT NULL | FK→ | The actual calculated element when an element contains a calculation that includes elements from the logical view. |
| 4 | `RELTN_TYPE_FLAG` | DOUBLE | NOT NULL |  |  |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_ELEMENT_ID` | [DA_ELEMENT](DA_ELEMENT.md) | `DA_ELEMENT_ID` |
| `PARENT_ELEMENT_ID` | [DA_ELEMENT](DA_ELEMENT.md) | `DA_ELEMENT_ID` |

