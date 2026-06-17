# WHC_D_COMPLICATION_BRIDGE

> A Dimension Bridge table to allow the Fact table row to be associated to many Complication Dimension rows

**Description:** WHC_D_COMPLICATION_BRIDGE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 2 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 3 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 4 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `WHC_D_COMPLICATION_BRIDGE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `WHC_D_COMPLICATION_GROUP_ID` | DOUBLE | NOT NULL | FK→ | foreign key to whc_d_complication_type.whc_d_complication_type_id |
| 8 | `WHC_D_COMPLICATION_TYPE_ID` | DOUBLE | NOT NULL | FK→ | foreign key to whc_d_complication_group.whc_d_complication_group_id |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WHC_D_COMPLICATION_GROUP_ID` | [WHC_D_COMPLICATION_GROUP](WHC_D_COMPLICATION_GROUP.md) | `WHC_D_COMPLICATION_GROUP_ID` |
| `WHC_D_COMPLICATION_TYPE_ID` | [WHC_D_COMPLICATION_TYPE](WHC_D_COMPLICATION_TYPE.md) | `WHC_D_COMPLICATION_TYPE_ID` |

