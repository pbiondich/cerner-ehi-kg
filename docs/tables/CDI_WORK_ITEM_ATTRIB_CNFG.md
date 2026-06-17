# CDI_WORK_ITEM_ATTRIB_CNFG

> This table will store work item attribute configuration information.

**Description:** Cdi Work Item Attribute Configuration  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIBUTE_CD` | DOUBLE | NOT NULL |  | Defines the type of attribute. |
| 2 | `CDI_WORK_ITEM_ATTRIB_CNFG_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDI_WORK_ITEM_ATTRIB_CNFG table. |
| 3 | `CDI_WORK_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | The work queue identifier. |
| 4 | `MULTI_SELECT_ENABLE_IND` | DOUBLE | NOT NULL |  | indicates whether or not this attribute's multi select control is enabled. |
| 5 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether or not this attribute is required. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `WARN_IND` | DOUBLE | NOT NULL |  | Indicates whether or not this attribute is setup to warn if blank. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_WORK_QUEUE_ID` | [CDI_WORK_QUEUE](CDI_WORK_QUEUE.md) | `CDI_WORK_QUEUE_ID` |

