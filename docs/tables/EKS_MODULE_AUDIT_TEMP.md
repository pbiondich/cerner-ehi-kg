# EKS_MODULE_AUDIT_TEMP

> Used to allow reports to easily determine which templates are used within a module.

**Description:** Contains cross-reference of templates used within modules.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MODULE_NAME` | CHAR(30) | NOT NULL |  | Name of module template is associated with |
| 2 | `TEMPLATE_NAME` | CHAR(30) |  |  | Template name |
| 3 | `TEMPLATE_NUM` | DOUBLE | NOT NULL |  | Ordinal number of template within module |
| 4 | `TEMPLATE_TYPE` | CHAR(1) | NOT NULL |  | type of template (evoke, logic, action, etc.) |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

