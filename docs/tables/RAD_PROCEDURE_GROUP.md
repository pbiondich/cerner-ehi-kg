# RAD_PROCEDURE_GROUP

> The Rad_Procedure_Group table contains general information about a procedure group. A procedure group is a way to group procedures together for replacement purposes.

**Description:** Rad Procedure Group  
**Table type:** REFERENCE  
**Primary key:** `PROC_GROUP_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `GROUP_DESC` | VARCHAR(50) |  |  | The Group_Desc is the description of the procedure grouping. |
| 3 | `GROUP_TYPE_CD` | DOUBLE | NOT NULL |  | This column contains a code value to designate the type of grouping for the procedures. This allow application to distinguish the group defined for relevant priors or just groupings of procedures for other purposes such as Mammo group. |
| 4 | `PROC_GROUP_ID` | DOUBLE | NOT NULL | PK | The Proc_Group_Id uniquely identifies a row in the Rad_Procedure_Group table. It serves no other purpose other than to uniquely identify the row. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RAD_FOLLOW_UP_CONTROL](RAD_FOLLOW_UP_CONTROL.md) | `PROC_GROUP_ID` |
| [RAD_PROCEDURE_ASSOC](RAD_PROCEDURE_ASSOC.md) | `PROC_GROUP_ID` |

