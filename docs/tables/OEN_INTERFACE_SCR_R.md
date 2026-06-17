# OEN_INTERFACE_SCR_R

> oen interface script relationship

**Description:** Lists which interface uses which scripts.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONTEXT_FLAG` | DOUBLE |  |  | This lists the type of script that is being used. |
| 3 | `INTERFACE_ID` | DOUBLE | NOT NULL | FK→ | Interface id. This is foreign key from oen_interface table. |
| 4 | `SCRIPT_ID` | DOUBLE | NOT NULL | FK→ | Script id. This is foreign key from oen_script_list table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VERSION_NBR` | DOUBLE | NOT NULL |  | The Version changes when the script is check into/outof production.Column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INTERFACE_ID` | [OEN_INTERFACE](OEN_INTERFACE.md) | `INTERFACE_ID` |
| `SCRIPT_ID` | [OEN_SCRIPT_LIST](OEN_SCRIPT_LIST.md) | `SCRIPT_ID` |

