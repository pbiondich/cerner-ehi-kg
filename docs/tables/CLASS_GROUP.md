# CLASS_GROUP

> Classification grouping table.

**Description:** CLASS GROUP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHILD_CLASS_NODE_ID` | DOUBLE | NOT NULL | FK→ | A foreign key to the class_node table reflecting the child of a parent - child relationship. |
| 6 | `CLASS_GROUP_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 7 | `CLASS_INSTANCE_CD` | DOUBLE | NOT NULL |  | The codevalue for this particular instance of a classification. |
| 8 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 9 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was inserted. |
| 10 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 11 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 12 | `PARENT_CLASS_NODE_ID` | DOUBLE | NOT NULL | FK→ | The parent class node. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_CLASS_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |
| `PARENT_CLASS_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |

