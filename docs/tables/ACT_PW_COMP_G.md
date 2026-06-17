# ACT_PW_COMP_G

> Used to define groups of components within a pathway.

**Description:** Pathway component group activity table  
**Table type:** ACTIVITY  
**Primary key:** `ACT_PW_COMP_G_ID`, `ACT_PW_COMP_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACT_PW_COMP_G_ID` | DOUBLE | NOT NULL | PK | Unique identifier of the group. |
| 2 | `ACT_PW_COMP_ID` | DOUBLE | NOT NULL | PK FK→ | Unique identifier of a component within the group. |
| 3 | `ANCHOR_COMPONENT_IND` | DOUBLE | NOT NULL |  | Designates a component group member as the anchor component for the group. Only used by groups with a LINKEDCOMP type_mean. |
| 4 | `DESCRIPTION` | VARCHAR(99) |  |  | Group Description |
| 5 | `INCLUDED_IND` | DOUBLE | NOT NULL |  | Denotes that an item is included in the group |
| 6 | `LINKING_RULE_FLAG` | DOUBLE | NOT NULL |  | A flag that determines the type of linking rule to be used for the component group. Only used by groups with a LINKEDCOMP type_mean. 0 - Not Set, 1 - At Least, 2 - Exactly, and 3 - At Most. |
| 7 | `LINKING_RULE_QUANTITY` | DOUBLE | NOT NULL |  | A quantity to be applied in conjunction with the linking_rule_flag. Only used by groups with a LINKEDCOMP type_mean. |
| 8 | `OVERRIDE_REASON_FLAG` | DOUBLE | NOT NULL |  | Controls the manner in which override reasons are harvested for plan component linking groups. 0 - Tooltip only; 1 - Dialog - optional; 2 - Dialog - required |
| 9 | `PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | Pathway entry id from the pathway table that this group belongs to. |
| 10 | `PW_COMP_SEQ` | DOUBLE |  |  | Sequence of the component within the group. |
| 11 | `TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Meaning that identifies the type of group. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACT_PW_COMP_ID` | [ACT_PW_COMP](ACT_PW_COMP.md) | `ACT_PW_COMP_ID` |
| `PATHWAY_ID` | [PATHWAY](PATHWAY.md) | `PATHWAY_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ACT_PW_COMP_G_ACTION](ACT_PW_COMP_G_ACTION.md) | `ACT_PW_COMP_G_ID` |
| [ACT_PW_COMP_G_ACTION](ACT_PW_COMP_G_ACTION.md) | `ACT_PW_COMP_ID` |

