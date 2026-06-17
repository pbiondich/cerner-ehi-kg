# SCH_DATE_APPLY

> Stores the resource and date to which the resource template is going to apply.

**Description:** Scheduling Date Apply  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Action_flag is used to determine what action to take for the date. 0 - No Change, 1 - Add Template, 2 - Change Template, 3 - Delete Template. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `APPLY_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status. Some examples are applied, duplicated or requested. |
| 4 | `RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the resource. A resource is an item of limited availability. Associates the date to a resource. |
| 5 | `RES_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the resource group associated to the date. |
| 6 | `SCH_DATE_APPLY_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is internally generated. |
| 7 | `SCH_DATE_DT_TM` | DATETIME | NOT NULL |  | The date associated to the date set. This column was duplicated from the SCH_DATE_LIST table for performance reasons. |
| 8 | `SCH_DATE_LIST_ID` | DOUBLE | NOT NULL | FK→ | Identifies what date the resource is associated to. It is the primary key of the SCH_DATE_LIST table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RESOURCE_CD` | [SCH_RESOURCE](SCH_RESOURCE.md) | `RESOURCE_CD` |
| `RES_GROUP_ID` | [SCH_RES_GROUP](SCH_RES_GROUP.md) | `RES_GROUP_ID` |
| `SCH_DATE_LIST_ID` | [SCH_DATE_LIST](SCH_DATE_LIST.md) | `SCH_DATE_LIST_ID` |

