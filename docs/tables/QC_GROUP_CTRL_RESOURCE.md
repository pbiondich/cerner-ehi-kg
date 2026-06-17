# QC_GROUP_CTRL_RESOURCE

> Contains information about the group control resource for quality control.

**Description:** Quality Control Group Control Resource  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTROL_GROUP_CD` | DOUBLE | NOT NULL |  | This is the control group to which this control and service resource is associated. |
| 4 | `CONTROL_ID` | DOUBLE | NOT NULL | FK→ | This relates the control on the control_material table to the appropriate control group. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PREV_QC_GROUP_CTRL_RESOURCE_ID` | DOUBLE | NOT NULL |  | This is used to group the modified values for a given quality control group control resource. |
| 7 | `QC_GROUP_CTRL_RESOURCE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a specific quality control group control resource. |
| 8 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Identifies the service resource that is related to this control group. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTROL_ID` | [CONTROL_MATERIAL](CONTROL_MATERIAL.md) | `CONTROL_ID` |

