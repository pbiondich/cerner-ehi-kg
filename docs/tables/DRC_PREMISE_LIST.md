# DRC_PREMISE_LIST

> Table is used to store a list of values for a premise if more than one value is valid in a premise. This could include route groups where multiple routes are applicable. The table is initially populated with Multum content but a user has the ability to m

**Description:** It is used to store a list of values for a premise.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DRC_PREMISE_ID` | DOUBLE | NOT NULL |  | The premise this list is getting built for. |
| 3 | `DRC_PREMISE_LIST_ID` | DOUBLE | NOT NULL |  | Unique Identifier. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Represents the value of the date you are building the list for. (i.e. NOMENCLATURE ID) |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | Represents the data you are building the list for. (i.e. NOMENCLATURE) |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

