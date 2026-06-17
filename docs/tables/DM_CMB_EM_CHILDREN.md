# DM_CMB_EM_CHILDREN

> List of child tables that reference PERSON and also are indirectly related to ENCOUNTER

**Description:** DM_CMB_EM_CHILDREN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CHILD_CMB_COLUMN` | VARCHAR(30) | NOT NULL |  | Name of PERSON foreign key column on child table that takes part in person combines; this column needs to be correctly updated after encounter move operation |
| 3 | `CHILD_PK_COLUMN` | VARCHAR(30) | NOT NULL |  | Name of primary key column on child table |
| 4 | `CHILD_TABLE` | VARCHAR(30) | NOT NULL |  | Name of child table that takes part in person combines and is indirectly related to ENCOUNTER |
| 5 | `DM_CMB_EM_CHILDREN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DM_CMB_EM_CHILDREN table. |
| 6 | `FROM_CLAUSE` | VARCHAR(1000) |  |  | List of table names to join, including child_table and parent_table above |
| 7 | `PARENT_CMB_COLUMN` | VARCHAR(30) | NOT NULL |  | Name of PERSON foreign key column on parent table that takes part in person combines; this column has the correct value after encounter move operation |
| 8 | `PARENT_TABLE` | VARCHAR(30) | NOT NULL |  | Name of parent table that takes part in person combines and direct child of ENCOUNTER |
| 9 | `RUN_ORDER` | DOUBLE | NOT NULL |  | Run Order Sequence |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `WHERE_CLAUSE` | VARCHAR(2000) |  |  | Join predicates for the table names listed above in the from clause |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

